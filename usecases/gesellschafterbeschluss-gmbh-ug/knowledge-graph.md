# Gesellschafterbeschluss bei GmbH/UG KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.gesellschafterbeschluss_gmbh_ug`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `company.identity` | Welche Gesellschafts- und Registerdaten bestimmen den Zielrechtstraeger? | `open` | notary_clerk |
| `resolution.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten resolution.type fachlich zu klaeren? | `open` | notary |
| `shareholders.present` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten shareholders.present fachlich zu klaeren? | `open` | notary_clerk |
| `majority.requirement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten majority.requirement fachlich zu klaeren? | `open` | notary |
| `articles.wording` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten articles.wording fachlich zu klaeren? | `open` | notary |
| `register.filing` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten register.filing fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.resolution_minutes` | Dokument/Nachweis: beschluss niederschrift | `open` |
| `doc.current_articles` | Dokument/Nachweis: aktuell satzung | `open` |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.quorum_majority_review` | Prueftor: beschlussfaehigkeit majority pruefung | `open` |
| `gate.register_package_ready` | Prueftor: register paket ready | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
