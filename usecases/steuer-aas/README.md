# Steuer-aaS Steuer-Readiness

Status: KG-Basis
KG-Knoten: `case.steuer_aas`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`

## Ziel

Steuer-Readiness-Usecase fuer deterministische Aufnahme, ELSTER-nahe Vorbereitung und Pruefnachweise ohne echte Steuerdaten im Git-Repository.

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
| `tax.subject` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.subject fachlich zu klaeren? | tax_clerk | `tax_data` |
| `tax.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.type fachlich zu klaeren? | tax_clerk | `tax_data` |
| `period.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten period.scope fachlich zu klaeren? | tax_clerk | `deadline_data` |
| `elster.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten elster.identity fachlich zu klaeren? | system_betreuer | `technical_metadata` |
| `documents.package` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten documents.package fachlich zu klaeren? | tax_clerk | `metadata_only` |
| `audit.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten audit.evidence fachlich zu klaeren? | compliance | `metadata_only` |

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
