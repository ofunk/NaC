# Geschaeftsanteilsuebertragung GmbH

Status: KG-Basis
KG-Knoten: `case.geschaeftsanteilsuebertragung_gmbh`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.gmbhg.15`, `src.hgb.12`

## Ziel

Verkauf, Schenkung oder sonstige Uebertragung von GmbH-Geschaeftsanteilen mit Beteiligten, Anteilskette, Zustimmungsvorbehalten, Gegenleistung, Gesellschafterliste und Registervollzug.

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
| `company.identity` | Welche Gesellschafts- und Registerdaten bestimmen den Zielrechtstraeger? | notary_clerk | `company_register_data` |
| `share.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten share.identity fachlich zu klaeren? | notary | `company_financial_data` |
| `seller.identity` | Wer verkauft und wie werden Identitaet, Geschaeftsfaehigkeit und Vertretung geprueft? | notary_clerk | `personal_or_company_data` |
| `buyer.identity` | Wer erwirbt und welche Erwerbs-, Verbraucher- oder Berechtigtenstruktur ist zu klaeren? | notary | `compliance_data` |
| `consents.restrictions` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consents.restrictions fachlich zu klaeren? | notary | `company_data` |
| `consideration.tax` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consideration.tax fachlich zu klaeren? | notary | `financial_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.transfer_agreement` | Dokument/Nachweis: uebertragung vereinbarung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.shareholder_list` | Dokument/Nachweis: gesellschafter list | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.consent_evidence` | Dokument/Nachweis: zustimmung nachweis | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.transfer_type`: Entscheidung: uebertragung art. Optionen: `sale`, `gift`, `mixed`, `trust_or_pool`, `unknown`.
- `decision.consent_needed`: Entscheidung: zustimmung needed. Optionen: `yes`, `no`, `already_available`, `blocked`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.chain_of_title_review` | Prueftor: kette of title pruefung | notary |
| `gate.shareholder_list_ready` | Prueftor: gesellschafter list ready | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-bnotk-xnp` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-handelsregister` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
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
