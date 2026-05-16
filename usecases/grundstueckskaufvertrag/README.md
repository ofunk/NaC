# Grundstueckskaufvertrag

Status: KG-Basis
KG-Knoten: `case.grundstueckskaufvertrag`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.311b`, `src.gbo`

## Ziel

Legacy-Starteralias fuer usecases/immobilienkaufvertrag; bleibt zur Kompatibilitaet erhalten, waehrend neue Workflow-Arbeit den kanonischen Usecase nutzt.

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
| `property.identity` | Welches Grundstueck, Grundbuchblatt, Flurstueck, Einheit oder welche aktuelle Bezeichnung identifiziert den Gegenstand? | notary_clerk | `property_register_data` |
| `seller.identity` | Wer verkauft und wie werden Identitaet, Geschaeftsfaehigkeit und Vertretung geprueft? | notary_clerk | `personal_data` |
| `buyer.identity` | Wer erwirbt und welche Erwerbs-, Verbraucher- oder Berechtigtenstruktur ist zu klaeren? | notary_clerk | `personal_data` |
| `purchase.price` | Welcher Kaufpreis, Zahlungsweg, Faelligkeitsmechanismus und welche Voraussetzungen gelten? | notary | `financial_data` |
| `encumbrances.current` | Welche Rechte, Belastungen oder Beschraenkungen bleiben bestehen, werden geloescht oder uebernommen? | notary_clerk | `property_register_data` |
| `financing.required` | Ist eine Finanzierung erforderlich und muss eine Grundschuld koordiniert werden? | notary_clerk | `financial_data` |
| `possession.transfer` | Wann gehen Besitz, Nutzungen, Lasten, Gefahr, Versicherungen und oeffentliche Abgaben ueber? | notary | `mandate_metadata` |
| `public.approvals` | Welche kommunalen, steuerlichen, familien-, gerichts-, verwalter- oder behoerdlichen Genehmigungen sind erforderlich? | notary_clerk | `mandate_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.contract_draft` | Dokument/Nachweis: vertrag entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.approvals` | Dokument/Nachweis: genehmigungen | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.financing_route`: Entscheidung: finanzierung weg. Optionen: `separate`, `combined`, `not_required`, `unknown`.
- `decision.encumbrance_handling`: Entscheidung: belastung handling. Optionen: `delete`, `assume`, `preserve`, `mixed`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.land_register_review` | Prueftor: grundbuch register pruefung | notary |
| `gate.consumer_draft_period` | Prueftor: consumer entwurf frist | notary |
| `gate.execution_readiness` | Prueftor: vollzug bereitschaft | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-grundbuch-portal` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-bnotk-xnp` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

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
