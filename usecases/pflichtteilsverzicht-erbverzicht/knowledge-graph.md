# Pflichtteilsverzicht / Erbverzicht KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.pflichtteilsverzicht_erbverzicht`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `future_decedent.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten future_decedent.identity fachlich zu klaeren? | `open` | notary |
| `waiver_party.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten waiver_party.identity fachlich zu klaeren? | `open` | notary |
| `waiver.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten waiver.scope fachlich zu klaeren? | `open` | notary |
| `descendant.effect` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten descendant.effect fachlich zu klaeren? | `open` | notary |
| `compensation.model` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten compensation.model fachlich zu klaeren? | `open` | client |
| `family.fairness_flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten family.fairness_flags fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.waiver_contract` | Dokument/Nachweis: verzicht vertrag | `open` |
| `doc.compensation_evidence` | Dokument/Nachweis: abfindung nachweis | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.personal_presence_review` | Prueftor: persoenlich anwesenheit pruefung | `open` |
| `gate.fairness_review` | Prueftor: angemessenheit pruefung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
