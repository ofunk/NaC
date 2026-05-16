# Grundschuld / Hypothekenbestellung

Status: KG-Basis
KG-Knoten: `case.grundschuld_hypothek`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.gbo`

## Ziel

Bestellung, Aenderung oder Refinanzierung einer Grundschuld oder Hypothek mit Eigentuemer, Schuldner, Glaeubiger, Rang und Vollstreckungsunterwerfung.

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
| `owner.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten owner.identity fachlich zu klaeren? | notary_clerk | `personal_or_company_data` |
| `debtor.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten debtor.identity fachlich zu klaeren? | notary | `financial_data` |
| `lender.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten lender.identity fachlich zu klaeren? | notary_clerk | `mandate_metadata` |
| `charge.amount` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten charge.amount fachlich zu klaeren? | notary_clerk | `financial_data` |
| `security.purpose` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten security.purpose fachlich zu klaeren? | notary | `financial_data` |
| `ranking.requirement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten ranking.requirement fachlich zu klaeren? | notary_clerk | `property_register_data` |
| `enforcement.clause` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten enforcement.clause fachlich zu klaeren? | notary | `financial_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.bank_instruction` | Dokument/Nachweis: bank belehrung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.charge_type`: Entscheidung: grundschuld art. Optionen: `land_charge`, `mortgage`, `amendment`, `refinancing`, `unknown`.
- `decision.execution_clause_scope`: Entscheidung: vollzug clause umfang. Optionen: `property_only`, `personal_assets`, `both`, `not_requested`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.bank_instruction_review` | Prueftor: bank belehrung pruefung | notary_clerk |
| `gate.rank_review` | Prueftor: rang pruefung | notary |

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
