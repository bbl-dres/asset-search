## Anforderungen Lösungsarchitektur EDM

| Titel             | Anforderungen Energiedatenmanagement (EDM) - lösungsneutral   |
|-------------------|---------------------------------------------------------------|
| David Rasner, BBL | Author                                                        |
| Status Fachlich   | geprüft                                                       |
| 07.07.2026        | Stand                                                         |
| Intern            | Klassifizierung                                               |

## Inhalte:

Management Summary

Priorisierungs-Prämissen

1. Zweck und Lesart

2. Funktionale Anforderungen (A)

A1 Erfassung, Ablesung &amp; Integration (ERF)

A2 Datenmodell &amp; Synchronisation (MOD)

A3 Berechnung, Aufbereitung &amp; Datenqualität (CAL)

A4 Auswertung, Berichtswesen &amp; Bereitstellung (AUS)

A5 Zugriff &amp; Administration (ADM)

A6 Energiecontrolling &amp; Alarmierung (CTL)

Abgrenzung (WIRD NICHT)

3. Nicht-funktionale Anforderungen (B)

B1 Sicherheit (SEC)

B2 Datenqualität (DAT)

B3 Verfügbarkeit &amp; Betrieb (BET)

B4 Benutzbarkeit (USE)

B5 Interoperabilität (IOP)

B6 Wartbarkeit &amp; Portabilität (WAR)

B7 Sicherheits- &amp; Datenschutz-Governance (BBL-Bringpflicht - kein Entwickleraufwand)

4. Rahmenbedingungen / Constraints (C)

5. Transition / Migration (D)

6. Offene Punkte

7. Verweise und Anhänge

## Management Summary

Worum es geht. Das EDM sammelt alle Energie-, Wasser- und Abfalldaten der BBL-Liegenschaften, rechnet sie korrekt zusammen und liefert die geprüften Zahlen für das Klima-Reporting (ecCo/VEK/ESTAT) und die Betriebsoptimierung. SAP bleibt das führende System; das EDM ergänzt die Verbrauchs- und Emissionsdaten.

Was die Lösung können muss. Daten aus vielen Quellen automatisch übernehmen, lückenlos und nachvollziehbar speichern, korrekt und reproduzierbar zur CO2-Bilanz verrechnen und regulatorisch exportieren - abgesichert über Rollen, eIAM/AGOV-Login und einen fälschungssicheren Protokoll. Das auditierbare Klima-Reporting ist der eigentliche Zweck.

Die wirklich harten Anforderungen. Nicht der ganze Katalog (~95 Punkte) entscheidet, sondern wenige Gates:

- Zugriff &amp; Sicherheit: Berechtigungskonzept mit Rollen über das zentrale IAM, IKT-Grundschutz und ISDS-Konzept, fälschungssicheres Protokoll.
- Korrekte Zahlen: reproduzierbare CO2-Bilanz, lückenlose Historie, sauberer Abgleich mit SAP.
- Kein Lock-in: Vollexport, verlustfreie Migration, klares Betriebsmodell.

Aufwand und Realität. Kein Produkt am Markt erfüllt heute alle Anforderungen - bewertet wird darum nur, ob die Gates sitzen. Wichtig für den Entscheid: Die Sicherheits- und Datenschutz-Pflichten (Schutzbedarf, ISDS, Klassifizierung, Löschkonzept) muss das BBL erbringen, auch bei immer einem Kaufprodukt. Beim Selberbauen kommt die ganze Produktverantwortung dauerhaft dazu.

Empfehlung. Die grösste unterschätzte Falle beim Selberbauen ist nicht die Entwicklung, sondern : laufendes Betrieb und Verantwortung über 5+ Jahre Patchen, wiederkehrende Sicherheitstests, Wiederanlauf-Tests, Pflege - alles allein durch ein internes Team, mit hohem Personalrisiko. Ein Anbieter verteilt diese Last auf viele Kunden.

## Priorisierungs-Prämissen

Die Prioritäten sind pragmatisch für ein internes Fachtool gesetzt, nicht nach dem Massstab einer öffentlich verfügbaren IT Lösung. Annahmen:

1. Schutzbedarf = Grundschutz (noch durch Schutzbedarfsanalyse zu bestätigen). Ergibt diese «erhöhten Schutz», wandern u. a. Penetrationstests, Verschlüsselungstiefe und Verfügbarkeitsziele zurück auf MUSS.
2. Zugang intern, über eIAM/AGOV gated , kein öffentlicher Zugang (nur BV Mitarbeiter).

3.

3. Daten im Tagesbatch, keine Echtzeit-Kritikalität  Verfügbarkeit/Support pragmatisch dimensioniert.
4. Anforderungen, die in einer Buy-Variante nicht vorschreibbar sind (z. B. interne Modularität eines Standardprodukts), sind als SOLL /Bewertungskriterium geführt - sonst würde der Variantenentscheid vorweggenommen.

Die Spalte «Begründung Prio» hält fest, warum eine Anforderung so eingestuft ist, damit die Abstufung in der Variantenrunde nicht ohne Kenntnis des Grundes wieder hochdiskutiert wird.

| Priorität   | Bedeutung                                               |
|-------------|---------------------------------------------------------|
| MUSS        | Zwingend (fachlich kritisch oder rechtlich verbindlich) |
| SOLL        | Nicht zwingend, Ausnahme kann begründet werden          |
| KANN        | Mehrwert, spätere Ausbaustufe                           |
| WIRD NICHT  | Bewusst ausserhalb des Scope                            |

## 1. Zweck und Lesart

Lösungsneutrale Anforderungsbasis für das EDM des BBL-Immobilienportfolios - was, nicht womit oder durch wen. Sie ist der Eingang für die spätere Variantenbewertung; dort wird je Variante und Anforderung bewertet (erfüllt / teilweise / nicht).

Geschäftszweck. Vollständige, korrekte und aktuelle Erfassung, Verarbeitung und Auswertung der Energiedaten (Strom, Wärme, Gas, PV-Erzeugung) der BBL-Liegenschaften. Das EDM ist die geprüfte Energiedaten-Basis für das separate THG-Projekt (Emissionsbilanzierung Scope 1/2/3 im Modell ecCo als Nachfolger RUMBA; Netto-Null 2040 gemäss KlG Art. 10), für die Energiestatistik (VEK, ESTAT) und für die interne Objektsteuerung. Wasser läuft datenformgleich mit; Abfall und die Emissionsbilanzierung sind abgegrenzt (WN-03, WN-04).

System-of-Record (Once-Only). SAP ERP (BBL) ist das Leitsystem für Immobilienstammdaten - insbesondere RE-FX für Struktur/Flächen/EBF und MDG für Geschäftspartner und gibt sie lesend ins EDM. Das EDM führt die Zähler-, Verbrauchs- und Bewegungsdaten sowie die Zuordnungs- und Aufbereitungsregeln (Aggregation, EBF-Aufteilung, Energieträger-Umrechnung, Witterungsbereinigung). Die Rolle von SAP Data Warehouse und SAP PM ist noch abzugrenzen (offene Punkte 5 und 6).

Normativer Rahmen (Kurzfassung). Es gelten die acht handlungsleitenden Prinzipien der Strategie Digitale Bundesverwaltung sowie verbindlich u. a. DigiV, ISG/ISV (Schutzbedarf  Grundschutz/erhöht, ISDS), DSG/DSV, eIAM/AGOV, Once-Only mit SAP ERP und die CH-Souveränität.

- BK DTI Vorgaben: https://www.bk.admin.ch/de/vorgaben
- Prinzipien Strategie Digitale Bundesverwaltung: https://www.bk.admin.ch/de/prinzipien
- BACS Informatiksicherheitsvorgaben Bund: https://www.ncsc.admin.ch/ncsc/de/home/dokumentation/sicherheitsvorgaben-bund.html

Als zusätzliche Hilfestellung können die Checkpunkte zur Anwendungsüberprüfung der Unternehmensarchitekturprinzipien VBS genutzt werden:

- Für das BBL nicht verbindlich:  https://confluence.bit.admin.ch/x/jobjSw

## 2. Funktionale Anforderungen (A)

## Annahmen:

- Fokus Energie. Das EDM bewirtschaftet Energiedaten (Strom, Wärme, Gas, PV-Erzeugung). Die THG-/Emissionsbilanzierung (Scope 1/2/3) liegt im separaten THG-Projekt; das EDM liefert die Energiedaten interoperabel zu (siehe FA-AUS-02, WN-04).

## A1 Erfassung, Ablesung &amp; Integration (ERF)

| ID          | Anforderung                                                                                                                                                                                                                                                                                            | Prio Produktiv   | Prio MVP   | Begründung Prio                                                                                                      | Nachweis                                                        |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| FA- ERF -01 | Hersteller unabhängige und frei parametrierbares Interface um Daten aus allen relevanten Quellen automatisch und wiederholbar übernehmen (Lastgänge, Submetering, PV-Erzeugung, Datenlogger/Gateway, Wetter); Quellformate und Importzeiten einstellbar. MQTT, SMTP, xlsx / csv via sFTP und REST-API. | MUSS             |            | Ohne Erfassung kein EDM - das ist die Grundfunktion                                                                  | Alle Quelltypen angebunden; Wiederholim port ohne Dubletten     |
| FA- ERF -02 | Objektportfolio / -struktur und Immobilien- (Flächen/EBF) sowie Anlagen- Stammdaten (Leistung-Ausgelegt, Typ, Hersteller, ...) lesend aus SAP RE-FX oder anderem System übernehmen, keine Doppelerfassung (Once-Only)                                                                                  | MUSS             |            | Wirtschaftseinheiten, Gebäude müssen synchron mit dem Bestand sein und Flächen/EBF sind die Basis aller Berechnungen | Stammdaten im EDM vorhanden; keine Doppelpflege                 |
| FA- ERF -03 | Einzelne im EDM gepflegte Felder zurück nach RE-FX schreiben oder auf API Schnittstelle zur Verfügung stellen; welche Felder, ist noch offen                                                                                                                                                           | KANN             |            | Gegenrichtung zu Once-Only; Feld-Hoheit erst zu klären (offener Punkt 5). Nicht bauen, bevor entschieden             | Rückschreib en nur definierter Felder; Hoheitsmatri x vorhanden |

| FA- ERF -04        | Ausfallüberwachung auf ebene Zähler und auf ebene Datenlogger / -übertragung. Fällt eine Quelle aus, wird das erkannt und gemeldet; nach Behebung werden die fehlenden Daten, sofern diese auf dem Datenlogger zwischengespeichert werden konnten, automatisch nachgeladen.                | MUSS   | eine möglichst lückenlose Erfassung der Energie- und Wasserverbräuche reduzieren den Aufwand im Bereich CAL                                                  | Simulierter Ausfall Meldung; fehlende Daten vollständig nachgeladen   |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| FA- ERF -05        | Manuelle Ablesung über Ableseaufträge mit Erinnerung; Werte landen in der Zeitreihe; pro Zähler abschaltbar, sobald automatisch gemessen wird                                                                                                                                              | MUSS   | Nicht jeder Zähler kann im Gebäude an ein automatische Zählererfassung via Datenlogger angebunden werden - ohne manuelle Erfassung fehlen gewisse Verbräuche | Ablesung in der Zeitreihe; Auftrag terminierbar                       |
| FA- ERF -06        | Mobile/Feld-WebApp für die Ablesung vor Ort                                                                                                                                                                                                                                                | SOLL   | Komfort, kein Muss - Werte lassen sich auch nacherfassen; native App spürbar teurer                                                                          | Ablesung am Mobilgerät erfassbar und synchronisiert                   |
| FA- ERF -07        | Meteodaten müssen mindestens in einer Stundenauflösung von allen Meteo- Schweiz Stationen im System zur Verfügung stehen                                                                                                                                                                   | MUSS   | Ohne Meteo-Daten keine Heizgradtagberechnung und keine Referenzverbrauchsberechnung möglich                                                                  | Meteo Daten sind in der Granularität verfügbar                        |
| FA- ERF -08 (NE U) | Erstellung von Messkonzept sowie Topologieschema-Zähler werden im Tool erstellt. Diese Informationen werden genutzt für den Aufbau des neuen Standortes. Für bestehende Strukturen im System soll ein zurück lesen möglich sein um fehlende Messkonzepte nachträglich erstellen zu können. | MUSS   | Senkt Aufwand in den Projektphasen                                                                                                                           |                                                                       |
| FA- ERF -09 (NE U) | Geführtes Onboarding neuer Standorte/Datenquellen: automatisch erkannte Datenpunkte werden als Entwürfe vorgeschlagen, fachlich geprüft und erst nach Freigabe übernommen (Discovery, keine Blindübernahme)                                                                                | SOLL   | Senkt Aufwand und Fehlerquote beim Anschluss neuer Liegenschaften; Übernahme bleibt kontrolliert                                                             | Neuer Datenpunkt erscheint als Entwurf; Übernahme erst nach Review    |
| FA- ERF -10 (NE U) | Rohdaten-Vollsicht der Übertragungskette (jede empfangene Nachricht einsehbar, zeitlich begrenzt vorgehalten) zur Qualitätssicherung der Erfassung                                                                                                                                         | MUSS   | Diagnose: unterscheidet «Quelle sendet nicht» von «System verarbeitet nicht»                                                                                 | Empfangene Rohnachricht zu beliebigem Zeitpunkt einsehbar             |
| FA- ERF -11 (NE U) | Momentan-/Zustandswerte (Leistung, Temperaturen, Betriebszustände) zusätzlich zu Zählerständen erfassen und den Objekten zuordnen                                                                                                                                                          | SOLL   | Voraussetzung für Effizienz- Kennzahlen (COP) und Betriebsdiagnose über reine Verbräuche hinaus                                                              | Momentanw erte in Zeitreihe, Objekt zugeordnet                        |

## A2 Datenmodell &amp; Synchronisation (MOD)

| ID          | Anforderung                                                                                                                                                                                                                                                                                                                        | Prio Produktiv   | Prio MVP   | Begründung Prio                                                                                                                                           | Nachweis                                                                                                       |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| FA- MO D-01 | Struktur (Buchungskreis Wirtschaftseinheit Technische Anlage (Beispiel Heizzentrale) Gebäude Fläche Zähler Zählwerk) lückenlos führen; jede Änderung der Struktur und einer Messgrösse (Metric oder Variablen) erzeugt einen neuen Zeitabschnitt, alte Werte bleiben datiert erhalten                                              | MUSS             |            | Grundlage dafür, dass historische Werte korrekt bleiben und Berechnung über den gesamten Erfassungszeitraum konsistent bleiben.                           | Strukturänder ung erzeugt neuen Zeitabschnitt; Historie lückenlos                                              |
| FA- MO D-02 | 15-Minuten-Werte korrekt zu Tages-, Wochen-, Monats- und Jahreswerten zusammenfassen; beim Wechsel der Granularität zählt nichts doppelt. Mindestdatenhaltung, 15-Minuten-Werte 10 Jahre, Tages- und Wochen-Werte 7 Jahre, Monats- und Jahres-Werte 10 Jahre.                                                                      | MUSS             |            | Voraussetzung für korrekte Jahreswerte und Kennzahlen                                                                                                     | Aggregation 15minJahr reproduzierbar ; kein Sprung beim Wechsel                                                |
| FA- MO D-03 | Beim Nachladen aus SAP gehen keine Daten verloren: bestehende Objekte werden über eine feste Kennung (Wirtschaftseinheit, Gebäude) wiedererkannt (keine Dubletten), Änderungen erzeugen einen neuen Zeitabschnitt (alte Werte bleiben gültig), in SAP entfernte Objekte bleiben mit ihrer Historie erhalten (nur inaktiv markiert) | MUSS             |            | Die jahrelange Historie ist der Wert des Systems; ein Abgleich, der SAP 1:1 spiegelt, würde sie überschreiben oder löschen. Produktselektionsentscheidend | In SAP entferntes Objekt bleibt mit Historie erhalten wird per Datum geschlossen; Abgleichproto koll vorhanden |

| FA- MO D-04         | Kanonische Parametrierung: Zähler werden Anlagen-Typen Strukturiert zugewiesen, welche mit Attributen ergänzt zu einem vergleichbaren Pool werden (gleiche Anlagen-typen miteinander vergleichen). je Anlagentyp müssen Kennzahl-Definitionen (Formeln, z. B. COP = Wärme/Strom) hinterlegbar sein -erst damit wird der «vergleichbare Pool» tatsächlich rechenbar.   | MUSS   | Das EDM wird einer breiteren Nutzerschaft zugänglich gemacht, da das Messkonzept wissen unwichtiger wird. Daten werden strukturiert und so nutzbar für weitere Systeme (BI-Tool, SAP, ....), der Aufwand für Änderungen und Erweiterungen sinkt auf ein Minimum Einmal entwickeln und dann ausrollen auf alle.   | Anlagenstrukt ur im System ausgebaut. Anlagen- Typen und Attribute sind definiert.   |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| FA- MO D- 05 ( NEU) | Bewusste Versions-Korrektur: fehldatierte Gültigkeitszeiträume (gültig ab) durch den Fachanwender rückdatierbar -mit Überlappungsschutz, Pflicht-Begründung und Protokoll, ohne Datenbank-Eingriff                                                                                                                                                                    | SOLL   | Erfassungsdatum physischer Beginn ist ein Regelfall; ohne geführte Korrektur entstehen undokumentierte Backend-Eingriffe                                                                                                                                                                                         | Rückdatierung mit Begründung; Überlappung wird abgewiesen                            |
| FA- MO D- 06 ( NEU) | Strukturpflege direkt im Strukturbaum: Anlagen (inkl. Unteranlagen) verschieben, Zähler/Zählwerke umhängen, Gebäude/Zähler anlegen -jede Änderung erzeugt historisierte Zuordnungszeiträume                                                                                                                                                                           | SOLL   | Strukturänderungen sind Alltag; Pflege am Ort der Anschauung senkt Fehler                                                                                                                                                                                                                                        | Umhängen erzeugt neuen Zuordnungsze itraum; Historie einsehbar                       |
| FA- MO D- 07 ( NEU) | Hierarchische Aggregation AnlageUnteranlagen (Parent/Child) mit ausgewiesenem Abdeckungsgrad der Untermessung                                                                                                                                                                                                                                                         | SOLL   | Zeigt, welcher Anteil einer Hauptmessung durch Untermessungen abgedeckt ist und hilft bei einer 100% Untermessungsabdeckung Zählerausfälle zu detektieren.                                                                                                                                                       | Parent/Child- Ansicht mit Abdeckungsgr ad                                            |

## A3 Berechnung, Aufbereitung &amp; Datenqualität (CAL)

| ID                 | Anforderung                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Prio Produktiv   | Prio MVP   | Begründung Prio                                                                                                                                                                         | Nachweis                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| FA- CAL- 01        | Verbräuche den Gebäuden zuordnen und aufsummieren; fehlt eine gebäudescharfe Messung, nach Energiebezugsfläche (EBF) aufteilen. Aufteilungsregeln ohne Programmieren einstellbar Zuordnungs-Formeln müssen Addition UND Subtraktion mit Faktor erlauben (Eigenerzeugung: Verbrauch = Netzbezug + PV-Erzeugung Netz-Abgabe); die Quellenauswahl nach Medium filtern, aber nicht hart nach Richtung -sonst sind PV- Konstellationen nicht abbildbar.                                   | MUSS             |            | Grundfunktion; die Regeln müssen fachlich pflegbar sein                                                                                                                                 | Aggregat = Summe; Aufteilung gemäss EBF- Anteilen; Regel im UI pflegbar |
| FA- CAL- 02        | Witterungsbereinigung (Heizgradtage/Klimadaten) und Umrechnung der Energieträger auf eine gemeinsame Einheit (kWh) über versionierte Heizwerte; jederzeit reproduzierbar rohe UND bereinigte Reihe gemeinsam ausweisen (Nachvollziehbarkeit), laufende (angebrochene) Periode nicht bereinigen, Normperiode definieren.                                                                                                                                                              | MUSS             |            | Vergleichbare Energiekennzahlen über Träger und Jahre; die Werte gehen ans THG-Projekt und müssen prüfbar sein                                                                          | Neuberechn ung eines Stichtags identisch; Verfahren dokumentiert        |
| FA- CAL- 03        | Datenqualität sichern: unplausible Werte erkennen, Lücken melden, Korrekturen über einen Freigabeworkflow mit Protokoll. (a) Ersatzwerte in Zeitreihe UND Auswertungen dauerhaft sichtbar kennzeichnen, (b) Energiemenge der Korrektur über Zählerstände gesichert, (c) QS- Ausweis Soll (Zählerstands-Differenz) vs. effektiv verteilte Menge, (d) Korrektur wiederholbar (Wiedereröffnen), (e) benachbarte Lückenperioden zusammenführbar (Fehleinlesungen dazwischen verwerfbar). | MUSS             |            | Geprüfte Daten sind der Zweck des Tools SOLL MUSS. Ohne Formel- Zeitreihen ist keine korrekte Gebäudebilanz mit Eigenerzeugung (PV) möglich -das wird ab Tag 1 gebraucht, nicht später. | Unplausibler Wert markiert; Lücke gemeldet; Korrektur protokolliert     |
| FA- CAL- 05 ( NEU) | Ersatzwert-Korrektur am Ort der Entdeckung: fehlerhaft gebildete Ersatzwerte direkt aus der Lastgang-Ansicht prüfen, Lücken-Perioden zusammenführen und mit gewählter Methode neu bilden. Rechtsgrundlage für die Ersatzwerte müssen nach Metering Code Schweiz (MC- CH2025, 6.2-6.3.3) - VSE umgesetzt werden                                                                                                                                                                       | MUSS             |            | Verkürzt den Weg von der Sichtung zur Korrektur auf zwei Klicks                                                                                                                         | Markierung im Chart führt zur Korrektur; Neuberechn ung aus der Ansicht |
| FA- CAL- 06 ( NEU) | Qualitätssicherung der Ersatzwertbildung: je Lücke Soll (Zählerstands-Differenz) gegen effektiv verteilte Menge ausweisen                                                                                                                                                                                                                                                                                                                                                            | MUSS             |            | Prüfbarkeit der Korrektur selbst- keine Energie «verloren» oder «erfunden»                                                                                                              | Soll/Verteilt je Lücke mit Abweichung sichtbar                          |
| FA- CAL- 07 ( NEU) | Zählerstands-Anomalien (Sprünge, Rücksetzer, Negativwerte) als eigene Fallklasse erkennen und über Workflow korrigieren, ausschliessen oder bestätigen                                                                                                                                                                                                                                                                                                                               | SOLL             |            | Zählerwechsel /Fehleinlesungen sind die häufigste Ursache falscher Jahreswerte                                                                                                          | Anomalie- Workflow mit Entscheidun g und Protokoll                      |

| ID                 | Anforderung                                                                                                                                                                                                                                                                                                                      | Prio Produktiv   | Prio MVP   | Begründung Prio                                                                            | Nachweis                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| FA- AUS- 01        | Auswertungen und Dashboards je Objekt/Wirtschaftseinheit/Portfolio (Verbrauch, Erzeugung), periodisch und ad hoc Auswertungen müssen mit einem klick von 15min Werten in kW 1Jahr Tageswerte kWh 3Jahre Wochenwerte kWh 3Jahre Monatswerte kWh 5 Jahre Jahreswerte kWh 10 Jahre wechseln können. die Ladezeit dieser Charts <2s. | MUSS             |            | Kern-Ergebnis des Tools. Grundvoraussetzung für eine effiziente Arbeitsweise mit dem Tool. | Auswertung über frei wählbaren Zeitraum/Ebene                       |
| FA- AUS- 02        | Energiedaten interoperabel ans THG-Projekt bereitstellen (definiertes Schema, Granularität - Energieträgerscharf, Aggregation) sowie Energiestatistik-Exporte (VEK /ESTAT) im geforderten Format                                                                                                                                 | MUSS             |            | Daseinszweck: Energiedaten-Basis für THG-Reporting und Statistik                           | Bereitstellung im vereinbarten Schema; Export im geforderten Format |
| FA- AUS- 03        | Sprachen DE/FR/IT (DE Basis, FR/IT umschaltbar)                                                                                                                                                                                                                                                                                  | SOLL             |            | Überwiegend DE- Nutzende; FR/IT bei Bedarf                                                 | UI/Bericht in DE; FR/IT aktivierbar                                 |
| FA- AUS- 04        | Offene API / I14Y-Registrierung für aggregierte Kennzahlen                                                                                                                                                                                                                                                                       | KANN             |            | Ohne konkreten Abnehmer auf Vorrat - als Möglichkeit, nicht als Erwartung                  | API/Eintrag bei Bedarf                                              |
| FA- AUS- 05        | Kartenbezug/Geosuche (EPSG:2056)                                                                                                                                                                                                                                                                                                 | KANN             |            | Kein Kernnutzen,                                                                           | Gebäude /Heizzentralen verortet                                     |
| FA- AUS- 06 ( NEU) | Energiesignatur je Messgrösse (Tagesenergie vs. Aussentemperatur) mit Vorher /Nachher-Färbung ab dokumentierter Optimierungsmassnahme und rechnerischem Wirkungsnachweis (kWh/Jahr, CHF/Jahr, witterungsfair)                                                                                                                    | SOLL             |            | Macht die Wirkung jeder Betriebsoptimierung belegbar                                       | Signatur mit Vorher /Nachher; Einsparung beziffert                  |
| FA- AUS- 07 ( NEU) | Betriebszeiten-Profil (Wochentag × Stunde) mit einstellbarer Nutzungszeit und Kennzahl «Verbrauch ausserhalb Nutzungszeit» (%, kWh/Jahr, CHF/Jahr)                                                                                                                                                                               | SOLL             |            | Nacht- /Wochenendverbrauch ist das direkteste Sparpotenzial                                | Profil mit Nutzungszeit- Zone und Kennzahl                          |
| FA- AUS- 08 ( NEU) | Energiefluss-Diagramm (Sankey) je Periode aus der Anlagenstruktur, richtungsgetrennt                                                                                                                                                                                                                                             | KANN             |            | Vermittelt die Energieströme des Standorts auf einen Blick                                 | Sankey je Monat abrufbar                                            |
| FA- AUS- 09 ( NEU) | Lastspitzen-Ursachenanalyse: je Spitze die Beiträge aller Messstellen gleichen Mediums im selben Zeitfenster (inkl. entlastender Erzeugung) sowie Peak-Shaving- Potenzial je Schwelle                                                                                                                                            | SOLL             |            | Grundlage für Lastmanagement und Leistungstarif-Optimierung                                | Drilldown je Spitze mit Anteilen; Potenzial je Schwelle             |
| FA- AUS- 10 ( NEU) | Standard-Analyseformen: Dauerlinie, Kalender-Heatmap, Periodenvergleiche (DoD /DoW/WoW/MoM/YoY), frei kombinierbare Zusatz-Zeitreihen inkl. Wetter-Overlay                                                                                                                                                                       | SOLL             |            | Handwerkszeug der Energieanalyse                                                           | Analysesichten je Messgrösse abrufbar                               |
| FA- AUS- 11 ( NEU) | Effizienz-Kennzahlen je Anlagentyp (z.B. COP, JAZ) formelbasiert definierbar und als Langzeit-Trend abrufbar                                                                                                                                                                                                                     | SOLL             |            | Schleichende Degradation wird sichtbar, bevor sie Geld kostet                              | KPI-Definition je Typ; Trend je Anlage                              |
| FA- AUS- 12 ( NEU) | PNG-/CSV-Export jeder Lastgang-Ansicht                                                                                                                                                                                                                                                                                           | SOLL             |            | Weiterverwendung in Berichten ohne Systemzugang                                            | Export aus der Ansicht                                              |

## A5 Zugriff &amp; Administration (ADM)

| ID          | Anforderung                                                                                                                                                                                   | Prio Produktiv   | Prio MVP   | Begründung Prio                                                                                             | Nachweis                                                           |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| FA- ADM- 01 | Rollenbasierte Berechtigungen (nur nötige Rechte, zeitlich begrenzbar, Superuser geregelt)                                                                                                    | MUSS             |            | Zugriffsschutz und Datenschutz (DSG)                                                                        | Nutzer sieht nur zugewiesene OE /Funktionen; Vergabe protokolliert |
| FA- ADM- 02 | Referenzdaten pflegen: Energieträger-Umrechnung (Heizwerte, z. B. m³- Gas kWh), Wetterstationen, Klassifikationen - versioniert mit Gültigkeitsdatum. Emissionsfaktoren liegen im THG-Projekt | MUSS             |            | Ohne pflegbare, versionierte Heizwerte keine vergleichbaren, reproduzierbaren Energiekennzahlen (FA-CAL-02) | Heizwert- /Referenzänderung neue Version mit Gültigkeitsdatum      |
| FA- ADM- 03 | Getrennte Test- und Produktivumgebung mit getrennten Daten                                                                                                                                    | MUSS             |            | Betriebshygiene; günstig umzusetzen                                                                         | Test- und Prod- Daten strikt getrennt                              |

| FA- ADM- 04 (N EU)   | Integrierte, durchsuchbare Wissensdatenbank (Konzept-, Anwender- und Änderungs-Doku) mit kontextbezogenen Hilfe-Einstiegen aus den Fachseiten   | SOLL   | Wissenssicherung personenunabhängig; senkt Einarbeitungs- und Supportaufwand   | Hilfe-Einstieg öffnet passende Doku; Volltextsuche   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------|------------------------------------------------------|
| FA- ADM- 05 (N EU)   | Aufgaben-/Ideenspeicher mit Priorisierung, Aufwand/Nutzen und Test- Status je Thema                                                             | KANN   | Nachvollziehbare Weiterentwicklung; Anforderungen gehen nicht verloren         | Backlog mit Status im System                         |
| FA- ADM- 06 (N EU)   | Übersetzungspflege im laufenden System (DB-gestützt, CSV-Ex-/Import) statt Code-Änderung je Textkorrektur                                       | KANN   | Sprachpflege durch Fachpersonen ohne Release                                   | Textänderung ohne Release wirksam                    |

## A6 Energiecontrolling &amp; Alarmierung (CTL)

| ID                 | Anforderung                                                                                                                                              | Prio Produktiv   | Prio MVP   | Begründung Prio                                                                           | Nachweis                                                                   |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| FA- CTL- 01        | Auffällige Verbräuche (über Schwelle oder vom Muster abweichend) erkennen und melden                                                                     | SOLL             |            | Typischer Mehrwert eines EMIS; im Tagesbatch machbar, aber nicht für die Auswertung nötig | Anomalie über Schwelle /Muster Benachrichtigung; Fehlalarm-Quote steuerbar |
| FA- CTL- 02        | Soll-Ist-Vergleich gegen Energie-Zielpfade je Objekt mit Abweichungsanzeige                                                                              | KANN             |            | Steuerungsmehrwert, spätere Ausbaustufe; Netto-Null-Bezug entsteht über das THG-Projekt   | Zielpfad je Objekt hinterlegt; Abweichung IstZiel ausgewiesen              |
| FA- CTL- 03 (N EU) | Benchmarking je Gebäude (kWh/m²·a auf Basis EBF) gegen Zielwerte aus der Projektplanung (eigene Werte, Minergie, SIA 380 /1, SNBS) mit Ampelstatus       | SOLL             |            | Verbindet Betrieb mit Planungs- Soll; GL-taugliche Sicht                                  | Kennzahl je Gebäude gegen Zielwert mit Status                              |
| FA- CTL- 04 (N EU) | Massnahmen-/Ereignisjournal direkt am Lastgang (u.a. Typ «Optimierung»), Ereignisse als Marker in der Zeitreihe und als Trigger für den Wirkungsnachweis | SOLL             |            | Dokumentiert, warum sich Verbräuche ändern -verknüpft Massnahme und Messung               | Ereignis am Zeitpunkt erfasst; Marker im Chart                             |
| FA- CTL- 05 (N EU) | Vorfall-Management für Erfassungsstörungen: Posteingang mit Wurzel-Ursache je Vorfall, In-App-Benachrichtigung und E-Mail- Kanal                         | SOLL             |            | Aus «Zähler sendet nicht» wird ein bearbeitbarer Vorfall statt einer stillen Lücke        | Vorfall mit Ursache und Status im Posteingang                              |

## Abgrenzung (WIRD NICHT)

Bewusst ausserhalb des Scope, damit die Entscheidung dokumentiert statt implizit ist.

| ID     | Abgrenzung                               | Prio       | Begründung                                                                                                                  |
|--------|------------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------|
| WN- 01 | Energiekosten/Tarife /Rechnungsprüfung   | WIRD NICHT | Kaufmännische Funktion; bleibt in SAP FI. Das EDM liefert nur Mengen/Kennzahlen                                             |
| WN- 02 | Mieter-/Nebenkostenabrechnung            | WIRD NICHT | Gehört zum Mietprozess in SAP RE-FX. EDM kann die Verteilschlüssel anhand des effektiven Verbrauches liefern.               |
| WN- 03 | Abfalldaten                              | WIRD NICHT | Andere Datenform (Mengen/Fraktionen je Abholung, kein Lastgang); passt nicht ins Zählermodell                               |
| WN- 04 | THG-/Emissionsbilanzierung (Scope 1/2/3) | WIRD NICHT | Eigenes THG-Projekt; das EDM liefert die Energiedaten interoperabel zu (FA-AUS-02), bilanziert aber selbst keine Emissionen |

## 3. Nicht-funktionale Anforderungen (B)

## Folgend:

- Verankert an ISO/IEC 25010 / 25012.
- BK DTI Vorgaben:  https://www.bk.admin.ch/de/vorgaben
- BACS Informatiksicherheitsvorgaben Bund: https://www.ncsc.admin.ch/ncsc/de/home/dokumentation/sicherheitsvorgaben-bund.html
- Priorisierung unter Annahme von BACS Grundschutz: https://www.ncsc.admin.ch/ncsc/de/home/dokumentation/sicherheitsvorgaben-bund /sicherheitsverfahren/grundschutz.html

## B1 Sicherheit (SEC)

| ID   | Anforderung   | Prio Produktiv   | Prio MVP   | Begründung   | Nachweis   |
|------|---------------|------------------|------------|--------------|------------|

| NFA- SEC- 01        | Verschlüsselung in-transit (TLS, erzwungen) und at-rest (Tiefe risikobasiert, verschärft bei erhöhtem Schutzbedarf); Schlüssel getrennt verwaltet                                 | MUSS   | Stand der Technik; Tiefe skaliert mit Schutzbedarf, Hängt von den Auslandstandorten ab und wie diese Daten klassifiziert werden.   | TLS erzwungen; at- rest aktiv; Key- Mgmt getrennt                |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| NFA- SEC- 02        | Manipulationsgeschützter Audit-Trail: sicherheitsrelevante Zugriffe (inkl. Admin) Fachdaten-Änderungen/Korrekturen (wer/was und /wann)                                            | MUSS   | Zugriffs- + Änderungsnachweis; ISG /DSG-relevant                                                                                   | Beides protokolliert, manipulationsgesc hützt; Frist gesetzt     |
| NFA- SEC- 03        | Datenintegrität: Werte gegen unbefugte/unbemerkte Änderung geschützt; Import vollständig/unverfälscht (Duplikat-/Lückenkontrolle)                                                 | MUSS   | Zweck = prüfbare Zahlen                                                                                                            | Wertänderung nur über protokollierten Pfad; Importprüfung greift |
| NFA- SEC- 04 (N EU) | Least-Privilege auf Datenbank-Ebene: Anwendung verbindet ohne Superuser-Rechte; keine Dienste-Ports öffentlich, wo lokal genügt                                                   | SOLL   | Begrenzt den Schaden einer kompromittierten Anwendung                                                                              | App-Rolle ohne Superuser; Portbindung minimal                    |
| NFA- SEC- 05 (N EU) | Sicherheits-Gates in der Auslieferungs-Pipeline: Secret-Scan, Abhängigkeits-Audit (kritisch = blockierend), statische Analyse auf Injektionsmuster -vor jedem Release automatisch | SOLL   | Verhindert die häufigsten Fehlerklassen strukturell statt per Review-Disziplin                                                     | Release mit kritischem Befund wird blockiert                     |
| NFA- SEC- 06 (N EU) | Strikte Content-Security-Policy ohne unsafe-inline (XSS-Härtung des gesamten Frontends)                                                                                           | SOLL   | Wirksamste Einzelmassnahme gegen Script-Injection                                                                                  | CSP ohne unsafe- inline aktiv                                    |
| NFA- SEC- 07 (N EU) | Dokumentierte Sicherheitsarchitektur/Threat Model und wiederkehrende interne Sicherheits-Audits mit Findings-Verfolgung                                                           | SOLL   | Sicherheitsniveau bleibt nachvollziehbar und wird periodisch geprüft                                                               | Threat Model aktuell; Audit- Findings nachverfolgt               |

Weiteres an seinem Ort: Zugriffsschutz/RBAC  FA-ADM-01 · 2FA eIAM/AGOV  CON-06 · CH-Hoheit  CON-07.

## B2 Datenqualität (DAT)

| ID          | Anforderung                                                                                  | Prio Produktiv   | Prio MVP   | Begründung                              | Nachweis                             |
|-------------|----------------------------------------------------------------------------------------------|------------------|------------|-----------------------------------------|--------------------------------------|
| NFA- DAT-01 | Messbare DQ-Ziele je Quelle/Periode (Aktualität, Vollständigkeit, Genauigkeit) mit Schwellen | SOLL             |            | Zielwerte aus offenem Punkt 4           | Schwellen gemessen /eingehalten      |
| NFA- DAT-02 | Durchgängige Lineage je Datenobjekt (Herkunft Faktor-Version Ergebnis)                       | SOLL             |            | Audit-Veredelung über FA- CAL-02 hinaus | Lineage zu beliebigem Wert abfragbar |

## B3 Verfügbarkeit &amp; Betrieb (BET)

| ID                   | Anforderung                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Prio Produktiv   | Prio MVP   | Begründung                                                  | Nachweis                                            |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|-------------------------------------------------------------|-----------------------------------------------------|
| NFA - BET- 01        | Backup/Recovery mit RTO/RPO; Wiederanlauf ohne Verlust über RPO hinaus                                                                                                                                                                                                                                                                                                                                                                                                                  | MUSS             |            | Datenverlust = teuerster Schaden                            | Recovery- Test bestanden                            |
| NFA - BET- 02        | Performance, es muss eine fliessende Arbeitsweise möglich sein. Der Seitenwechsel inkl. das Laden von Standard-Zeitreiehen <1s (15min - 1Jahr, Tag 1-Jahr, Woche 2Jahre, Monate 5Jahre, Jahre 10Jahre), übernehmen von Änderungen in den Stammdaten < 300 - 500ms, Exports von csv können im Hintergrund laufen max. 20s jedoch stark abhängig von der export-Grösse Skalierbarkeit für Zeitreihenvolumen 40'000 Zähler mit 8 Register, 15-min, 80 User und 30 gleichzeitig am Arbeiten | MUSS             |            | Muss reale Datenmenge tragen                                | Lasttest bestanden                                  |
| NFA - BET- 03        | Verfügbarkeit & Support pragmatisch (Bürozeiten; kein 24×7)                                                                                                                                                                                                                                                                                                                                                                                                                             | SOLL             |            | Tagesbatch; vorbehältlich Schutzbedarf                      | SLA passend zur Kritikalität                        |
| NFA - BET- 04        | Betriebsprozesse (Incident/Change/Release) und operatives Monitoring                                                                                                                                                                                                                                                                                                                                                                                                                    | SOLL             |            | Auf Tool- Grösse skalierbar                                 | Betriebshand buch; Monitoring aktiv                 |
| NFA - BET- 05 ( NEU) | Ausliefer-Sicherheit: automatischer Funktionstest nach jedem Deployment; bei Fehlschlag automatischer Rückfall auf den letzten funktionierenden Stand                                                                                                                                                                                                                                                                                                                                   | SOLL             |            | Begrenzt Ausfallzeit durch fehlerhafte Releases auf Minuten | Fehlerhaftes Release wird automatisch zurückgerollt |

| NFA - BET- 06 ( NEU)   | Betriebs-Cockpit: Job-Status, Tagesvollständigkeit der Erfassung, Deployment-Zustand auf einen Blick   | SOLL   | Betriebszustand ohne Log- Analyse beurteilbar   | Cockpit zeigt Zustand aller Erfassungs- Jobs   |
|------------------------|--------------------------------------------------------------------------------------------------------|--------|-------------------------------------------------|------------------------------------------------|

## B4 Benutzbarkeit (USE)

| ID          | Anforderung                                                                     | Prio Produktiv              | Prio MVP   | Begründung                                                               | Nachweis                        |
|-------------|---------------------------------------------------------------------------------|-----------------------------|------------|--------------------------------------------------------------------------|---------------------------------|
| NFA- USE-01 | Funktional brauchbares, konsistentes UI (auch für Gelegenheits-/Ablesenutzende) | MUSS                        |            | Tool muss bedienbar sein                                                 | Usability-Feedback dokumentiert |
| NFA- USE-02 | Barrierefreiheit WCAG 2.1 AA / eCH-0059                                         | SOLL MUSS bei Betroffenheit |            | Wird MUSS, sobald betroffene Mitarbeitende es brauchen (offener Punkt 2) | Prüfung nach Klärung            |
| NFA- USE-03 | CD-Bund-Theming                                                                 | KANN                        |            | Keine Rechtspflicht intern                                               | -                               |

## B5 Interoperabilität (IOP)

| ID          | Anforderung                                                                 | Prio Produktiv   | Prio MVP   | Begründung                           | Nachweis                  |
|-------------|-----------------------------------------------------------------------------|------------------|------------|--------------------------------------|---------------------------|
| NFA-IOP- 01 | Once-Only: kein Schattenregister, Stammdaten read-only aus führendem System | MUSS             |            | Vorgabe CON-05; Umsetzung FA- ERF-02 | Keine Doppelpflege belegt |
| NFA-IOP- 02 | Offene (FAIR) Schnittstellen ohne proprietäre Pflicht-Formate               | SOLL             |            | Relevant mit externen Konsumenten    | API-Doku offen            |
| NFA-IOP- 03 | eCH-Konformität / I14Y der API                                              | KANN             |            | Macht FA-AUS-04 standardkonform      | Eintrag bei Bedarf        |

## B6 Wartbarkeit &amp; Portabilität (WAR)

| ID                  | Anforderung                                                                                                                                                                  | Prio Produktiv          | Prio MVP   | Begründung                                                                | Nachweis                                           |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|------------|---------------------------------------------------------------------------|----------------------------------------------------|
| NFA- WAR- 01        | Datenexport/Exit: Vollexport in offenen Formaten, dokumentiertes Schema, kein Lock-in                                                                                        | MUSS                    |            | Kernkriterium gegen Lock-in                                               | Vollexport + Exit- Szenario                        |
| NFA- WAR- 02        | Modularität/Entkopplung, versionierte Verträge                                                                                                                               | SOLL (Bewertungs krit.) |            | In Buy nicht vorschreibbar                                                | Architekturdoku zeigt Entkopplung                  |
| NFA- WAR- 03        | Testbarkeit; Patch-/Release-Zyklus inkl. Schwachstellenmanagement                                                                                                            | SOLL                    |            | Hygiene + sicherheitsrelevant                                             | Testkonzept; Patch-SLA                             |
| NFA- WAR- 04        | Ressourcenschonender Betrieb (P026)                                                                                                                                          | KANN                    |            | Geringe Hebelwirkung                                                      | Nachweis bei Bedarf                                |
| NFA- WAR- 05 (NE U) | Lückenlose Änderungshistorie des Systems selbst: jede Code-/Schema- Änderung versioniert; Schema-Änderungen als nummerierte, idempotente Migrationen mit Anwendungsprotokoll | SOLL                    |            | Reproduzierbarkeit des Systems -nicht nur der Daten                       | Migrationslauf protokolliert; Stand reproduzierbar |
| NFA- WAR- 06 (NE U) | Getrennte Entwicklungsumgebung mit produktionsnah geseedeten Daten und definierter Promotions-Pipeline (Entwicklung Freigabe Produktion)                                     | SOLL                    |            | Änderungen werden am echten Datenbild getestet, bevor sie produktiv gehen | Promotionsweg mit Gates dokumentiert               |
| NFA- WAR- 07 (NE U) | Änderungs-Kommunikation im System: anwenderverständliche Release Notes («Was ist neu») mit Verweis auf Doku und Aufgaben                                                     | KANN                    |            | Anwender erfahren Neuerungen ohne Schulungsaufwand                        | Release Notes je Periode abrufbar                  |

## B7 Sicherheits- &amp; Datenschutz-Governance (BBL-Bringpflicht - kein Entwickleraufwand)

| ID     | Anforderung                                                               | Prio Produktiv   | Prio MVP   | Regime   |
|--------|---------------------------------------------------------------------------|------------------|------------|----------|
| GOV-01 | Schutzbedarfsanalyse (Schuban); bei erhöht ISDS-Konzept mit Risikoanalyse | MUSS             | MUSS       | ISG/ISV  |

| GOV-02   | Klassifizierungskonzept (Informationsklassifizierung + Schutzbedarf je Datenkategorie)   | MUSS        | KANN     | ISG   |
|----------|------------------------------------------------------------------------------------------|-------------|----------|-------|
| GOV-03   | Cybervorfall-Prozess (Melde-/Eskalation ISBO/BACS)                                       | MUSS        | SOLL     | ISG   |
| GOV-04   | Penetrationstests risikobasiert; bei erhöht zwingend                                     | SOLL        | Abklären | ISG   |
| GOV-05   | Bearbeitungsverzeichnis (DSG Art. 12)                                                    | MUSS        | KANN     | DSG   |
| GOV-06   | Personendaten-Inventar; DSFA-Vorabprüfung (Durchführung nur bei hohem Risiko)            | MUSS / SOLL | Abklären | DSG   |
| GOV-07   | Aufbewahrung/Löschkonzept (GEVER-konform)                                                | MUSS        | KANN     | DSG   |
| GOV-08   | ISO 27'000 IT Sercurity                                                                  | SOLL        | KANN     |       |

## 4. Rahmenbedingungen / Constraints (C)

Gegebene, extern vorgegebene Randbedingungen (nicht verhandelbar).

| ID      | Constraint                                                                                                                    | Prio Produktiv                      | Prio MVP   | Bereich          |
|---------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|------------|------------------|
| CON- 01 | Vorgaben DTI (DigiV) einhalten                                                                                                | MUSS                                | MUSS       | Rechtlich        |
| CON- 02 | ISG/ISV und DSG/DSV verbindlich                                                                                               | MUSS                                | MUSS       | Rechtlich        |
| CON- 03 | Berichtszweck KlG Art. 10 / CO2-Gesetz / EnG                                                                                  | MUSS                                | MUSS       | Rechtlich        |
| CON- 04 | Barrierefreiheit gemäss BehiG prüfen; Umfang abhängig von Zugänglichkeit (intern vs. publikumszugänglich) Level in NFA-USE-02 | SOLL wird zu MUSS bei Betroffenheit | SOLL       | Rechtlich        |
| CON- 05 | Once-Only mit SAP ERP als führendem System (RE-FX, MDG u. a.)                                                                 | MUSS                                | MUSS       | Architektur      |
| CON- 06 | eIAM/AGOV als Identitäts-/Zugriffsdienst (2FA)                                                                                | MUSS                                | MUSS       | Architektur      |
| CON- 07 | CH-Souveränität: Daten und Betrieb in der Schweiz, CH-Durchgriff                                                              | MUSS                                | MUSS       | Architektur      |
| CON- 08 | Methodik RIAB/TOGAF/W010, HERMES; GEVER für geschäftsrelevante Ablage                                                         | MUSS / SOLL                         | SOLL       | Architektur      |
| CON- 09 | Interne Product Ownership beim BBL; Datenverantwortung der Vorsysteme bei den Fachstellen                                     | MUSS                                | MUSS       | Organisator isch |
| CON- 10 | Beschaffungsweg regelkonform (BöB/VöB, SB017) - Variantendetail separat                                                       | MUSS                                | MUSS       | Organisator isch |

## 5. Transition / Migration (D)

| ID      | Anforderung                                                                                                                                                                                       | Prio Produktiv   | Prio MVP   | Begründung Prio                                                                                                             | Nachweis                                                                    |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| MIG- 01 | Verlustfreie Übernahme von Historie (Zeitreihen inkl. Zeitabschnitte), Struktur/Zuordnungen (inkl. EBF-Aufteilungen), Konfiguration (Faktoren, Wetterstationen, Klassifikationen, Ableseaufträge) | MUSS             |            | jahrelange Historie ist der Wert des Systems                                                                                | Stichproben- Jahreswerte vor /nach identisch; Referenzobjekt strukturgleich |
| MIG- 02 | Lückenfreier Übergang (keine Tageslücke) mit definiertem Cut-over und Rückfalloption                                                                                                              | MUSS             |            | eine Tageslücke zerstört Jahreswerte                                                                                        | keine Lücke am Cut- over; Rollback-Plan                                     |
| MIG- 03 | Parallelbetrieb Alt/Neu mit Differenzabgleich für definierte Periode                                                                                                                              | SOLL             |            | senkt Risiko, aber nicht zwingend                                                                                           | Differenzbericht im Toleranzband                                            |
| MIG- 04 | Geordnete Stilllegung Altsystem (Datenexport/-archivierung, Vertrags- /Lizenzbeendigung, Aufbewahrung der Nachweise)                                                                              | MUSS             |            | sauberer Abschluss + Nachweispflicht                                                                                        | Stilllegungs- und Exportnachweis                                            |
| MIG- 05 | Konzept und Funktionen (API für Daten, Export-csv für Struktur und Attribute inkl. Historisierung) für eine nächste Migration müssen zur Verfügung stehen. API First                              | MUSS             |            | "Offenheit" senkt das Risiko für den Anwender in seiner Entscheidung auf ein zukünftiges nutzbringenderes Tool zu wechseln. | Konzept und Schnittstellen geprüft.                                         |

## 6. Offene Punkte

|   Nr | Offener Punkt                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------|
|    1 | Schutzbedarf bestätigen (Grundschutz vs. erhöht) - steuert die Sicherheits- und Verfügbarkeitsprioritäten |
|    2 | Barrierefreiheit: Geltung WCAG 2.1 AA für dieses interne Tool mit ISBO/Rechtsdienst klären                |
|    3 | Reporting-Schnittstellen ecCo/VEK/ESTAT: Format, Aggregationsgrad, Periodizität                           |
|    4 | Konkrete NFA-Zielwerte (Verfügbarkeit, Antwortzeiten, Latenz-SLA, Vollständigkeitsgrad)                   |
|    5 | SAP-Modul-Abgrenzung je Datenobjekt (RE-FX, MDG, Data Warehouse); DWH ggü. EDM-Berichtswesen              |
|    6 | SAP PM: technische Anlagen/Zähler künftig aus PM beziehen oder im EDM führen? (aktuell nicht in PM)       |
|    7 | Migrationsumfang/Historientiefe und Cut-over-Strategie                                                    |
|    8 | Betriebs-/Trägerschaftsmodell und HERMES-Rollen verbindlich klären                                        |

## 7. Verweise und Anhänge

Datei

Geändert

Keine Dateien zum Freigeben verfügbar

Ziehen Sie Dateien an diese Stelle, um sie hochzuladen, oder Dateien suchen