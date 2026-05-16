# Ehevertrag / Scheidungsfolgenvereinbarung

Status: KG-Basis
KG-Knoten: `case.ehevertrag_scheidungsfolgen`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.1410`

## Ziel

Ehevertrag oder Scheidungsfolgenvereinbarung mit Gueterstand, Ausgleich, Versorgung, Unterhalt, Vermoegensauseinandersetzung und Angemessenheitspruefung.

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
| `spouses.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten spouses.identity fachlich zu klaeren? | notary_clerk | `personal_data` |
| `marriage.context` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten marriage.context fachlich zu klaeren? | notary | `family_data` |
| `property.regime` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten property.regime fachlich zu klaeren? | notary | `financial_data` |
| `asset.disclosure` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten asset.disclosure fachlich zu klaeren? | spouses | `financial_data` |
| `maintenance.rules` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten maintenance.rules fachlich zu klaeren? | notary | `sensitive_family_financial_data` |
| `pension.equalization` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten pension.equalization fachlich zu klaeren? | notary | `financial_data` |
| `child.family.flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten child.family.flags fachlich zu klaeren? | notary | `sensitive_family_data` |
| `asset.transfer` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten asset.transfer fachlich zu klaeren? | notary_clerk | `financial_or_property_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.agreement_draft` | Dokument/Nachweis: vereinbarung entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.asset_schedule_reference` | Dokument/Nachweis: vermoegen schedule referenz | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.instrument_type`: Entscheidung: instrument art. Optionen: `pre_marriage`, `marriage_contract`, `divorce_consequence`, `unknown`.
- `decision.fairness_risk`: Entscheidung: angemessenheit risk. Optionen: `low`, `medium`, `high`, `blocked`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.fairness_review` | Prueftor: angemessenheit pruefung | notary |
| `gate.simultaneous_presence` | Prueftor: gleichzeitig anwesenheit | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-idaas` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-grundbuch-portal` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

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
