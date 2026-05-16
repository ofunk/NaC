# Beglaubigung von Unterschriften

Status: KG-Basis
KG-Knoten: `case.unterschriftsbeglaubigung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.hgb.12`

## Ziel

Oeffentliche Beglaubigung von Unterschriften oder Handzeichen fuer Registeranmeldungen, Vollmachten, Genehmigungen, Loeschungsbewilligungen oder Behoerdenerklaerungen.

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
| `signer.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten signer.identity fachlich zu klaeren? | notary_clerk | `personal_data` |
| `document.purpose` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten document.purpose fachlich zu klaeren? | notary_clerk | `mandate_metadata` |
| `signature.mode` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten signature.mode fachlich zu klaeren? | notary | `mandate_metadata` |
| `language.understanding` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten language.understanding fachlich zu klaeren? | notary | `sensitive_process_data` |
| `representation.context` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten representation.context fachlich zu klaeren? | notary_clerk | `personal_or_company_data` |
| `copies.routing` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten copies.routing fachlich zu klaeren? | notary_clerk | `mandate_metadata` |
| `special.form` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten special.form fachlich zu klaeren? | notary | `mandate_metadata` |
| `fee.metadata` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten fee.metadata fachlich zu klaeren? | notary_clerk | `financial_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.signed_document` | Dokument/Nachweis: signed dokument | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.certification_note` | Dokument/Nachweis: beglaubigung note | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.certification_scope`: Entscheidung: beglaubigung umfang. Optionen: `signature_only`, `with_authority_evidence`, `blocked`, `unknown`.
- `decision.routing`: Entscheidung: routing. Optionen: `paper`, `electronic`, `register_filing`, `foreign_use`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.identity_and_signature` | Prueftor: identitaet und unterschrift | notary |
| `gate.form_route` | Prueftor: form weg | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-idaas` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
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
