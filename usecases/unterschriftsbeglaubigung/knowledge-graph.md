# Beglaubigung von Unterschriften KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.unterschriftsbeglaubigung`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `signer.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten signer.identity fachlich zu klaeren? | `open` | notary_clerk |
| `document.purpose` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten document.purpose fachlich zu klaeren? | `open` | notary_clerk |
| `signature.mode` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten signature.mode fachlich zu klaeren? | `open` | notary |
| `language.understanding` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten language.understanding fachlich zu klaeren? | `open` | notary |
| `representation.context` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten representation.context fachlich zu klaeren? | `open` | notary_clerk |
| `copies.routing` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten copies.routing fachlich zu klaeren? | `open` | notary_clerk |
| `special.form` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten special.form fachlich zu klaeren? | `open` | notary |
| `fee.metadata` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten fee.metadata fachlich zu klaeren? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.signed_document` | Dokument/Nachweis: signed dokument | `open` |
| `doc.certification_note` | Dokument/Nachweis: beglaubigung note | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.identity_and_signature` | Prueftor: identitaet und unterschrift | `open` |
| `gate.form_route` | Prueftor: form weg | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
