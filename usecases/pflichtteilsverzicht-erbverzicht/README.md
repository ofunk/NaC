# Pflichtteilsverzicht / Erbverzicht

Status: KG-Basis
KG-Knoten: `case.pflichtteilsverzicht_erbverzicht`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.2346_2348`

## Ziel

Vertraglicher Erb- oder Pflichtteilsverzicht, typischerweise in der Familiennachfolge, mit Beteiligten, Verzichtsumfang, Abfindung, Erstreckung auf Abkoemmlinge und Angemessenheitspruefung.

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
| `future_decedent.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten future_decedent.identity fachlich zu klaeren? | notary | `personal_data` |
| `waiver_party.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten waiver_party.identity fachlich zu klaeren? | notary | `family_data` |
| `waiver.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten waiver.scope fachlich zu klaeren? | notary | `sensitive_legal_data` |
| `descendant.effect` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten descendant.effect fachlich zu klaeren? | notary | `family_data` |
| `compensation.model` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten compensation.model fachlich zu klaeren? | client | `financial_data` |
| `family.fairness_flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten family.fairness_flags fachlich zu klaeren? | notary | `sensitive_family_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.waiver_contract` | Dokument/Nachweis: verzicht vertrag | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.compensation_evidence` | Dokument/Nachweis: abfindung nachweis | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.waiver_type`: Entscheidung: verzicht art. Optionen: `erbverzicht`, `pflichtteilsverzicht`, `limited`, `unknown`.
- `decision.compensation`: Entscheidung: abfindung. Optionen: `none`, `cash`, `asset_transfer`, `mixed`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.personal_presence_review` | Prueftor: persoenlich anwesenheit pruefung | notary |
| `gate.fairness_review` | Prueftor: angemessenheit pruefung | notary |

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
