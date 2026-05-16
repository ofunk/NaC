# Loeschungsbewilligung / Grundbuchloeschung

Status: KG-Basis
KG-Knoten: `case.loeschungsbewilligung_grundbuchloeschung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.gbo.19_29_46`, `src.bgb.875`

## Ziel

Loeschung eingetragener Grundbuchrechte, haeufig alter Grundschulden nach Darlehensrueckzahlung, mit Glaeubigerlegitimation, Eigentuemerzustimmung, Formnachweis und Einreichungsspur.

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
| `right.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten right.identity fachlich zu klaeren? | notary_clerk | `property_register_data` |
| `creditor.authorization` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten creditor.authorization fachlich zu klaeren? | notary | `company_or_financial_data` |
| `owner.consent` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten owner.consent fachlich zu klaeren? | notary_clerk | `personal_or_company_data` |
| `brief.status` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten brief.status fachlich zu klaeren? | notary_clerk | `financial_metadata` |
| `filing.route` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten filing.route fachlich zu klaeren? | notary_clerk | `technical_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.deletion_consent` | Dokument/Nachweis: loeschung zustimmung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.right_letter` | Dokument/Nachweis: right brief | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.deletion_type`: Entscheidung: loeschung art. Optionen: `full`, `partial`, `correction`, `unknown`.
- `decision.brief_handling`: Entscheidung: brief handling. Optionen: `book_right`, `letter_present`, `replacement_evidence`, `blocked`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.authority_review` | Prueftor: befugnis pruefung | notary |
| `gate.filing_ready` | Prueftor: einreichung ready | notary_clerk |

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
