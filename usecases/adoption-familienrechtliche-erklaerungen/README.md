# Adoption / familienrechtliche Erklaerungen

Status: KG-Basis
KG-Knoten: `case.adoption_familienrechtliche_erklaerungen`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.bgb.1750`

## Ziel

Notarieller Usecase fuer Adoptionszustimmungen und familienrechtliche Erklaerungen mit Identitaet, Zustimmungsbeteiligten, Familiengericht, Geschaeftsfaehigkeit, Unwiderruflichkeitswarnung und besonders sensibler Datenfuehrung.

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
| `case.type` | Welche Adoptions- oder familienrechtliche Erklaerung wird benoetigt? | notary | `sensitive_family_data` |
| `child.identity_context` | Welcher Kinder- oder Adoptivkontext ist relevant, ohne Rohdaten in Git zu speichern? | client | `sensitive_personal_data` |
| `consenting_party.identity` | Wer erteilt die Zustimmung und sind Geschaeftsfaehigkeit, Alter oder Unterstuetzungsbedarf geklaert? | notary | `sensitive_personal_data` |
| `court.destination` | Welches Familiengericht erhaelt die Erklaerung und welche Referenz wird verwendet? | notary_clerk | `mandate_metadata` |
| `irrevocability.warning` | Welche Belehrungen zu Unwiderruflichkeit, Bedingungen oder Fristen muessen dokumentiert werden? | notary | `sensitive_process_data` |
| `additional.approvals` | Sind elterliche, vormundschaftliche, ehebezogene, behoerdliche oder gerichtliche Zustimmungen relevant? | notary | `sensitive_family_data` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.consent_declaration` | Dokument/Nachweis: zustimmung erklaerung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.court_reference` | Dokument/Nachweis: gericht referenz | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.declaration_route`: Entscheidung: erklaerung weg. Optionen: `adoption_consent`, `withdrawal_or_revocation`, `other_family_declaration`, `unknown`.
- `decision.approval_status`: Entscheidung: genehmigung status. Optionen: `not_required`, `required`, `available`, `blocked`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.capacity_and_warning` | Prueftor: geschaeftsfaehigkeit und belehrung | notary |
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
