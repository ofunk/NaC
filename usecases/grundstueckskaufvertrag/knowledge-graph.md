# Grundstueckskaufvertrag KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `legacy-alias`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.grundstueckskaufvertrag`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `property.identity` | Welches Grundstueck, Grundbuchblatt, Flurstueck, Einheit oder welche aktuelle Bezeichnung identifiziert den Gegenstand? | `open` | notary_clerk |
| `seller.identity` | Wer verkauft und wie werden Identitaet, Geschaeftsfaehigkeit und Vertretung geprueft? | `open` | notary_clerk |
| `buyer.identity` | Wer erwirbt und welche Erwerbs-, Verbraucher- oder Berechtigtenstruktur ist zu klaeren? | `open` | notary_clerk |
| `purchase.price` | Welcher Kaufpreis, Zahlungsweg, Faelligkeitsmechanismus und welche Voraussetzungen gelten? | `open` | notary |
| `encumbrances.current` | Welche Rechte, Belastungen oder Beschraenkungen bleiben bestehen, werden geloescht oder uebernommen? | `open` | notary_clerk |
| `financing.required` | Ist eine Finanzierung erforderlich und muss eine Grundschuld koordiniert werden? | `open` | notary_clerk |
| `possession.transfer` | Wann gehen Besitz, Nutzungen, Lasten, Gefahr, Versicherungen und oeffentliche Abgaben ueber? | `open` | notary |
| `public.approvals` | Welche kommunalen, steuerlichen, familien-, gerichts-, verwalter- oder behoerdlichen Genehmigungen sind erforderlich? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | `open` |
| `doc.contract_draft` | Dokument/Nachweis: vertrag entwurf | `open` |
| `doc.approvals` | Dokument/Nachweis: genehmigungen | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.land_register_review` | Prueftor: grundbuch register pruefung | `open` |
| `gate.consumer_draft_period` | Prueftor: consumer entwurf frist | `open` |
| `gate.execution_readiness` | Prueftor: vollzug bereitschaft | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
