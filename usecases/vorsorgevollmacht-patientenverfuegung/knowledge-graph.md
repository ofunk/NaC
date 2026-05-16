# Vorsorgevollmacht und Patientenverfuegung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.vorsorgevollmacht_patientenverfuegung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `principal.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten principal.identity fachlich zu klaeren? | `open` | notary |
| `agent.identities` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten agent.identities fachlich zu klaeren? | `open` | principal |
| `authority.financial` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten authority.financial fachlich zu klaeren? | `open` | principal |
| `authority.health` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten authority.health fachlich zu klaeren? | `open` | principal |
| `patient.directive` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten patient.directive fachlich zu klaeren? | `open` | principal |
| `effectiveness.rules` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten effectiveness.rules fachlich zu klaeren? | `open` | notary |
| `self_dealing.release` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten self_dealing.release fachlich zu klaeren? | `open` | notary |
| `central_register` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten central_register fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.power_of_attorney_draft` | Dokument/Nachweis: vollmacht of attorney entwurf | `open` |
| `doc.patient_directive_draft` | Dokument/Nachweis: patient verfuegung entwurf | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.capacity_review` | Prueftor: geschaeftsfaehigkeit pruefung | `open` |
| `gate.health_scope_review` | Prueftor: gesundheit umfang pruefung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
