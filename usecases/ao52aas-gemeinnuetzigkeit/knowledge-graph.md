# AO52 gemeinnuetziges Softwareunternehmen KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `active-intake`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.ao52aas_gemeinnuetzigkeit`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `purpose.model` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten purpose.model fachlich zu klaeren? | `open` | founder |
| `entity.form` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten entity.form fachlich zu klaeren? | `open` | notary_clerk |
| `funding.model` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten funding.model fachlich zu klaeren? | `open` | founder |
| `governance.rules` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten governance.rules fachlich zu klaeren? | `open` | notary |
| `tax.precheck` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.precheck fachlich zu klaeren? | `open` | tax_specialist |
| `software.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten software.scope fachlich zu klaeren? | `open` | founder |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.intake_package` | Dokument/Nachweis: aufnahme paket | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.identity` | Prueftor: identitaet | `open` |
| `gate.notarial_review` | Prueftor: notariell pruefung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
