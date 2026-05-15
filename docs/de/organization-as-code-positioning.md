# Positionierung: Notariat as Code, NoC und Enterprise Control Plane

Status: verbindliche Projektpositionierung

Letzte inhaltliche Anpassung: 2026-05-15

## Zweck

Dieses Dokument ist kein alter Konzeptzettel, sondern der verbindliche
Begriffsrahmen fuer den aktuellen NoC-Stand. Es trennt Zielmodell,
Betriebsprinzip, Produktname und implementierte Repo-Flaechen.

Der laufende Entwicklungsstand steht in [roadmap/BUILD_NOW.md](../../roadmap/BUILD_NOW.md).

## Begriffsrahmen

| Begriff | Bedeutung in diesem Repo |
| --- | --- |
| `Notariat as Code` | Zielmodell: notarielle Vorgangsarten, Rollen, Freigaben, Nachweise, Plugins und Workflows werden deklarativ, versioniert und pruefbar beschrieben. |
| `NoC` | Konkrete Referenzumsetzung dieses Zielmodells in diesem Repository. |
| `Enterprise Control Plane` | Plattformname fuer die Bedien-, Kontroll- und Ausfuehrungsschicht von NoC. |
| `Enterprise GitOps` | Operatives Steuerungsprinzip: Aenderungen laufen ueber Branch, Pull Request, Review, Freigabe, Checks und Merge. |

`Organization as Code` bleibt die allgemeinere Oberkategorie. Dieses Repo ist
die notariatsspezifische Auspraegung: `Notariat as Code`.

## Was heute konkret ist

NoC ist nicht mehr nur Dokumentation. Auf `main` gibt es am 2026-05-15 eine
erste ausfuehrbare notariatsspezifische Runtime-Flaeche:

- usecase-lokale statische Knowledge Graphs unter [usecases/](../../usecases),
  jeweils als `knowledge-graph.graph.json` und `knowledge-graph.md`,
- eine KG-Validierung ueber [scripts/validate_knowledge_graph.py](../../scripts/validate_knowledge_graph.py),
- eine notarielle KG-Runtime unter [src/notary_kg/](../../src/notary_kg),
- eine CLI unter [scripts/notary_kg.py](../../scripts/notary_kg.py),
- eine no-code KG-Editor-Ansicht fuer Fachpersonal mit Vertrag in
  [workflows/contracts/kg-editor.contract.json](../../workflows/contracts/kg-editor.contract.json),
- ein strikter Quality Gate ueber [scripts/quality_gate.py](../../scripts/quality_gate.py).

Die Produktstruktur ist verbindlich getrennt:

- [plugins/](../../plugins): installierbare Plugin-Artefakte,
- [workflows/](../../workflows): Skills, Workflow-Vertraege und deterministische
  Python-Workflows,
- [usecases/](../../usecases): konkrete notarielle Vorgangsarten mit jeweils
  eigener statischer KG/DB.

## Was bewusst nicht behauptet wird

NoC ersetzt kein vorgeschriebenes Fachsystem und keine notarielle
Berufspflichtpruefung. Das Repo behauptet aktuell auch nicht:

- produktionsreife Ende-zu-Ende-Automation fuer notarielle Vorgaenge,
- unkontrollierte SaaS-Verarbeitung von Mandatsdaten,
- Ersetzung von XNP, Kartenleser-, morris- oder Registerportal-Pflichten,
- fachliche Wahrheit durch ein LLM ohne versionierte Aenderung, Review und
  Freigabe.

Das LLM ist Eingabeoberflaeche. Verbindlich wird ein Stand erst durch
versionierte Aenderung, Validierung, Review, Merge und Nachweis.

## Architekturzuordnung

| Schicht | Aufgabe | Aktuelle Repo-Flaechen |
| --- | --- | --- |
| Intent Layer | fachliche Absicht, Policies, Rollen, Usecases | [policies/](../../policies), [usecases/](../../usecases), [prompts/de/](../../prompts/de) |
| Control Layer | Branch, Pull Request, Review, Freigabe, Rulesets | [AGENTS.md](../../AGENTS.md), [.github/copilot-instructions.md](../../.github/copilot-instructions.md), [.cursor/rules/](../../.cursor/rules) |
| Execution Layer | deterministische Runtime und Workflow-Ausfuehrung | [src/](../../src), [scripts/](../../scripts), [workflows/](../../workflows) |
| Evidence Layer | Nachweise, SBOM, Eventstream, Gantt-Fortschritt | [sbom/](../../sbom), [docs/de/eventstream/](eventstream), [roadmap/GANTT.md](../../roadmap/GANTT.md) |

## Produktversprechen

Notarielle Vorgangsarten, Plugins, Workflows, Rollen, Freigaben und Nachweise
laufen deklarativ, auditierbar und automatisiert ueber Git, ohne dass Fachseite
oder Betrieb die Compliance-Kette aus Branch, Review, Check und Merge umgehen.

## Ein-Satz-Pitch

Notariat as Code ist ein Betriebsmodell, in dem notarielle Vorgangsarten,
Plugins, Workflows, Policies und operative Aenderungen deklarativ in Git
beschrieben und ueber eine Enterprise Control Plane in pruefbare Ausfuehrung
ueberfuehrt werden.
