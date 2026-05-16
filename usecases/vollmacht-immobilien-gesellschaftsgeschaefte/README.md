# Vollmacht fuer Immobilien- oder Gesellschaftsgeschaefte

Status: KG-Basis
KG-Knoten: `case.vollmacht_immobilien_gesellschaft`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.167_129`, `src.bgb.311b`, `src.hgb.12`

## Ziel

Notarielle oder oeffentlich beglaubigte Vollmachten fuer Immobilienvertraege, Registeranmeldungen, Gesellschafterversammlungen oder Anteilsuebertragungen mit Umfang, Form und Nachweisen.

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
| `principal.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten principal.identity fachlich zu klaeren? | notary | `personal_or_company_data` |
| `agent.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten agent.identity fachlich zu klaeren? | principal | `personal_data` |
| `transaction.scope` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten transaction.scope fachlich zu klaeren? | notary | `mandate_metadata` |
| `form.requirement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten form.requirement fachlich zu klaeren? | notary | `legal_metadata` |
| `limitations.expiry` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten limitations.expiry fachlich zu klaeren? | notary | `mandate_metadata` |
| `delivery.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten delivery.evidence fachlich zu klaeren? | notary_clerk | `mandate_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.power_of_attorney` | Dokument/Nachweis: vollmacht of attorney | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.scope_reference` | Dokument/Nachweis: umfang referenz | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.form_route`: Entscheidung: form weg. Optionen: `notarial_deed`, `public_certification`, `electronic_certification`, `blocked`, `unknown`.
- `decision.scope_type`: Entscheidung: umfang art. Optionen: `real_estate`, `company_register`, `shareholder_resolution`, `share_transfer`, `mixed`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.form_review` | Prueftor: form pruefung | notary |
| `gate.delivery_control` | Prueftor: zustellung kontrolle | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-idaas` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
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
