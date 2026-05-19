# Plugin Gantt

Last update: 2026-05-19

```mermaid
gantt
    title Plugin delivery plan
    dateFormat  YYYY-MM-DD
    axisFormat  %Y-%m

    section Core gates
    Regulated core manifest and skill baseline :done,   p1, 2026-04-01, 2026-05-14
    Plugin validation in quality gate          :done,   p2, 2026-04-15, 2026-05-14
    Marketplace packaging policy               :active, p3, 2026-05-14, 14d
    Plugin logo and README catalog             :active, p3a, 2026-05-16, 7d
    IDaaS eID/IAM companion                    :active, p4, 2026-05-14, 14d
    AusweisApp eID local preflight             :active, p4a, 2026-05-16, 14d

    section Notary entry gates
    CyberJack RFID readiness plugin            :active, p5, 2026-05-01, 21d
    Local operator HW bridge                   :done,   p5a, 2026-05-19, 1d
    BNotK XNP readiness plugin                 :active, p6, after p5, 21d
    beN notary mailbox companion               :active, p6b, 2026-05-16, 14d
    PKCS7 certificate-bundle evidence plugin   :active, p6a, 2026-05-15, 14d
    Handelsregister plugin                     :active, p7, after p6, 28d

    section Follow-up plugins
    beA portal companion                       :active, p8, 2026-05-16, 28d
    Grundbuch portal companion                 :        p9, 2026-06-15, 28d
    ELSTER ERiC companion                      :        p10, 2026-07-01, 28d
    OCI evidence companion                     :        p11, 2026-07-01, 28d
```

## Status

| Plugin | Purpose | Status | Next gate |
| --- | --- | --- | --- |
| `noc-regulated-core` | Shared regulated workflow guardrails | Baseline ready | Recheck GPT Store/workspace packaging assumptions. |
| `noc-idaas` | German eID verification and IAM projection readiness | Active | Confirm connector boundary and data-processing basis before any production pilot. |
| `noc-ausweisapp-eid` | Local AusweisApp eID session preflight without PIN or identity dumps | Active | Installable MVP added; next gate is workstation validation against the local AusweisApp status endpoint and an approved eID backend route. |
| `noc-cyberjack-rfid` | Local card, RFID-off, SAK and XNP local-interface readiness | Active | Windows DriverPackage, morris middleware, optional morris loopback API/PCSC probe, Linux driver preflight and CLI-started local Operator-Webapp bridge are implemented; current local gate still needs a connected cyberJack reader or manual attestation. |
| `noc-bnotk-xnp` | XNP authentication readiness | Active | Runnable local reader-prompt evidence now binds XNP preflight to the CyberJack gate and can pass through the optional morris API probe; next gate is workstation validation with XNP installed. |
| `noc-ben-portal` | beN notary mailbox companion | Active | Installable MVP added with NotarNet beN visual identity, XNP-first Day0 boundary and local metadata-only preflight; next gate is workstation validation with XNP and beN installed. |
| `noc-pkcs7-certbundle` | Local PKCS#7/P7B certificate-bundle evidence without signing | Active | Installable MVP added with metadata-only local inspection, no PFX/PKCS#12 import, no private-key access and no signature operation; CI hardening removes PEM-shaped test literals from source fixtures. |
| `noc-handelsregister` | Register filing readiness | Active | Bind to GmbH formation usecase. |
| `noc-bea-portal` | beA workflow companion | Active | BRaK beA visual identity is bound to the plugin manifest and rendered assets; next gate is local Client Security and card-reader readiness scripting. |
| `noc-elster-eric` | ELSTER/ERiC companion | Planned | Keep separate from notarial core unless needed. |
| `noc-grundbuch-portal` | Land register companion | Planned | Bind to purchase-contract starter. |
| `noc-oci-evidence` | OCI evidence operations | Planned | Keep as infrastructure/evidence plugin, not a usecase. |

## Packaging Note

OpenAI GPT Store publication and workspace app installation are different
channels. Public GPT Store packages must be checked against current OpenAI
publishing rules before release; workspace-only apps and internal notary pilots
remain a separate track.

## Visual Catalog Note

[plugins/README.md](README.md) now acts as the readable plugin catalog with
logo/icon assets, primary workflow links, source links and operating-boundary
summaries for every installable plugin.
