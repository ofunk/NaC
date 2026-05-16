# Erbscheinsantrag / Nachlassangelegenheiten

Status: KG-Basis
KG-Knoten: `case.erbscheinsantrag_nachlass`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.2353`, `src.gbo`

## Ziel

Antrag und Erklaerungen fuer Erbschein, Nachlassgericht, Ausschlagung, eidesstattliche Versicherung und Erbnachweise.

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
| `decedent.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten decedent.identity fachlich zu klaeren? | applicant | `personal_data` |
| `residence.jurisdiction` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten residence.jurisdiction fachlich zu klaeren? | notary_clerk | `mandate_metadata` |
| `applicants.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten applicants.identity fachlich zu klaeren? | notary_clerk | `personal_data` |
| `heirship.basis` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten heirship.basis fachlich zu klaeren? | notary | `sensitive_family_data` |
| `family.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten family.evidence fachlich zu klaeren? | applicant | `family_data` |
| `dispositions.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten dispositions.evidence fachlich zu klaeren? | notary_clerk | `sensitive_legal_data` |
| `renunciations.disclaimers` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten renunciations.disclaimers fachlich zu klaeren? | notary | `sensitive_legal_data` |
| `oath.statement` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten oath.statement fachlich zu klaeren? | notary | `sensitive_process_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.death_certificate_reference` | Dokument/Nachweis: death bescheinigung referenz | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.application_draft` | Dokument/Nachweis: anmeldung entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.family_evidence` | Dokument/Nachweis: familie nachweis | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.certificate_type`: Entscheidung: bescheinigung art. Optionen: `national_erbschein`, `european_certificate`, `renunciation`, `other`, `unknown`.
- `decision.oath_required`: Entscheidung: eid erforderlich. Optionen: `notary`, `court`, `not_required`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.heirship_review` | Prueftor: erbrecht pruefung | notary |
| `gate.oath_readiness` | Prueftor: eid bereitschaft | notary |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

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
