# Uebersetzungsstatus

## Verbindliche Regel

`de` und `en` sind verpflichtende Standardsprachen nach
[policies/language-policy.yaml](../../policies/language-policy.yaml). Jede
Aenderung an lokalisierten Inhalten muss beide Sprachen pflegen.
Fuer deutsches Recht und notarielle Usecases ist Deutsch die fuehrende und
rechtlich bindende Sprache; Englisch ist nur Uebersetzung oder Orientierung.

## Aktueller Stand

- [docs/de/](.) enthaelt die deutsche Ausgangsfassung.
- [README.md](../../README.md) ist die deutsch gefuehrte GitHub-Startseite und
  fuehrt Startpfade in einer Deutsch/English-Tabelle.
- [usecases/](../../usecases) wird als deutsche fachliche Usecase-Flaeche
  gefuehrt.
- Die englischen Einstiegsfassungen werden parallel gepflegt, aber nicht als
  Navigationsziel aus diesem deutschen Lesefluss verlinkt.
- Die wichtigsten englischen Einstiegs-, Governance-, Betriebs-, Eventstream-,
  Service- und aktiven Pluginplan-Dokumente sind nicht mehr nur Dateispiegel.
- Alte Omnistation-Importe werden in beiden Sprachpfaden getrennt gefuehrt; die
  deutschen Originalartefakte bleiben im deutschen Importordner
  nachvollziehbar.

## Technische Kontrolle

[scripts/validate_language_parity.py](../../scripts/validate_language_parity.py)
prueft:

- Pflicht-Sprachordner fuer `de` und `en`,
- Dateiparitaet fuer lokalisierte Flaechen,
- Root-README- und Usecase-Sprachregeln,
- sprachgleiche Markdown-Links fuer lokalisierte Dokumente und Prompts,
- keine identischen Markdown-/Textspiegel zwischen `docs/de` und `docs/en`.

## Naechster sinnvoller Schritt

Tiefere Fachtexte koennen weiter stilistisch geschaerft werden. Neue fachliche
Aenderungen muessen aber ab jetzt wieder beide Sprachpfade direkt mitziehen.
