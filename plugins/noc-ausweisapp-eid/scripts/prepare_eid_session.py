from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Callable


PLUGIN_NAME = "noc-ausweisapp-eid"
SCHEMA_VERSION = "noc.eid-session-evidence/v1"
DEFAULT_STATUS_URL = "http://127.0.0.1:24727/eID-Client?Status=json"
DEFAULT_CLAIMS = "GivenNames,FamilyName,DateOfBirth"
SOURCE_REFERENCES = [
    "https://www.ausweisapp.bund.de/das-brauchen-sie",
    "https://www.ausweisapp.bund.de/sdk/intro.html",
    "https://www.ausweisapp.bund.de/sdk/desktop.html",
    "https://www.ausweisapp.bund.de/so-werden-sie-diensteanbieter",
]


def hash_identifier(value: str | None) -> str | None:
    if not value:
        return None
    digest = hashlib.sha256(value.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def check_result(
    check_id: str,
    title: str,
    status: str,
    severity: str,
    message: str,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": check_id,
        "title": title,
        "status": status,
        "severity": severity,
        "message": message,
    }
    if details:
        result["details"] = details
    return result


def evaluate_overall_status(checks: list[dict[str, Any]]) -> str:
    if any(item["status"] == "failed" and item["severity"] == "blocker" for item in checks):
        return "blocked"
    if any(item["status"] != "passed" for item in checks):
        return "manual_review"
    return "ready"


def parse_claims(value: str) -> list[str]:
    claims = [item.strip() for item in value.split(",") if item.strip()]
    seen: set[str] = set()
    deduped: list[str] = []
    for claim in claims:
        if claim not in seen:
            seen.add(claim)
            deduped.append(claim)
    return deduped


def fetch_json(url: str, timeout: float = 3.0) -> tuple[int, dict[str, Any]]:
    request = urllib.request.Request(url, headers={"User-Agent": "NoC AusweisApp eID/0.1"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read(64 * 1024).decode("utf-8", errors="replace")
        payload = json.loads(raw)
        return response.status, payload


def probe_ausweisapp_status(
    status_url: str,
    fetcher: Callable[[str, float], tuple[int, dict[str, Any]]] = fetch_json,
) -> dict[str, Any]:
    try:
        http_status, payload = fetcher(status_url, 3.0)
    except (OSError, urllib.error.URLError, TimeoutError) as exc:
        return check_result(
            "ausweisapp_status",
            "AusweisApp status",
            "manual_review",
            "manual",
            "AusweisApp status endpoint is not reachable on localhost.",
            {"error": exc.__class__.__name__},
        )
    except json.JSONDecodeError:
        return check_result(
            "ausweisapp_status",
            "AusweisApp status",
            "manual_review",
            "manual",
            "AusweisApp status endpoint answered, but not with JSON.",
        )

    version = str(payload.get("Implementation-Version", "unknown"))
    vendor = str(payload.get("Implementation-Vendor", "unknown"))
    spec = str(payload.get("Specification-Version", "unknown"))
    status = "passed" if http_status == 200 else "manual_review"
    return check_result(
        "ausweisapp_status",
        "AusweisApp status",
        status,
        "info" if status == "passed" else "manual",
        "AusweisApp status endpoint answered without exposing identity attributes.",
        {
            "http_status": http_status,
            "implementation_version": version,
            "implementation_vendor": vendor,
            "specification_version": spec,
        },
    )


def build_activation_url(tc_token_url: str | None) -> str | None:
    if not tc_token_url:
        return None
    encoded = urllib.parse.quote(tc_token_url, safe="")
    return f"http://127.0.0.1:24727/eID-Client?tcTokenURL={encoded}"


def build_evidence(args: argparse.Namespace) -> dict[str, Any]:
    checks = [
        probe_ausweisapp_status(args.status_url),
    ]

    claims = parse_claims(args.claim_set)
    if not claims:
        checks.append(
            check_result(
                "claim_set",
                "Claim set",
                "failed",
                "blocker",
                "At least one requested claim name is required.",
            )
        )
    else:
        checks.append(
            check_result(
                "claim_set",
                "Claim set",
                "passed",
                "info",
                "Requested claim names are recorded as metadata only.",
                {"count": len(claims)},
            )
        )

    if args.tc_token_url and not args.production_eid_approved:
        checks.append(
            check_result(
                "production_approval",
                "Production eID approval",
                "manual_review",
                "manual",
                "A tcTokenURL was provided; production eID still needs documented approval.",
            )
        )

    activation_url = build_activation_url(args.tc_token_url)
    return {
        "schema_version": SCHEMA_VERSION,
        "plugin": PLUGIN_NAME,
        "created_utc": datetime.now(tz=UTC).isoformat(),
        "overall_status": evaluate_overall_status(checks),
        "purpose": args.purpose,
        "claim_set": {
            "requested": claims,
            "backend_assertion_required": True,
        },
        "tc_token": {
            "provided": bool(args.tc_token_url),
            "sha256": hash_identifier(args.tc_token_url),
        },
        "activation": {
            "desktop_activation_url_available": activation_url is not None,
            "full_url_stored": False,
        },
        "checks": checks,
        "policy": {
            "pin_captured": False,
            "can_captured": False,
            "puk_captured": False,
            "card_data_captured": False,
            "identity_attributes_captured": False,
            "tc_token_url_stored": False,
            "metadata_only": True,
        },
        "approvals": {
            "production_eid_transaction": bool(args.production_eid_approved),
            "personal_data_processing": bool(args.personal_data_processing_approved),
            "backend_assertion_import": bool(args.backend_assertion_import_approved),
        },
        "source_references": SOURCE_REFERENCES,
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare metadata-only AusweisApp eID session evidence."
    )
    parser.add_argument("--purpose", default="local-eid-preflight")
    parser.add_argument("--claim-set", default=DEFAULT_CLAIMS)
    parser.add_argument("--status-url", default=DEFAULT_STATUS_URL)
    parser.add_argument("--tc-token-url", default=None)
    parser.add_argument("--production-eid-approved", action="store_true")
    parser.add_argument("--personal-data-processing-approved", action="store_true")
    parser.add_argument("--backend-assertion-import-approved", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--output", type=Path, default=None, help="Optional evidence JSON path.")
    parser.add_argument(
        "--show-activation-url",
        action="store_true",
        help="Print the local activation URL to the console only. It is never written to evidence.",
    )
    return parser.parse_args(argv)


def write_output(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    evidence = build_evidence(args)
    if args.output:
        write_output(args.output, evidence)

    if args.json:
        print(json.dumps(evidence, indent=2, ensure_ascii=True))
    else:
        print(f"Plugin: {PLUGIN_NAME}")
        print(f"Status: {evidence['overall_status']}")
        print(f"Purpose: {evidence['purpose']}")
        print(f"Claims: {', '.join(evidence['claim_set']['requested'])}")
        print("Identity attributes captured: no")
        print("Backend assertion required: yes")

    if args.show_activation_url and args.tc_token_url:
        print(
            "Activation URL (local only, do not store in Git): "
            f"{build_activation_url(args.tc_token_url)}",
            file=sys.stderr,
        )

    return 0 if evidence["overall_status"] != "blocked" else 1


if __name__ == "__main__":
    raise SystemExit(main())
