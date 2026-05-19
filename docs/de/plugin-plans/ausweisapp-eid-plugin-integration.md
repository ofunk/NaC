# AusweisApp-eID-Plugin-Integration

## Zweck

Dieser Plan ergaenzt `noc-idaas` um einen lokalen AusweisApp-eID-Adapter. Das
Plugin `noc-ausweisapp-eid` prueft, ob die AusweisApp lokal erreichbar ist,
bereitet eine zweckgebundene eID-Session vor und erzeugt metadata-only Evidence.
Es liest keine Personalausweisdaten direkt aus der Karte in Codex aus.

Die offizielle AusweisApp-Dokumentation trennt diese Ebenen klar: Fuer die
Online-Ausweisfunktion braucht die nutzende Person eine aktivierte
Online-Ausweisfunktion, eine bekannte sechsstellige PIN, die AusweisApp und ein
NFC-faehiges Smartphone oder USB-Kartenlesegeraet. Die SDK-Dokumentation sagt
zudem, dass lokale Client-Anwendungen keine Personendaten direkt von der
AusweisApp erhalten; die Daten kommen nach erfolgreicher Authentisierung ueber
das Backend, zum Beispiel den eID-Server. Diensteanbieter brauchen dafuer eine
Anbindung an eID-Server, eID-Service oder Identifizierungsdienst und je nach
Modell ein Berechtigungszertifikat.

## Einordnung im NoC-Konzept

Der Baustein ist ein neues lokales Plugin, aber kein Ersatz fuer die bestehende
IDaaS-Schicht:

- `noc-cyberjack-rfid` prueft Kartenleser, PC/SC, morris und lokale
  Workstation-Readiness.
- `noc-ausweisapp-eid` prueft AusweisApp-Status, Zweck, Claim-Set und
  eID-Session-Grenze.
- `noc-idaas` verarbeitet genehmigte Backend-Assertions weiter zu minimalen
  verifizierten Claims und optionaler IAM-Projektion.

## Day0

- Zweck, Tenant, Rolle, Reviewer und minimalen Claim-Satz festlegen.
- Klaeren, ob ein Smartphone als Kartenleser oder ein USB-Kartenleser verwendet
  wird.
- Bei USB-Kartenleser zuerst `noc-cyberjack-rfid` ausfuehren.
- AusweisApp-Installation und lokalen Statusendpunkt pruefen.
- Online-Ausweisfunktion, sechsstellige PIN und Kartenverfuegbarkeit nur als
  menschliche Voraussetzung bestaetigen; PIN, CAN und PUK werden nie abgefragt.
- Backend-Route festlegen: Identifizierungsdienst, eID-Service oder eigener
  eID-Server mit Berechtigungszertifikat, sofern erforderlich.
- Datenschutzgrundlage, AVV/DPA-Bedarf und Retention festlegen.

## Day1

- Metadata-only Evidence erzeugen:

```powershell
python plugins\noc-ausweisapp-eid\scripts\prepare_eid_session.py --json
```

- Wenn ein reviewed Backend eine `tcTokenURL` liefert, wird diese nur lokal
  verwendet und in Evidence nur gehasht.
- Produktive eID-Transaktion erst nach dokumentierter menschlicher Freigabe
  starten.
- Backend-Assertion pruefen und nur den genehmigten minimalen Claim-Satz an
  `noc-idaas` weitergeben.

## Day2

- AusweisApp-Version, Reader-Pfad, eID-Servicevertrag,
  Berechtigungszertifikat, Claim-Set, Retention und Zweckbindung
  rezertifizieren.
- Fehlerhafte Sessions, abgelaufene Assertions und Widerrufe nachverfolgen.
- Bei Wechsel von eID-Service oder Identifizierungsdienst den AVV/DPA- und
  Exit-Pfad neu pruefen.

## Sicherheitsgrenzen

- Keine PINs, CAN, PUK, Kartenrohdaten, vollstaendigen Ausweisdumps,
  Session-Cookies, Access Tokens, Zertifikate oder privaten Schluessel im Repo.
- Keine echten Personendaten an LLMs ohne dokumentierte Freigabe und
  Verarbeitungsgrundlage.
- Codex darf die AusweisApp-Readiness pruefen und Sessions vorbereiten, aber
  nicht behaupten, direkt die Personalausweisdaten lokal auszulesen.
- Identity Claims duerfen nur aus einem genehmigten Backend uebernommen werden.

## Quellen

- [AusweisApp: Das brauchen Sie](https://www.ausweisapp.bund.de/das-brauchen-sie)
- [AusweisApp SDK: Introduction](https://www.ausweisapp.bund.de/sdk/intro.html)
- [AusweisApp SDK: Desktop](https://www.ausweisapp.bund.de/sdk/desktop.html)
- [AusweisApp: So werden Sie Diensteanbieter](https://www.ausweisapp.bund.de/so-werden-sie-diensteanbieter)
