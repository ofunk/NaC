# Schenkungsvertrag / Uebertragungsvertrag KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.schenkungsvertrag_uebertragung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `transferor.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten transferor.identity fachlich zu klaeren? | `open` | notary_clerk |
| `transferee.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten transferee.identity fachlich zu klaeren? | `open` | notary_clerk |
| `asset.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten asset.identity fachlich zu klaeren? | `open` | notary_clerk |
| `reserved.rights` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten reserved.rights fachlich zu klaeren? | `open` | notary |
| `reversion.rights` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten reversion.rights fachlich zu klaeren? | `open` | notary |
| `consideration.obligations` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consideration.obligations fachlich zu klaeren? | `open` | notary |
| `consents.approvals` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consents.approvals fachlich zu klaeren? | `open` | notary_clerk |
| `tax.family.flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.family.flags fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.transfer_draft` | Dokument/Nachweis: uebertragung entwurf | `open` |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | `open` |
| `doc.approvals` | Dokument/Nachweis: genehmigungen | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.asset_review` | Prueftor: vermoegen pruefung | `open` |
| `gate.family_tax_review` | Prueftor: familie steuer pruefung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
