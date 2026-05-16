# Teilungserklaerung nach WEG KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.teilungserklaerung_weg`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `property.identity` | Welches Grundstueck, Grundbuchblatt, Flurstueck, Einheit oder welche aktuelle Bezeichnung identifiziert den Gegenstand? | `open` | notary_clerk |
| `owner.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten owner.identity fachlich zu klaeren? | `open` | notary |
| `unit.structure` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten unit.structure fachlich zu klaeren? | `open` | client |
| `ownership.shares` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten ownership.shares fachlich zu klaeren? | `open` | client |
| `plans.certificates` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten plans.certificates fachlich zu klaeren? | `open` | client |
| `encumbrance.handling` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten encumbrance.handling fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.division_declaration` | Dokument/Nachweis: teilung erklaerung | `open` |
| `doc.plans_certificate` | Dokument/Nachweis: plaene bescheinigung | `open` |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.plan_certificate_review` | Prueftor: plan bescheinigung pruefung | `open` |
| `gate.land_register_implementation` | Prueftor: grundbuch register umsetzung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
