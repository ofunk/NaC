# Vorsorgevollmacht und Patientenverfuegung

Status: KG-Basis
KG-Knoten: `case.vorsorgevollmacht_patientenverfuegung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`

## Ziel

Vorsorgevollmacht, Gesundheitsvollmacht und Patientenverfuegung mit Umfang, Bevollmaechtigten, Wirksamkeit, Register und Ausfertigungsverwaltung.

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
| `principal.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten principal.identity fachlich zu klaeren? | notary | `personal_data` |
| `agent.identities` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten agent.identities fachlich zu klaeren? | principal | `personal_data` |
| `authority.financial` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten authority.financial fachlich zu klaeren? | principal | `financial_data` |
| `authority.health` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten authority.health fachlich zu klaeren? | principal | `health_or_sensitive_data` |
| `patient.directive` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten patient.directive fachlich zu klaeren? | principal | `health_or_sensitive_data` |
| `effectiveness.rules` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten effectiveness.rules fachlich zu klaeren? | notary | `mandate_metadata` |
| `self_dealing.release` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten self_dealing.release fachlich zu klaeren? | notary | `mandate_metadata` |
| `central_register` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten central_register fachlich zu klaeren? | notary_clerk | `personal_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.power_of_attorney_draft` | Dokument/Nachweis: vollmacht of attorney entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.patient_directive_draft` | Dokument/Nachweis: patient verfuegung entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.instrument_scope`: Entscheidung: instrument umfang. Optionen: `power_only`, `patient_directive_only`, `combined`, `unknown`.
- `decision.register`: Entscheidung: register. Optionen: `register`, `do_not_register`, `needs_review`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.capacity_review` | Prueftor: geschaeftsfaehigkeit pruefung | notary |
| `gate.health_scope_review` | Prueftor: gesundheit umfang pruefung | notary |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
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
