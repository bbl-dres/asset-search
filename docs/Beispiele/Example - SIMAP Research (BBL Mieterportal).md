## SIMAP Research

| Titel            | Referenzbericht: Abgeschlossene IT-Vergaben für das Mieterportal   |
|------------------|--------------------------------------------------------------------|
| Author           | David Rasner BBL                                                   |
| Status           | Entwurf                                                            |
| Stand 11.06.2026 |                                                                    |
| Klassifizierung  | Intern                                                             |

## Inhalt:

Management Summary

1. Ziel von Dokument
2. Referenz-Vergaben (funktionale Treffer)
3. Abrufbare Rahmenverträge (Beschaffungsweg ohne neue Ausschreibung)
4. Track-Record der im Marktscreening genannten Partner
5. Verweise und Anhang

5.1 Verweise

5.2 Anhang

## Management Summary

Das Vorhaben Mieterportal erfordert externe Entwicklungskapazität für eine wiederverwendbare Open-Source-Plattform (BPMN-Prozess-Engine, FormularEngine, Portal, eIAM/AGOV). Dieser Bericht wertet sämtliche seit Plattformstart von simap.ch (07/2024) publizierten Zuschläge aus (2'397 Datensätze, CPV 72/48) und beantwortet drei Beschaffungsfragen:

1. Der Markt liefert. Für jedes Element des Anforderungsprofils existiert mindestens eine abgeschlossene Schweizer Vergabe mit KMU-Gewinner. Der fachlich nächste Treffer - der Antrags-Workflow «Nutzer an IMMO inkl. Raumprogramm» der Stadt Zürich (CHF 346k, inpeek AG) - belegt, dass der Kern-Use-Case als Projekt unter CHF 350k umsetzbar ist. Vergleichbare Plattformvorhaben auf Kantonsebene (SmartService SZ, eBaubewilligung SG) liegen bei CHF 1,5 Mio.
2. Der Beschaffungsweg existiert bereits. Mit dem Rahmenvertrag SPRINT (Laufzeit bis 2033, BBL abrufberechtigt) ist das WTO-Verfahren bereits durchlaufen: MVP (&lt;1 Mio.) als Mini-Tender in Los 1, Plattform-Ausbau (1-5 Mio.) in Los 2. Mehrere im Marktscreening identifizierte Partner (Adfinis, Softcom, Liip) sind Vertragspartner. Zu prüfen bleiben die Zulässigkeit der Tranchierung (BöB Art. 15) und die Abdeckung der langfristigen Produktpflege. Für den Formular-Layer besteht mit dem Formularservice 2026-2036 (JAXForms) zudem ein abrufbarer BBL-Vertrag als Alternative zum Eigenbau.
3. Das Lock-in-Risiko der Buy-Variante ist empirisch belegt. Die Vergabehistorie der evidence-Plattform (Glaux Group: &gt;55 Mio. Gesamtvolumen, davon sieben freihändige Folgevergaben) zeigt das Abhängigkeitsmuster proprietärer Fachlösungen - und stützt die CreateEmpfehlung der ABC-Analyse.

Empfehlung: Beschaffung über SPRINT-Mini-Tender (Los 1 für den MVP); die hier dokumentierten Referenzvergaben dienen als Marktnachweis im Förderentscheid und als Basis für Einladungslisten. Konkrete Engine-Erfahrung (Operaton/Flowable) ist über simap nicht herleitbar und im Mini-Tender als Anbieterreferenz abzufragen.

## 1. Ziel von Dokument

Dieser Bericht schafft die vergaberechtliche und marktliche Evidenzbasis für den Beschaffungsentscheid zum Mieterportal. Er beantwortet auf Grundlage abgeschlossener IT-Vergaben ( simap.ch, 07/2024-06/2026) drei Fragen:

1. Marktnachweis: Welche vergleichbaren Vorhaben (Antrags-Workflow, Formular-Engine, Portal, BPMN, Open Source) wurden in der Schweiz bereits vergeben - zu welchen Preisen, in welchen Verfahren, an welche Anbieter?
2. Beschaffungsweg: Welche bestehenden Rahmenverträge erlauben den Abruf externer Entwicklungskapazität ohne neue WTO-Ausschreibung?
3. Risikoevidenz: Was zeigt die Vergabepraxis über die Folgekosten und Abhängigkeiten der Buy-Variante?

Anforderungsprofil (aus Lösungsarchitektur): wiederverwendbare Plattform mit BPMN-Prozess-Engine, Formular-Engine (Schema statt Code), Cockpit /Inbox, CD Bund/WCAG, eIAM/AGOV, Open Source, CH-Souveränität; Umsetzung als Create-Variante (Best-of-Breed-Stack) mit externer Entwicklungskapazität.

## Match-Rating:

| Rating   | Bedeutung                                                                                   |
|----------|---------------------------------------------------------------------------------------------|
|          | nahezu deckungsgleich: Antrags-Workflow + Formulare + Portal in der öffentlichen Verwaltung |
|          | stark verwandt: E-Gov-Portal oder Prozess-/Formularplattform, Teilaspekte des Profils       |

Kontext: Marktevidenz oder Track-Record, fachlich weiter entfernt

## 2. Referenz-Vergaben (funktionale Treffer)

|    | Datum   | Auftraggeber                           | Gegenstand (was wurde gemacht)                                                                                 | Verfahren   | Volumen CHF          | Zuschlagsempfänger                           | Match   | Kommentar                                                                                                                                                                                 |
|----|---------|----------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------|----------------------|----------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | 2026-04 | Stadt Zürich, Hochbaudeparte ment      | Workflow «Antrag Nutzer an IMMO inkl. Raumprogramm» -Antrags- Workflow von Nutzern an die Immobilienverwaltung | freihändig  | 345'727              | inpeek AG , Bern                             |         | Fast identische Domäne zum Mieterportal (Raumbedarf Prüfung Immobilienamt); beweist, dass dieser Use-Case als <350k- Projekt umsetzbar ist. simap                                         |
|  2 | 2025-12 | eGovernment St. Gallen digital.        | eBaubewilligungSG -digitaler Baubewilligungsprozess: geführter Antrag, Prüfung, Verfügung                      | freihändig  | 1'465'663            | Adfinis AG , Bern                            |         | Muster «Antrag-Prüfung- Freigabe» 1:1; Open-Source- Haus, im Marktscreening als Partner genannt, SPRINT-Los-1- Partner (Konsortium). simap                                                |
|  3 | 2026-01 | Amt für Informatik Kanton Schwyz       | «SmartService»- Prozessautomatisierungsplattform mit für kantonale Formularfunktionalität Leistungen           | offen       | 1'476'344            | ELCA Informatique SA, Pully                  |         | Wörtlich das Plattform-Zielbild (Prozesse + Formulare als wiederverwendbare Plattform); Preisreferenz für eine Kantonslösung. simap                                                       |
|  4 | 2026-03 | BBL                                    | Formularservice 2026-2036- Bereitstellung/Betrieb des Formular- Services der Bundesverwaltung                  | offen       | 4'311'028            | JAXForms AG , Zürich                         |         | Form-Engine-Referenz; bestehender BBL-Vertrag für den Formular-Layer ggf. direkt abrufbar statt selbst bauen. Dazu: Formularlösung Kanton BS (2'764'000), Stadt Lausanne (210'200). simap |
|  5 | 2025-10 | Stadt Biel                             | Software-Lösung Prozessmanagement -BPMN-basierte Prozessplattform                                              | offen       | 143'670              | Abel Systems , Basel                         |         | Einziger Zuschlag schweizweit mit explizitem BPMN-Bezug im Publikationstext; zeigt: kleines KMU, kleines Budget, gleiches Thema. simap                                                    |
|  6 | 2025-06 | Fonds für Verkehrssicherhe it          | FVS-Portal -Neuentwicklung Fachportal (Gesuche, Verwaltung)                                                    | offen       | 1'060'375            | Liip AG , Fribourg                           |         | Portal-Neubau im Bundesumfeld, Open Source, agil; Liip ist SPRINT-Los-2-Partner. simap                                                                                                    |
|  7 | 2025-09 | BBL                                    | F25156 SAKUBA Webportal- Webportal-Entwicklung für das BBL                                                     | freihändig  | 1'392'024            | Puzzle ITC AG , Bern                         |         | BBL kennt den Anbieter bereits; Open-Source-/OpenShift- Kompetenz (passt zu RHOS- Betriebsmodell). simap                                                                                  |
|  8 | 2026-01 | iGovPortal.ch (Verein)                 | Neuentwicklung Bürgerportal «NextGen» -Lose u.a. für - Keycloak Integration, Wartung, Weiterentwicklung        | offen       | Stundensätze 135-141 | Blackpoints AG, Zürich; IMS AG, Ittigen      |         | Gemeinschaftliche Portal- Plattform mehrerer Kantone; einziger Zuschlag mit explizitem Keycloak-Bezug (Stack-Match Auth-Layer). simap                                                     |
|  9 | 2025-01 | Kanton Luzern, Dienststelle Informatik | Entwicklungsleistungen E-Government -Rahmen für Individualentwicklung von E-Gov-Lösungen                       | offen       | je ~1'060'000        | Softcom Technologies SA , Fribourg + ti&m AG |         | E-Gov-Individualentwicklung als beschaffter Dienstleistungsrahmen; Softcom ist SPRINT-Los-1-Partner. simap                                                                                |
| 10 | 2025-03 | BBL                                    | F25066 Amtsblattportal Übergangslösung -Portalbetrieb/- entwicklung                                            | freihändig  | 681'030              | mimacom ag , Bern                            |         | mimacom ist das Schweizer Flowa -Haus direkter Bezug zur ble Prozess-Engine-Entscheidung (Flowable-Core als Operaton- Fallback). simap                                                    |
| 11 | 2025-04 | Kanton Wallis, Migrationsdienst        | eMigration «Portail Administrés»- Bürger-Antragsportal                                                         | freihändig  | 173'057              | Proactive Solutions SA , Sion                |         | Kleines Westschweizer KMU, Antragsportale als Kerngeschäft (2. Zuschlag: MontagnePro NG, 250'870). simap                                                                                  |
| 12 | 2024-09 | Kantonales Sozialamt Zürich            | Digitalisierung «Melde- und Abrechnungswesen» -Melde- /Antragsprozesse                                         | freihändig  | 358'027              | OwnShip Technology AG , Zürich               |         | Prozessdigitalisierung als kompaktes Projekt einer kleinen Firma. simap                                                                                                                   |
| 13 | 2026-02 | Stadt Zürich, GUD                      | Freiwilligen-Plattform -Matching /Workflow-Plattform                                                           | offen       | 276'875              | Apps with love AG , Bern                     |         | Plattform mit Rollen/Workflows, Berner KMU, offenes Verfahren gewonnen. simap                                                                                                             |
| 14 | 2026-05 | Kantonale Steuerverwaltung             | Redesign Steuerportal                                                                                          | freihändig  | 459'798              | Information Factory AG, Zürich               |         | Portal-Redesign freihändig vergeben -Beispiel für den <230k…460k-Bereich. simap                                                                                                           |
| 15 | 2025-02 | Stadt Biel                             | Ablösung Schalterlösung SOZ/ESD («guichets»)                                                                   | freihändig  | 345'000              | e-nov8 GmbH, Meilen                          |         | Guichet-/Schalterlösung durch Kleinstfirma. simap                                                                                                                                         |
| 16 | 2025-04 | eGovernment St. Gallen digital.        | E-Signatur-Dienst                                                                                              | offen       | 1'633'186            | DeepCloud AG, Wittenbach                     |         | E-Gov-Baustein, angrenzend (Signatur statt Prozess/Formular). simap                                                                                                                       |
| 17 | 2025-02 | AIO Kanton Solothurn                   | Workflow-Plattform «EVA» (auf ServiceNow)                                                                      | offen       | 4'870'137            | Plat4mation GmbH, Winterthur                 |         | Buy-Variante in der Praxis: Workflow-Plattform auf US-SaaS -illustriert TCO/Souveränitäts- Tradeoff aus dem Marktscreening. simap                                                         |

| 18   | 2026-02   | Dienststelle Asyl LU / Kanton BE u.a.   | Fallführungssoftware (evidence- Plattform), mehrere Vergaben   | offen + 7× freihändig   | > 55 Mio. gesamt   | Glaux Group AG, Bern   | Marktführer Fall- /Geschäftsverwaltung; die 7 freihändigen Folgevergaben (u.a. Justizvollzug BE 32,7 Mio.) belegen das , vor Lock-in-Muster dem das Marktscreening beim Buy-Vertical warnt -Argument für Create.   |
|------|-----------|-----------------------------------------|----------------------------------------------------------------|-------------------------|--------------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## 3. Abrufbare Rahmenverträge (Beschaffungsweg ohne neue Ausschreibung)

|    | Rahmenvertrag                                                                 | Vergabestelle   | Partner                                                                                                                                                                                                             | Abruf                                                                                                | Eignung für das Mieterportal                                                                                                                                                                                                                                                            |
|----|-------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | SPRINT (24194) 104 «Software- Projekte realisieren und integrieren», bis 2033 | BBL             | Los 1 (<1 Mio./Lifecycle, Dach 149,6 Mio., 12 Partner): u.a. queo/Adfinis , , linkyard, MindNow, /Limetree Softcom Intersim · Los 2 (1-5 Mio., Dach 54 Mio., 5 Partner): , ti&m, IPT, LHIND, Liip European Dynamics | elektronischer Mi unter ni-Tender den Partnern; Bedarfsstelle lt. Publikation: « Bun » desverwaltung | Primärer Weg : MVP (<1 Mio.) als Los-1-Mini-Tender, Plattform-Ausbau (1-5 Mio.) als Los-2-Mini-Tender. Leistungen decken Entwicklung + inkl. Open Source Cloud ab. Prüfen: Zulässigkeit der Tranchierung (BöB Art. 15), Abdeckung langfristiger Produktpflege. miniten · der.info simap |
|  2 | Formularservice 2026-2036 (25104)                                             | BBL             | JAXForms AG                                                                                                                                                                                                         | Abruf                                                                                                | Formular-Layer als Service statt Eigenbau -gegen das Schema-statt-Code-Prinzip abwägen                                                                                                                                                                                                  |
|  3 | ICT- Fachunterstützung Individualentwicklu ng .NET (24132), Dach 162 Mio.     | BBL             | adesso, Accenture/Trivadis, Swisscom, ti&m u.a.                                                                                                                                                                     | Abruf                                                                                                | nur falls .NET-Weg; Grossanbieter                                                                                                                                                                                                                                                       |
|  4 | IKT-Entwicklung /Architektur Java ISC-EJPD (25115), Dach 43 Mio.              | BBL             | adesso, AKROS/consulteer, Orange Business/Glue u.a.                                                                                                                                                                 | Abruf                                                                                                | Java-Kapazität; Bedarfsstellen-Abdeckung prüfen                                                                                                                                                                                                                                         |
|  5 | IT- Projektabwicklung UVEK (24045), 15 Lose                                   | BBL             | Akros, adesso, Ergon, ELCA, Adnovum u.a.                                                                                                                                                                            | Abruf                                                                                                | PL/BA/QS-Rollen, nicht Entwicklung                                                                                                                                                                                                                                                      |
|  6 | DigiAgriFoodCH (25086) 708                                                    | BBL             | Liip, ti&m, Unic                                                                                                                                                                                                    | Abruf                                                                                                | auf das Programm DigiAgriFood beschränkt- vermutlich nicht nutzbar, als Muster interessant                                                                                                                                                                                              |

## 4. Track-Record der im Marktscreening genannten Partner

Alle Zuschläge seit 07/2024; 5 von 6 genannten Partnern sind vergaberechtlich belegt, davon 4 mit BBL-Aufträgen:

|    | Partner        | Zuschläge (Auswahl)                                                                                                                                                             | Volumen sichtbar   |
|----|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|  1 | Adfinis AG     | eBaubewilligungSG (1,47 Mio.); RE2 -Neubau der simap-Plattform selbst, Konsortium mit Puzzle ITC + queo KISSimap.ch (5,74 Mio.); BBL Logdatensammler (757k)                     | ~8 Mio.            |
|  2 | Puzzle ITC AG  | BBL: SAKUBA Webportal (1,39 Mio.), DPS Betrieb/Weiterentwicklung (1,47 Mio.); swisstopo MONTEIS; Stadt ZH decidim; IGE Linux (1,9 Mio.)                                         | ~6,5 Mio.          |
|  3 | Liip AG        | BBL: NUX Statistikportal (1,76 Mio.), EMAS 2.0 (1,16 Mio.), OGD-Plattform (708k); FVS-Portal (1,06 Mio.); Winterthur Portal- Relaunch (1,08 Mio.); SPRINT Los 2; DigiAgriFoodCH | ~6 Mio. + Rahmen   |
|  4 | mimacom ag     | BBL Amtsblattportal (681k) -Flowable-Spezialist                                                                                                                                 | 0,7 Mio.           |
|  5 | Camptoca mp SA | Web-GIS-Rahmenvertrag BS (361k), Red-Hat-Lizenzen VD/UNIL                                                                                                                       | ~2 Mio.            |
|  6 | VSHN AG        | keine Zuschläge im Zeitraum                                                                                                                                                     | -                  |

## 5. Verweise und Anhang

## 5.1 Verweise

- Quelle: simap.ch Public API (vollständig seit Plattformstart 01.07.2024)
- Datenbasis: 2'397 Zuschläge (CPV 72000000 IT-Dienste / 48000000 Software + Stichwortsuchen), je angereichert mit Zuschlagsempfänger, Preis und Auftragsbeschreibung.
- Rohdaten: simap\_awards\_all.csv
- Detail-Annex: SHORTLIST.md

## Methodik: README.md

## 5.2 Anhang

| Datei                      | Geändert                       |
|----------------------------|--------------------------------|
| Datei research.py          | 11.06.2026 by Rasner David BBL |
| Datei SHORTLIST.md         | 11.06.2026 by Rasner David BBL |
| Datei simap_awards_all.csv | 11.06.2026 by Rasner David BBL |
| Datei README.md            | 11.06.2026 by Rasner David BBL |

Ziehen Sie Dateien an diese Stelle, um sie hochzuladen, oder Dateien suchen Alle herunterladen