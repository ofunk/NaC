# Schenkungsvertrag / Uebertragungsvertrag

Status: KG-Basis
KG-Knoten: `case.schenkungsvertrag_uebertragung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.518`, `src.bgb.311b`, `src.gbo`

## Ziel

Schenkungs- oder Uebertragungsvertrag, haeufig familieninterne Immobilienuebertragung, mit Vorbehaltsrechten, Rueckforderungsrechten, Pflegepflichten, Steuerbezug und Grundbuchvollzug.

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
| `transferor.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten transferor.identity fachlich zu klaeren? | notary_clerk | `personal_data` |
| `transferee.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten transferee.identity fachlich zu klaeren? | notary_clerk | `personal_or_family_data` |
| `asset.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten asset.identity fachlich zu klaeren? | notary_clerk | `property_or_financial_data` |
| `reserved.rights` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten reserved.rights fachlich zu klaeren? | notary | `family_or_financial_data` |
| `reversion.rights` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten reversion.rights fachlich zu klaeren? | notary | `sensitive_legal_data` |
| `consideration.obligations` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consideration.obligations fachlich zu klaeren? | notary | `financial_data` |
| `consents.approvals` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten consents.approvals fachlich zu klaeren? | notary_clerk | `mandate_metadata` |
| `tax.family.flags` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten tax.family.flags fachlich zu klaeren? | notary | `sensitive_family_financial_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.transfer_draft` | Dokument/Nachweis: uebertragung entwurf | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.land_register_excerpt` | Dokument/Nachweis: grundbuch register excerpt | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.approvals` | Dokument/Nachweis: genehmigungen | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.transfer_type`: Entscheidung: uebertragung art. Optionen: `gift`, `mixed_gift`, `transfer_with_obligations`, `unknown`.
- `decision.reserved_rights`: Entscheidung: vorbehalten rights. Optionen: `none`, `usufruct`, `residential_right`, `reversion`, `mixed`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.asset_review` | Prueftor: vermoegen pruefung | notary |
| `gate.family_tax_review` | Prueftor: familie steuer pruefung | notary |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
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
