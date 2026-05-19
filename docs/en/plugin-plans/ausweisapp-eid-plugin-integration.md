# AusweisApp eID Plugin Integration

## Purpose

This plan adds a local AusweisApp eID adapter next to `noc-idaas`. The
`noc-ausweisapp-eid` plugin checks local AusweisApp reachability, prepares a
purpose-bound eID session and creates metadata-only evidence. It does not read
Personalausweis identity data directly from the card into Codex.

The official AusweisApp documentation separates these layers clearly. Users
need an activated online ID function, a known six-digit PIN, the AusweisApp and
an NFC-capable smartphone or USB card reader. The SDK documentation also states
that local client applications do not receive personal data directly from
AusweisApp; the data is received by the backend, for example the eID server,
after successful authentication. Service providers need a connection to an eID
server, eID service or identification service and, depending on the model, an
authorization certificate.

## Fit In The NoC Concept

This is a new local plugin, but it does not replace the existing IDaaS layer:

- `noc-cyberjack-rfid` checks card reader, PC/SC, morris and local workstation
  readiness.
- `noc-ausweisapp-eid` checks AusweisApp status, purpose, claim set and the eID
  session boundary.
- `noc-idaas` turns approved backend assertions into minimal verified claims
  and optional IAM projection.

## Day0

- Define purpose, tenant, role, reviewer and minimal claim set.
- Decide whether the reader path is smartphone-as-card-reader or USB card
  reader.
- For USB card reader paths, run `noc-cyberjack-rfid` first.
- Check AusweisApp installation and the local status endpoint.
- Confirm online ID function, six-digit PIN and card availability only as human
  prerequisites; never request PIN, CAN or PUK.
- Define the backend route: identification service, eID service or own eID
  server with authorization certificate where required.
- Define privacy basis, DPA need and retention.

## Day1

- Generate metadata-only evidence:

```powershell
python plugins\noc-ausweisapp-eid\scripts\prepare_eid_session.py --json
```

- If a reviewed backend provides a `tcTokenURL`, use it only locally and store
  only its hash in evidence.
- Start productive eID transactions only after documented human approval.
- Review the backend assertion and pass only the approved minimal claim set to
  `noc-idaas`.

## Day2

- Recertify AusweisApp version, reader path, eID service contract,
  authorization certificate, claim set, retention and purpose binding.
- Track failed sessions, expired assertions and revocations.
- Recheck DPA and exit path when changing the eID service or identification
  service.

## Safety Boundaries

- No PINs, CAN, PUK, card raw data, full identity-document dumps, session
  cookies, access tokens, certificates or private keys in the repository.
- No real personal data to LLMs without documented approval and processing
  basis.
- Codex may check AusweisApp readiness and prepare sessions, but must not claim
  that it can directly read local Personalausweis identity data.
- Identity claims may only be imported from an approved backend.

## Sources

- [AusweisApp: Das brauchen Sie](https://www.ausweisapp.bund.de/das-brauchen-sie)
- [AusweisApp SDK: Introduction](https://www.ausweisapp.bund.de/sdk/intro.html)
- [AusweisApp SDK: Desktop](https://www.ausweisapp.bund.de/sdk/desktop.html)
- [AusweisApp: So werden Sie Diensteanbieter](https://www.ausweisapp.bund.de/so-werden-sie-diensteanbieter)
