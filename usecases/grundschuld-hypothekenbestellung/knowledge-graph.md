# Grundschuld / Hypothekenbestellung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.grundschuld_hypothek`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `property.identity` | Welches Grundstueck, Grundbuchblatt, Flurstueck, Einheit oder welche aktuelle Bezeichnung identifiziert den Gegenstand? | `open` | notary_clerk |
| `owner.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten owner.identity fachlich zu klaeren? | `open` | notary_clerk |
| `debtor.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten debtor.identity fachlich zu klaeren? | `open` | notary |
| `lender.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten lender.identity fachlich zu klaeren? | `open` | notary_clerk |
| `charge.amount` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten charge.amount fachlich zu klaeren? | `open` | notary_clerk |
| `security.purpose` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten security.purpose fachlich zu klaeren? | `open` | notary |
| `ranking.requirement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten ranking.requirement fachlich zu klaeren? | `open` | notary_clerk |
| `enforcement.clause` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten enforcement.clause fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.bank_instruction` | Dokument/Nachweis: bank belehrung | `open` |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.bank_instruction_review` | Prueftor: bank belehrung pruefung | `open` |
| `gate.rank_review` | Prueftor: rang pruefung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
