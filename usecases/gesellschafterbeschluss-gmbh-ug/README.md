# Gesellschafterbeschluss bei GmbH/UG

Status: KG-Basis
KG-Knoten: `case.gesellschafterbeschluss_gmbh_ug`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.gmbhg.53`, `src.hgb.12`

## Ziel

Gesellschafterbeschluesse fuer Satzungsaenderungen, Kapitalmassnahmen, Geschaeftsfuehrerbestellungen, Zustimmungen zu Anteilsuebertragungen oder sonstige Gesellschaftsentscheidungen.

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
| `resolution.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten resolution.type fachlich zu klaeren? | notary | `company_data` |
| `shareholders.present` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten shareholders.present fachlich zu klaeren? | notary_clerk | `personal_or_company_data` |
| `majority.requirement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten majority.requirement fachlich zu klaeren? | notary | `company_data` |
| `articles.wording` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten articles.wording fachlich zu klaeren? | notary | `company_data` |
| `register.filing` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten register.filing fachlich zu klaeren? | notary_clerk | `technical_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.resolution_minutes` | Dokument/Nachweis: beschluss niederschrift | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.current_articles` | Dokument/Nachweis: aktuell satzung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.notarial_form`: Entscheidung: notariell form. Optionen: `notarial_deed_required`, `certified_signature`, `private_resolution_only`, `unknown`.
- `decision.register_relevance`: Entscheidung: register relevance. Optionen: `yes`, `no`, `needs_review`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.quorum_majority_review` | Prueftor: beschlussfaehigkeit majority pruefung | notary |
| `gate.register_package_ready` | Prueftor: register paket ready | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-bnotk-xnp` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-handelsregister` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-cyberjack-rfid` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

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
