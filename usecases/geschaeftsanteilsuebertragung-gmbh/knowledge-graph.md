# Geschaeftsanteilsuebertragung GmbH KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `next10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.geschaeftsanteilsuebertragung_gmbh`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `company.identity` | Welche Gesellschafts- und Registerdaten bestimmen den Zielrechtstraeger? | `open` | notary_clerk |
| `share.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten share.identity fachlich zu klaeren? | `open` | notary |
| `seller.identity` | Wer verkauft und wie werden Identitaet, Geschaeftsfaehigkeit und Vertretung geprueft? | `open` | notary_clerk |
| `buyer.identity` | Wer erwirbt und welche Erwerbs-, Verbraucher- oder Berechtigtenstruktur ist zu klaeren? | `open` | notary |
| `consents.restrictions` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consents.restrictions fachlich zu klaeren? | `open` | notary |
| `consideration.tax` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consideration.tax fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.transfer_agreement` | Dokument/Nachweis: uebertragung vereinbarung | `open` |
| `doc.shareholder_list` | Dokument/Nachweis: gesellschafter list | `open` |
| `doc.consent_evidence` | Dokument/Nachweis: zustimmung nachweis | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.chain_of_title_review` | Prueftor: kette of title pruefung | `open` |
| `gate.shareholder_list_ready` | Prueftor: gesellschafter list ready | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
