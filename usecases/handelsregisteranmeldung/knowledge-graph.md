# Handelsregisteranmeldung KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.handelsregisteranmeldung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `entity.identity` | Welcher Rechtstraeger und welches Registerblatt sind betroffen? | `open` | notary_clerk |
| `event.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten event.type fachlich zu klaeren? | `open` | notary |
| `signers.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten signers.identity fachlich zu klaeren? | `open` | notary_clerk |
| `corporate.resolution` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten corporate.resolution fachlich zu klaeren? | `open` | notary |
| `attachments.required` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten attachments.required fachlich zu klaeren? | `open` | notary_clerk |
| `effective.date` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten effective.date fachlich zu klaeren? | `open` | notary |
| `xnp.route` | Welcher XNP-, Karten-, Signatur- und Uebermittlungsweg wird genutzt? | `open` | notary_clerk |
| `fees.costs` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten fees.costs fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | `open` |
| `doc.corporate_evidence` | Dokument/Nachweis: gesellschaft nachweis | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.public_certification` | Prueftor: oeffentlich beglaubigung | `open` |
| `gate.electronic_format` | Prueftor: electronic format | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
