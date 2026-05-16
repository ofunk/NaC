# Vereinsregisteranmeldung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.vereinsregisteranmeldung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `association.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten association.identity fachlich zu klaeren? | `open` | notary_clerk |
| `filing.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten filing.type fachlich zu klaeren? | `open` | notary |
| `board.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten board.identity fachlich zu klaeren? | `open` | notary_clerk |
| `resolution.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten resolution.evidence fachlich zu klaeren? | `open` | association |
| `articles.current` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten articles.current fachlich zu klaeren? | `open` | association |
| `filing.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten filing.route fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | `open` |
| `doc.minutes_resolution` | Dokument/Nachweis: niederschrift beschluss | `open` |
| `doc.articles` | Dokument/Nachweis: satzung | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.signer_authority` | Prueftor: unterzeichner befugnis | `open` |
| `gate.register_package_ready` | Prueftor: register paket ready | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
