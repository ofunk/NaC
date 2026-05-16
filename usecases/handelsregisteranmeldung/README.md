# Handelsregisteranmeldung

Status: KG-Basis
KG-Knoten: `case.handelsregisteranmeldung`
KG: [knowledge-graph.graph.json](knowledge-graph.graph.json) / [knowledge-graph.md](knowledge-graph.md)
Primaere Quellenanker: `src.beurkg`, `src.hgb.12`, `src.gmbhg`

## Ziel

Registeranmeldung fuer Aenderungen wie Geschaeftsfuehrerwechsel, Sitzverlegung, Kapitalmassnahmen, Firma, Unternehmensgegenstand oder Prokura.

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
| `entity.identity` | Welcher Rechtstraeger und welches Registerblatt sind betroffen? | notary_clerk | `company_register_data` |
| `event.type` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten event.type fachlich zu klaeren? | notary | `company_data` |
| `signers.identity` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten signers.identity fachlich zu klaeren? | notary_clerk | `personal_or_company_data` |
| `corporate.resolution` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten corporate.resolution fachlich zu klaeren? | notary | `company_data` |
| `attachments.required` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten attachments.required fachlich zu klaeren? | notary_clerk | `company_data` |
| `effective.date` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten effective.date fachlich zu klaeren? | notary | `mandate_metadata` |
| `xnp.route` | Welcher XNP-, Karten-, Signatur- und Uebermittlungsweg wird genutzt? | notary_clerk | `technical_metadata` |
| `fees.costs` | Welche Angaben, Nachweise und Freigaben sind fuer den Knoten fees.costs fachlich zu klaeren? | notary_clerk | `financial_metadata` |

## Dokumente und Nachweise

| Artefakt | Zweck | Speicherregel |
| --- | --- | --- |
| `doc.register_application` | Dokument/Nachweis: register anmeldung | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |
| `doc.corporate_evidence` | Dokument/Nachweis: gesellschaft nachweis | Nur Metadaten, synthetische Referenzen oder Verweis auf freigegebenen Evidenzspeicher. |

## Entscheidungen

- `decision.event_route`: Entscheidung: ereignis weg. Optionen: `standard`, `special_review`, `blocked`, `unknown`.
- `decision.signature_method`: Entscheidung: signatur methode. Optionen: `in_office`, `video`, `existing_certified_power`, `unknown`.

## Prueftore

| Prueftor | Pruefzweck | Verantwortung |
| --- | --- | --- |
| `gate.public_certification` | Prueftor: oeffentlich beglaubigung | notary |
| `gate.electronic_format` | Prueftor: electronic format | notary_clerk |

## Plugin-Abhaengigkeiten

| Plugin | Zweck |
| --- | --- |
| `noc-regulated-core` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-bnotk-xnp` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-handelsregister` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |
| `noc-cyberjack-rfid` | Fachliche oder technische Begleitfaehigkeit fuer diesen Usecase. |

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
