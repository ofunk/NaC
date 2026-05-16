# Vollmacht fuer Immobilien- oder Gesellschaftsgeschaefte KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.vollmacht_immobilien_gesellschaft`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `principal.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten principal.identity fachlich zu klaeren? | `open` | notary |
| `agent.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten agent.identity fachlich zu klaeren? | `open` | principal |
| `transaction.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten transaction.scope fachlich zu klaeren? | `open` | notary |
| `form.requirement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten form.requirement fachlich zu klaeren? | `open` | notary |
| `limitations.expiry` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten limitations.expiry fachlich zu klaeren? | `open` | notary |
| `delivery.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten delivery.evidence fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.power_of_attorney` | Dokument/Nachweis: vollmacht of attorney | `open` |
| `doc.scope_reference` | Dokument/Nachweis: umfang referenz | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.form_review` | Prueftor: form pruefung | `open` |
| `gate.delivery_control` | Prueftor: zustellung kontrolle | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
