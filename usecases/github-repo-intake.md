# GitHub-Usecase-Repository-Aufnahme

Scan-Datum: 2026-05-14

Authentifizierter GitHub-Nutzer: `ofunk-nvidia`

## Entscheidungsuebersicht

| Repository | Entscheidung | Begruendung |
| --- | --- | --- |
| `ofunk/Online-GmbH-Gruendung` | Nach `usecases/online-gmbh-gruendung/` kanonisiert | Der Repository-Name bezeichnet einen konkreten notariellen Usecase. Das Repository war leer; deshalb wurden keine Quelldateien importiert. |
| `ofunk/NaaS` | Nicht pauschal verschieben; schrittweise zerlegen | Die README beschreibt eine Notariats-Workflow-Plattform mit Usecases und Workflows. Der Inhalt ist breiter als ein einzelner Usecase und muss ueber reviewte Aenderungen in [usecases/](.) und [workflows/](../workflows) zerlegt werden. |
| `ofunk/IDaaS` | Als Plugin [plugins/noc-idaas/](../plugins/noc-idaas) migriert | Das ist ein Konzept fuer Identitaetspruefung und IAM-Projektion. Es gehoert in die Plugin-Schicht, nicht in den Usecase-Katalog. |
| `ofunk/oci-landing-zone` | Nicht nach `usecases/` verschieben | Das ist Infrastruktur- und Evidenzarbeit und bereits im Plugin-Track `noc-oci-evidence` abgebildet. |
| `ofunk/PaaS` | Nicht nach `usecases/` verschieben | Das ist eine VS-Code-Erweiterung bzw. Orchestrator-Integration, kein notarieller Fachusecase. |
| `ofunk/1gem8` | Nicht nach `usecases/` verschieben | Das ist ein Startup-Workspace-Konzept, kein notarieller Fachusecase. |
| `ofunk/Steuer-aaS` | Nach [steuer-aas/](steuer-aas) kanonisiert | Das Repository war leer, wurde vom Owner aber ausdruecklich als Usecase eingeordnet. Es ist jetzt der kanonische Steuer-Readiness-Usecase fuer notar-nahe Gruendung, Gemeinnuetzigkeit, steuerliche Registrierung und Evidenz-Workflows. |
| `ofunk/AO52aaS` | Nach [ao52aas-gemeinnuetzigkeit/](ao52aas-gemeinnuetzigkeit) kanonisiert | Das Repository enthielt `docs/gemeinnuetzigkeit/` mit Material zur Gruendung eines gemeinnuetzig ausgerichteten Softwareunternehmens. Es gehoert in den Usecase-Katalog, weil es notarielle Gesellschaftsgruendung, Satzungsvorbereitung, steuerliche Gemeinnuetzigkeits-Vorpruefung und moegliche Hybridstruktur-Entscheidungen steuert. |

## Folgepunkte

- Relevantes Material aus `ofunk/NaaS` nur ueber einen reviewten
  Migrationsplan in Usecase- und Workflow-Bestandteile zerlegen.
- `ofunk/Online-GmbH-Gruendung` als externe Quellenreferenz fuehren, bis das
  Alt-Repository archiviert, umgeleitet oder formal durch dieses Repository
  ersetzt ist.
- `ofunk/AO52aaS` als externe Quellenreferenz fuehren, bis das Alt-Repository
  archiviert, umgeleitet oder formal durch dieses Repository ersetzt ist.
- `ofunk/Steuer-aaS` als externe Quellenreferenz fuehren, bis das
  Alt-Repository archiviert, umgeleitet oder formal durch dieses Repository
  ersetzt ist.
- Neue notarielle Usecases direkt unter [usecases/](.) anlegen, statt separate
  Repositories zu erzeugen, sofern keine formale Split-Entscheidung
  dokumentiert ist.
