# Bautraegervertrag

Status: KG-Basis
KG-Knoten: `case.bautraegervertrag`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.311b`, `src.bgb.650u`, `src.abschlagsv`, `src.gbo.19_29_46`

## Ziel

Kauf eines Grundstuecks oder einer Einheit vom Bautraeger mit Bauverpflichtungen, Ratenplan, Bautenstand, Sicherheiten und Verbraucherschutz-Prueftoren.

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
| `developer.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten developer.identity fachlich zu klaeren? | notary_clerk | `company_data` |
| `buyer.identity` | Wer erwirbt und welche Erwerbs-, Verbraucher- oder Berechtigtenstruktur ist zu klaeren? | notary | `personal_data` |
| `object.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten object.identity fachlich zu klaeren? | notary_clerk | `property_register_data` |
| `construction.specification` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten construction.specification fachlich zu klaeren? | developer | `property_metadata` |
| `installment.plan` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten installment.plan fachlich zu klaeren? | notary | `financial_data` |
| `defects.acceptance` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten defects.acceptance fachlich zu klaeren? | notary | `mandate_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.developer_contract_draft` | Dokument/Nachweis: developer vertrag entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.specification_package` | Dokument/Nachweis: beschreibung paket | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.land_register_state` | Dokument/Nachweis: grundbuch register state | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.payment_model`: Entscheidung: zahlung modell. Optionen: `installments`, `security_alternative`, `blocked`, `unknown`.
- `decision.object_state`: Entscheidung: gegenstand state. Optionen: `planned`, `under_construction`, `completed`, `mixed`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.consumer_draft_period` | Prueftor: consumer entwurf frist | notary |
| `gate.installment_review` | Prueftor: rate pruefung | notary |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-grundbuch-portal` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-bnotk-xnp` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-idaas` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

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
