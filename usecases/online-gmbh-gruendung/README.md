# GmbH-Gruendung / UG-Gruendung

Status: KG-Basis
KG-Knoten: `case.online_gmbh_gruendung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.gmbhg`, `src.hgb.12`

## Ziel

Gruendung einer GmbH oder UG mit Satzung, Gruendern, Stammkapital, Geschaeftsfuehrung, Registeranmeldung und notarseitiger Identitaets- und Signaturbereitschaft.

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
| `company.name` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten company.name fachlich zu klaeren? | notary_clerk | `company_data` |
| `company.seat` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten company.seat fachlich zu klaeren? | founder | `company_data` |
| `company.object` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten company.object fachlich zu klaeren? | founder | `company_data` |
| `founders.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten founders.identity fachlich zu klaeren? | notary_clerk | `personal_or_company_data` |
| `capital.structure` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten capital.structure fachlich zu klaeren? | notary | `financial_data` |
| `management.appointment` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten management.appointment fachlich zu klaeren? | notary_clerk | `personal_data` |
| `register.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten register.route fachlich zu klaeren? | notary_clerk | `mandate_metadata` |
| `beneficial.owner.flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten beneficial.owner.flags fachlich zu klaeren? | notary | `compliance_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.articles` | Dokument/Nachweis: satzung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.shareholder_list` | Dokument/Nachweis: gesellschafter list | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.model_protocol`: Entscheidung: modell protocol. Optionen: `model_protocol`, `individual_articles`, `unknown`.
- `decision.online_route`: Entscheidung: online weg. Optionen: `online`, `in_office`, `hybrid`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.card_xnp_readiness` | Prueftor: karte xnp bereitschaft | notary_clerk |
| `gate.register_filing_ready` | Prueftor: register einreichung ready | notary |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-cyberjack-rfid` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
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
