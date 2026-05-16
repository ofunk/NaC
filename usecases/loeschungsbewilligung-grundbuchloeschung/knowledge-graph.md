# Loeschungsbewilligung / Grundbuchloeschung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.loeschungsbewilligung_grundbuchloeschung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `property.identity` | Welches Grundstueck, Grundbuchblatt, Flurstueck, Einheit oder welche aktuelle Bezeichnung identifiziert den Gegenstand? | `open` | notary_clerk |
| `right.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten right.identity fachlich zu klaeren? | `open` | notary_clerk |
| `creditor.authorization` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten creditor.authorization fachlich zu klaeren? | `open` | notary |
| `owner.consent` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten owner.consent fachlich zu klaeren? | `open` | notary_clerk |
| `brief.status` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten brief.status fachlich zu klaeren? | `open` | notary_clerk |
| `filing.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten filing.route fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.deletion_consent` | Dokument/Nachweis: loeschung zustimmung | `open` |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | `open` |
| `doc.right_letter` | Dokument/Nachweis: right brief | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.authority_review` | Prueftor: befugnis pruefung | `open` |
| `gate.filing_ready` | Prueftor: einreichung ready | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
