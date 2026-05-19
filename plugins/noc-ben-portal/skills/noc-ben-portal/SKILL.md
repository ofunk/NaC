---
name: noc-ben-portal
description: Use when planning beN mailbox activation, incoming or outgoing beN messages, beN-to-beA communication, XNP-first setup, card-reader readiness or metadata-only evidence work for a notary office.
---

# NoC beN Portal

## Operating Boundary

Runtime mode: `local-notary-mailbox-companion`.

This plugin is for notarial work. Default to plan-preview, local execution, explicit human approval and metadata-only evidence. beN and XNP remain authoritative; do not perform external writes unless a separate reviewed connector explicitly implements that action.

## Allowed Work

- Prepare beN readiness and XNP-first setup checklists.
- Prepare BNotK card, token and card-reader readiness checklists.
- Create beN activation, send, receive, beN-to-beA and export evidence plans for human execution.
- Import explicit evidence metadata supplied by the user.

## Prohibited Work

- Store passwords, PINs, private keys, certificate material, session cookies, one-time codes or XNP API keys in Git.
- Store or infer card raw data, card secrets, PIN values, mailbox secrets or notarial matter content.
- Bypass human review for mailbox, register, XNP, notarial or other regulated actions.
- Upload notarial matter content to an LLM unless an explicit approved data-processing basis exists.
- Scrape protected portals or exceed published usage limits.

## Workflow

1. Classify the matter, actor role, reviewer role, data class and target system.
2. Check Day0 prerequisites: XNP first setup, local workstation, card path, beN availability and missing approvals.
3. Produce a human-readable Day1 plan preview before any local or external action.
4. Ask for explicit human approval for beN activation, mailbox actions, register retrievals, XNP actions, notarial actions or cloud applies.
5. Capture evidence metadata only: timestamp, actor role, source, hash, decision, result and follow-up owner.
6. For Day2, report drift, expired access, failed checks, version changes and recertification tasks.

## Output Shape

Return concise sections named `Readiness`, `Plan`, `Approval Needed`, `Evidence`, and `Day2 Follow-up`. If something cannot proceed, put it under `Approval Needed` and reference `docs/de/plugin-operations/account-and-approval-requests.md` and `docs/en/plugin-operations/account-and-approval-requests.md`.

## Source Plan

- `docs/de/plugin-plans/ben-portal-plugin-integration.md`
- `docs/en/plugin-plans/ben-portal-plugin-integration.md`
