# GmbH-Gruendung / UG-Gruendung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.online_gmbh_gruendung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `company.name` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten company.name fachlich zu klaeren? | `open` | notary_clerk |
| `company.seat` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten company.seat fachlich zu klaeren? | `open` | founder |
| `company.object` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten company.object fachlich zu klaeren? | `open` | founder |
| `founders.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten founders.identity fachlich zu klaeren? | `open` | notary_clerk |
| `capital.structure` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten capital.structure fachlich zu klaeren? | `open` | notary |
| `management.appointment` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten management.appointment fachlich zu klaeren? | `open` | notary_clerk |
| `register.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten register.route fachlich zu klaeren? | `open` | notary_clerk |
| `beneficial.owner.flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten beneficial.owner.flags fachlich zu klaeren? | `open` | notary |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.articles` | Dokument/Nachweis: satzung | `open` |
| `doc.shareholder_list` | Dokument/Nachweis: gesellschafter list | `open` |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.card_xnp_readiness` | Prueftor: karte xnp bereitschaft | `open` |
| `gate.register_filing_ready` | Prueftor: register einreichung ready | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
