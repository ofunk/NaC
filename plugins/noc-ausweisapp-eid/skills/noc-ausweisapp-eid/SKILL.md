---
name: noc-ausweisapp-eid
description: Use when preparing local German Personalausweis eID sessions through AusweisApp, checking AusweisApp localhost readiness, defining minimal eID claim sets, or explaining why Codex cannot directly dump identity attributes from the card.
---

# NoC AusweisApp eID

## Operating Boundary

Runtime mode: `local-ausweisapp-eid-preflight`.

This plugin prepares AusweisApp-oriented eID sessions and metadata-only
evidence. It does not directly read Personalausweis identity attributes from the
card, capture PIN/CAN/PUK values, store `tcTokenURL` session values in Git, or
replace an eID server. For physical USB reader checks, run `noc-cyberjack-rfid`
first. For verified-claim projection, hand approved backend results to
`noc-idaas`.

## Allowed Work

- Explain the official AusweisApp/eID boundary: local clients do not receive
  identity attributes directly from AusweisApp.
- Check AusweisApp localhost readiness through metadata-only status probes.
- Define purpose, tenant, actor, reviewer and minimal claim set.
- Prepare a local eID session evidence preview.
- Hash `tcTokenURL` values in evidence instead of storing full URLs.
- Route identity attributes through an approved eID server, eID service or
  identification service.

## Prohibited Work

- Request, store, infer or transmit PIN, CAN, PUK, card raw data, card serial
  values, full identity-document dumps, session cookies, access tokens,
  certificates or private keys.
- Claim that Codex can directly read identity attributes from the AusweisApp
  local SDK connection.
- Start production eID transactions without documented approval and reviewed
  backend routing.
- Upload real identity data or client personal data to an LLM without an
  explicit approved data-processing basis.
- Reuse verified claims beyond the documented purpose.

## Workflow

1. Classify purpose, tenant, actor role, reviewer role and requested claim set.
2. If a USB card reader path is in scope, require `noc-cyberjack-rfid`
   readiness first.
3. Run:

   ```powershell
   python plugins\noc-ausweisapp-eid\scripts\prepare_eid_session.py --json
   ```

4. If a reviewed backend provides a `tcTokenURL`, pass it only for local session
   preview; keep the evidence hash-only.
5. Require human approval before production eID, backend assertion import or
   IAM projection.
6. Pass approved minimal verified claims to `noc-idaas`.

## Output Shape

Return concise sections named `Readiness`, `Claim Set`, `Approval Needed`,
`Evidence`, and `Day2 Follow-up`.

## Source Plans

- `docs/de/plugin-plans/ausweisapp-eid-plugin-integration.md`
- `docs/en/plugin-plans/ausweisapp-eid-plugin-integration.md`
