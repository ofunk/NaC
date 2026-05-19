# NoC AusweisApp eID

![Personalausweis logo](assets/personalausweis-logo.svg)

Local Codex plugin for AusweisApp-oriented German eID preflight. It sits
between the local card-reader gate and `noc-idaas`: `noc-cyberjack-rfid`
confirms the workstation and reader path, this plugin prepares the AusweisApp
session boundary, and `noc-idaas` turns approved backend results into minimal
verified claims.

## Status

Installable MVP. The plugin can create metadata-only readiness evidence from the
local AusweisApp status endpoint and can prepare a purpose-bound eID session
handoff. It does not directly read identity attributes from the card.

The official AusweisApp SDK states that local client applications do not receive
personal data directly from AusweisApp; the eID server receives the data after a
successful authentication. Therefore productive Personalausweis data extraction
requires an approved eID server or identification service, a data-processing
basis and human approval.

## Runnable MVP

Run the local preflight from the repository root:

```powershell
python plugins\noc-ausweisapp-eid\scripts\prepare_eid_session.py --json
```

For a purpose-bound preflight with a minimal claim set:

```powershell
python plugins\noc-ausweisapp-eid\scripts\prepare_eid_session.py --purpose notarial-client-intake --claim-set GivenNames,FamilyName,DateOfBirth --json
```

If a reviewed backend provides a `tcTokenURL`, pass it only for a local session
preview. The evidence stores a hash, not the full session URL:

```powershell
python plugins\noc-ausweisapp-eid\scripts\prepare_eid_session.py --tc-token-url https://example.invalid/eid/tctoken --json
```

The generated JSON follows `contracts/eid-session-evidence.schema.json` and
records only metadata: AusweisApp local status reachability, purpose, requested
claim names, approval flags, source references and policy boundaries.

## Visual Identity

The plugin uses `assets/personalausweis-logo.svg` as the source mark and the
generated `assets/icon.png` and `assets/logo.png` files for Codex plugin UI
surfaces. Source: `Personalausweis_logo.svg` from Wikimedia Commons, marked as
public domain for copyright purposes because it consists of simple geometric
forms. Wikimedia also notes that trademark restrictions may still apply. The
logo is used here only as a local recognition cue for the eID preflight plugin
and does not imply endorsement by the rights holder, Wikimedia or the Wikimedia
Foundation.

## Install Boundary

- Runs as a local Codex plugin from this repository.
- Uses the AusweisApp localhost status endpoint for metadata-only readiness.
- Requires `noc-cyberjack-rfid` first when a physical USB reader path must be
  confirmed.
- Requires an approved eID server, eID service or identification service before
  real identity attributes are received by a backend.
- Keeps PINs, CAN, PUK, card raw data, full identity dumps, session cookies,
  access tokens, certificates and production `tcTokenURL` values out of Git.
- Produces evidence metadata before any sensitive action.
- Requires human approval for production eID transactions, personal-data
  processing, backend assertion import and IAM projection.

## Day0

- Confirm the purpose, tenant, role, reviewer and minimal claim set.
- Confirm AusweisApp is installed and reachable locally.
- Confirm Online-Ausweisfunktion and six-digit PIN are available with the human
  holder; do not request or store the PIN.
- Confirm whether the reader path is smartphone-as-card-reader or USB reader.
- For USB reader paths, run `noc-cyberjack-rfid` first.
- Confirm the backend route: identification service, eID service, or own eID
  server with Berechtigungszertifikat.

## Day1

- Run `scripts/prepare_eid_session.py` and attach metadata-only evidence.
- Start a productive eID transaction only after documented approval and a
  reviewed backend route.
- Import only minimal verified claims from the approved backend into the
  downstream `noc-idaas` contract.

## Day2

- Recertify AusweisApp version, localhost endpoint, eID service contract,
  Berechtigungszertifikat status, claim-set minimization and retention.
- Review failed sessions, expired assertions and purpose-binding drift.

## Required Accounts And Approvals

- Approved data-processing basis for personal data
- Approved eID server, eID service or identification service
- Berechtigungszertifikat decision where no identification service is used
- Human approval for production eID transaction
- Reviewer approval for backend assertion import
- AVV/DPA decision for SaaS identification services

See `docs/de/plugin-operations/account-and-approval-requests.md` and
`docs/en/plugin-operations/account-and-approval-requests.md` for the
consolidated request list.
