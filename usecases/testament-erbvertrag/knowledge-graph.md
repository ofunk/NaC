# Testament / Erbvertrag KG-Review-Sicht

Status: usecase-lokale statische KG-Basis
Letzte Aktualisierung: 2026-05-16
Kataloggruppe: `top10`
Usecase: [README.md](README.md)
Maschinenlesbarer KG: [knowledge-graph.graph.json](knowledge-graph.graph.json)
KG-Knoten: `case.testament_erbvertrag`

## Betriebsmodell

Diese Datei ist die deutsch gefuehrte menschliche Review-Sicht auf den usecase-lokalen statischen KG. Die JSON-Datei daneben ist der maschinenlesbare Workflow-Zustand. Workflows duerfen Status- und Evidenzreferenzen nur ueber reviewte Git-Aenderungen fortschreiben; echte Mandatswerte bleiben ausserhalb des Repository.

## Offene Informationsknoten

| ID | Fachliche Klaerung | Status | Rolle |
| --- | --- | --- | --- |
| `testator.identity` | Wer errichtet die Verfuegung und wie werden Identitaet und Testierfaehigkeit geprueft? | `open` | notary |
| `capacity.flags` | Gibt es Hinweise zu Geschaeftsfaehigkeit, Sprache, Hoeren, Sehen, Krankheit oder Unterstuetzung? | `open` | notary |
| `family.structure` | Welche Ehegatten, Kinder, Angehoerige, fruehere Ehen oder Abhaengigkeiten sind relevant? | `open` | testator |
| `assets.categories` | Welche relevanten Vermoegenskategorien bestehen, ohne Detailwerte in Git zu speichern? | `open` | testator |
| `dispositions.wishes` | Wer soll erben, Vermaechtnisse erhalten, Testamentsvollstrecker sein oder Bedingungen unterliegen? | `open` | testator |
| `prior.dispositions` | Gibt es fruehere Verfuegungen und sind sie widerruflich oder bindend? | `open` | notary |
| `executor.choice` | Sollen Testamentsvollstrecker, Ersatzerben, Sorgerechtswuensche oder Verwaltungsregeln aufgenommen werden? | `open` | testator |
| `custody.register` | Welche Verwahrungs- und Registrierschritte sind nach der Beurkundung erforderlich? | `open` | notary_clerk |

## Dokumente

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `doc.disposition_draft` | Dokument/Nachweis: verfuegung entwurf | `open` |
| `doc.prior_dispositions` | Dokument/Nachweis: vorherig verfuegungen | `open` |

## Prueftore

| ID | Bezeichnung | Status |
| --- | --- | --- |
| `gate.capacity_review` | Prueftor: geschaeftsfaehigkeit pruefung | `open` |
| `gate.binding_effect_review` | Prueftor: bindung wirkung pruefung | `open` |

## Datenschutzregel

Alle `value`-Felder bleiben in Git leer oder `null`. Der KG speichert nur Workflow-Status, offene fachliche Klaerungen und Evidenzreferenzen; echte Mandatsdaten, Secrets und personenbezogene Rohdaten gehoeren nicht in dieses Repository.
