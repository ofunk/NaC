# Ehevertrag / Scheidungsfolgenvereinbarung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.ehevertrag_scheidungsfolgen`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `spouses.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten spouses.identity fachlich zu klaeren? | `open` | notary_clerk |
| `marriage.context` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten marriage.context fachlich zu klaeren? | `open` | notary |
| `property.regime` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten property.regime fachlich zu klaeren? | `open` | notary |
| `asset.disclosure` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten asset.disclosure fachlich zu klaeren? | `open` | spouses |
| `maintenance.rules` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten maintenance.rules fachlich zu klaeren? | `open` | notary |
| `pension.equalization` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten pension.equalization fachlich zu klaeren? | `open` | notary |
| `child.family.flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten child.family.flags fachlich zu klaeren? | `open` | notary |
| `asset.transfer` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten asset.transfer fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.agreement_draft` | Dokument/Nachweis: vereinbarung entwurf | `open` |
| `doc.asset_schedule_reference` | Dokument/Nachweis: vermoegen schedule referenz | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.fairness_review` | Prueftor: angemessenheit pruefung | `open` |
| `gate.simultaneous_presence` | Prueftor: gleichzeitig anwesenheit | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
