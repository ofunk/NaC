# Account And Approval Requests For NoC Plugins

This file is the Day0 request register for productive regulated-industry plugin use. It intentionally contains no real account names, secrets, mailbox identifiers, tax identifiers, certificate material or mandate content.

## Global Controls

| Area | Request | Needed Before | Owner | Notes |
| --- | --- | --- | --- | --- |
| GitHub | Repository write access, branch protection, required checks and CODEOWNER review | productive plugin releases | platform owner | Private repo access must be explicit. |
| Evidence | DMS or audit store decision, retention class, hash policy and deletion hold process | any evidence import | compliance owner | Metadata-only by default. |
| Security | Secret storage decision for future connectors | any write adapter | security owner | Use local OS store or tenant Vault, not Git. |
| Review | Two-person approval matrix for regulated actions | Day1 regulated workflows | managing partner or notary | Required before card/PIN prompts, submissions, register applications, XNP/XNotar handoffs or notarial actions. |

## Plugin-Specific Requests

| Plugin | Accounts / Approvals To Request | Blocking For |
| --- | --- | --- |
| `noc-regulated-core` | GitHub repository write access; Approved reviewer roster; Evidence storage decision | Day1 productive use |
| `noc-ausweisapp-eid` | Privacy basis for personal data; Approved backend route through an identification service, eID service or own eID server; Authorization-certificate decision where no identification service is used; DPA decision for SaaS identification services; Human approval for productive eID transaction and backend assertion import | Day1 productive use |
| `noc-handelsregister` | Mode decision: citizen preflight or notary-side workflow; Completed `noc-cyberjack-rfid` and `noc-bnotk-xnp` readiness for notary-side workflows; Notary appointment or notary office workflow; Bundesnotarkammer online procedure app; eID-capable official ID and PIN; Applicant and reviewer approval for the register application package | Day1 productive use |
| `noc-bnotk-xnp` | Completed `noc-cyberjack-rfid` card/SAK readiness; BNotK/XNP access for the notary office; Local XNP login and active Amtstaetigkeitskontext; XNotar/register module or exchange-folder route; Notarial software vendor interface approval; Local workstation admin approval | Day1 productive use |
| `noc-ben-portal` | beN mailbox access; completed XNP first setup; BNotK card or approved authentication method; supported card reader for BNotK card paths; notary-office policy for beN activation, mailbox actions, exports and evidence | Day1 productive use |
| `noc-bea-portal` | beA mailbox access; beA card or approved authentication method; supported card reader for beA card paths; beA Client Security on local workstation; firm policy for eEB and exports | Day1 productive use |
| `noc-elster-eric` | ELSTER organization or user access; Local certificate or approved auth method; ERiC manufacturer registration if server-side integration is pursued; Tax representation approval | Day1 productive use |
| `noc-cyberjack-rfid` | BNotK chip/signature card or local Schneider/SCP-card availability; Security-class-3 card reader; BNotK SAK lite or XNP card path; secureFramework communication path; Approved hardware procurement; Local workstation admin approval; Driver/vendor support channel | Day1 productive use |
| `noc-grundbuch-portal` | State-specific Grundbuchportal access; Authorized professional role confirmation; Cost-center approval; Retention/DMS decision | Day1 productive use |
| `noc-oci-evidence` | OCI tenancy access; Compartment admin or delegated policy; Vault/key-management approval; Budget owner; Audit retention owner | Day1 productive use |

## External Write Adapter Hold Points

Do not implement or enable direct external write adapters until these are approved in writing:

- beA send/receive/eEB automation path, card-reader/token boundary and Client
  Security boundary.
- Card/SAK gate for BNotK chip/signature card or local Schneider/SCP-card availability, security-class-3 reader, secureFramework and no PIN capture.
- XNP/notarial software official interface contract, completed Card/SAK gate, local authentication gate, Amtstaetigkeitskontext and credential boundary.
- beN activation, send/receive and beN-to-beA path, completed XNP first setup,
  card-reader/token boundary and no mailbox content in LLM contexts.
- ELSTER/ERiC manufacturer or portal-operator onboarding, if server-side integration is pursued.
- Grundbuchportal authorized direct adapter, state-specific terms and legitimate-interest evidence.
- Handelsregister online application route, mode decision, completed Card/SAK and XNP gates for notary-side workflows, applicant authority and eID/app readiness.
- AusweisApp/eID production route, backend connection to identification service,
  eID service or own eID server, authorization-certificate decision, privacy
  basis, DPA status and no local PIN or identity-data storage.
- OCI Resource Manager apply permissions, Vault policy and audit retention.

## Day2 Recertification

- Reconfirm account ownership and role necessity at least quarterly for pilots and before production release.
- Reconfirm local workstation prerequisites after OS, XNP, beA Client Security, ERiC, browser, driver or card-reader updates.
- Re-run `python3 scripts/validate_plugins.py` after each plugin manifest change.
