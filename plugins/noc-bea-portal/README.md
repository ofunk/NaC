# NoC beA Portal

![beA logo](assets/logo.png)

Local beA workflow companion for BRaK beA/ERV readiness, beA card or token availability, card-reader and Client Security checks, mailbox/eEB task planning and evidence capture without storing PINs, card data, mailbox secrets or mandate content in Git.

## Status

Installable MVP plugin scaffold. The plugin provides local Codex skill guidance, a machine-readable security contract and marketplace metadata. External write adapters are intentionally not enabled in this first version.

## Visual Identity

The plugin uses the beA logo asset from the official [BRaK beA and ERV page](https://www.brak.de/anwaltschaft/bea-erv/) as its store and composer recognition mark. The visual mark is only a recognition cue for the local companion; beA and the official beA portal remain authoritative, and BRaK/beA trademark or usage rights are not transferred by this repository.

## Install Boundary

- Runs as a local Codex plugin from this repository.
- Keeps secrets, PINs, certificates, portal sessions and mandate content outside Git.
- Produces plan previews and evidence metadata before any sensitive action.
- Requires human approval for regulated submissions, portal actions, notarial actions and cloud applies.

## Day0

- Confirm mailbox owner, user role, beA card or token readiness, supported card-reader availability and Client Security availability.

## Day1

- Create human-approved send/receive/eEB plan and evidence checklist.

## Day2

- Track Client Security versions, failed sends, eEB deadlines and export integrity.

## Required Accounts And Approvals

- beA mailbox access
- beA card or approved authentication method
- Supported card reader for beA card workflows
- beA Client Security on local workstation
- Firm policy for eEB and exports

See [docs/de/plugin-operations/account-and-approval-requests.md](../../docs/de/plugin-operations/account-and-approval-requests.md) and [docs/en/plugin-operations/account-and-approval-requests.md](../../docs/en/plugin-operations/account-and-approval-requests.md) for the consolidated request list.
