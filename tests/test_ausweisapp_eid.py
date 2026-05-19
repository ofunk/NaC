from __future__ import annotations

import argparse
import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "plugins" / "noc-ausweisapp-eid" / "scripts" / "prepare_eid_session.py"


def load_eid_module():
    spec = importlib.util.spec_from_file_location("prepare_eid_session", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {SCRIPT_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


eid = load_eid_module()


class AusweisAppEidTests(unittest.TestCase):
    def test_hash_identifier_does_not_return_raw_value(self) -> None:
        raw = "https://example.invalid/eid/tctoken?session=secret"
        hashed = eid.hash_identifier(raw)
        self.assertIsNotNone(hashed)
        self.assertTrue(hashed.startswith("sha256:"))
        self.assertNotIn(raw, hashed)

    def test_activation_url_is_not_stored_in_evidence(self) -> None:
        args = argparse.Namespace(
            purpose="notarial-client-intake",
            claim_set="GivenNames,FamilyName,DateOfBirth",
            status_url="http://127.0.0.1:24727/eID-Client?Status=json",
            tc_token_url="https://example.invalid/eid/tctoken?session=secret",
            production_eid_approved=False,
            personal_data_processing_approved=False,
            backend_assertion_import_approved=False,
        )
        original_probe = eid.probe_ausweisapp_status
        eid.probe_ausweisapp_status = lambda status_url: eid.check_result(
            "ausweisapp_status",
            "AusweisApp status",
            "passed",
            "info",
            "Reachable",
        )
        try:
            evidence = eid.build_evidence(args)
        finally:
            eid.probe_ausweisapp_status = original_probe

        serialized = str(evidence)
        self.assertNotIn(args.tc_token_url, serialized)
        self.assertEqual(evidence["tc_token"]["sha256"], eid.hash_identifier(args.tc_token_url))
        self.assertTrue(evidence["tc_token"]["provided"])
        self.assertTrue(evidence["activation"]["desktop_activation_url_available"])
        self.assertFalse(evidence["activation"]["full_url_stored"])
        self.assertEqual(evidence["overall_status"], "manual_review")
        self.assertFalse(evidence["policy"]["identity_attributes_captured"])

    def test_probe_status_redacts_to_metadata(self) -> None:
        def fake_fetcher(url: str, timeout: float):
            return 200, {
                "Implementation-Version": "2.5.1",
                "Implementation-Vendor": "Governikus GmbH & Co. KG",
                "Specification-Version": "1.4",
            }

        result = eid.probe_ausweisapp_status("http://localhost/status", fake_fetcher)
        self.assertEqual(result["status"], "passed")
        self.assertEqual(result["details"]["implementation_version"], "2.5.1")
        self.assertNotIn("GivenNames", str(result))

    def test_empty_claim_set_blocks_evidence(self) -> None:
        args = argparse.Namespace(
            purpose="notarial-client-intake",
            claim_set="",
            status_url="http://127.0.0.1:24727/eID-Client?Status=json",
            tc_token_url=None,
            production_eid_approved=False,
            personal_data_processing_approved=False,
            backend_assertion_import_approved=False,
        )
        original_probe = eid.probe_ausweisapp_status
        eid.probe_ausweisapp_status = lambda status_url: eid.check_result(
            "ausweisapp_status",
            "AusweisApp status",
            "passed",
            "info",
            "Reachable",
        )
        try:
            evidence = eid.build_evidence(args)
        finally:
            eid.probe_ausweisapp_status = original_probe

        self.assertEqual(evidence["overall_status"], "blocked")


if __name__ == "__main__":
    unittest.main()
