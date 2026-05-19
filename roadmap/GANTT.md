# NoC Global Gantt

Last update: 2026-05-19

Every push must update this global Gantt. Changes under `plugins/`,
`workflows/`, or `usecases/` must also update the matching area Gantt:

- `plugins/GANTT.md`
- `workflows/GANTT.md`
- `usecases/GANTT.md`

```mermaid
gantt
    title NoC global delivery plan
    dateFormat  YYYY-MM-DD
    axisFormat  %Y-%m

    section A: Plugins and marketplace readiness
    Plugin inventory and installability gate     :done,    a1, 2026-04-01, 2026-05-14
    GPT Store and workspace packaging split      :active,  a2, 2026-05-14, 21d
    IDaaS plugin migration                       :active,  a3, 2026-05-14, 14d
    Repository consolidation ledger              :active,  a4, 2026-05-14, 7d
    PKCS7 local certificate-bundle evidence      :active,  a4a, 2026-05-15, 14d
    SBOM for AI governance baseline              :active,  a4b, 2026-05-15, 21d
    Runtime and HW minimum requirements SBOM     :active,  a4c, 2026-05-15, 14d
    AusweisApp eID local preflight               :active,  a4d, 2026-05-16, 14d
    beA card-reader companion identity           :active,  a4e, 2026-05-16, 14d
    beN notary mailbox companion                 :active,  a4f, 2026-05-16, 14d
    Plugin logo catalog and README matrix        :active,  a4g, 2026-05-16, 7d
    Notary pilot plugin readiness                :         a5, after a4, 35d
    Publication and support operations           :         a6, after a5, 28d

    section B: Notary workflows
    Workflow layer separation                    :active,  b1, 2026-05-14, 14d
    KG runtime status CLI MVP                    :done,    b1a, 2026-05-15, 1d
    Project voice and active-build docs cleanup  :done,    b1b, 2026-05-15, 1d
    START_HERE operational entry cleanup         :done,    b1c, 2026-05-15, 1d
    Documentation folder taxonomy cleanup        :done,    b1d, 2026-05-15, 1d
    Clickable documentation links rule           :done,    b1e, 2026-05-15, 1d
    Manual-only PDF export during development    :done,    b1f, 2026-05-15, 1d
    Main-merge completion reporting rule         :done,    b1g, 2026-05-15, 1d
    Repo-wide German-leading language rule       :done,    b1h, 2026-05-15, 1d
    Root README language-pair link cleanup       :done,    b1i, 2026-05-15, 1d
    Localized docs translation cleanup           :done,    b1j, 2026-05-15, 1d
    No-code KG editor contract MVP              :done,    b1k, 2026-05-15, 1d
    Local operator HW bridge                     :done,    b1l, 2026-05-19, 1d
    Skill plus Python workflow contracts         :active,  b2, 2026-05-15, 28d
    Deterministic workflow runner MVP            :active,  b3, 2026-05-15, 35d
    Day2 evidence and drift operations           :         b4, after b3, 28d

    section C: Notary usecases
    GitHub usecase intake                        :done,    c1, 2026-05-14, 1d
    Top-10 notarial KG baseline                  :done,    c2, 2026-05-15, 1d
    Next-10 notarial KG baseline                 :done,    c3, 2026-05-15, 1d
    Case-local KG folder migration               :done,    c3a, 2026-05-15, 1d
    German-leading usecase language rule         :done,    c3b, 2026-05-15, 1d
    KG editor binding for usecase KGs            :done,    c3c, 2026-05-15, 1d
    German usecase review surfaces               :done,    c3d, 2026-05-16, 1d
    GmbH formation canonicalization              :active,  c4, 2026-05-14, 21d
    AO52 nonprofit formation intake              :active,  c5, 2026-05-14, 21d
    Steuer-aaS tax usecase intake                :active,  c6, 2026-05-14, 21d
    Static KG-fed workflow state model           :active,  c7, 2026-05-15, 28d
    Pilot-ready usecase packages                 :         c8, after c7, 35d
```

## Progress Snapshot

| Track | Scope | Status | Progress | Current gate |
| --- | --- | --- | --- | --- |
| A | Installable plugins for notary offices | Active | 71% | `plugins/README.md` now provides a readable logo catalog with plugin links, source links and operating boundaries; `noc-ausweisapp-eid` now adds a local AusweisApp eID preflight boundary between card-reader readiness and IDaaS claims; `noc-bea-portal` has BRaK beA visual identity and an active card-reader/Client-Security readiness boundary; `noc-ben-portal` adds the NotarNet beN visual identity, XNP-first Day0 boundary and local metadata-only preflight for notary mailbox workflows; `noc-cyberjack-rfid` detects REINER SCT DriverPackage, morris middleware and optional morris loopback API/PCSC locally; `noc-pkcs7-certbundle` adds a separate local certificate-bundle evidence track without signing; OpenAI-backed processing has an AVV/DPA governance section; and SBOM for AI has a repo-wide baseline, minimum-requirements inventory and strict validator. |
| B | Installable skills and deterministic Python workflows | Active | 43% | First executable KG runtime package and CLI are implemented with unit tests; `START_HERE` is now the operational entry path distinct from the README overview, startup verification has environment profiles for base, plugin-dev and notary-workstation setups, docs are grouped into `eventstream/`, `issues/`, `operations/` and `service-model/`, README/index references now have clickable-link validation, PDF export is manual-only during active development, `fertig` means merged to `main` plus clean local `main`, the GitHub root README uses a Deutsch/English start table, language parity now blocks copied identical localized Markdown/text mirrors, the KG editor exposes a safe no-code form/checklist view plus patch contract, and the local Operator-Webapp now uses a CLI-started `127.0.0.1` bridge for hardware-readiness checks. |
| C | Notarial usecases such as property, register, company, association, estate, family and power-of-attorney matters | Active | 59% | Every usecase now owns a case-local static KG; German is explicit as the leading and legally binding language for German-law notarial usecases; README files, KG review views and human-readable KG values are German-led; Fachpersonal edits those KGs through the no-code editor view instead of raw JSON. |

## Rule

The strict quality gate includes `scripts/validate_gantt_progress.py`. A change
set that does not update `roadmap/GANTT.md` is not push-ready. A change set that
touches `plugins/`, `workflows/`, or `usecases/` must update the matching area
Gantt as well.
