# beN Portal Plugin Integration Plan

Stand: 2026-05-16

## Ziel

Dieses Dokument plant die Integration des besonderen elektronischen Notarpostfachs `beN` als lokales NoC-Plugin. Ziel ist nicht, beN, XNP oder die Systeme der Bundesnotarkammer zu ersetzen oder Postfachaktionen heimlich zu automatisieren. Ziel ist ein sicherer, auditierbarer Arbeitsrahmen, in dem NoC:

- beN-Voraussetzungen prueft,
- die XNP-Ersteinrichtung als vorgelagerten Day0-Gate behandelt,
- lokale BNotK-Karten-, Token- und Kartenleserpfade kontrolliert begleitet,
- beN-Aktivierung, Empfang, Versand, beN-zu-beA-Kommunikation und Exporte als NoC-Prozessplaene dokumentiert,
- Nachweise minimiert speichert.

beN und XNP bleiben fuehrend fuer Postfachzugang, Aktivierung, Versand, Empfang, Signatur, Entschluesselung und rollenbezogene Rechte. NoC fuehrt Governance, Prozessstatus, Evidence, Freigabe und Audit.

## Quellenlage und Integrationsanker

Aus der offiziellen NotarNet-beN-Seite ergeben sich folgende Integrationsanker:

- Die Bundesnotarkammer richtet fuer jede Notarin und jeden Notar sowie fuer Notariatsverwalterinnen und Notariatsverwalter ein besonderes elektronisches Notarpostfach ein.
- Massgeblich fuer die Einrichtung ist die im Notarverzeichnis eingetragene Amtstaetigkeit.
- beN dient vorrangig der sicheren elektronischen Kommunikation mit Gerichten und kann auch fuer Kommunikation mit Behoerden, Notarkammern, sonstigen Organisationen des Notariats, anderen Notarinnen und Notaren sowie der Anwaltschaft als beN-zu-beA-Kommunikation genutzt werden.
- Die Bundesnotarkammer stellt neben der technischen Infrastruktur eine Anwendung zur Aktivierung des Postfachs sowie zum Empfang und Versand von Nachrichten bereit.
- Die Aktivierung von beN kann erst nach der Ersteinrichtung der XNP-Anwendung erfolgen.

## Leitentscheidung

Die erste NoC-Integration erfolgt als lokaler Companion nach dem XNP-Gate. Sie fuehrt keine verdeckte Browser-Automation, keine Postfachsynchronisierung und keine direkte XNP- oder beN-API-Aktion aus. Der sichere Start ist ein lokaler Preflight, der XNP-Ersteinrichtung, Kartenleserpfad, beN-Verfuegbarkeit, Rollenstatus und NoC-Evidence abbildet.

```text
Notariatsarbeitsplatz
  XNP
  beN Anwendung
  BNotK Karte / Token / Kartenleser
  noc-ben-portal
        |
        | minimierte Evidence / Workflow-Status
        v
NoC
  beN workflow status
  tenant evidence store
  audit journal
```

## Visuelle Store-Kennung

Das Plugin verwendet das beN-Logo von der offiziellen NotarNet-beN-Produktseite als Store- und Composer-Erkennungszeichen. Diese visuelle Bindung dient nur der Wiedererkennbarkeit des lokalen NoC-Companions. beN, XNP und die offiziellen BNotK-/NotarNet-Systeme bleiben fuehrend; Marken- und Nutzungsrechte werden dadurch nicht uebertragen.

## Plugin-Grenzen

### Das Plugin darf

- XNP-Ersteinrichtung und lokalen Arbeitsplatzkontext als Voraussetzung pruefen,
- BNotK-Karten-, Token- und Kartenleserbereitschaft als Checkliste fuehren,
- beN-Aktivierung, Empfang, Versand, beN-zu-beA-Kommunikation und Exporte als Plan Preview vorbereiten,
- Dateinamen, Groessen, Hashes und Strukturmetadaten erfassen, wenn der Nutzer diese bewusst bereitstellt,
- NoC-Evidence zu Nutzerbestaetigungen und beN-Aktionen erzeugen,
- Drift durch XNP-/beN-/Treiber-/Kartenleser-Aenderungen sichtbar machen.

### Das Plugin darf nicht

- PINs, Kartenrohdaten, Zertifikate, Private Keys, XNP-API-Keys oder Postfachgeheimnisse speichern,
- beN oder XNP aus der Cloud steuern,
- Nachrichten ohne lokale Nutzerbestaetigung senden, empfangen oder bestaetigen,
- geschuetzte Postfachinhalte scrapen,
- notarielle Amtstaetigkeit oder Berufstraegerverantwortung ersetzen,
- Mandats- oder Urkundsinhalte ungefiltert in LLM-Kontexte geben.

## Vorgeschlagene Plugin-API

### Readiness und Diagnose

- `ben.health`
  - prueft Plugin-Version, Betriebssystem, Benutzerkontext und lokale Voraussetzungen.
- `ben.check_xnp_first_setup`
  - dokumentiert, ob XNP-Ersteinrichtung und lokaler Arbeitsplatzkontext bereit sind.
- `ben.check_card_reader_path`
  - prueft nur Readiness fuer Karte, Token und Kartenleser; keine PIN- oder Kartenwert-Erfassung.
- `ben.check_application_available`
  - dokumentiert beN-Verfuegbarkeit ohne Postfachzugriff.

### Prozessvorbereitung

- `ben.prepare_activation`
  - erstellt eine Aktivierungs-Checkliste nach XNP-Ersteinrichtung.
- `ben.prepare_incoming_message`
  - erstellt eine Empfangs- und Fristen-Checkliste ohne Inhaltsabruf.
- `ben.prepare_outgoing_message`
  - erstellt eine Versand-Checkliste mit Anlagenhashes und Freigabepunkten.
- `ben.prepare_ben_to_bea`
  - strukturiert beN-zu-beA-Kommunikation als Plan Preview.

### Evidence und Audit

- `ben.record_user_attestation`
  - speichert ausdrueckliche Nutzerbestaetigung als Evidence.
- `ben.record_export`
  - hasht ein vom Nutzer bereitgestelltes Exportpaket lokal.
- `ben.get_evidence`
  - gibt minimierte Evidence zurueck.

## MVP-Scope

1. Installierbares Plugin `noc-ben-portal`.
2. Lokaler Preflight `prepare_ben_session.py`.
3. Store-/Composer-Logo aus der NotarNet-beN-Seite.
4. XNP-first Gate als Day0-Voraussetzung.
5. Kartenleser-/Token-Grenze ohne PIN- oder Kartendaten.
6. Metadata-only Evidence.

## Nicht im MVP

- Direktes Abrufen von beN-Nachrichten.
- Direktes Senden von beN-Nachrichten.
- Automatische Postfachaktivierung.
- Automatische PIN-Eingabe.
- Direkte XNP- oder beN-API-Nutzung.
- Browser-Scraping oder RPA gegen geschuetzte beN-Oberflaechen.

## Akzeptanzkriterien fuer den ersten PR

- Plugin-Manifest und Marketplace-Eintrag vorhanden.
- Offizielle NotarNet-Quelle ist verlinkt.
- Plugin bleibt Companion-only und bindet an XNP-first.
- Keine Geheimnisse, PINs, Kartenwerte, XNP-API-Keys oder Notariatsinhalte im Repo.
- Striktes Quality Gate besteht.

## Quellen

- NotarNet beN: https://notarnet.de/produkte/ben
- NotarNet XNP: https://notarnet.de/produkte/xnp
- BNotK Onlinehilfe XNP: https://onlinehilfe.bnotk.de/technischer-bereich/systembetreuer/xnp-die-basisanwendung-der-bnotk.html
