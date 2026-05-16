# Vereinsregisteranmeldung

Status: KG-Basis
KG-Knoten: `case.vereinsregisteranmeldung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.77`

## Ziel

Vereinsregisteranmeldungen fuer Vorstandsaenderungen, Satzungsaenderungen, Gruendung oder Aufloesung mit oeffentlicher Beglaubigung, Beschluessen und Anlagen.

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
| `association.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten association.identity fachlich zu klaeren? | notary_clerk | `association_register_data` |
| `filing.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten filing.type fachlich zu klaeren? | notary | `association_data` |
| `board.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten board.identity fachlich zu klaeren? | notary_clerk | `personal_data` |
| `resolution.evidence` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten resolution.evidence fachlich zu klaeren? | association | `association_data` |
| `articles.current` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten articles.current fachlich zu klaeren? | association | `association_data` |
| `filing.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten filing.route fachlich zu klaeren? | notary_clerk | `technical_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.minutes_resolution` | Dokument/Nachweis: niederschrift beschluss | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.articles` | Dokument/Nachweis: satzung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.certification_route`: Entscheidung: beglaubigung weg. Optionen: `paper`, `video_allowed`, `electronic`, `unknown`.
- `decision.attachment_complete`: Entscheidung: attachment vollstaendigkeit. Optionen: `complete`, `incomplete`, `special_review`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.signer_authority` | Prueftor: unterzeichner befugnis | notary |
| `gate.register_package_ready` | Prueftor: register paket ready | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-bnotk-xnp` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
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
