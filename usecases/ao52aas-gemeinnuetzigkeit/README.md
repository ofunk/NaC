# AO52 gemeinnuetziges Softwareunternehmen

Status: KG-Basis
KG-Knoten: `case.ao52aas_gemeinnuetzigkeit`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.gmbhg`, `src.hgb.12`

## Ziel

Vorbereitungs- und Readiness-Paket fuer ein gemeinnuetzig ausgerichtetes Softwareunternehmen mit Zweckbindung, Governance, Finanzierung sowie Register- und Steuerklaerungen.

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
| `purpose.model` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten purpose.model fachlich zu klaeren? | founder | `company_strategy` |
| `entity.form` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten entity.form fachlich zu klaeren? | notary_clerk | `company_register_data` |
| `funding.model` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten funding.model fachlich zu klaeren? | founder | `financial_data` |
| `governance.rules` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten governance.rules fachlich zu klaeren? | notary | `company_register_data` |
| `tax.precheck` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.precheck fachlich zu klaeren? | tax_specialist | `tax_data` |
| `software.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten software.scope fachlich zu klaeren? | founder | `business_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.intake_package` | Dokument/Nachweis: aufnahme paket | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.workflow_route`: Entscheidung: workflow weg. Optionen: `notarial_review`, `external_system_route`, `blocked`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.identity` | Prueftor: identitaet |  |
| `gate.notarial_review` | Prueftor: notariell pruefung |  |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-bnotk-xnp` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-handelsregister` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-elster-eric` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

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
