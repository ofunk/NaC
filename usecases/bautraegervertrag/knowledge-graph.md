# Bautraegervertrag KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.bautraegervertrag`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `developer.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten developer.identity fachlich zu klaeren? | `open` | notary_clerk |
| `buyer.identity` | Wer erwirbt und welche Erwerbs-, Verbraucher- oder Berechtigtenstruktur ist zu klaeren? | `open` | notary |
| `object.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten object.identity fachlich zu klaeren? | `open` | notary_clerk |
| `construction.specification` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten construction.specification fachlich zu klaeren? | `open` | developer |
| `installment.plan` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten installment.plan fachlich zu klaeren? | `open` | notary |
| `defects.acceptance` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten defects.acceptance fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.developer_contract_draft` | Dokument/Nachweis: developer vertrag entwurf | `open` |
| `doc.specification_package` | Dokument/Nachweis: beschreibung paket | `open` |
| `doc.land_register_state` | Dokument/Nachweis: grundbuch register state | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.consumer_draft_period` | Prueftor: consumer entwurf frist | `open` |
| `gate.installment_review` | Prueftor: rate pruefung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
