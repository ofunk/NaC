from __future__ import annotations

import argparse
import json
import socket
import sys
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


PLUGIN_NAME = "noc-ben-portal"
SCHEMA_VERSION = "noc.ben.session-preflight/v1"
XNP_PORTS = range(12774, 12785)


def utc_now() -> str:
    return datetime.now(tz=UTC).replace(microsecond=0).isoformat()


def check_result(
    check_id: str,
    title: str,
    status: str,
    severity: str,
    message: str,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "id": check_id,
        "title": title,
        "status": status,
        "severity": severity,
        "message": message,
        "details": details or {},
    }


def probe_xnp_local_interface() -> dict[str, Any]:
    open_ports: list[int] = []
    for port in XNP_PORTS:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.25):
                open_ports.append(port)
        except OSError:
            continue

    if open_ports:
        return {
            "status": "reachable",
            "host": "127.0.0.1",
            "open_ports": open_ports,
            "api_key_observed": False,
        }
    return {
        "status": "not_reachable",
        "host": "127.0.0.1",
        "port_range": [min(XNP_PORTS), max(XNP_PORTS)],
        "api_key_observed": False,
    }


def manual_status(value: str, positive_status: str = "passed") -> tuple[str, str, str]:
    if value == "yes":
        return positive_status, "info", "Manually attested as available."
    if value == "no":
        return "failed", "blocker", "Manually attested as unavailable."
    return "manual_review", "manual", "Manual attestation is still missing."


def evaluate_status(checks: list[dict[str, Any]]) -> str:
    if any(check["status"] == "failed" for check in checks):
        return "blocked"
    if any(check["status"] == "manual_review" for check in checks):
        return "manual_review"
    return "ready"


def next_required_action(status: str) -> str:
    if status == "blocked":
        return "Resolve the blocker before any beN activation, mailbox action or XNP handoff."
    if status == "manual_review":
        return "Complete local XNP, card-reader, beN availability and approval review before treating the beN preflight as ready."
    return "Proceed with the local beN plan preview; human approval is still required for activation, send, receive or export actions."


def build_evidence(
    args: argparse.Namespace,
    xnp_interface: dict[str, Any] | None = None,
) -> dict[str, Any]:
    xnp_local = xnp_interface if xnp_interface is not None else probe_xnp_local_interface()
    xnp_reachable = xnp_local.get("status") == "reachable"
    xnp_manual_status, xnp_manual_severity, xnp_manual_message = manual_status(args.manual_xnp_ready)
    if args.manual_xnp_ready == "unknown" and xnp_reachable:
        xnp_manual_status = "passed"
        xnp_manual_severity = "info"
        xnp_manual_message = "XNP localhost interface is reachable without reading or using an API key."

    card_status, card_severity, card_message = manual_status(args.manual_card_path_ready)
    ben_status, ben_severity, ben_message = manual_status(args.manual_ben_available)
    role_status = "manual_review" if args.mailbox_role == "unknown" else "passed"

    checks = [
        check_result(
            "xnp_first_setup",
            "XNP first setup prerequisite",
            xnp_manual_status,
            xnp_manual_severity,
            xnp_manual_message,
            xnp_local,
        ),
        check_result(
            "bnotk_card_or_token_path",
            "BNotK card/token and reader path",
            card_status,
            card_severity,
            card_message,
            {"manual_card_path_ready": args.manual_card_path_ready},
        ),
        check_result(
            "ben_application_available",
            "beN application availability",
            ben_status,
            ben_severity,
            ben_message,
            {"manual_ben_available": args.manual_ben_available},
        ),
        check_result(
            "notary_role_context",
            "Notary mailbox role context",
            role_status,
            "manual" if role_status == "manual_review" else "info",
            (
                "Mailbox role is not yet identified."
                if role_status == "manual_review"
                else f"Mailbox role is {args.mailbox_role}."
            ),
            {"mailbox_role": args.mailbox_role},
        ),
    ]
    status = evaluate_status(checks)

    return {
        "schema_version": SCHEMA_VERSION,
        "plugin": PLUGIN_NAME,
        "preflight_id": f"BEN-PF-{uuid.uuid4()}",
        "generated_at": utc_now(),
        "overall_status": status,
        "mode": "local_dry_run",
        "intent": args.intent,
        "mailbox_role": args.mailbox_role,
        "xnp_local_interface": xnp_local,
        "operator_actions": [
            "Use the local notary workstation where XNP, the card reader and beN are installed.",
            "Confirm that XNP first setup has been completed before beN activation planning.",
            "Confirm card-reader or token readiness locally; do not enter PINs or card values into Codex.",
            "Perform beN activation, send, receive and export actions only in the official local beN/XNP path.",
        ],
        "policy": {
            "pin_captured": False,
            "card_data_captured": False,
            "xnp_api_key_captured": False,
            "xnp_login_performed": False,
            "ben_mailbox_content_captured": False,
            "external_network_calls": False,
            "localhost_only": True,
            "productive_mailbox_write": False,
        },
        "checks": checks,
        "next_required_action": next_required_action(status),
    }


def write_output(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a local beN/XNP/card-reader readiness and evidence preview."
    )
    parser.add_argument(
        "--intent",
        default="activation_readiness",
        choices=["activation_readiness", "mailbox_receive_plan", "mailbox_send_plan", "ben_to_bea_plan", "export_evidence_plan"],
        help="beN preflight intent.",
    )
    parser.add_argument(
        "--mailbox-role",
        default="unknown",
        choices=["notary", "notary-administrator", "notary-office-staff", "unknown"],
        help="Local role for the beN mailbox workflow.",
    )
    parser.add_argument(
        "--manual-xnp-ready",
        default="unknown",
        choices=["yes", "no", "unknown"],
        help="Manual attestation that XNP first setup and local workstation context are ready.",
    )
    parser.add_argument(
        "--manual-card-path-ready",
        default="unknown",
        choices=["yes", "no", "unknown"],
        help="Manual attestation that the BNotK card/token and reader path is ready.",
    )
    parser.add_argument(
        "--manual-ben-available",
        default="unknown",
        choices=["yes", "no", "unknown"],
        help="Manual attestation that beN is locally available for the intended workflow.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional JSON evidence output path.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print full JSON evidence to stdout.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a non-zero exit code unless the beN preflight is fully ready.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    evidence = build_evidence(args)

    if args.output:
        write_output(args.output, evidence)

    if args.json:
        print(json.dumps(evidence, indent=2, ensure_ascii=True))
    else:
        print(f"{PLUGIN_NAME}: {evidence['overall_status']}")
        print(evidence["next_required_action"])

    if args.strict and evidence["overall_status"] != "ready":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
