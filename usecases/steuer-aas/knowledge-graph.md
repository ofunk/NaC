# Steuer-aaS Steuer-Readiness KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `active-intake`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.steuer_aas`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `tax.subject` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.subject fachlich zu klaeren? | `open` | tax_clerk |
| `tax.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.type fachlich zu klaeren? | `open` | tax_clerk |
| `period.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten period.scope fachlich zu klaeren? | `open` | tax_clerk |
| `elster.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten elster.identity fachlich zu klaeren? | `open` | system_betreuer |
| `documents.package` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten documents.package fachlich zu klaeren? | `open` | tax_clerk |
| `audit.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten audit.evidence fachlich zu klaeren? | `open` | compliance |

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
