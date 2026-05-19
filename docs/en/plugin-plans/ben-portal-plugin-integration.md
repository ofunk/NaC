# beN Portal Plugin Integration Plan

Status: `active`

## Goal

This plan defines how NoC supports workflows around the German special electronic notary mailbox, `beN`, without replacing beN, XNP or the official systems of the Bundesnotarkammer. The target is a local companion that checks XNP-first setup, BNotK card or token readiness, card-reader prerequisites, beN activation planning, send/receive planning and metadata-only evidence.

beN and XNP remain authoritative for mailbox access, activation, sending, receiving, signature, decryption and role-based permissions. NoC owns governance, workflow status, evidence, approval and audit.

## Source And Integration Anchors

The official NotarNet beN page provides these anchors:

- The Bundesnotarkammer sets up a special electronic notary mailbox for every notary and notary administrator.
- The notary activity entered in the notary register is decisive for setup.
- beN primarily supports secure electronic communication with courts and can also support communication with authorities, notary chambers, other notarial organizations, other notaries and lawyers through beN-to-beA communication.
- The Bundesnotarkammer provides an application for mailbox activation and for receiving and sending messages.
- beN activation is possible only after the initial XNP setup has been completed.

## Leading Decision

The first NoC implementation path is a local companion after the XNP gate. It does not perform hidden browser automation, mailbox synchronization or direct XNP/beN API actions. The safe starting point is a local preflight that records XNP setup, card-reader path, beN availability, role context and NoC evidence.

## Visual Store Identity

The plugin uses the beN logo asset from the official NotarNet beN product page as its store and composer recognition mark. This visual binding is only a recognition cue for the local NoC companion. beN, XNP and the official BNotK/NotarNet systems remain authoritative; trademark or usage rights are not transferred by this repository.

## Plugin Boundaries

The plugin may:

- check XNP first setup and local workstation context,
- prepare BNotK card, token and card-reader readiness checklists,
- prepare beN activation, receive, send, beN-to-beA and export plan previews,
- record metadata, hashes and explicit attestations supplied by the user,
- report drift after XNP, beN, driver or card-reader changes.

The plugin must not:

- store PINs, card raw data, certificates, private keys, XNP API keys or mailbox secrets,
- control beN or XNP from the cloud,
- send, receive or acknowledge messages without local user action,
- scrape protected mailbox content,
- replace notarial responsibility,
- upload notarial matter content to an LLM without approved processing basis.

## Proposed Plugin API

### Readiness And Diagnosis

- `ben.health`
- `ben.check_xnp_first_setup`
- `ben.check_card_reader_path`
- `ben.check_application_available`

### Process Preparation

- `ben.prepare_activation`
- `ben.prepare_incoming_message`
- `ben.prepare_outgoing_message`
- `ben.prepare_ben_to_bea`

### Evidence And Audit

- `ben.record_user_attestation`
- `ben.record_export`
- `ben.get_evidence`

## MVP Scope

- Installable `noc-ben-portal` plugin.
- Local `prepare_ben_session.py` preflight.
- Store and composer logo from the NotarNet beN page.
- XNP-first Day0 gate.
- Card-reader/token boundary without PIN or card-data handling.
- Metadata-only evidence.

## Not In The MVP

- Direct beN message retrieval.
- Direct beN message sending.
- Automatic mailbox activation.
- Automatic PIN entry.
- Direct XNP or beN API usage.
- Browser scraping or RPA against protected beN surfaces.

## Acceptance Criteria For The First PR

- Plugin manifest and marketplace entry exist.
- Official NotarNet source is linked.
- The plugin remains companion-only and binds to XNP-first setup.
- No secrets, PINs, card values, XNP API keys or notarial matter content are stored in the repository.
- The strict quality gate passes.

## Sources

- NotarNet beN: https://notarnet.de/produkte/ben
- NotarNet XNP: https://notarnet.de/produkte/xnp
- BNotK Online Help XNP: https://onlinehilfe.bnotk.de/technischer-bereich/systembetreuer/xnp-die-basisanwendung-der-bnotk.html
