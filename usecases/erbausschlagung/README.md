# Erbausschlagung

Status: KG-Basis
KG-Knoten: `case.erbausschlagung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.1945`

## Ziel

Erbausschlagung gegenueber dem Nachlassgericht mit Frist, Identitaet, Vertretung, Minderjaehrigen- oder Betreuungsbezug und Zustellnachweis.

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
| `renouncer.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten renouncer.identity fachlich zu klaeren? | notary | `personal_data` |
| `deadline.status` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten deadline.status fachlich zu klaeren? | notary | `sensitive_process_data` |
| `heirship.basis` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten heirship.basis fachlich zu klaeren? | applicant | `family_data` |
| `representation.minors` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten representation.minors fachlich zu klaeren? | notary | `sensitive_family_data` |
| `delivery.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten delivery.route fachlich zu klaeren? | notary_clerk | `mandate_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.renunciation_declaration` | Dokument/Nachweis: ausschlagung erklaerung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.death_or_court_reference` | Dokument/Nachweis: tod oder gericht referenz | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.approval_evidence` | Dokument/Nachweis: genehmigung nachweis | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.deadline_risk`: Entscheidung: frist risk. Optionen: `low`, `urgent`, `expired_or_unclear`, `unknown`.
- `decision.approval_needed`: Entscheidung: genehmigung needed. Optionen: `yes`, `no`, `needs_review`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.deadline_review` | Prueftor: frist pruefung | notary |
| `gate.court_delivery` | Prueftor: gericht zustellung | notary_clerk |

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
