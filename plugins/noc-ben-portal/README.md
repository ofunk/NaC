# NoC beN Portal

![beN logo](assets/logo.png)

Local beN workflow companion for notaries and notary administrators. It checks XNP-first readiness, BNotK card or token availability, card-reader prerequisites, beN activation planning, mailbox send/receive planning and metadata-only evidence without storing PINs, card data, XNP secrets, mailbox secrets or notarial matter content in Git.

## Status

Installable MVP plugin scaffold with a runnable local preflight script. External write adapters are intentionally not enabled in this first version.

## Visual Identity

The plugin uses the beN logo asset from the official [NotarNet beN product page](https://notarnet.de/produkte/ben) as its store and composer recognition mark. The visual mark is only a recognition cue for the local companion; beN, XNP and the official BNotK/NotarNet systems remain authoritative, and NotarNet/BNotK trademark or usage rights are not transferred by this repository.

## Install Boundary

- Runs as a local Codex plugin from this repository.
- Treats XNP first setup as a Day0 prerequisite for beN activation.
- Keeps secrets, PINs, certificates, portal sessions, mailbox secrets and notarial matter content outside Git.
- Produces plan previews and evidence metadata before any sensitive action.
- Requires human approval for mailbox actions, notarial actions, register actions and cloud applies.

## Day0

- Confirm notary or notary-administrator role, XNP first setup, BNotK card or token readiness, supported card-reader availability and beN application availability.

## Day1

- Create human-approved beN activation, receive, send, beN-to-beA and evidence checklists.

## Day2

- Track XNP versions, beN availability, failed mailbox checks, export integrity and card-reader drift.

## Local Preflight

```bash
python plugins/noc-ben-portal/scripts/prepare_ben_session.py --json
```

The script reports readiness only. It does not log in to XNP, does not activate beN, does not read mailbox content and does not collect PINs or card data.

## Required Accounts And Approvals

- beN mailbox access
- XNP first setup and local XNP workstation context
- BNotK card or approved authentication method
- Supported card reader for BNotK card workflows
- Firm or notary-office policy for mailbox actions, exports and evidence

See [docs/de/plugin-operations/account-and-approval-requests.md](../../docs/de/plugin-operations/account-and-approval-requests.md) and [docs/en/plugin-operations/account-and-approval-requests.md](../../docs/en/plugin-operations/account-and-approval-requests.md) for the consolidated request list.
