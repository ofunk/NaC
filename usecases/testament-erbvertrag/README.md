# Testament / Erbvertrag

Status: KG-Basis
KG-Knoten: `case.testament_erbvertrag`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`

## Ziel

Vorbereitung und Beurkundung letztwilliger Verfuegungen oder Erbvertraege mit Testierfaehigkeit, Familiensituation, Vermoegen, Vorverfuegungen und Verwahrung.

Deutsch ist fuer diesen Usecase die fuehrende fachliche Sprache. Technische IDs, Plugin-Namen und Workflow-Schluessel bleiben stabile Identifier.

## Umfang

- Fachliche Aufnahme der offenen Informationsknoten aus der KG-Tabelle.
- Erstellung oder Pruefung der erforderlichen Urkunden-, Antrags- und Nachweispakete.
- Review-Gates fuer Identitaet, Vertretung, Datenschutz, Fristen, Fachpruefung und Einreichungsreife.
- Nachweisfuehrung ausschliesslich ueber Metadaten oder freigegebene externe Evidenzspeicher.

## Ausserhalb des Umfangs

- Keine Speicherung echter Mandatswerte, personenbezogener Rohdaten oder Secrets in Git.
- Keine automatische fachliche Rechtsentscheidung ohne notarielle Pruefung und Freigabe.
- Keine Umgehung von Vier-Augen-Freigaben, gesetzlichen Formvorgaben oder lokalen Notariatsprozessen.

## Erforderliche Informationsknoten

| Knoten | Fachliche Klaerung | Rolle | Datenschutzklasse |
| --- | --- | --- | --- |
| `testator.identity` | Wer errichtet die Verfuegung und wie werden Identitaet und Testierfaehigkeit geprueft? | notary | `personal_data` |
| `capacity.flags` | Gibt es Hinweise zu Geschaeftsfaehigkeit, Sprache, Hoeren, Sehen, Krankheit oder Unterstuetzung? | notary | `sensitive_personal_data` |
| `family.structure` | Welche Ehegatten, Kinder, Angehoerige, fruehere Ehen oder Abhaengigkeiten sind relevant? | testator | `family_data` |
| `assets.categories` | Welche relevanten Vermoegenskategorien bestehen, ohne Detailwerte in Git zu speichern? | testator | `financial_data` |
| `dispositions.wishes` | Wer soll erben, Vermaechtnisse erhalten, Testamentsvollstrecker sein oder Bedingungen unterliegen? | testator | `sensitive_personal_data` |
| `prior.dispositions` | Gibt es fruehere Verfuegungen und sind sie widerruflich oder bindend? | notary | `sensitive_legal_data` |
| `executor.choice` | Sollen Testamentsvollstrecker, Ersatzerben, Sorgerechtswuensche oder Verwaltungsregeln aufgenommen werden? | testator | `sensitive_personal_data` |
| `custody.register` | Welche Verwahrungs- und Registrierschritte sind nach der Beurkundung erforderlich? | notary_clerk | `mandate_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.disposition_draft` | Dokument/Nachweis: verfuegung entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.prior_dispositions` | Dokument/Nachweis: vorherig verfuegungen | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.instrument_type`: Entscheidung: instrument art. Optionen: `single_testament`, `joint_will`, `inheritance_contract`, `unknown`.
- `decision.executor`: Entscheidung: testamentsvollstrecker. Optionen: `yes`, `no`, `needs_review`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.capacity_review` | Prueftor: geschaeftsfaehigkeit pruefung | notary |
| `gate.binding_effect_review` | Prueftor: bindung wirkung pruefung | notary |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

## Lieferaufgaben

1. Informationsknoten mit synthetischen oder metadatenbasierten Beispielen pruefen.
2. Erforderliche Dokument- und Nachweisreferenzen fachlich abgleichen.
3. Prueftore mit Verantwortlichkeiten und Blockadewirkung validieren.
4. Workflow- und Plugin-Abhaengigkeiten gegen die genehmigte Zielumgebung pruefen.
5. Aenderungen nur ueber Review, Freigabe und GitOps-Vollzug uebernehmen.

## Annahmekriterien

- Die deutsch gefuehrte Review-Sicht ist vollstaendig und verweist auf den lokalen KG.
- Alle `value`-Felder im KG bleiben leer oder `null`.
- Personenbezogene oder mandatsbezogene Rohdaten werden nicht in Git gespeichert.
- Relevante Prueftore blockieren Entwurf, Beurkundung, Beglaubigung oder Einreichung bis zur Freigabe.
- Nachweise werden nur als Metadaten oder externe Evidenzreferenzen gefuehrt.
