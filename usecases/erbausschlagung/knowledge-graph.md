# Erbausschlagung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.erbausschlagung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `decedent.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten decedent.identity fachlich zu klaeren? | `open` | applicant |
| `renouncer.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten renouncer.identity fachlich zu klaeren? | `open` | notary |
| `deadline.status` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten deadline.status fachlich zu klaeren? | `open` | notary |
| `heirship.basis` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten heirship.basis fachlich zu klaeren? | `open` | applicant |
| `representation.minors` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten representation.minors fachlich zu klaeren? | `open` | notary |
| `delivery.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten delivery.route fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.renunciation_declaration` | Dokument/Nachweis: ausschlagung erklaerung | `open` |
| `doc.death_or_court_reference` | Dokument/Nachweis: tod oder gericht referenz | `open` |
| `doc.approval_evidence` | Dokument/Nachweis: genehmigung nachweis | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.deadline_review` | Prueftor: frist pruefung | `open` |
| `gate.court_delivery` | Prueftor: gericht zustellung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
