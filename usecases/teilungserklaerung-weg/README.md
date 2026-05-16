# Teilungserklaerung nach WEG

Status: KG-Basis
KG-Knoten: `case.teilungserklaerung_weg`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.gbo.19_29_46`, `src.weg.8`

## Ziel

Aufteilung eines Gebaeudes in Wohnungs- oder Teileigentum mit Teilungserklaerung, Gemeinschaftsordnung, Plaenen, Bescheinigungen und Grundbuchumsetzung.

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
| `owner.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten owner.identity fachlich zu klaeren? | notary | `personal_or_company_data` |
| `unit.structure` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten unit.structure fachlich zu klaeren? | client | `property_metadata` |
| `ownership.shares` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten ownership.shares fachlich zu klaeren? | client | `property_metadata` |
| `plans.certificates` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten plans.certificates fachlich zu klaeren? | client | `property_metadata` |
| `encumbrance.handling` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten encumbrance.handling fachlich zu klaeren? | notary | `property_register_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.division_declaration` | Dokument/Nachweis: teilung erklaerung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.plans_certificate` | Dokument/Nachweis: plaene bescheinigung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.use_case`: Entscheidung: nutzung vorgang. Optionen: `residential`, `partial`, `mixed`, `unknown`.
- `decision.special_use_rights`: Entscheidung: sonderfall nutzung rights. Optionen: `yes`, `no`, `needs_review`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.plan_certificate_review` | Prueftor: plan bescheinigung pruefung | notary_clerk |
| `gate.land_register_implementation` | Prueftor: grundbuch register umsetzung | notary |

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
