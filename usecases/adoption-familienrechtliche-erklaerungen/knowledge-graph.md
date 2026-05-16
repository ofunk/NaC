# Adoption / familienrechtliche Erklaerungen KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.adoption_familienrechtliche_erklaerungen`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `case.type` | Welche Adoptions- oder familienrechtliche Erklaerung wird benoetigt? | `open` | notary |
| `child.identity_context` | Welcher Kinder- oder Adoptivkontext ist relevant, ohne Rohdaten in Git zu speichern? | `open` | client |
| `consenting_party.identity` | Wer erteilt die Zustimmung und sind Geschaeftsfaehigkeit, Alter oder Unterstuetzungsbedarf geklaert? | `open` | notary |
| `court.destination` | Welches Familiengericht erhaelt die Erklaerung und welche Referenz wird verwendet? | `open` | notary_clerk |
| `irrevocability.warning` | Welche Belehrungen zu Unwiderruflichkeit, Bedingungen oder Fristen muessen dokumentiert werden? | `open` | notary |
| `additional.approvals` | Sind elterliche, vormundschaftliche, ehebezogene, behoerdliche oder gerichtliche Zustimmungen relevant? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.consent_declaration` | Dokument/Nachweis: zustimmung erklaerung | `open` |
| `doc.court_reference` | Dokument/Nachweis: gericht referenz | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.capacity_and_warning` | Prueftor: geschaeftsfaehigkeit und belehrung | `open` |
| `gate.court_delivery` | Prueftor: gericht zustellung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
