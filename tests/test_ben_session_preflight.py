from __future__ import annotations

import argparse
import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "plugins" / "noc-ben-portal" / "scripts" / "prepare_ben_session.py"


def load_ben_module():
    spec = importlib.util.spec_from_file_location("prepare_ben_session", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {SCRIPT_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ben = load_ben_module()


def args(**overrides):
    values = {
        "intent": "activation_readiness",
        "mailbox_role": "notary",
        "manual_xnp_ready": "yes",
        "manual_card_path_ready": "yes",
        "manual_ben_available": "yes",
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class BenSessionPreflightTests(unittest.TestCase):
    def test_preflight_ready_when_all_prerequisites_are_attested(self) -> None:
        evidence = ben.build_evidence(
            args(),
            xnp_interface={"status": "reachable", "host": "127.0.0.1", "open_ports": [12774]},
        )

        self.assertEqual(evidence["overall_status"], "ready")
        self.assertFalse(evidence["policy"]["pin_captured"])
        self.assertFalse(evidence["policy"]["ben_mailbox_content_captured"])

    def test_preflight_blocks_when_xnp_is_not_ready(self) -> None:
        evidence = ben.build_evidence(
            args(manual_xnp_ready="no"),
            xnp_interface={"status": "not_reachable", "host": "127.0.0.1"},
        )

        self.assertEqual(evidence["overall_status"], "blocked")
        self.assertIn("beN activation", evidence["next_required_action"])

    def test_preflight_requires_manual_review_for_unknown_role(self) -> None:
        evidence = ben.build_evidence(
            args(mailbox_role="unknown"),
            xnp_interface={"status": "reachable", "host": "127.0.0.1", "open_ports": [12774]},
        )

        self.assertEqual(evidence["overall_status"], "manual_review")
        role_check = next(check for check in evidence["checks"] if check["id"] == "notary_role_context")
        self.assertEqual(role_check["status"], "manual_review")

    def test_operator_actions_do_not_request_secret_values(self) -> None:
        evidence = ben.build_evidence(
            args(),
            xnp_interface={"status": "reachable", "host": "127.0.0.1", "open_ports": [12774]},
        )

        actions = " ".join(evidence["operator_actions"]).lower()
        self.assertIn("do not enter pins", actions)
        self.assertNotIn("api key eingeben", actions)


if __name__ == "__main__":
    unittest.main()
