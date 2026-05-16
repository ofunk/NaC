# Erbscheinsantrag / Nachlassangelegenheiten KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.erbscheinsantrag_nachlass`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `decedent.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten decedent.identity fachlich zu klaeren? | `open` | applicant |
| `residence.jurisdiction` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten residence.jurisdiction fachlich zu klaeren? | `open` | notary_clerk |
| `applicants.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten applicants.identity fachlich zu klaeren? | `open` | notary_clerk |
| `heirship.basis` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten heirship.basis fachlich zu klaeren? | `open` | notary |
| `family.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten family.evidence fachlich zu klaeren? | `open` | applicant |
| `dispositions.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten dispositions.evidence fachlich zu klaeren? | `open` | notary_clerk |
| `renunciations.disclaimers` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten renunciations.disclaimers fachlich zu klaeren? | `open` | notary |
| `oath.statement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten oath.statement fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.death_certificate_reference` | Dokument/Nachweis: death bescheinigung referenz | `open` |
| `doc.application_draft` | Dokument/Nachweis: anmeldung entwurf | `open` |
| `doc.family_evidence` | Dokument/Nachweis: familie nachweis | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.heirship_review` | Prueftor: erbrecht pruefung | `open` |
| `gate.oath_readiness` | Prueftor: eid bereitschaft | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
