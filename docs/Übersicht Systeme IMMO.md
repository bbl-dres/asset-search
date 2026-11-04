## Übersicht Systeme IMMO (Arbeitsdokument)

<!-- image -->

## Inhalte:

1. Ziel von Dokument
5. Anhang

```
2. 3. Diagramm als Übersicht 3. Interne Fachanwendungen / Geschäftsobjekte (BBL IMMO intern) 3.1. SAP RE-FX (Real Estate Flexible) 3.2. Korasoft Flächenmanagement Fiori App (FLM Info-App) 3.3. CAFM Basisplan - Korasoft DWG (Autodesk AutoCAD) 3.4. Kalkulation kostenorientierte Miete (KoMi) 3.5. SAP PM (Plant Maintenance) 3.6. Mieterportal 3.7. InterWatt EDM (Energiedatenmanagement) 3.8. Wüest Dimensions - BBL Erhaltungsplanung (EHP) 3.9. DALA / FileNet Planverwaltung 3.10. SAP PS (Project System) 3.11. ActaNova GEVER 3.12. BBL GIS IMMO (ESRI ArcGIS Enterprise) 3.13. BIM / CDE (Common Data Environment) Bund 3.14. SAP FI (Financial Accounting) 3.15. SAP CO (Controlling) 3.16. SAP FI-AA (Asset Accounting) 3.17. SAP IM (Investment Management) 3.18. SAP EPPM (Enterprise Project and Portfolio Management) 3.19. WSM (Workspace Management) 3.20. BVML (Beschaffungs- und Vergabemanagementlösung) 3.21. MDG (Master Data Governance) 4. Externe Fachanwendungen / Geschäftsobjekte (Extern, BBL IMMO relevant) 4.1. SIMAP (Beschaffungsplattform von Bund und bundesnahen Organisationen) 4.2. Kantonale Amtliche Vermessung (Schweiz) 4.3. BFS Eidgenössische Gebäude- und Wohnungsregister GWR (Schweiz) 4.4. Swisstopo APIs (Schweiz) 4.5. Grundbuch (Schweiz) 4.6. BFS Betriebs- und Unternehmensregister (Schweiz) 4.7. Digitaler Produktpass (EU / Schweiz)
```

## 1. Ziel von Dokument

Dieses Dokument stellt die für den Bereich Bauten des Bundesamtes für Bauten und Logistik (BBL) dar. Es dient als physische Datenarchitektur zentrales Arbeitsinstrument im Rahmen des Programms , um die Datenlandschaft transparent abzubilden und aktiv zu steuern. SUPERB

## Die primären Ziele sind:

- Gesamtübersicht: Inventarisierung aller relevanten internen und externen Systeme, sowie deren Geschäftsobjekte.
- Datenmodellierung: Dokumentation der konzeptuellen Datenmodelle und Identifikation der zentralen Geschäftsobjekte zur Sicherstellung einer konsistenten Datenhaltung.
- Priorisierung &amp; Steuerung: Grundlage für die priorisierte Abarbeitung von Dokumentationslücken ('Zu prüfen' vs. 'Geprüft') und die schrittweise Ergänzung fehlender Modellbeschreibungen.
- Architekturgrundlage: Basis für die technische Ausgestaltung der Schnittstellen und die Integration in die künftige ERP-Landschaft (S/4HANA) des Bundes.

## 2. 3. Diagramm als Übersicht

Bild: Übersicht Systeme (Q4 2025). Quelle

<!-- image -->

## 3. Interne Fachanwendungen / Geschäftsobjekte (BBL IMMO intern)

## Prioritäten:

- Support, ERP relevant Hoch:

ERP relevant, aber kein direkter Einfluss auf Stammdatenmanagement

- Mittel:

- Sonstiges Niedrig:

## Übersicht als Tabelle:

|   # | Bereich / Fachanwendung                    |   SUPERB PI | Beschreibung                                                                                                                                                                                                                                     | Geprüft       | Status (Produktiv / Planung)   | Kommentar                |
|-----|--------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|--------------------------------|--------------------------|
|     | Immobilienmanagement                       |             |                                                                                                                                                                                                                                                  |               |                                |                          |
|   1 | SAP RE-FX (Real Estate Flexible)           |        25.1 | SAP-Modul für die kaufmännische Verwaltung von Immobilien mit Stammdatenverwaltung für Wirtschaftseinheiten, Grundstücke, Gebäude und Mietobjekte                                                                                                | OK            | Produktiv                      |                          |
|   2 | Korasoft FLM (Fiori App Flächenmanagement) |        25.1 | Webbasierte Anwendung zur Visualisierung und Analyse von Flächendaten auf Basis der architektonischen Objekte aus SAP RE-FX                                                                                                                      | OK            | Produktiv                      |                          |
|   3 | CAFM Basisplan (Korasoft DWG)              |        25.1 | Technische Grundrisspläne mit standardisierten Layer-Strukturen gemäss BBL-Richtlinien als Basis für Flächenmutationen in SAP RE-FX                                                                                                              | OK            | Produktiv                      |                          |
|   4 | KoMi (Kalkulation kostenorientierte Miete) |        25.1 | Spezialisierte Anwendung zur Berechnung und Verwaltung kostenorientierter Mieten für Bundesimmobilien                                                                                                                                            | OK            | Produktiv (Legacy)             | Rückbau 2026 geplant.    |
|   5 | Mieterportal                               |        25.2 | Zentrale digitale Plattform des BBL, die als Single Point of Contact für alle immobilienbezogenen Services dient - von Störungsmeldungen über Bedarfsanmeldungen für Unterbringung bis zu Flächeninformationen und internen Vermietungsprozessen | Zu definieren | Konzeption                     |                          |
|   6 | WSM (Workspace Management)                 |        28.1 | System für Arbeitsplatzverwaltung SAP Flächenmanagement Integration von grafischen Informationen zu Ausstattungen (Möblierung) basierend auf Multispace Katalog Ausstattung BBL.                                                                 | Zu definieren | Konzeption                     | geplante Umsetzung 2026. |
|     | Objektmanagement                           |             |                                                                                                                                                                                                                                                  |               |                                |                          |
|   7 | SAP PM (Plant Maintenance)                 |        25.2 | SAP-Modul für die Verwaltung und Optimierung von Instandhaltungsprozessen (Wartungsplanung) für Anlagen und technische Einrichtungen                                                                                                             | OK            | Produktiv                      |                          |
|   8 | InterWatt EDM (Energiedatenmanagement)     |        25.2 | System zur Erfassung, Analyse und Optimierung von Energiedaten mit Zählerstrukturen und Verbrauchswerten                                                                                                                                         | OK            | Produktiv                      | NON SAP FAW              |

|   9 | Wüest EHP (Erhaltungsplanung)                                    | 25.2         | Cloud-basierte Anwendung für die Zustandsbasierte Mehrjahresplanung von Erhaltungsmassnahmen inkl. Investitionsbedarf des Immobilienportfolios   | OK            | Produktiv          | NON SAP FAW                                                         |
|-----|------------------------------------------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|---------------|--------------------|---------------------------------------------------------------------|
|     | Dokumentenmanagement                                             |              |                                                                                                                                                  |               |                    |                                                                     |
|  10 | FileNet DALA Planverwaltung                                      | 25.2         | Dokumentenmanagementsystem für die strukturierte Speicherung und Versionierung technischer Pläne und Dokumente                                   | OK            | Produktiv          |                                                                     |
|  11 | FileNet DALA SAP                                                 | 25.2         | Dokumentenmanagementsystem für SAP                                                                                                               | OK            | Produktiv          | Konzeptuelles Datenmodell identisch wie FileNet DALA Planverwaltung |
|  12 | ActaNova GEVER (Geschäftsverwaltung)                             | 25.3         | Geschäftsverwaltungssystem für die elektronische Aktenführung und Dokumentenverwaltung gemäss eCH-0039                                           | OK            | Produktiv          |                                                                     |
|  13 | SAP PS (Project System)                                          | 25.3         | SAP-Modul für das Management von Bauprojekten mit Projektplanung, Ressourcenverwaltung und Budgetcontrolling                                     | OK            | Produktiv          |                                                                     |
|  14 | BIM/CDE (Building Information Modeling /Common Data Environment) | 25.3         | Plattform für methodische digitale Bauwerksdokumentation nach ISO 16739 Standard                                                                 | OK            | Produktiv          | WTO / Einführung                                                    |
|  15 | SAP EPPM (Enterprise Portfolio and Project Management)           | 28.1         | SAP-Modul für Portfolio- und Projektmanagement (Klammermodul für PS/PM)                                                                          | OK            | Produktiv          | Einführung 2025- 2026, erste Funktionalität produktiv.              |
|  16 | Sonstiges BBL GIS IMMO (Geographic Information System)           | 25.3         | Geografisches Informationssystem auf Basis ESRI ArcGIS Enterprise zur räumlichen Visualisierung und Analyse von Immobiliendaten                  | OK            | Produktiv          |                                                                     |
|  17 | BVML (Beschaffungs- und Vergabemanagementlösung)                 | 28.1         | SAP Entwicklung für Beschaffungs- und Vergabeprozessen                                                                                           | Zu prüfen     | Konzeption         | Teilproduktiv, go live zivil 06/2026 geplant.                       |
|  18 | MDG (Master Data Governance)                                     | 28.3         | SAP-Modul für die zentrale Führung der Stammdaten Geschäftspartner GP auf Bundesebene                                                            | Zu definieren | Produktiv          | Verantwortliches FA: EFV                                            |
|  19 | SAP Business Warehouse (BW)                                      | 28.3         | Zu definieren                                                                                                                                    | Zu definieren | Produktiv          |                                                                     |
|     | Finanzen / (Portfoliomanagement)                                 |              |                                                                                                                                                  |               |                    |                                                                     |
|  20 | SAP FI (Finance)                                                 | 28.2         | SAP-Modul für Finanzwesen                                                                                                                        | Zu prüfen     | Produktiv          |                                                                     |
|  21 | SAP CO (Controlling)                                             | 28.2         | SAP-Modul für Controlling                                                                                                                        | Zu prüfen     | Produktiv          |                                                                     |
|  22 | SAP FI-AA (Financial Accounting - Asset                          | 28.1         | SAP-Modul für die Anlagenbuchhaltung                                                                                                             | Zu prüfen     | Produktiv          |                                                                     |
|  23 | SAP IM (Investment Management)                                   | 28.1         | SAP-Modul für Investitionsmanagement und Investitionscontrolling                                                                                 | Zu prüfen     | Produktiv          |                                                                     |
|     | Domotik (OUT OF SCOPE)                                           |              |                                                                                                                                                  |               |                    |                                                                     |
|  24 | Siemens Desigo CC                                                | OUT OF SCOPE | Gebäudeleittechnik (BMS) - führend für Anlagen-/Objekt-Stammdaten (GA, HKL, Alarme)                                                              | Zu definieren | Produktiv          | Zentrale BMS- Plattform, kritisch für Gebäudebetrieb                |
|  25 | Siemens Alarm Control Center                                     | OUT OF SCOPE | Alarmzentrale / Ereignismanagement                                                                                                               | Zu definieren | Produktiv          | Sicherheitskritisch e Alarmverwaltung                               |
|  26 | Sauter Vision Center                                             | OUT OF SCOPE | BMS/SCADA - Anlagen-, Raum- und Trend-Stammdaten                                                                                                 | Zu definieren | Produktiv          | Alternative /ergänzende BMS- Lösung                                 |
|  27 | Honeywell EBI                                                    | OUT OF SCOPE | Enterprise Buildings Integrator (BMS)                                                                                                            | Zu definieren | Produktiv          | Standortspezifisch e BMS-Lösung                                     |
|  28 | Indico - WinCC OA / Runtime Advanced                             | OUT OF SCOPE | SCADA / Automation (WinCC OA)                                                                                                                    | Zu definieren | Produktiv          | Spezialisierte SCADA- Anwendung                                     |
|  29 | Kieback & Peter                                                  | OUT OF SCOPE | GLT/GA-System                                                                                                                                    | Zu definieren | Produktiv (Legacy) | Legacy-System, läuft aus                                            |
|  30 | PiSystem - Saturn Tridium (Niagara)                              | OUT OF SCOPE | Integrationsplattform GA (Controller, Punkte, Objekte)                                                                                           | Zu definieren | Produktiv          | Wichtige Integrationsplattfor m für heterogene                      |
|  31 | Alarmserver / AlarmWorX64                                        | OUT OF SCOPE | Alarmserver (ICONICS)                                                                                                                            | Zu definieren | Produktiv          | Zentrale Alarmverteilung                                            |
|  32 | ALBV Alarmierung                                                 | OUT OF SCOPE | Alarmierung / Meldelinien                                                                                                                        | Zu definieren | Produktiv          | Kritische Alarmweiterleitung ausserhalb Bürozeiten                  |
|  33 | Optec - Janitza GridVis                                          | OUT OF SCOPE | Energiemesstechnik (Stromnetz, Lastgänge, Zähler-Stammdaten)                                                                                     | Zu definieren | Produktiv          | Wichtig für Energiemonitoring                                       |
|  34 | SolarLog                                                         | OUT OF SCOPE | PV-Monitoring, Anlagestammdaten PV/Strings/Wechselrichter                                                                                        | Zu definieren | Produktiv          | Überwachung PV- Anlagen                                             |
|  35 | Regelsystem - SwissControlSystem (SCS)                           | OUT OF SCOPE | Regelungsplattform / Anlagenobjekte                                                                                                              | Zu definieren | Produktiv          | Schweizer Lösung für Regelungstechnik                               |
|  36 | Securiton Securigate                                             | OUT OF SCOPE | Zutritt/Perimeter - Türen, Leser, Rechte (Zutritts-Stammdaten)                                                                                   | Zu definieren | Produktiv          | Sicherheitskritisch, Integration mit HR nötig                       |
|  37 | Salto Systems Local IO Bridge                                    | OUT OF       | Schnittstelle lokale Zutrittspunkte                                                                                                              | Zu            | Produktiv          | Ergänzung zu Securigate                                             |
|     |                                                                  | SCOPE        |                                                                                                                                                  | definieren    |                    |                                                                     |

Tabelle: Zu dokumentierend Fachanwendungen / Geschäftsobjekte

## 3.1. SAP RE-FX (Real Estate Flexible)

## Dokumentation:

- API Verzeichniss Bund: https://confluence.bit.admin.ch/x/dMDqQQ
- SUPERB Excel Datenkatalog:  Ergänzen
- SUPERB Fachonzepte: https://confluence.bit.admin.ch/x/e6ZaEw
- SUPERB Fachkonzept:  Fachanwendung - K\_SUPERB\_Fachkonzept\_ERP\_IMMO\_D0.21.60.10.05\_Immobiliendaten bewirtschaften V1. 1.docx
- Wertetabelle\_ERP\_Immo (Excel): Abgenommene MVP Fachkonzepte (DO21.40.10) - SUPERB Immobilien - Confluence
- SAP Online Dokumentation:  https://help.sap.com/saphelp\_erp60\_sp/helpdata/de/8d/5fd0531d8b4208e10000000a174cb4/frameset.htm
- SAP Dokumentation Architektonisches Objekt:  https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/d3a3eb7caa1842858bf0372e17ad3909 /bf769561a0014bc49b893c5246627e31.html?locale=de-DE

## SAPRE-FX Geschaftsobjekte

<!-- image -->

Bild: Begriffe und Geschäftsobjekte in SAP RE-FX.  Quelle

<!-- image -->

Bild Links: Geschäftsobjekte SUPERB Fachkonzept\_ERP\_IMMO (28.07.2021). Quelle

Bild Rechts: Geschäftsobjekte SUPERB Fachkonzept\_ERP\_IMMO mit Zuordnung Verantwortlichkeiten (28.07.2021). Quelle

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt               | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Geprüft            |
|----|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
|  1 | Wirtschaftseinheit (WE)       | Organisatorische Einheit zur Verwaltung von Immobilien. Dient als übergeordnete Struktur für die kaufmännische und technische Verwaltung von Gebäuden und Grundstücken.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | OK                 |
|  2 | Grundstück (GR)               | Repräsentiert eine Liegenschaft mit definierten Grundstücksdaten wie Fläche, Lage, Nutzungsart und grundbuchrechtlichen Informationen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | OK                 |
|  3 | Gebäude (GE)                  | Physisches Gebäude mit technischen und baulichen Eigenschaften. Beinhaltet Informationen zu Baujahr, Zustand, Flächen, Ausstattung und technischen Anlagen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | OK                 |
|  4 | Mietobjekt (FP/MF /ME)        | Vermietbare Einheit (z.B. Wohnung, Büro, Stellplatz) mit spezifischen Eigenschaften wie Grösse, Ausstattung und Nutzungsart. Basis für Mietverträge. Flächenpool, Mietfläche und Mieteinheit sind Typen. FP = Flächenpool MF = Mietfläche ME = Mieteinheit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | OK                 |
|  5 | Vertrag                       | Miet- oder Pachtvertrag mit allen rechtlichen und kommerziellen Bedingungen. Beinhaltet Vertragslaufzeiten, Konditionen und Vertragspartner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | OK                 |
|  6 | Konditionen                   | Definiert die finanziellen Bedingungen wie Miete, Nebenkosten, Kautionen und Zahlungsmodalitäten. Basis für die Abrechnung.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | OK                 |
|  7 | Architektonisches Objekt (AO) | Hierarchisch strukturiertes Objekt im Facility Management. Dient zur Abbildung der physischen oder organisatorischen Struktur einer Immobilie in SAP RE-FX. Typen von Architektonischen Objekten (AO): : Oberste organisatorische Einheit für Verwaltung und Gruppierung mehrerer Immobilienobjekte. AO-Wirtschaftseinheit : Abbildung eines einzelnen Grundstücks mit Katasterinformationen innerhalb einer Wirtschaftseinheit. AO-Grundstück : Spezifische Teilfläche auf einem Grundstück, z.B. Parkplatz oder Aussenanlage. AO-Grundstücksfläche : Physisches Bauwerk mit eigener Gebäudenummer und Gebäudestammdaten. AO-Gebäude : Stockwerk oder Geschoss eines Gebäudes mit eindeutiger ID. AO-Ebene : Kleinste abgeschlossene Einheit innerhalb einer Ebene, wie Büroraum oder Lagerfläche. AO-Raum | OK gehört zu RE-FX |
|  8 | Bemessung                     | Erfassung und Verwaltung verschiedener Flächenkennzahlen und -Kategorien, zum jeweiligen Architektonischen Objekt. Flächenarten SIA 416 Energiebezugsfläche EBF Anteil Vermietbare Fläche VMF Arbeitsplätze Flächen Reinigung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | OK gehört zu RE-FX |
|  9 | Sonstiges                     | Keine physische Geschäftsobjekte: Belegung: Dokumentiert die tatsächliche Nutzung und den Belegungsstatus von Mietobjekten. Erfasst Zeiträume, Nutzer und Art der Belegung. Objektzuordnung: Verknüpft verschiedene Objekte miteinander und definiert deren hierarchische oder funktionale Beziehungen (z.B. Gebäude zu Grundstück, Mietobjekt zu Gebäude).                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Zu prüfen          |

Tabelle: Geschäftsobjekte SAP RE-FX

## 3.2. Korasoft Flächenmanagement Fiori App (FLM Info-App)

- Dokumentation:
- Hersteller Webseite: https://www.korasoft.net/en/home-english/
- Fachanwendungen BBL Bauten (Intranet): https://intranet.efd-bbl.admin.ch/intraefdbbl/de/home/themen/fachanwendungen.html

## Konzeptuelles Datenmodell:

| Geschäftsobjekt   | Beschreibung                                                                             | Status    |
|-------------------|------------------------------------------------------------------------------------------|-----------|
| Koordinaten       | FLM verwaltet Koordinaten von Objekten für eine Karte                                    | OK        |
| Reinigungsplan    | Auf Basis von Grundrissen werden in FLM Reinigungspläne erstellt, oder nur visualisiert? | Zu prüfen |
| Sonstige?         |                                                                                          | Zu prüfen |

Tabelle: Geschäftsobjekte Korasoft Flächenmanagement (FLM)

## 3.3. CAFM Basisplan - Korasoft DWG (Autodesk AutoCAD)

## Dokumentation:

- Hier ist ein CAFM Basisplan gemeint (Grundriss) - Grundrisse mutieren Architektonische Objekte (Geometrie) und Bemessungen im RE-FX.
- BBL CAD Richtlinie (Link ActaNova):  CAD-Richtlinien-Entwurf (211.4-1/22/2)
- BBL Korasoft DWG (Datei, Muster Vorlage):  Fachanwendung - BBL Korasoft DWG Vorlage.dwg
- BBL Korasoft DWG Layer als Excel:  Fachanwendung - BBL Korasoft DWG Layer.xlsx
- Hersteller Webseite: https://www.autodesk.com/ch-de/products/autocad-web/overview?term=1-YEAR&amp;tab=subscription
- DWG Format: https://en.wikipedia.org/wiki/.dwg

## Offene Punkte:

- Varianten möglich:
- Variante 1: Geschäftsobjekte = DWG Layer entsprechend BBL CAD Richtlinie
- Variante 2: Geschäftsobjekte = Architekturobjekte RE-FX (Beispiel: AO-Raum, AO-Ebene, AO-Parkplatz)

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt     | Beschreibung                              | Geprüft   |
|----|---------------------|-------------------------------------------|-----------|
|  1 | 0                   | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  2 | Defpoints           | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  3 | V_REFERENZPUNKT     | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  4 | R_AOID              | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  5 | R_RAUMPOLYGON       | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  6 | R_GESCHOssPOLYGON   | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  7 | A_SCHRAFFUR         | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  8 | A_SANITAER          | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
|  9 | V_PLANLAYOUT        | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 10 | V_ACHSEN            | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 11 | V_BEMAssUNG         | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 12 | V_TEXT              | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 13 | A_ARCHITEKTUR       | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 14 | R_RAUMSTEMPEL       | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 15 | R_FUEHRUNGSLINIE    | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 16 | R_RAUMPOLYGON-ABZUG | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 17 | A_ELEKTRO           | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 18 | A_HEIZUNG-KUEHLUNG  | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |
| 19 | A_LUEFTUNG          | DWG Layer entsprechend BBL CAD Richtlinie | Zu prüfen |

Tabelle: Geschäftsobjekte Autodesk AutoCAD

## 3.4. Kalkulation kostenorientierte Miete (KoMi)

## Dokumentation:

- Legacy Lösung, wird abgelöst
- Beschreibung (BBL ActaNova): Beschreibung KoMi V2\_0\_1 Stand 2013\_02\_22.pdf
- Die benötigten Daten für eine Berechnung werden als CSV Dateien importiert
- 3.2Import der Quelldaten

<!-- image -->

ImMenupunktImportwerdendieImportederverschiedenenQuelldateiengestartet.Ausserdemkann

DieDateienwerden im CSV-Format(durchSemikolon getrennteFelder)geliefert.DasFormat der einzelnenDateienistindenfolgendenKapitelnbeschrieben.

## 3.1 Stammdaten

<!-- image -->

Bild Link: Import Dropdown KoMi.  Quelle

Bild Rechts: Stammdaten KoMi. Quelle

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt          | Beschreibung                                                                                                                                                                                      | Geprüft   |
|----|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Report 1 Gebäude         | Input CSV. Diese Datei liefert den Anschaffungswert und die Nutzungsdauer der Gebäude, welche im Besitz des Bundes sind. Wirtschaftseinheit Gebäudenummer Anschaffungswert Nutzungsdauer          | OK        |
|  2 | Report 2 Ausbau Zumieten | Input CSV. Enthält die Ausbaukosten und die Abschreibungsdauer von gemieteten Gebäuden, die durch das BBL ausgebaut worden sind. Wirtschaftseinheit Gebäudenummer Ausbaukosten Abschreibungsdauer | OK        |
|  3 | Report 3 Grundstücke     | Input CSV. Diese Datei liefert die Buchwerte von Grundstücken, die im Besitz des Bundes sind. Wirtschaftseinheit Gebäudenummer Buchwert                                                           | OK        |

|   4 | Report 4 Zumieten      | Input CSV. Die Kosten für gemietete Gebäude und Grundstücke werden in dieser Datei geliefert. Wirtschaftseinheit Gebäudenummer Zumietkosten                                                                                                                                                                    | OK   |
|-----|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
|   5 | Report 7 Drittmieter   | Input CSV. Mieteinnahmen von Dritten werden in dieser Datei pro Mietobjekt geliefert. Wirtschaftseinheit Gebäudenummer Mieteinnahmen                                                                                                                                                                           | OK   |
|   6 | Grunddaten Gebäude     | Input CSV. Die Datei enthält Daten zur Bestimmung der Kostensätze, zum Erkennen ob kostenorientiert vermietet wird und die Bezeichnung für die Abrechnung. Aufgelistet sind Gebäude im Besitz des Bundes. Wirtschaftseinheit Gebäudenummer Gebäudetext Teilportfolio Gebäudeart 2. Stufe Mietmodell            | OK   |
|   7 | Grunddaten Grundstücke | Input CSV. Die Bezeichnung und das Mietmodell für alle Grundstücke in Besitz des Bundes sind in der Datei enthalten. Mittels Mietmodell wird ermittelt ob kostenorientierte Miete zu erheben ist und die Bezeichnung wird in der Abrechnung verwendet. Wirtschaftseinheit Gebäudenummer Bezeichnung Mietmodell | OK   |
|   8 | Sonstiges?             | Gebäudearten 1. Stufe Gebäudearten 2. Stufe Teilportfolios Kostensatzarten Kostensätze Mieter                                                                                                                                                                                                                  | OK   |

Tabelle: Kostenorientierte Miete KoMi

## 3.5. SAP PM (Plant Maintenance)

## Dokumentation:

- SAP Online Hilfe: https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/e98c7c41bbe8439e90daa5c114a7573b /bed5b853dcfcb44ce10000000a174cb4.html?locale=de-DE
- Viele Funktionen von Modul PM werden durch Wüest-Partner abgelöst
- Viele Funktionen von Modul PM werden durch InterWatt Energiedatenmanagement EDM abgelöst

## Konzeptuelles Datenmodell:

<!-- image -->

Bild: Begriffe und Geschäftsobjekte in SAP PM (Plant Maintenance). Quelle

|    | Geschäftsobjekt                      | Beschreibung                                                                                                                                                                                               | Geprüft   | Kommentar                                                                                                     |
|----|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
|  1 | Kernobjekte SAP PM                   |                                                                                                                                                                                                            |           |                                                                                                               |
|  2 | Technischer Platz                    | Physisches/Logisches Geschäftsobjekt: Räumliche oder funktionale Strukturierung der Instandhaltungsobjekte. Repräsentiert Orte wie Gebäude, Etage, Raum oder Anlage in hierarchischer Struktur.            | OK        | PM-Kernobjekt. Kann hierarchisch strukturiert sein (Gebäude Etage Raum). Oberste Struktur für Instandhaltung. |
|  3 | Equipment                            | Physisches/Logisches Geschäftsobjekt: Individuelles, zu wartendes technisches Objekt mit eigener Nummer und Historie (z.B. Aufzug, Heizkessel, Klimaanlage). Kann an Technischen Plätzen installiert sein. | OK        | PM-Kernobjekt. Beweglich oder fest installiert. Träger von Wartungsplänen und technischen Daten.              |
|  4 | Instandhaltungsmeld ung (IH-Meldung) | Logisches Geschäftsobjekt: Dokumentation einer Störung, eines Schadens oder Wartungsbedarfs. Enthält Priorität, Schadensbeschreibung und kann Auftrag auslösen.                                            | OK        | PM-Kernobjekt. Eingangskanal für ungeplante Instandhaltung. Basis für Störungsanalyse.                        |
|  5 | Instandhaltungsauftr ag (IH-Auftrag) | Logisches Geschäftsobjekt: Arbeitsauftrag zur Durchführung von Wartungs-, Inspektions- oder Instandsetzungsarbeiten. Enthält Vorgänge, Termine, Material und Kosten.                                       | OK        | PM-Kernobjekt. Zentrales Planungs- und Steuerungselement. Kostenträger für Instandhaltung.                    |
|  6 | Wartungsauftrag                      | Logisches Geschäftsobjekt: Spezieller IH-Auftrag für planmässige, vorbeugende Wartung. Wird meist automatisch aus Wartungsplänen generiert.                                                                | OK        | Untertyp des IH-Auftrags. Für regelmässige, geplante Wartungsarbeiten.                                        |
|  7 | Arbeitsauftrag                       | Logisches Geschäftsobjekt: IH-Auftrag für korrektive Instandsetzung nach Störungen oder Schäden. Meist aus Meldungen erzeugt.                                                                              | OK        | Untertyp des IH-Auftrags. Für ungeplante Reparaturen und Störungsbehebung.                                    |
|  8 | Serviceauftrag                       | Logisches Geschäftsobjekt: IH-Auftrag für Dienstleistungen, oft durch externe Firmen. Kann Serviceverträge abbilden.                                                                                       | OK        | Untertyp des IH-Auftrags. Integration mit Einkauf für Fremdleistungen.                                        |
|  9 | Wartungsplan                         | Logisches Geschäftsobjekt: Definition zyklischer Wartungsaktivitäten. Generiert automatisch Wartungsaufträge nach Zeit-, Leistungs- oder Zustandskriterien.                                                | OK        | PM-Kernobjekt. Basis für vorbeugende Instandhaltung. Reduziert ungeplante Ausfälle.                           |
| 10 | Arbeitsplan                          | Logisches Geschäftsobjekt: Standardisierte Arbeitsabläufe für wiederkehrende Instandhaltungstätigkeiten. Definiert Vorgänge, Zeiten und benötigte Ressourcen.                                              | OK        | PM-Kernobjekt. Vorlage für effiziente Auftragsabwicklung. Kann Equipment- oder TP-spezifisch sein.            |
| 11 | Messpunkt/Zähler                     | Logisches Geschäftsobjekt: Definierter Punkt zur Erfassung von Messwerten (z.B. Temperatur, Druck, Betriebsstunden, Verbrauch) an Equipment oder Technischen Plätzen.                                      | OK        | PM-Kernobjekt. Basis für zustandsabhängige Wartung und Verbrauchserfassung.                                   |
| 12 | Messbeleg                            | Logisches Geschäftsobjekt: Dokumentation konkreter Messwerte zu einem Zeitpunkt. Kann bei Grenzwertüberschreitung automatisch Meldungen auslösen.                                                          | OK        | PM-Kernobjekt. Historie von Zustandsdaten. Wichtig für Trendanalysen und Früherkennung.                       |
| 13 | Wichtige Relationen                  |                                                                                                                                                                                                            |           |                                                                                                               |
| 14 | Wirtschaftseinheit (aus RE-FX)       | Referenzobjekt aus RE-FX: Oberste organisatorische Struktur für die Verwaltung der Technischen Plätze einer Liegenschaft.                                                                                  | OK        | Schnittstelle zu RE-FX. Verbindet kaufmännische und technische Immobilienverwaltung.                          |

|   15 | Gebäude (aus RE- FX)    | Referenzobjekt aus RE-FX: Kann optional direkt mit Technischen Plätzen verknüpft werden eindeutige Zuordnung zwischen kaufmännischem Objekt und technischer Struktur.   | OK   | Alternative/zusätzliche Verknüpfung zu WE. Ermöglicht gebäudespezifisches technisches Management.   |
|------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|-----------------------------------------------------------------------------------------------------|
|   16 | Material (aus MM)       | Physisches Geschäftsobjekt aus MM: Ersatzteile und Verbrauchsmaterial für Instandhaltungsarbeiten. In Aufträgen als Komponenten geplant.                                | OK   | Integration mit Materialwirtschaft. Lagerbestand, Beschaffung, Reservierungen.                      |
|   17 | Kostenstelle (aus CO)   | Referenzobjekt aus CO: Kostenträger für Instandhaltungskosten. Aufträge werden auf Kostenstellen abgerechnet.                                                           | OK   | Integration mit Controlling. Kostenanalyse und Budgetkontrolle für Instandhaltung.                  |
|   18 | Arbeitsplatz (aus PP)   | Physisches/Logisches Geschäftsobjekt aus PP: Kapazitäten wie Werkstätten oder Technikergruppen für Instandhaltungsarbeiten.                                             | OK   | Integration mit PP. Kapazitätsplanung für interne Instandhaltung.                                   |
|   19 | Lieferant (aus MM)      | Referenzobjekt aus MM: Externe Dienstleister für Serviceaufträge. Verknüpfung zu Rahmenverträgen und Konditionen.                                                       | OK   | Integration mit Einkauf. Verwaltung externer Instandhaltungspartner.                                |
|   20 | Personal (aus HR)       | Referenzobjekt aus HR: Techniker und Handwerker, die Aufträgen zugeordnet werden. Mit Qualifikationen und Verfügbarkeiten.                                              | OK   | Integration mit HR. Personaleinsatzplanung und Zeiterfassung.                                       |
|   21 | Stückliste (aus MM /PP) | Logisches Geschäftsobjekt aus MM/PP: Strukturierte Ersatzteilliste für Equipment. Definiert benötigte Komponenten für Wartung.                                          | OK   | Integration mit MM/PP. Vereinfacht Materialplanung für Standardwartungen.                           |

Tabelle: SAP PM (Plant Maintenance)

## 3.6. Mieterportal

## Dokumentation:

- : SUPERB\_Fachkonzept\_ERP\_IMMO\_Mieterportal NEW V01.docx Fachkonzept Mieterportal NEW
- : Mieterportal\_Gesamtkonzept Übersicht (internes Dokument) Gesamtkonzept Übersicht
- : Gesamtkonzept Mieterportal https://confluence.bit.admin.ch/x/4rrsOw
- : SAP PM Integration https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/e98c7c41bbe8439e90daa5c114a7573b

## Hinweise:

- Die Integration erfolgt primär über SAP-Module (PM, RE-FX, EPPM)
- Zentrale Landing Page als einheitlicher Einstiegspunkt geplant
- Mehrere Use Cases befinden sich noch in Entwicklung (WSM, 3D-Visualisierung)

## : Konzeptuelles Datenmodell

|    | Gruppe / Geschäftsobjekt   | Beschreibung                                                                                                           | Geprüft   | Kommentar                                     |
|----|----------------------------|------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------|
|  1 | Störungsmeldung            |                                                                                                                        |           |                                               |
|  2 | Störmeldung                | Dokumentation einer Störung im Gebäudebetrieb mit Priorität, Schadensbeschreibung und Verknüpfung zu Technischem Platz | Zu prüfen | Integration mit SAP PM IW24                   |
|  3 | Technischer Platz          | Räumliche oder funktionale Strukturierung der Instandhaltungsobjekte (Gebäude, Etage, Raum)                            | Zu prüfen | Verknüpfung zu RE-FX Architektonisches Objekt |
|  4 | Störungsart                | Kategorisierung der Störung (Gebäudetechnik, Bürotechnik, Mobiliar, etc.)                                              | Zu prüfen |                                               |
|  5 | Störungsstatus             | Aktueller Bearbeitungsstatus (offen, in Bearbeitung, abgeschlossen)                                                    | Zu prüfen |                                               |
|  6 | Bedarfsanmeldung           |                                                                                                                        |           |                                               |
|  7 | Unterbringungsbedarf       | Antrag für räumlichen Bedarf mit Angaben zu Arbeitsplätzen und sonstigen Anforderungen                                 | Zu prüfen | Integration mit SAP ePPM                      |
|  8 | Arbeitsstilform            | Kategorisierung der Arbeitsplatztypen für NAW-Faktor Flächenbedarfsermittlung                                          | Zu prüfen |                                               |
|  9 | Genehmigungsstatus         | Status der Bedarfsgenehmigung (eingereicht, in Prüfung, genehmigt, abgelehnt)                                          | Zu prüfen | Workflow mit GS-Genehmigung                   |
| 10 | Flächeninformation         |                                                                                                                        |           |                                               |
| 11 | Mietobjekt                 | Vermietbare Einheit mit Flächenangaben, Verträgen und Kosten                                                           | Zu prüfen | Aus SAP RE-FX                                 |
| 12 | Belegungsdaten             | Aktuelle Nutzung und Belegungsstatus von Mietobjekten                                                                  | Zu prüfen | Integration Korasoft FLM                      |
| 13 | Verbrauchsdaten            | Energieverbrauch (Wärme, Strom, Wasser, Abfall) je Mietobjekt                                                          | Zu prüfen | Integration EDM/InterWatt                     |
| 14 | Ausstattung                |                                                                                                                        |           |                                               |
| 15 | Inventarobjekt             | Möbel und Einrichtungsgegenstände mit Metadaten (Beschaffung, Alter, Hersteller)                                       | Zu prüfen | Geplant für WSM Integration                   |
| 16 | Raumausstattungsplan       | 2D/3D Darstellung der Möblierung                                                                                       | Zu prüfen | CAD/DWG Integration                           |
| 17 | Dienstleistungen           |                                                                                                                        |           |                                               |
| 18 | Serviceanfrage             | Anfragen für Zusatzreinigung, Umzüge, Transportleistungen                                                              | Zu prüfen | SHOP-Funktionalität geplant                   |
| 19 | Leistungskatalog           | Verfügbare Services mit Preisen und SLA-Definitionen                                                                   | Zu prüfen |                                               |
| 20 | Benutzerverwaltung         |                                                                                                                        |           |                                               |
| 21 | Mieter/Nutzer              | Interne Verwaltungseinheiten (ILBO) mit Berechtigungen                                                                 | Zu prüfen | IAM/eIAM Integration                          |
| 22 | Ansprechpartner            | Rollenzuordnung je Objekt (PFM, OM, Kundendienst)                                                                      | Zu prüfen |                                               |

Tabelle: Konzeptuelles Datenmodell Mieterportal

## 3.7. InterWatt EDM (Energiedatenmanagement)

## Dokumentation:

- Hersteller: https://interwatt.ingsoft.com/de-de/
- Fachanwendungen BBL Bauten (Intranet): https://intranet.efd-bbl.admin.ch/intraefdbbl/de/home/themen/fachanwendungen.html
- Dokumentation:
- PDF Logisches Datenmodell:  Fachanwendung - InterWatt - Logische Systemübersicht 19-01-2025.pdf
- VISIO Logisches Datenmodell: Fachanwendung - InterWatt - Logische Systemübersicht 19-01-2025.vsdx

## Konzeptuelles Datenmodell:

<!-- image -->

Bild: Logische Systemübersicht InterWatt. Quelle

|    | Geschäftsobjekt                               | Beschreibung                                                                                  | Geprüft   |
|----|-----------------------------------------------|-----------------------------------------------------------------------------------------------|-----------|
|  1 | Organisationseinheit                          | Strukturierte Organisationseinheiten, z. B. Abteilungen oder Bereiche. BBL Wirtschaftseinheit | OK        |
|  2 | Personen                                      | Individuen mit spezifischen Eigenschaften wie Name, E-Mail, Nutzername.                       | OK        |
|  3 | Rechtezuweisung                               | Vergabe von Berechtigungen an Personen innerhalb der Organisation.                            | OK        |
|  4 | Einheit = Heizzentrale                        | Physische oder logische Einheiten für Energiemanagement.                                      | OK        |
|  5 | Einheit = Gebäude                             | Physische oder logische Einheiten für Energiemanagement.                                      | OK        |
|  6 | Einheit = Teilfläche                          | Physische oder logische Einheiten für Energiemanagement.                                      | OK        |
|  7 | Zähler                                        | Messgeräte zur Erfassung von Energieverbräuchen.                                              | OK        |
|  8 | Zählwerk                                      | Einzelne Messgrössen eines Zählers, z. B. Strom, Wasser oder Wärme.                           | OK        |
|  9 | Zähl- und Messwerte                           | Gespeicherte Werte aus Zählwerken, inkl. Plausibilisierungsregeln.                            | OK        |
| 10 | Zählerhierarchie                              | Strukturierte Beziehung zwischen Zählern, z. B. Haupt- und Unterzähler.                       | OK        |
| 11 | Medien                                        | Energiemedien wie Strom, Gas, Wärme oder Wasser.                                              | OK        |
| 12 | Verbrauchsart                                 | Kategorisierung des Energieverbrauchs, z. B. Endenergie, Nutzenergie.                         | OK        |
| 13 | Energieverbrauch je Medium                    | Erfasster Verbrauch für jedes Medium über einen Zeitraum.                                     | OK        |
| 14 | Emission                                      | Erfassung der mit dem Energieverbrauch verbundenen Emissionen.                                | OK        |
| 15 | Primärenergie                                 | Energiemengen vor Umwandlungsverlusten zur Ermittlung von Umweltwirkungen.                    | OK        |
| 16 | Energieverbrauch je EnDes (Energiedeskriptor) | Detaillierte Messung von Energieverbrauchsparametern.                                         | OK        |
| 17 | Energieverbrauch je Zählwerk                  | Spezifischer Verbrauchswert pro Zählwerk und Zeitraum.                                        | OK        |
| 18 | Übergreifender Energiefaktor                  | Faktoren zur Normalisierung und Vergleichbarkeit von Energieverbrauch.                        | OK        |
| 19 | Zuordnung übergreifender Energiefaktor        | Verknüpfung der Energiefaktoren mit spezifischen Einheiten oder Zählern.                      | OK        |

Tabelle: Geschäftsobjekte InterWatt Energiedatenmanagement

## 3.8. Wüest Dimensions - BBL Erhaltungsplanung (EHP)

## Dokumentation:

- Hersteller: https://www.wuestpartner.com/ch-de/services-produkte/digitale-loesungen-fuer-immobilien/wuest-dimensions/
- Fachanwendungen BBL Bauten (Intranet): https://intranet.efd-bbl.admin.ch/intraefdbbl/de/home/themen/fachanwendungen.html
- Login, BBL EHP Produktion: https://www.wuestdimensions.com/?goIndexHtml&amp;kc\_idp\_hint=bbl-sso
- Login, BBL EHP Testumgebung: https://test.wuestdimensions.com/?goIndexHtml&amp;kc\_idp\_hint=bbl-sso
- Technische Dokumentation (benötigt ein Login): Dokumentation - Wüest Hub
- Einschätzung von BBL Team Erhaltungsplanung, welche Geschäftsobjekt relevant sind: Fachanwendung - Wüest Partner Dimensions (BBL EHP) API Geschäftsobjekte.xlsx
- Wüest Dimensions ist modular Aufgebaut:
- Bewertung &amp; Planung:
- Immobilienbewertung und Erhaltungsplanung
- Sanierungsplanung mit Budgetierung und Kostenschätzungen
- Sustainability Management:
- Erfassung und Analyse von Nachhaltigkeitsmerkmalen
- Management von energetischen und ökologischen Kennzahlen
- MLI Markt- &amp; Standortinformationen:
- Marktdaten und Standortanalysen für Immobilien
- Mikrostandortprofile und Vergleichsobjekte
- Transaction Management:
- Unterstützung des Immobilientransaktionsprozesses
- Verwaltung von Transaktionsdaten
- Accounting &amp; Controlling:
- Buchhalterische Erfassung von Immobilienaktivitäten
- Finanzplanung und Kostenkontrolle
- Auftragsmanagement:
- Verwaltung immobilienbezogener Aufträge
- Auftragsplanung und Zahlungsabwicklung
- Asset &amp; Portfolio Management:
- Verwaltung von Immobilienportfolios
- Portfolioanalyse, Benchmarking und strategische Planung
- Construction &amp; Development - aktuell nicht von BBL lizensiert:
- Management von Bauprojekten
- Kontrolle von Baukosten und Projektdokumentation

Bild: Durch BBL lizensierte Module von Wüest Dimensions. Quelle

<!-- image -->

## Konzeptuelles Datenmodell:

## OM-Erhaltungsplanung

<!-- image -->

Bild: Logisches Datenmodell Erhaltungsplanung (Fachliche Sicht)

|    | Gruppe auf Deutsch   | Geschäftsobjekt                              | Beschreibung                                       | Geprüft   |
|----|----------------------|----------------------------------------------|----------------------------------------------------|-----------|
|  1 | Bucheinträge         | Bucheinträge                                 | Buchhalterische Einträge und Transaktionen         | Zu prüfen |
|  2 | Buchungsanweisungen  | Buchungsanweisungen                          | Verwaltung von Booking instructions                | Zu prüfen |
|  3 | Rechner              | Bewertungen berechnen                        | Bewertungsberechnung für Immobilien                | Zu prüfen |
|  4 | Rechner              | Geführte Prozesse berechnen                  | Geführte Berechnungsprozesse                       | Zu prüfen |
|  5 | Rechner              | AUL hedonische Funktionen berechnen          | Berechnung für AUL hedonic functions               | Zu prüfen |
|  6 | Rechner              | Schlanke AUL hedonische Funktionen berechnen | Berechnung für lean AUL hedonic functions          | Zu prüfen |
|  7 | Rechner              | Schlanke hedonische Bewertungen berechnen    | Verwaltung von Calculating lean hedonic valuations | Zu prüfen |
|  8 | Rechner              | Sanierungen berechnen                        | Berechnung von Sanierungskosten und -massnahmen    | Zu prüfen |
|  9 | Rechner              | Verschiedenes berechnen                      | Diverse Berechnungsfunktionen                      | Zu prüfen |
| 10 | Kunden               | Kunden                                       | Kundendaten und -verwaltung                        | Zu prüfen |
| 11 | Datenboxen           | Datenboxen                                   | Container für Datenzusammenstellungen              | Zu prüfen |
| 12 | Datenboxen           | Stammdaten                                   | Zentrale Stammdaten für Systemprozesse             | Zu prüfen |
| 13 | Datenboxen           | Attribute                                    | Eigenschaften und Merkmale von Objekten            | Zu prüfen |
| 14 | Datenboxen           | Kompetenzstufen                              | Verwaltung von Competence levels                   | Zu prüfen |
| 15 | Datenboxen           | Ausgaben/Budgets                             | Kosten- und Budgetverwaltung                       | Zu prüfen |
| 16 | Datenboxen           | Budgetanpassungen                            | Anpassungen an bestehenden Budgets                 | Zu prüfen |
| 17 | Datenboxen           | Aktivierungen                                | Aktivierung von Investitionen als Anlagevermögen   | Zu prüfen |
| 18 | Datenboxen           | Benutzerdefinierter Kontenplan               | Verwaltung von Custom account plan                 | Zu prüfen |
| 19 | Datenboxen           | IVM-Flächenmodell importieren                | Import von IVM area model                          | Zu prüfen |
| 20 | Datenboxen           | Bewertung importieren                        | Import von valuation                               | Zu prüfen |
| 21 | Datenboxen           | Bucheinträge importieren                     | Import von book entries                            | Zu prüfen |
| 22 | Datenboxen           | Zahlungen importieren                        | Import von payments                                | Zu prüfen |
| 23 | Datenboxen           | Wechselkurse                                 | Verwaltung von Exchange rates                      | Zu prüfen |
| 24 | Lizenzinhaber        | Lizenzinhaber                                | Verwaltung von License holders                     | Zu prüfen |
| 25 | Darlehen             | Darlehen                                     | Verwaltung von Loans                               | Zu prüfen |
| 26 | Darlehen             | Hypothekenzertifikate                        | Verwaltung von Mortgage certificates               | Zu prüfen |
| 27 | Darlehen             | Portfolio-Limits                             | Verwaltung von Portfolio limits                    | Zu prüfen |

|   28 | Darlehen            | Zinsbedingungen                               | Verwaltung von Interest conditions               | Zu prüfen   |
|------|---------------------|-----------------------------------------------|--------------------------------------------------|-------------|
|   29 | MLI                 | Marktstandortinformationen                    | Verwaltung von MLI                               | Zu prüfen   |
|   30 | Aufträge            | Aufträge                                      | Auftragsverwaltung                               | Zu prüfen   |
|   31 | Zahlungen           | Zahlungen                                     | Zahlungsverwaltung                               | Zu prüfen   |
|   32 | Zahlungen           | Zuweisungen                                   | Zuordnungen zwischen Objekten                    | Zu prüfen   |
|   33 | Portfolios          | Portfolios                                    | Verwaltung von Immobilienportfolios              | Zu prüfen   |
|   34 | Portfolios          | Benchmarks                                    | Vergleichsdaten für Performance-Messung          | Zu prüfen   |
|   35 | Portfolios          | Benchmark-Zahlen                              | Kennzahlen für Leistungsvergleiche               | Zu prüfen   |
|   36 | Portfolios          | Budgetanpassungen                             | Anpassungen an bestehenden Budgets               | Zu prüfen   |
|   37 | Portfolios          | Konsolidiertes Budget                         | Zusammengeführte Budgetplanung                   | Zu prüfen   |
|   38 | Portfolios          | Genehmigungsprozess für konsolidiertes Budget | Genehmigungsworkflow für Budgets                 | Zu prüfen   |
|   39 | Portfolios          | Zuweisungen                                   | Zuordnungen zwischen Objekten                    | Zu prüfen   |
|   40 | Portfolios          | Kostenperioden                                | Zeiträume für Ausgabenplanung                    | Zu prüfen   |
|   41 | Portfolios          | Immobilienverwaltungsgesellschaften           | Verwaltung von Property management companies     | Zu prüfen   |
|   42 | Projekte            | Projekte                                      | Projektmanagement für Bauvorhaben                | Zu prüfen   |
|   43 | Immobilieneinheiten | Immobilieneinheiten                           | Grundlegende Immobilieneinheiten                 | Zu prüfen   |
|   44 | Immobilieneinheiten | Attribute                                     | Eigenschaften und Merkmale von Objekten          | Zu prüfen   |
|   45 | Immobilieneinheiten | Zuweisungen                                   | Zuordnungen zwischen Objekten                    | Zu prüfen   |
|   46 | Immobilieneinheiten | Gebäude                                       | Gebäudespezifische Daten                         | Zu prüfen   |
|   47 | Immobilieneinheiten | Gebäudenachhaltigkeit                         | Nachhaltigkeitsmerkmale von Gebäuden             | Zu prüfen   |
|   48 | Immobilieneinheiten | RB-Qualitätsprofil                            | Qualitätsprofil nach RB-Standard                 | Zu prüfen   |
|   49 | Immobilieneinheiten | Sanierung                                     | Sanierungsplanung und -umsetzung                 | Zu prüfen   |
|   50 | Immobilieneinheiten | Grundstücke                                   | Verwaltung von Land plots                        | Zu prüfen   |
|   51 | Immobilieneinheiten | Referenzwerte                                 | Referenz- und Vergleichswerte                    | Zu prüfen   |
|   52 | Immobilieneinheiten | Ausgaben/Budgets                              | Kosten- und Budgetverwaltung                     | Zu prüfen   |
|   53 | Immobilieneinheiten | Investitionsdaten                             | Investitionsbezogene Daten                       | Zu prüfen   |
|   54 | Immobilieneinheiten | Hypothekenzertifikate                         | Verwaltung von Mortgage certificates             | Zu prüfen   |
|   55 | Immobilieneinheiten | Marktwerte                                    | Verwaltung von Market values                     | Zu prüfen   |
|   56 | Immobilieneinheiten | Marktwerte VO                                 | Verwaltung von Market values VO                  | Zu prüfen   |
|   57 | Immobilieneinheiten | Flächeneinheitslisten                         | Listen von Flächeneinheiten                      | Zu prüfen   |
|   58 | Immobilieneinheiten | IVM-Flächenmodell                             | Flächenmodell nach IVM-Standard                  | Zu prüfen   |
|   59 | Immobilieneinheiten | Besuche                                       | Verwaltung von Visits                            | Zu prüfen   |
|   60 | Immobilieneinheiten | Dokumente                                     | Dokumentenverwaltung                             | Zu prüfen   |
|   61 | Immobilieneinheiten | CD-Projekt                                    | Verwaltung von CD project                        | Zu prüfen   |
|   62 | Immobilieneinheiten | Versionen                                     | Versionsverwaltung von Daten                     | Zu prüfen   |
|   63 | Immobilieneinheiten | Versionen Grunddaten                          | Versionierte Grunddaten                          | Zu prüfen   |
|   64 | Immobilieneinheiten | Versionen Investitionsdaten                   | Versionierte Investitionsdaten                   | Zu prüfen   |
|   65 | Immobilieneinheiten | Versionen Gebäude                             | Versionshistorie von Gebäuden                    | Zu prüfen   |
|   66 | Immobilieneinheiten | Versionen Grundstücke                         | Verwaltung von Versions land plots               | Zu prüfen   |
|   67 | Immobilieneinheiten | Versionen Referenzwerte                       | Versionierte Referenzwerte                       | Zu prüfen   |
|   68 | Immobilieneinheiten | Versionen Attribute                           | Versionierte Attribute                           | Zu prüfen   |
|   69 | Immobilieneinheiten | Versionen Qualitätsprofil                     | Versionshistorie von Qualitätsprofilen           | Zu prüfen   |
|   70 | Immobilieneinheiten | Version Gebäudekomponenten                    | Versionierte Gebäudekomponenten                  | Zu prüfen   |
|   71 | Immobilieneinheiten | Aktivierungen                                 | Aktivierung von Investitionen als Anlagevermögen | Zu prüfen   |
|   72 | Immobilieneinheiten | Strategien                                    | Strategische Planungen für Objekte               | Zu prüfen   |
|   73 | Immobilieneinheiten | Benchmarks                                    | Vergleichsdaten für Performance-Messung          | Zu prüfen   |
|   74 | Immobilieneinheiten | Gebäudekomponenten                            | Komponenten und Bauteile von Gebäuden            | Zu prüfen   |
|   75 | Immobilieneinheiten | Steuern                                       | Verwaltung von Taxes                             | Zu prüfen   |
|   76 | Immobilieneinheiten | Geschäftsereignisse                           | Verwaltung von Business events                   | Zu prüfen   |
|   77 | Immobilieneinheiten | Verbrauchsperioden                            | Verbrauchszeiträume für Ressourcen               | Zu prüfen   |
|   78 | Immobilieneinheiten | Kostenstellen                                 | Kostenstellen-Management                         | Zu prüfen   |
|   79 | Stakeholder         | Stakeholder                                   | Beteiligte Parteien                              | Zu prüfen   |
|   81 | Stakeholder         | Niederlassungen                               | Verwaltung von Branches                          | Zu prüfen   |
|   82 | Transaktionen       | Transaktionen                                 | Transaktionsdaten und                            | Zu prüfen   |
|      |                     |                                               | -verwaltung                                      |             |

|   83 | Transaktionen            | Immobilieneinheit            | Verwaltung von Property unit            | Zu prüfen   |
|------|--------------------------|------------------------------|-----------------------------------------|-------------|
|   84 | Benutzer                 | Benutzer                     | Benutzerverwaltung                      | Zu prüfen   |
|   85 | Benutzerkontext          | Benutzerkontext              | Kontextinformationen zum Benutzer       | Zu prüfen   |
|   86 | Bewertungen              | Bewertungen                  | Verwaltung von Valuations               | Zu prüfen   |
|   87 | Bewertungen              | Objektdaten                  | Grunddaten für Bewertungsobjekte        | Zu prüfen   |
|   88 | Bewertungen              | Attribute                    | Eigenschaften und Merkmale von Objekten | Zu prüfen   |
|   89 | Bewertungen              | Gebäude                      | Gebäudespezifische Daten                | Zu prüfen   |
|   90 | Bewertungen              | Gebäudenachhaltigkeit        | Nachhaltigkeitsmerkmale von Gebäuden    | Zu prüfen   |
|   91 | Bewertungen              | Sanierung                    | Sanierungsplanung und -umsetzung        | Zu prüfen   |
|   92 | Bewertungen              | IWV-Wiederbeschaffungskosten | Wiederbeschaffungskostenberechnung      | Zu prüfen   |
|   93 | Bewertungen              | Grundstücke                  | Verwaltung von Land plots               | Zu prüfen   |
|   94 | Bewertungen              | Referenzwerte                | Referenz- und Vergleichswerte           | Zu prüfen   |
|   95 | Bewertungen              | Kennzahlen                   | Schlüsselkennzahlen für Bewertungen     | Zu prüfen   |
|   96 | Bewertungen              | Sensitivitätsanalyse         | Verwaltung von Sensitivity Analysis     | Zu prüfen   |
|   97 | Bewertungen              | Wertkorrekturen              | Verwaltung von Value corrections        | Zu prüfen   |
|   98 | Bewertungen              | Mikrostandortprofil          | Verwaltung von Micro-location profile   | Zu prüfen   |
|   99 | Bewertungen              | Qualitätsprofil              | Qualitätsbewertungsprofile              | Zu prüfen   |
|  100 | Bewertungen              | Konten                       | Verwaltung von Accounts                 | Zu prüfen   |
|  101 | Bewertungen              | Periodeninformation          | Zeitraumbezogene Daten                  | Zu prüfen   |
|  102 | Bewertungen              | Flächeneinheitsliste         | Flächenauflistung für Bewertungen       | Zu prüfen   |
|  103 | Bewertungen              | Liste der Nutzungen          | Nutzungsarten-Katalog                   | Zu prüfen   |
|  104 | Bewertungen              | Baukosten                    | Baukosten für Projekte                  | Zu prüfen   |
|  105 | Bewertungen              | Investitionskosten           | Investitionskosten für Objekte          | Zu prüfen   |
|  106 | Bewertungen              | Ertragswert                  | Verwaltung von Income value             | Zu prüfen   |
|  107 | Bewertungen              | Bodenwert/Grundstückswert    | Verwaltung von Land value               | Zu prüfen   |
|  108 | Bewertungen              | Wiederbeschaffungskosten     | Kosten für Ersatz von Gebäudeteilen     | Zu prüfen   |
|  109 | Bewertungen              | Vergleichswert               | Verwaltung von Comparison value         | Zu prüfen   |
|  110 | Bewertungen              | Empfehlung                   | Empfehlungen für Massnahmen             | Zu prüfen   |
|  111 | Bewertungen              | Risikoprämienmodell          | Verwaltung von Risk premium model       | Zu prüfen   |
|  112 | Bewertungen              | Gebäudekomponenten           | Komponenten und Bauteile von Gebäuden   | Zu prüfen   |
|  113 | Bewertungen              | Ausgaben/Budget              | Verwaltung von Expense/budget           | Zu prüfen   |
|  114 | Bewertungen              | Berichtswesen                | Berichtserstellung und -verwaltung      | Zu prüfen   |
|  115 | Bewertungen              | Vergleichsobjekte            | Verwaltung von Peers                    | Zu prüfen   |
|  116 | Verschiedene Hilfsmittel | Indexer-Webdienst            | Verwaltung von Indexer webservice       | Zu prüfen   |
|  117 | Verschiedene Hilfsmittel | ETL-Webdienst                | Verwaltung von ETL web service          | Zu prüfen   |
|  118 | Verschiedene Hilfsmittel | Vergleichbare Bewertungen    | Verwaltung von Comparable valuations    | Zu prüfen   |
|  119 | Verschiedene Hilfsmittel | Statische Karten             | Verwaltung von Static maps              | Zu prüfen   |
|  120 | Verschiedene Hilfsmittel | Standardkontenpläne          | Verwaltung von Standard account plans   | Zu prüfen   |
|  121 | Verschiedene Hilfsmittel | Systemzustandsprüfung        | Verwaltung von Health check             | Zu prüfen   |

Tabelle: Geschäftsobjekte Wüest Partner Dimensions - Erhaltungsplanung (EHP)

## 3.9. DALA / FileNet Planverwaltung

## Dokumentation:

- Hersteller Webseite:  https://www.ibm.com/products/filenet-content-manager
- IBM Online Dokumentation (Geschäftsobjekte): https://www.ibm.com/docs/de/filenet-p8-platform/5.6.0?topic=overview-business-objectmanagement

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt   | Beschreibung                                                                                                                                                                                                                                                            | Geprüft   |
|----|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Dokument          | Verwaltung von Dateien und anderen Datentypen (z.B. XML) Hat System- und benutzerdefinierte Eigenschaften Kann versioniert werden Unterstützt Inhaltsspeicherung und -indexierung Kann in verschiedene Formate (PDF, HTML) gerendert werden Hat Lebenszyklus-Management | OK        |

|   2 | Dossier (Ordner)           | Container zum Gruppieren von Objekten (Dokumenten) Hierarchische Struktur (Unterordner möglich) Erstellt logische Verknüpfungen zu Dokumenten Hat System- und benutzerdefinierte Eigenschaften            | OK        |
|-----|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|   3 | Anmerkung                  | Fügt Zusatzinformationen zu anderen Objekten hinzu Unabhängig absicherbar Kann eigene Inhalte haben An einzelne Dokumentversion gebunden Unabhängig vom annotierten Objekt änderbar                       | OK        |
|   4 | Benutzerdefinierte Objekte | Für Daten ohne Inhalt/Versionierung Hat System- und benutzerdefinierte Eigenschaften Kann an Workflows teilnehmen Unterstützt Ereignisverarbeitung Ideal für Metadaten-lastige Objekte (z.B. Kundendaten) | Zu prüfen |

Tabelle: Geschäftsobjekte DALA / FileNet

## 3.10. SAP PS (Project System)

## Dokumentation:

- SAP Online Dokumentation:  https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/4dd8cb7b1c484b4b93af84d00f60fdb8 /1ad4b65334e6b54ce10000000a174cb4.html

## Konzeptuelles Datenmodell:

SAPPS Geschaftsobjektefur Bauprojekte

<!-- image -->

Bild: Geschäftsobjekte im SAP PS. Quelle

|    | Geschäftsobjekt                    | Beschreibung                                                                                                                                                                                               | Geprüft   | Kommentar                                                                                                 |
|----|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------|
|  1 | Kernobjekte PS                     |                                                                                                                                                                                                            |           |                                                                                                           |
|  2 | Projektdefinition (Bauprojekt)     | Logisches Geschäftsobjekt: Stammdaten eines Bauprojekts mit übergeordneten Informationen wie Projektart, Start-/Endtermin, Organisationszuordnung und Verantwortlichkeiten. Höchste Hierarchieebene in PS. | OK        | PS-Kernobjekt. Eindeutige Projektnummer, enthält Kopfdaten für das gesamte Projekt.                       |
|  3 | Projektstrukturplan (PSP-Elemente) | Logisches Geschäftsobjekt: Strukturelemente zur hierarchischen Gliederung des Projekts. Träger für Termine, Kosten und Erlöse. Kann mehrere Ebenen haben (z.B. Gebäude Etage Gewerk).                      | OK        | PS-Kernobjekt. Auch "WBS-Elemente" genannt. Primäre Kostenträger im Projekt.                              |
|  4 | Netzpläne                          | Logisches Geschäftsobjekt: Container für zusammenhängende Vorgänge mit deren Anordnungsbeziehungen. Definiert Ablauflogik und Terminierung von Arbeitsabläufen.                                            | OK        | PS-Kernobjekt. Ein PSP-Element kann mehrere Netzpläne haben. Basis für Terminplanung.                     |
|  5 | Vorgänge (Aktivitäten)             | Logisches Geschäftsobjekt: Kleinste ausführbare Arbeitseinheit in einem Netzplan. Hat Dauer, Termine, Ressourcenbedarf und kann Kosten verursachen.                                                        | OK        | PS-Kernobjekt. Auch "Netzplanvorgang" genannt. Arten: Eigenbearbeitung, Fremdbearbeitung, Dienstleistung. |
|  6 | Meilensteine                       | Logisches Geschäftsobjekt: Vorgang mit Dauer null zur Kennzeichnung wichtiger Projektereignisse (z.B. "Baugenehmigung erteilt", "Rohbau fertiggestellt").                                                  | OK        | PS-Kernobjekt. Spezialform des Vorgangs. Wichtig für Fortschrittsmessung und Reporting.                   |
|  7 | Projektbudget (Funktion)           | Logisches Geschäftsobjekt: Planungsfunktion für Kosten auf PSP-Element-Ebene. Ermöglicht Budgetierung und Verfügbarkeitskontrolle.                                                                         | OK        | PS-Funktion. Keine eigenständige Entität, sondern Attribut der PSP-Elemente.                              |
|  8 | Projektabrechnung (Funktion)       | Logisches Geschäftsobjekt: Abrechnungsfunktion zur periodischen Verrechnung der Ist-Kosten von PSP-Elementen an Empfängerobjekte.                                                                          | OK        | PS-Funktion. Überträgt Kosten an Anlagen, Kostenstellen oder Ergebnisobjekte.                             |
|  9 | Wichtige Relationen                |                                                                                                                                                                                                            |           |                                                                                                           |
| 10 | Wirtschaftseinheit (aus RE-FX)     | Referenzobjekt aus RE-FX: Organisatorische Verwaltungseinheit für Immobilien. Kann Auftraggeber für Bauprojekte sein.                                                                                      | OK        | Schnittstelle zu RE-FX. Liefert organisatorischen Kontext für Bauprojekte.                                |
| 11 | Gebäude (aus RE- FX)               | Referenzobjekt aus RE-FX: Bei Sanierung/Umbau das bestehende Gebäude als Projektobjekt.                                                                                                                    | OK        | Schnittstelle zu RE-FX. Objektbezug für Sanierungsprojekte.                                               |
| 12 | Gebäude neu (in RE- FX)            | Referenzobjekt aus RE-FX: Neues Gebäude, das nach Projektabschluss durch AiB-Aktivierung in RE-FX angelegt wird.                                                                                           | OK        | Ergebnis eines Neubauprojekts. Entsteht durch Aktivierung der Anlage im Bau.                              |
| 13 | Anlage im Bau (aus FI-AA)          | Referenzobjekt aus FI-AA: Anlagenstammsatz für im Bau befindliche Anlagen. Sammelt alle aktivierungspflichtigen Projektkosten.                                                                             | OK        | Integration mit Anlagenbuchhaltung. Wird nach Projektende zu fertiger Anlage aktiviert.                   |
| 14 | Ressourcen (aus MM/HR/PM)          | Physisches/Logisches Geschäftsobjekt: Material (MM), Personal (HR) und Maschinen (PM), die in Vorgängen eingeplant werden.                                                                                 | OK        | Integration mit verschiedenen Modulen für Ressourcenplanung und -beschaffung.                             |
| 15 | Fonds (aus PSM- FM)                | Referenzobjekt aus PSM-FM: Budgetverwaltung für zweckgebundene öffentliche Mittel mit Verfügbarkeitskontrolle.                                                                                             | Zu prüfen | Nur relevant für öffentliche Auftraggeber. Alternative: CO-Innenauftrag oder Investment Management.       |

Tabelle: Geschäftsobjekte SAP PS (Project System)

## 3.11. ActaNova GEVER

## Dokumentation:

- Fachanwendung: https://www.efd.gever.admin.ch/

- Hersteller: https://www.rubicon.eu/en/products/acta-nova/

- Info BK: https://www.bk.admin.ch/bk/de/home/dokumentation/gever-bund.html

- eCH-0039:  https://www.ech.ch/de/ech/ech-0039/3.1

## Konzeptuelles Datenmodell:

## GEVER(eCH-0039)Geschaftsobjekte

Bild Links: eCH-0039. Quelle

<!-- image -->

Bild Rechts: Kontext Dokumentenmanagement (Bauwerksdokumentation). Quelle

|    | Geschäftsobjekt       | Beschreibung                                                                                                                         | Geprüft   |
|----|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Dossier (dossier)     | Die Basiskomponente Dossier kann zur Abbildung einer Dossier- und Subdossierstruktur sowie deren Metadaten verwendet werden.         | OK        |
|  2 | Dokument (document)   | Die Basiskomponente Dokument kann zur Abbildung eines Dokuments sowie dessen Metadaten verwendet werden                              | OK        |
|  3 | Anweisung (directive) | Die Basiskomponente Anweisung wird zur Abbildung einer Handlungsanweisung für den Empfänger verwendet.                               | OK        |
|  4 | Adresse (address)     | Die Basiskomponente Adresse wird zur Abbildung von Kontaktinformationen verwendet und implementiert [eCH-0046] Datenstandard Kontakt | OK        |
|  5 | Sonstige?             | Nachrichten (eCH-0147) Workflow                                                                                                      | Zu prüfen |

Tabelle: Geschäftsobjekte ActaNova GEVER

## 3.12. BBL GIS IMMO (ESRI ArcGIS Enterprise)

## Dokumentation:

- Excel Datenmodell:  Fachanwendung - BBL GIS IMMO - Modellbeschreibung.xlsx
- Fachanwendungen BBL Bauten (Intranet): https://intranet.efd-bbl.admin.ch/intraefdbbl/de/home/themen/fachanwendungen.html

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt   | Beschreibung                                                                                                                                                    | Geprüft   |
|----|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Gebäude           | BBL Gebäude als Punkt (WGS 84), entsprechend SAP RE-FX (Geschäftsobjekt Gebäude).                                                                               | OK        |
|  2 | Bodenabdeckung    | Bodenabdeckung als Polygon (WGS 84), entsprechend Amtlicher Vermessung (Schweiz), oder Sonstigen Quellen im Ausland. Verschnitten mit BBL Grundstückspolygonen. | OK        |

|   3 | Grundstück   | BBL Grundstück als Polygon (WGS 84), entsprechend Amtlicher Vermessung (Schweiz), oder Sonstigen Quellen im Ausland.   | OK        |
|-----|--------------|------------------------------------------------------------------------------------------------------------------------|-----------|
|   4 | Bauprojekt   | BBL Projekt (Bauprojekt) als Polygon (WGS 84), entsprechend BBL Projektcontrolling.                                    | OK        |
|   5 | Sonstige?    | Weitere Geschäftsobjekte sind in Entwicklung, 2025 keine neuen                                                         | Zu prüfen |

Tabelle: Geschäftsobjekte BBL GIS IMMO

## 3.13. BIM / CDE (Common Data Environment) Bund

## Dokumentation:

- Strukturiert nach ISO 16739
- Dokumentation IFC Schema (Building Smart Internation):  https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/
- Building Smart Data Dictionary: https://www.buildingsmart.org/users/services/buildingsmart-data-dictionary/

## Konzeptuelles Datenmodell:

Bild: IFC Räumliche Hierarchie (vereinfach).  Quelle

<!-- image -->

IFC/BIM/CDEGeschaftsobjekte(vereinfacht)

<!-- image -->

Bild: Übersicht IFC / BIM / CDE Geschäftsobjekte (vereinfacht).  Quelle

|    | Geschäftsobjekt      | Beschreibung                                                               | Geprüft   |
|----|----------------------|----------------------------------------------------------------------------|-----------|
|  1 | Räumliche Hierarchie |                                                                            |           |
|  2 | IfcProject           | Die oberste Organisationseinheit, die das gesamte Bauprojekt repräsentiert | OK        |
|  3 | IfcSite              | Repräsentiert das Baugrundstück und dessen geografische Lage               | OK        |
|  4 | IfcBuilding          | Das eigentliche Gebäude als zentrale bauliche Struktur                     | OK        |
|  5 | IfcBuildingStorey    | Ein einzelnes Stockwerk oder eine Ebene innerhalb des Gebäudes             | OK        |
|  6 | IfcSpace             | Ein definierter Raum oder Bereich innerhalb eines Geschosses               | OK        |
|  7 | IfcZone              | Eine gruppierte Sammlung von Räumen mit gemeinsamen Eigenschaften          | OK        |
|  8 | Bauliche Elemente    |                                                                            |           |
|  9 | IfcWall              | Tragende und nicht-tragende Wände                                          | OK        |
| 10 | IfcSlab              | Decken, Böden und Bodenplatten                                             | OK        |
| 11 | IfcDoor              | Türen und Türsysteme                                                       | OK        |
| 12 | IfcWindow            | Fenster und Fensterflächen                                                 | OK        |
| 13 | IfcRoof              | Dachkonstruktionen                                                         | OK        |
| 14 | IfcStair             | Treppen und Treppensysteme                                                 | OK        |

|   15 | IfcColumn                            | Stützen und Säulen                                                                             | OK        |
|------|--------------------------------------|------------------------------------------------------------------------------------------------|-----------|
|   16 | IfcBeam                              | Träger und Balken                                                                              | OK        |
|   17 | IfcCurtainWall                       | Vorhangfassaden                                                                                | OK        |
|   18 | IfcRailing                           | Geländer und Brüstungen                                                                        | OK        |
|   19 | Technische Systeme                   |                                                                                                |           |
|   20 | IfcSystem                            | Technische Systeme und Anlagen im Gebäude                                                      | OK        |
|   21 | IfcDistributionSystem                | TGA-Verteilsysteme (Heizung, Lüftung, Sanitär, Elektro)                                        | OK        |
|   22 | IfcDistributionElement               | TGA-Komponenten (Rohre, Kabel, Geräte)                                                         | OK        |
|   23 | IfcTransportElement                  | Aufzüge, Fahrtreppen, Fahrsteige                                                               | OK        |
|   24 | IfcFurniture                         | Möbel und Einrichtungsgegenstände                                                              | OK        |
|   25 | Element- und Systemtypen             |                                                                                                |           |
|   26 | IfcElementType                       | Definiert Typen von baulichen Elementen                                                        | OK        |
|   27 | IfcSystemType                        | Definiert Typen von technischen Systemen und Anlagen                                           | OK        |
|   28 | CDE-Dokumentenmanagement             |                                                                                                |           |
|   29 | Dokument                             | Technische Dokumentation und Unterlagen zum Projekt                                            | OK        |
|   30 | Vertrag                              | Vertragliche Vereinbarungen im Rahmen des Projekts                                             | Zu prüfen |
|   31 | Partner                              | Projektbeteiligte und Geschäftspartner                                                         | Zu prüfen |
|   32 | Kontakt                              | Kontaktinformationen der Projektbeteiligten                                                    | Zu prüfen |
|   33 | CDE-Garantie- und Vertragsmanagement |                                                                                                |           |
|   34 | Garantie/Gewährleistung              | Garantiedokumente mit Laufzeiten, Bedingungen und Leistungsumfang                              | Zu prüfen |
|   35 | Wartungsvertrag/SLA                  | Service Level Agreements für regelmässige Wartung und Instandhaltung                           | Zu prüfen |
|   36 | Garantiefall                         | Dokumentation von Garantieansprüchen und deren Abwicklung                                      | Zu prüfen |
|   37 | Lieferant/Hersteller                 | Verknüpfung zu Garantiegebern und Servicepartnern                                              | Zu prüfen |
|   38 | CDE-Projektmanagement                |                                                                                                |           |
|   39 | Aufgabe/Workflow                     | Planung und Überwachung von Aufgaben und Workflows für Planen, Datenmanagement, oder Sonstiges | Zu prüfen |
|   40 | Issue                                | Problemverfolgung und Mängelmanagement                                                         | Zu prüfen |
|   41 | Meilenstein                          | Wichtige Projekttermine und Phasen                                                             | Zu prüfen |
|   42 | Sonstige                             |                                                                                                |           |
|   43 | Sonstige                             | Anzahl der Geschäftsobjekte wurde nur auf die wesentlichen reduziert                           | Zu prüfen |

Tabelle: Geschäftsobjekte BIM / CDE (Common Data Environment) - ISO 16739

Gerne helfe ich dir, das konzeptuelle Datenmodell für SAP FI/CO zu verbessern. Basierend auf der umfangreichen Dokumentation erstelle ich eine präzisere Version mit korrekten SAP-Bezeichnungen:

## 3.14. SAP FI (Financial Accounting)

## Dokumentation:

- SAP Help Portal - S/4HANA Finance: https://help.sap.com/docs/SAP\_S4HANA\_FINANCE
- Learning Journey Financial Accounting: https://help.sap.com/learning-journeys/5002d32d7a261014ad3081b2533c7414
- EFV Rechnungsmodell Bund: https://www.efv.admin.ch/efv/de/home/themen/finanzpolitik\_grundlagen/rechnungsmodell.html
- HRM2 Handbuch: https://www.srs-cspcp.ch/sites/default/files/pages/2024-01-01-handbuch-hrm2-2.-auflage\_6.pdf
- IPSAS 2025 Handbook: https://www.ipsasb.org/publications/2025-handbook-international-public-sector-accounting-pronouncements

## Hinweise:

- Das FI-Modul bildet die externe Rechnungslegung ab und ist in der Schweiz stark durch HRM2 (Kantone/Gemeinden) und IPSAS (Bund) geprägt
- Universal Journal (ACDOCA) ersetzt in S/4HANA die klassischen FI-Tabellen und vereint FI/CO-Daten in Echtzeit
- Parallele Bewertung in verschiedenen Ledgern ermöglicht gleichzeitige IPSAS- und HRM2-konforme Berichterstattung
- Strikte Trennung zwischen Finanz- und Verwaltungsvermögen gemäss öffentlicher Rechnungslegung
- Integration mit SAP PSM-FM für Budgetkontrolle und Mittelbindung ist für Bundesverwaltung kritisch
- Mehrmandantenfähigkeit ermöglicht Abbildung verschiedener Departemente/Ämter
- ISO 20022 Standard für Zahlungsverkehr in der Schweiz obligatorisch

|    | Geschäftsobjekt                    | Beschreibung                                                             | Geprüft   | Kommentar                                                  |
|----|------------------------------------|--------------------------------------------------------------------------|-----------|------------------------------------------------------------|
|  1 | Organisationsstruktur              |                                                                          |           |                                                            |
|  2 | Buchungskreis (Company Code)       | Kleinste selbstständige Rechnungseinheit mit eigener Bilanz und GuV      | Zu prüfen | Zentrales Organisationselement, 1:1 zu juristischer Person |
|  3 | Geschäftsbereich (Business Area)   | Segment für interne Berichterstattung innerhalb oder über Buchungskreise | Zu prüfen | Optional, für Segmentberichterstattung                     |
|  4 | Funktionsbereich (Functional Area) | Klassifikation nach Aufgaben/Funktionen für Kostenrechnung               | Zu prüfen | Integration mit CO                                         |
|  5 | Hauptbuch (General Ledger)         | Leading Ledger und Non-Leading Ledger für parallele Bewertung            | Zu prüfen | 0L = Leading Ledger                                        |

|   6 | Stammdaten                                      |                                                                 |           |                                           |
|-----|-------------------------------------------------|-----------------------------------------------------------------|-----------|-------------------------------------------|
|   7 | Sachkonto (G/L Account)                         | Konto im Kontenplan mit Kontonummer und Konteneigenschaften     | Zu prüfen | Bilanz- oder GuV-Konto                    |
|   8 | Debitor (Customer)                              | Kundenstammsatz mit Adresse, Zahlungsbedingungen, Kreditlimit   | Zu prüfen | Integration mit SD möglich                |
|   9 | Kreditor (Vendor)                               | Lieferantenstammsatz mit Bankverbindung und Einkaufsbedingungen | Zu prüfen | Integration mit MM                        |
|  10 | Hausbank (House Bank)                           | Bankstammdaten für Zahlungsverkehr                              | Zu prüfen | ISO 20022 Standard für Schweiz            |
|  11 | Kontenplan (Chart of Accounts)                  | Verzeichnis aller Sachkonten eines Buchungskreises              | Zu prüfen | Operative und Konzern-Kontenplan          |
|  12 | Bewegungsdaten                                  |                                                                 |           |                                           |
|  13 | Belege (Document)                               | Belegkopf mit Belegnummer, Buchungsdatum, Periode, Währung      | Zu prüfen | Belegprinzip                              |
|  14 | Belegposition (Line Item)                       | Einzelposten mit Konto, Betrag, Soll/Haben-Kennzeichen          | Zu prüfen | Mind. 2 Positionen pro Beleg              |
|  15 | Hauptbuchbeleg (G/L Document)                   | Beleg für reine Sachkontenbuchungen                             | Zu prüfen | Umbuchungen, Abgrenzungen                 |
|  16 | Debitorenbeleg (Customer Document)              | Ausgangsrechnung oder Zahlungseingang                           | Zu prüfen | AR-Prozess                                |
|  17 | Kreditorenbeleg (Vendor Document)               | Eingangsrechnung oder Zahlungsausgang                           | Zu prüfen | AP-Prozess, Integration mit MM-Bestellung |
|  18 | Universal Journal (S/4HANA)                     |                                                                 |           |                                           |
|  19 | ACDOCA                                          | Universal Journal Einzelposten - vereint FI und CO              | Zu prüfen | Zentrale Tabelle in S/4HANA               |
|  20 | BKPF                                            | Belegkopf Buchhaltung (Header)                                  | Zu prüfen | Weiterhin vorhanden für Kompatibilität    |
|  21 | BSEG                                            | Belegsegment Buchhaltung (Line Items)                           | Zu prüfen | View auf ACDOCA in S/4HANA                |
|  22 | Anlagenbuchhaltung                              |                                                                 |           |                                           |
|  23 | Anlagenstamm (Asset Master)                     | Stammdaten der Anlage mit Anlagennummer und -klasse             | Zu prüfen | Integration FI-AA                         |
|  24 | Anlagenklasse (Asset Class)                     | Gruppierung mit Abschreibungsparametern                         | Zu prüfen | Definiert Nummernkreise und AfA           |
|  25 | Bewegungsart (Transaction Type)                 | Art der Anlagenbewegung (Zugang, Abgang, Transfer)              | Zu prüfen | Steuert Buchungslogik                     |
|  26 | Periodenabschluss                               |                                                                 |           |                                           |
|  27 | Abgrenzung (Accrual)                            | Transitorische Aktiven und Passiven                             | Zu prüfen | Periodengerechte Erfolgsermittlung        |
|  28 | Währungsumrechnung (Foreign Currency Valuation) | Bewertung zum Stichtagskurs                                     | Zu prüfen | Unrealisierte Kursdifferenzen             |

Tabelle: Konzeptuelles Datenmodell SAP FI

## 3.15. SAP CO (Controlling)

## Dokumentation:

- EFV Rechnungsmodell Bund: https://www.efv.admin.ch/efv/de/home/themen/finanzpolitik\_grundlagen/rechnungsmodell.html
- NFB Neues Führungsmodell: https://www.efv.admin.ch/efv/de/home/themen/finanzpolitik\_grundlagen/nfb.html
- SAP Help Portal - Controlling:  https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05
- Material Ledger Documentation: https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/af9ef57f504840d2b81be8667206d485
- Learning Journey Overhead Cost Controlling: https://learning.sap.com/learning-journeys/performing-overhead-cost-controlling-in-sap-s-4hana

## Hinweise:

- CO liefert Führungsinformationen für die interne Steuerung und ist nicht bilanzrelevant
- Primäre Kostenarten sind 1:1 mit Aufwandkonten aus FI verknüpft (automatische Anlage)
- Sekundäre Kostenarten existieren nur in CO für interne Verrechnungen
- Real-Time Integration zwischen FI und CO durch Universal Journal in S/4HANA
- Material Ledger ist ab S/4HANA obligatorisch und fungiert als Sub-Ledger
- Leistungsverrechnung zwischen Verwaltungseinheiten erfolgt über statistische Kennzahlen und Leistungsarten
- Projektcontrolling für Grossprojekte (&gt;10 Mio CHF) mit PS-Integration obligatorisch gemäss HERMES
- Produktkostenrechnung für kostenpflichtige Dienstleistungen der öffentlichen Verwaltung (Gebührenkalkulation)
- Account-based CO-PA ist strategische Richtung in S/4HANA (vs. costing-based)

|    | Geschäftsobjekt                                 | Beschreibung                                    | Geprüft   | Kommentar                            |
|----|-------------------------------------------------|-------------------------------------------------|-----------|--------------------------------------|
|  1 | Organisationsstruktur                           |                                                 |           |                                      |
|  2 | Kostenrechnungskreis (Controlling Area)         | Organisationseinheit für Kostenrechnung         | Zu prüfen | Kann mehrere Buchungskreise umfassen |
|  3 | Ergebnisbereich (Operating Concern)             | Organisationseinheit für Ergebnisrechnung CO-PA | Zu prüfen | Markt-/kundensegmentierte Sicht      |
|  4 | Kostenstellenrechnung (CO-OM-CCA)               |                                                 |           |                                      |
|  5 | Kostenstelle (Cost Center)                      | Ort der Kostenentstehung                        | Zu prüfen | Kleinste Verantwortungseinheit       |
|  6 | Kostenstellenhierarchie (Cost Center Hierarchy) | Standardhierarchie der Kostenstellen            | Zu prüfen | Muss vollständig sein                |
|  7 | Kostenart (Cost Element)                        | Primäre und sekundäre Kostenarten               | Zu prüfen | Primär = 1:1 mit FI-Sachkonto        |
|  8 | Leistungsart (Activity Type)                    | Art der erbrachten internen Leistung            | Zu prüfen | Für Leistungsverrechnung             |
|  9 | Statistische Kennzahl (Statistical Key Figure)  | Bezugsgrösse für Umlagen                        | Zu prüfen | z.B. Mitarbeiter, m²                 |
| 10 | Bewegungsdaten                                  |                                                 |           |                                      |
| 11 | Primärbuchung (Primary Posting)                 | Übernahme aus FI in Echtzeit                    | Zu prüfen | Über Kostenart                       |

|   12 | Umbuchung (Reposting)                       | Manuelle Kostenkorrekturen                    | Zu prüfen   | Transaktion KB11N                        |
|------|---------------------------------------------|-----------------------------------------------|-------------|------------------------------------------|
|   13 | Verteilung (Distribution)                   | Primärkosten auf Empfänger verteilen          | Zu prüfen   | Sender wird entlastet                    |
|   14 | Umlage (Assessment)                         | Primär- und Sekundärkosten umlegen            | Zu prüfen   | Mit sekundärer Kostenart                 |
|   15 | Leistungsverrechnung (Activity Allocation)  | Verrechnung interner Leistungen               | Zu prüfen   | Menge × Tarif                            |
|   16 | Innenaufträge (CO-OM-OPA)                   |                                               |             |                                          |
|   17 | Innenauftrag (Internal Order)               | Kontierungsobjekt für Massnahmen/Projekte     | Zu prüfen   | Sammler für Kosten                       |
|   18 | Auftragsart (Order Type)                    | Klassifizierung der Innenaufträge             | Zu prüfen   | Steuert Nummernkreis und Status          |
|   19 | Auftragsstatus (Order Status)               | System- und Anwenderstatus                    | Zu prüfen   | ERÖF, FREI, TABG, ABGS                   |
|   20 | Budget (Budget)                             | Genehmigte Mittel für Auftrag                 | Zu prüfen   | Mit Verfügbarkeitskontrolle              |
|   21 | Abrechnung (Settlement)                     | Periodische/finale Kostenverrechnung          | Zu prüfen   | An Kostenstelle, PSP-Element oder Anlage |
|   22 | Produktkostenrechnung (CO-PC)               |                                               |             |                                          |
|   23 | Kostenträger (Cost Object)                  | Produkt oder Dienstleistung als Kostensammler | Zu prüfen   | Für Herstellkostenermittlung             |
|   24 | Kalkulation (Product Cost Estimate)         | Plankalkulation mit Mengen- und Wertansatz    | Zu prüfen   | Standardpreisermittlung                  |
|   25 | Material-Ledger (Material Ledger)           | Istpreisermittlung und parallele Bewertung    | Zu prüfen   | Obligatorisch ab S/4HANA                 |
|   26 | Ergebnisrechnung (CO-PA)                    |                                               |             |                                          |
|   27 | Ergebnisobjekt (Profitability Segment)      | Kombination von Merkmalen                     | Zu prüfen   | Kunde, Produkt, Region etc.              |
|   28 | Merkmal (Characteristic)                    | Dimension der Ergebnisanalyse                 | Zu prüfen   | Max. 50 Merkmale                         |
|   29 | Wertfeld (Value Field)                      | Kennzahl (Erlös, Kosten, DB)                  | Zu prüfen   | Account-based oder costing-based         |
|   30 | Plan-/Ist-Vergleich                         |                                               |             |                                          |
|   31 | Planversion (Plan Version)                  | Container für Plandaten                       | Zu prüfen   | Version 0 = operative Planung            |
|   32 | Kostenstellenplanung (Cost Center Planning) | Planung von Kosten und Leistungen             | Zu prüfen   | Jahres- und Periodenplanung              |

Tabelle: Konzeptuelles Datenmodell SAP CO

## 3.16. SAP FI-AA (Asset Accounting)

## Dokumentation:

- Bundesverwaltung:
- SUPERB Fachkonzept Liegenschaftsrechnung (2020):  https://confluence.bit.admin.ch/download/attachments/324708178 /SUPERB\_Fachkonzept\_Liegenschaftsrechnung%20201021.docx?api=v2
- EFV Rechnungsmodell Bund: https://www.efv.admin.ch/efv/de/home/themen/finanzpolitik\_grundlagen/rechnungsmodell.html
- EFD Staatsrechnung:  https://www.efv.admin.ch/de/staatsrechnung#Weitere-Infos-zum-Thema-Staatsrechnung
- SAP Standard:
- SAP S/4HANA Finance - New Asset Accounting Overview:  https://www.michaelmanagement.com/blog/sap/new-asset-accountingoverview-of-sap-s4hana-finance
- Introducing New Asset Accounting in SAP S/4HANA: https://www.sap-press.com/introducing-new-asset-accounting-in-sap-s4hana-fi-aa\_4415/
- FI-AA Key Functionality Guide: https://buecher.espresso-tutorials.de/introduction-to-new-asset-accounting-in-sap-s4hana-fi-aa
- SAP Asset Accounting - Best Practices: https://sapinsider.org/topic/sap-finance/sap-asset-accounting/
- Asset Accounting Configuration in S/4 HANA: https://www.gauravconsulting.com/post/how-to-set-up-asset-accounting-configuration-insap-s-4-hana
- Integration FI-AA, RE-FX and GEF: https://learning.sap.com/learning-journeys/configuring-sap-s-4hana-cloud-private-edition-assetmanagement/exploring-integration-with-fi-aa-re-fx-and-gef
- FI Postings Integration with RE-FX: https://sapinsider.org/automate-fi-postings-by-integration-with-re-fx-through-account-determination/
- SAP Help Portal - Asset Accounting: https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/67e323b7117e4c91869c258933f47182 /592b3250326543f7bbceba6ae91fc061.html
- FI-AA Integration with Lease Accounting: https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/8fbeed5f2046489696a50ac7fd76f9c6 /a17af0fdf522415783a7b4e1d5d6e759.html

## Hinweise:

- Das FI-AA Modul ist zentral für die Verwaltung des BBL-Immobilienportfolios mit über 2'600 Gebäuden
- Parallele Bewertung in verschiedenen Ledgern ermöglicht gleichzeitige IPSAS- und OR-konforme Berichterstattung
- Universal Journal (ACDOCA) ersetzt in S/4HANA die klassischen FI-AA Tabellen für Bewegungsdaten
- Integration mit SAP RE-FX für Gebäudestammdaten ist kritisch für BBL
- Schweiz-spezifische Abschreibungsvorschriften gemäss EStV sind zu beachten
- SUPERB-Migration auf S/4HANA erfolgte im September 2023

## Konzeptuelles Datenmodell:

## 10 Werteflusse

WerteflussBauten(UbersichtSAP)

<!-- image -->

Bild: Werteflüsse (SUPERB Fachkonzept Liegenschaftsrechnung, 2020). Quelle

|    | Gruppe / Geschäftsobjekt                               | Beschreibung                                                                  | Geprüft   | Kommentar                                                        |
|----|--------------------------------------------------------|-------------------------------------------------------------------------------|-----------|------------------------------------------------------------------|
|  1 | Anlagenstammdaten                                      |                                                                               |           |                                                                  |
|  2 | Anlagenstamm (Asset Master)                            | Zentrale Stammdaten der Anlage mit allen Eigenschaften und Zuordnungen        | Zu prüfen | Tabelle: ANLA; Felder: Anlagennummer, Anlagenklasse, Bezeichnung |
|  3 | Zeitabhängige Zuordnungen (Time-Dependent Allocations) | Kostenstelle, Profit Center und andere Organisationszuordnungen mit Zeitbezug | Zu prüfen | Tabelle: ANLZ; Wichtig für BBL-Organisationsstruktur             |
|  4 | Abschreibungsparameter (Depreciation Terms)            | Nutzungsdauer, Abschreibungsschlüssel und Methoden je Bewertungsbereich       | Zu prüfen | Tabelle: ANLB; Schweiz-spezifische Steuervorschriften            |
|  5 | Anlagenwerte (Asset Values)                            | Kumulierte AHK, Abschreibungen und Restbuchwerte                              | Zu prüfen | Tabelle: ANLC; Parallele Bewertung IPSAS/OR                      |
|  6 | Anlagentexte (Asset Texts)                             | Mehrsprachige Beschreibungen der Anlagen                                      | Zu prüfen | Tabelle: ANLT; DE/FR/IT für Bundesverwaltung                     |
|  7 | Bewegungsdaten                                         |                                                                               |           |                                                                  |
|  8 | Anlagenbuchung Kopf (Asset Document Header)            | Belegkopf für Anlagenbuchungen mit Buchungsdatum und Bewegungsart             | Zu prüfen | Tabelle: ANEK                                                    |
|  9 | Anlagen-Einzelposten (Asset Line Items)                | Detaillierte Bewegungen je Abschreibungsbereich                               | Zu prüfen | Tabelle: ANEP                                                    |
| 10 | Anlagen-Periodenwerte (Asset Periodic Values)          | Aggregierte Werte je Periode                                                  | Zu prüfen | Tabelle: ANLP                                                    |
| 11 | Anlagenklassen                                         |                                                                               |           |                                                                  |
| 12 | Anlagenklasse (Asset Class)                            | Gruppierung von Anlagen mit gleichen Eigenschaften                            | Zu prüfen | Definiert Nummernkreise und Standardwerte                        |
| 13 | Anlagenhauptklasse (Asset Main Class)                  | Übergeordnete Kategorisierung der Anlagenklassen                              | Zu prüfen | Z.B. Immobilien, Technik, Fahrzeuge                              |
| 14 | Abschreibung                                           |                                                                               |           |                                                                  |
| 15 | Abschreibungsbereich (Depreciation Area)               | Bewertungsbereich für unterschiedliche Rechnungslegungsvorschriften           | Zu prüfen | Tabelle: T093A; IPSAS, OR, Steuerbilanz                          |
| 16 | Abschreibungsschlüssel (Depreciation Key)              | Definition der Abschreibungsmethode                                           | Zu prüfen | Tabelle: T090; Linear, degressiv, leistungsabhängig              |
| 17 | Abschreibungsverlauf (Depreciation Trace)              | Historie der durchgeführten Abschreibungen                                    | Zu prüfen | Für Revision und Nachvollziehbarkeit                             |
| 18 | Anlagen im Bau                                         |                                                                               |           |                                                                  |
| 19 | Anlagen im Bau (Assets under Construction)             | Sammelkonten für aktivierungspflichtige Investitionen                         | Zu prüfen | Integration mit PS für BBL-Bauprojekte                           |
| 20 | AiB-Abrechnung (AuC Settlement)                        | Aktivierung der Anlagen im Bau als fertige Anlagen                            | Zu prüfen | Überführung in Anlagenbestand                                    |
| 21 | S/4HANA-spezifisch                                     |                                                                               |           |                                                                  |
| 22 | Universal Journal                                      | Zentrale Tabelle für alle FI-AA Bewegungsdaten in Echtzeit                    | Zu prüfen | Tabelle: ACDOCA; Ab S/4HANA obligatorisch                        |
| 23 | Neue Anlagenbuchhaltung (New Asset Accounting)         | Modernisierte Strukturen und Prozesse ab S/4HANA                              | Zu prüfen | Verbesserte Performance und Integration                          |

## 3.17. SAP IM (Investment Management)

## Dokumentation:

- SAP Help Portal - Investment Management: https://help.sap.com/doc/saphelp\_nw74/7.4.16/en-US/0a/f6885322f03d58e10000000a174cb4 /frameset.htm
- SAP IM Tables Overview: https://sapstack.com/tables/module.php?module=IM
- Investment Management in SAP S/4HANA: https://blog.sap-press.com/planning-and-budgeting-for-investment-controlling-with-sap-s4hana
- CBS Consulting - IM Module Overview: https://www.cbs-consulting.com/us/investment-management-in-sap-practical-applications-and-uses/
- ERP College - IM Overview: https://erpcollege.co/2022/03/07/an-overview-of-investment-management-in-sap/

## Hinweise für BBL:

- Das IM-Modul umfasst ca. 70 Kerntabellen im SAP\_FIN Komponente
- Zentrale Tabellen: IMTP (Programme), IMPR (Positionen), IMAK (Anträge), IMAKZ (Zuordnungen), BPGE/BPJA (Budgets)
- Für BBL-spezifische SIA-Phasen und eBKP-H Strukturen sind Anpassungen in der Konfiguration erforderlich
- Workflow-Integration für mehrstufige Genehmigungsprozesse gemäss BBL-Kompetenzordnung möglich

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt                                                                | Beschreibung                                                                                                                   | Geprüft   | Kommentar                                                                              |
|----|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------|
|  1 | Investitionsprogramme                                                          |                                                                                                                                |           |                                                                                        |
|  2 | Investitionsprogramm (Investment Program)                                      | Oberste Hierarchieebene für strategische Investitionsplanung mit Genehmigungsjahr, Programmtyp und Verantwortlichem            | Zu prüfen | IM-Kerntabelle: IMTP; Texte: IMTT                                                      |
|  3 | Programmposition (Investment Program Position)                                 | Hierarchische Positionen innerhalb des Programms zur strukturierten Budgetverteilung mit interner und externer Positionsnummer | Zu prüfen | IM-Kerntabelle: IMPR; Parent-Child über PARNR; Texte: IMPU                             |
|  4 | Programmtyp (Program Type)                                                     | Konfiguration der Programmeigenschaften mit Planprofil und erlaubten Werten                                                    | Zu prüfen | IM-Customizing: TAI05; Texte: TAI05T                                                   |
|  5 | Planungsprofil (Planning Profile)                                              | Steuerung der Planungshorizonte und Wertearten für Mehrjahresplanung                                                           | Zu prüfen | IM-Customizing; Keine eigene Tabelle                                                   |
|  6 | Budgetprofil (Budget Profile)                                                  | Profil für Budgetierung mit Verfügbarkeitskontrolle und Toleranzgrenzen                                                        | Zu prüfen | IM-Customizing; Steuert BPGE/BPJA- Verhalten                                           |
|  7 | Investitionsanträge                                                            |                                                                                                                                |           |                                                                                        |
|  8 | Investitionsantrag (Appropriation Request)                                     | Investitionsantrag für Planungs- und Entscheidungsphase mit Antragsnummer und -typ                                             | Zu prüfen | IM-Kerntabelle: IMAK; Texte: IMAKT; Business Object: BUS2204                           |
|  9 | Variante des Investitionsantrags (Appropriation Request Variant)               | Alternative Realisierungsvarianten eines Investitionsantrags zur Vergleichsanalyse                                             | Zu prüfen | IM-Kerntabelle: IMAV; Texte: IMAVT; 1:n zu IMAK                                        |
| 10 | Antragstyp (Appropriation Request Type)                                        | Definition der Antragstypen mit Genehmigungsworkflow und Planungsprofilen                                                      | Zu prüfen | IM-Customizing: TAIF1; Texte: TAIF1T                                                   |
| 11 | Investitionsgrund (Investment Reason)                                          | Investitionsgründe mit prozentualer Verteilung für Kategorisierung                                                             | Zu prüfen | IM-Tabelle: IMAKPI; Referenz: T087I (CO)                                               |
| 12 | Umweltschutz-Investition (Environmental Investment)                            | Umweltschutz-Investitionsgründe mit prozentualer Zuordnung                                                                     | Zu prüfen | IM-Tabelle: IMAKPU; Spezialisierung von IMAKPI                                         |
| 13 | Investitionsmassnahmen                                                         |                                                                                                                                |           |                                                                                        |
| 14 | Innenauftrag als Massnahme (Internal Order as Investment Measure)              | Innenauftrag als Investitionsmassnahme für einfache Projekte                                                                   | Zu prüfen | CO-Referenz: AUFK; View: COAS; Verbindung über AUFK-IVPRO (Investitionsprofil)         |
| 15 | PSP-Element als Massnahme (WBS Element as Investment Measure)                  | PSP-Element als Investitionsmassnahme für komplexe Bauprojekte                                                                 | Zu prüfen | PS-Referenz: PRPS; Projekt: PROJ; Hierarchie: PRHI; Verbindung über Investitionsprofil |
| 16 | Instandhaltungsauftrag als Massnahme (Maintenance Order as Investment Measure) | Instandhaltungsauftrag als Investitionsmassnahme für Anlagen                                                                   | Zu prüfen | PM-Referenz: AUFK + AFIH; Spezielle Auftragsarten PM06/PM07                            |
| 17 | Zuordnung Massnahme zu Position (Measure Assignment to Position)               | Zuordnung von Massnahmen zu Programmpositionen                                                                                 | Zu prüfen | IM-Kerntabelle: IMZO; Verbindet IMPR mit AUFK/PRPS über OBJNR                          |
| 18 | Zuordnung Massnahme zu Antrag (Measure Assignment to Request)                  | Zuordnung von Massnahmen zu Anträgen                                                                                           | Zu prüfen | IM-Kerntabelle: IMAKZ; Verbindet IMAK mit Massnahmen                                   |
| 19 | Anlage im Bau (Asset under Construction)                                       | Anlagen im Bau für aktivierungspflichtige Investitionen                                                                        | Zu prüfen | FI-AA-Referenz: ANLI; Verbindung Massnahme zu AiB                                      |
| 20 | Planung und Budgetierung                                                       |                                                                                                                                |           |                                                                                        |
| 21 | Gesamtbudget (Overall Budget)                                                  | Gesamtbudget für Investitionsobjekte ohne Jahresaufteilung                                                                     | Zu prüfen | FM-Kerntabelle: BPGE; Details: BPEG; Nur bei Verfügbarkeitskontrolle "Gesamt"          |
| 22 | Jahresbudget (Annual Budget)                                                   | Jahresbudget mit periodischer Aufteilung                                                                                       | Zu prüfen | FM-Kerntabelle: BPJA; Details: BPEJ; Nur bei Verfügbarkeitskontrolle "Jahreswerte"     |
| 23 | Planwerte (Plan Values)                                                        | Planwerte für Kosten und Erlöse                                                                                                | Zu prüfen | CO-Referenz: COSP/COss (Legacy); S/4: ACDOCP                                           |
| 24 | Budgetverteilung (Budget Distribution)                                         | Budgetverteilung von Programm zu Massnahmen                                                                                    | Zu prüfen | IM-Prozess; Transaktion IM52; Nutzt IMZO- Verknüpfung                                  |
| 25 | Verfügbarkeitskontrolle (Budget Availability Control)                          | Verfügbarkeitskontrolle mit Toleranzgrenzen und Warnungen                                                                      | Zu prüfen | IM-Konfiguration; Steuert BPGE vs. BPJA- Nutzung                                       |
| 26 | Budgetergänzung (Budget Supplement)                                            | Budgetergänzungen und -umbuchungen                                                                                             | Zu prüfen | IM-Prozess; Ändert Werte in BPGE/BPJA                                                  |
| 27 | Abschreibungssimulation                                                        |                                                                                                                                |           |                                                                                        |

|   28 | Abschreibungssimulation (Depreciation Simulation)   | Simulation der Abschreibungen für Investitionsprojekte     | Zu prüfen   | IM-Kerntabelle: ANIA; Integration mit FI-AA                           |
|------|-----------------------------------------------------|------------------------------------------------------------|-------------|-----------------------------------------------------------------------|
|   29 | Abschreibungsbereiche (Depreciation Areas)          | Bewertungsbereiche für Abschreibungssimulation             | Zu prüfen   | IM-Kerntabelle: ANIB; Referenz zu FI-AA- Bewertungsbereichen          |
|   30 | Stammdaten                                          |                                                            |             |                                                                       |
|   31 | Verantwortlicher (Person Responsible)               | Verantwortliche Personen für Programme und Positionen      | Zu prüfen   | Referenz: TCJ04 (PS-Tabelle); Feld VERNR in IMTP/IMPR                 |
|   32 | Investitionsgrösse (Scale of Investment)            | Grössenkategorien für Investitionsobjekte                  | Zu prüfen   | IM-Customizing: TAIF5; Details: TAIF51                                |
|   33 | Genehmigungsworkflow (Approval Workflow)            | Genehmigungsworkflow für Anträge und Budgets               | Zu prüfen   | Workflow: WS00300022; Business Object: BUS2204                        |
|   34 | Reporting                                           |                                                            |             |                                                                       |
|   35 | IM-Verdichtung (IM Summarization)                   | Verdichtete Daten für Reporting                            | Zu prüfen   | IM-Reporting: IMCER (Anträge); IMCC, IMCH (Programme)                 |
|   36 | Drilldown-Berichte (Drilldown Reports)              | Berichte mit flexibler Hierarchienavigation                | Zu prüfen   | IM-Berichtswesen; Nutzt diverse Verdichtungstabellen                  |
|   37 | Plan-Ist-Vergleich (Plan/Actual Comparison)         | Plan-Ist-Vergleiche auf verschiedenen Ebenen               | Zu prüfen   | IM-Berichtswesen; Nutzt COSP/COss bzw. ACDOCA                         |
|   38 | S/4HANA-spezifisch                                  |                                                            |             |                                                                       |
|   39 | Universal Journal                                   | Zentrale Tabelle für alle FI-IM Bewegungsdaten in Echtzeit | Zu prüfen   | S/4-Kerntabelle: ACDOCA; Ersetzt mehrere Legacy-Tabellen              |
|   40 | Universal Planning                                  | Neue Planungstabelle für S/4HANA                           | Zu prüfen   | S/4-Kerntabelle: ACDOCP; Ersetzt COSP /COss für Planung               |
|   41 | SAC-Integration (SAC Integration)                   | SAP Analytics Cloud für Planung und Reporting              | Zu prüfen   | Cloud-Service; OData-Integration; Story: SAP_FI_IFP_IM_CAPEX_Planning |

Tabelle: Geschäftsobjekte SAP IM

## 3.18. SAP EPPM (Enterprise Project and Portfolio Management)

- Hier ist nicht die Standard SAP PPM Lösung gemeint
- Die SUPERB Version hat viele Ähnlichkeiten, aber ist nicht identisch

## Dokumentation:

- SUPERB Dokumentation:
- Zu ergänzen
- SAP Standard Dokumentation:
- SAP Learning - Business Processes in PPM: https://learning.sap.com/courses/business-processes-in-sap-s-4hana-portfolio-and-projectmanagement/introduction-to-sap-s-4hana
- SAP PPM Tables Overview:  https://sapstack.com/tables/module.php?module=PPM

## Hinweise:

- Die im Diagramm (Konzeptuelles Datenmodell )dargestellten Objekte (PS Projektdefinition, PSP Element, CO Innenauftrag, RE-FX Gebäude, etc.) sind zu anderen SAP-Modulen und keine EPPM-eigenen Geschäftsobjekte. externe Referenzen

## Konzeptuelles Datenmodell:

<!-- image -->

Bild: Konzeptuelles Datenmodell

|    | Gruppe / Geschäftsobjekt   | Beschreibung                                                                    | Geprüft   | Kommentar                                                                                                                                      |
|----|----------------------------|---------------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Portfolioverwaltung        |                                                                                 |           |                                                                                                                                                |
|  2 | Portfolio                  | Oberste Organisationsstruktur für strategische Projekt- und Programmverwaltung  | Zu prüfen | Hierarchische Parent-Child Beziehung zu Initiative Ein Portfolio ist ein unabhängig verwalteter Bereich ohne Interaktion zu anderen Portfolios |
|  3 | Initiative (Programm)      | Programm-Ebene zur Bündelung mehrerer zusammenhängender Projekte                | Zu prüfen | Container für mehrere Elemente                                                                                                                 |
|  4 | Element                    | Einzelnes Portfolio-Item, das ein konkretes Projekt oder Vorhaben repräsentiert | Zu prüfen | Zentrales Objekt mit vielen Verknüpfungen                                                                                                      |
|  5 | Klassifizierung            |                                                                                 |           |                                                                                                                                                |

|   6 | Klassifizierungshierarch ie   | Strukturierte Kategorisierungsebene für Portfolioelemente Alternative thematische oder organisatorische Gruppierung innerhalb des Portfolios   | Zu prüfen   | Parent für Bereiche Optionale Zuordnung zu Elementen                                  |
|-----|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------|---------------------------------------------------------------------------------------|
|   7 | Bereich                       | Thematische oder organisatorische Gruppierung innerhalb der des Portfolios Klassifizierung                                                     | Zu prüfen   | Zuordnung zu Elementen Optionale                                                      |
|   8 | Entscheidungspunkt            | Definierte Gates/Meilensteine für Projektfreigaben und Statusübergänge                                                                         | Zu prüfen   | Steuert Lebenszyklusstatus von Elementen                                              |
|   9 | Projektmanagement             |                                                                                                                                                |             |                                                                                       |
|  10 | Projektdefinition             | Hauptprojektebene mit Stammdaten, Terminen und Verantwortlichkeiten                                                                            | Zu prüfen   | 1:1 Verknüpfung mit Element                                                           |
|  11 | Phase                         | Projektphasen gemäss definierter Methodik (z.B. SIA-Phasen)                                                                                    | Zu prüfen   | Hierarchisch unter Projektdefinition                                                  |
|  12 | Aufgabe                       | Detaillierte Arbeitspakete mit Aufwand, Dauer und Terminen                                                                                     | Zu prüfen   | Hierarchisch unter Phase, kann Unteraufgaben haben                                    |
|  13 | Checkliste                    | Container für Qualitätssicherungs- und Compliance-Prüfungen                                                                                    | Zu prüfen   | Zugeordnet zu Aufgaben                                                                |
|  14 | Checklistenpunkt              | Einzelne Prüfpunkte innerhalb einer Checkliste                                                                                                 | Zu prüfen   | Detail-Ebene der Checkliste                                                           |
|  15 | Ressourcenmanagem ent         |                                                                                                                                                |             |                                                                                       |
|  16 | Rolle                         | Abstrakte Funktionsbeschreibung für Projektbeteiligte                                                                                          | Zu prüfen   | n:m Beziehung zu Geschäftspartnern                                                    |
|  17 | Geschäftspartner              | Konkrete Personen oder Organisationen als Projektressourcen                                                                                    | Zu prüfen   | Kann mehrere Rollen innehaben                                                         |
|  18 | Finanzplanung                 |                                                                                                                                                |             |                                                                                       |
|  19 | Finanzgruppe                  | Übergeordnete Gruppierung für Finanzplanungskategorien                                                                                         | Zu prüfen   | Container für Finanzkategorien                                                        |
|  20 | Finanzkategorie               | Kategorien für Budgetierung und Kostenplanung                                                                                                  | Zu prüfen   | Strukturiert Finanzplanung                                                            |
|  21 | Finanzsicht                   | Aggregierte Plan- und Ist-Werte aus finanzieller Perspektive                                                                                   | Zu prüfen   | View auf Finanzdaten eines Elements                                                   |
|  22 | Finanz- /Kapazitätsplanung    | Periodische Plan- und Kapazitätswerte mit Zeitbezug                                                                                            | Zu prüfen   | Detaillierte Planwerte pro Element und Periode                                        |
|  23 | Projektcontrolling            |                                                                                                                                                |             |                                                                                       |
|  24 | Massnahme                     | Definierte Aktionen zur Risikomitigation oder Chancennutzung                                                                                   | Zu prüfen   |                                                                                       |
|  25 | Risiko                        | Identifizierte Projektrisiken mit Eintrittswahrscheinlichkeit und Auswirkung                                                                   | Zu prüfen   |                                                                                       |
|  26 | Meilenstein                   | Wichtige Projektereignisse ohne Dauer für Fortschrittsmessung                                                                                  | Zu prüfen   |                                                                                       |
|  27 | Ergebnis                      | Definierte Projektergebnisse/Deliverables                                                                                                      | Zu prüfen   |                                                                                       |
|  28 | Systemtechnisch               |                                                                                                                                                |             |                                                                                       |
|  29 | Objektverknüpfung             | Generische Verknüpfungstabelle für flexible Objekt-Beziehungen                                                                                 | Zu prüfen   | Ermöglicht n:m Beziehungen zwischen verschiedenen Objekttypen wie SAP PS, RE-FX, etc. |

Tabelle: Geschäftsobjekte SAP PPM

## 3.19. WSM (Workspace Management)

## Dokumentation:

- Lean Business Case:  Facility FM- und Workspace Management WSM

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt   | Beschreibung   | Geprüft   | Kommentar   |
|----|-------------------|----------------|-----------|-------------|
|  1 |                   |                |           |             |
|  2 |                   |                |           |             |
|  3 |                   |                |           |             |
|  4 |                   |                |           |             |
|  5 |                   |                |           |             |

Tabelle: Geschäftsobjekte Workspace Management

## 3.20. BVML (Beschaffungs- und Vergabemanagementlösung)

## Dokumentation:

- FK - Umsetzung des harmonisierten Beschaffungsprozesses Bund Bundesamt für Bauten und Logistik:  https://www.efk.admin.ch/prufung /umsetzung-des-harmonisierten-beschaffungsprozesses-bund
- Dokumentation BVML Schnittstellen: https://confluence.bit.admin.ch/x/BMEWIw
- Beschaffungsstrategie der Bundesverwaltung 2021-2030:  https://www.bkb.admin.ch/dam/de/sd-web/Q5i6w36w5nc2/Wegleitung%20Monitoring% 20Umsetzung%20Beschaffungsstrategie%20der%20Bundesverwaltung.pdf
- Kompetenzzentrum Beschaffungswesen Bund (KBB): https://www.beschaffung.admin.ch/bpl/de/home/fachstellen/kompetenzzentrumbeschaffungswesen-bund-kbb.html
- SIMAP API Spezifikation: https://www.simap.ch/api/specifications/changelog.html
- TRIAS Leitfaden für öffentliche Beschaffungen: https://www.trias.swiss/grundlagen-und-einfuehrung
- Open Contracting Data Standard (OCDS): https://standard.open-contracting.org/latest/en/schema/reference/
- eCH-Standards für E-Government: https://www.ech.ch/fr/standard-uebersicht
- eIAM Identity &amp; Access Management: https://www.eiam.swiss/pages/index.html
- Bundesgesetz über das öffentliche Beschaffungswesen (BöB):  https://www.fedlex.admin.ch/eli/cc/2020/126/de

## Konzeptuelles Datenmodell:

## Entwurf, Inhalte zu prüfen

## BVML-HBB Losungsansatz

Abbildung 1: Losungsansatz zum Zusammenspiel BVML -HBB (Quelle:Programm SUPERB August 2024; Darstellung EFK)

<!-- image -->

## Datenfeld Mapping fur Schnittstelle BVML-GEVER

WirhabenimExcel imAnhang denFeldabgleichzwischenActa Nova und BVML durchgefuhrt.ImAnhang sendenwir euch dasExcelzu,dieGrinmarkiertenFelder sind diesewelche auf beidenSeitenvorhandenist.

GernekonnenwirdiesbeiunserernachstenSitzungvertieftbesprechenund dienenfur dieweitereDetaillierungendesFachkonzeptes-technischeKonzepterarbeitung. Wichtig ist, dass man den Zusammenhang mit dem Zielbild (welches zur Zeit erarbeitet wird) macht.

Wichtig:wirhabenkeineeinheitlicheNamenskonventionunddiesistzwingendabzugleichenzwischenBVML-GEVER

<!-- image -->

Bild Links: BVML - HBB Lösungsansatz.  Quelle

Bild Rechts: Datenfeld Mapping für Schnittstelle BVML-GEVER. Quelle

|    | Gruppe / Geschäftsobjekt               | Beschreibung                                                                                                                                  | Geprüft   | Kommentar                                    |
|----|----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------|
|  1 | Kernprozess-Entitäten                  |                                                                                                                                               |           |                                              |
|  2 | Vergabeverfahren (Procurement Process) | Zentraler Vergabeprozess von Ausschreibung bis Zuschlag mit eindeutiger OCID gemäss OCDS- Standard, durchläuft Phasen Planning, Tender, Award | Zu prüfen | Entspricht SUPERB /GENOVA@BIL Harmonisierung |

| 3                         | Vergabedossier (Award                                                                                                 | Komplette Dokumentation eines Vergabeverfahrens mit allen relevanten Unterlagen gemäss Art. 48                  | Zu prüfen   | 10 Jahre Aufbewahrungspflicht               |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------|---------------------------------------------|
| 4                         | Dossier) BöB                                                                                                          | Ausschreibung und Vergabe                                                                                       |             |                                             |
| 5                         | Ausschreibung (Tender) Strukturierte Ausschreibungsunterlagen mit BöB), Zuschlagskriterien (Art. 29 BöB) und          | technischen Spezifikationen, Eignungskriterien (Art. 27 Verfahrensart Zu                                        | prüfen      | Publikation via SIMAP API obligatorisch     |
| 6 Los (Lot)               | Teilmenge einer Ausschreibung zur KMU-freundlichen Aufteilung gemäss Art. 28 Spezifikationen und Zuschlagsmöglichkeit | BöB mit eigenen                                                                                                 | Zu prüfen   |                                             |
| 7 Position (Item)         | Einzelne Vergabeposition innerhalb eines Loses mit CPV-Code, Menge, Einheit und Details                               | technischen                                                                                                     | Zu prüfen   | CPV-Klassifikation zwingend für SIMAP       |
| 8 Angebot (Bid)           | Eingereichte Offerte eines Anbieters mit Preis, technischer Lösung, Nachweisen und                                    | Dokumenten gemäss Ausschreibungsanforderungen                                                                   | Zu prüfen   | QES-Signatur bei elektronischer Einreichung |
| 9                         | Bewertungsmatrix (Evaluation Matrix)                                                                                  | Strukturierte Bewertung aller Angebote nach definierten Kriterien mit Punktevergabe und Gewichtung              | Zu prüfen   | Nachvollziehbarkeit für Rechtsmittel        |
| 10                        | Zuschlag (Award)                                                                                                      | Vergabeentscheidung mit Begründung, Punktebewertung, Zuschlagssumme und Lieferantenzuordnung gemäss Art. 41 BöB | Zu prüfen   | 20-tägige Beschwerdefrist beachten          |
| 11                        | Verfügung (Decision)                                                                                                  | Formelle Vergabeverfügung mit Rechtsmittelbelehrung gemäss Art. 51 BöB                                          | Zu prüfen   |                                             |
| 12                        | Verfahrensmanagement                                                                                                  |                                                                                                                 |             |                                             |
| 13                        | Verfahrensart (Procedure Type)                                                                                        | Offenes, selektives, Einladungs- oder freihändiges Verfahren gemäss BöB/VöB                                     | Zu prüfen   |                                             |
| 14 (Prequalification)     | Präqualifikation                                                                                                      | Eignungsprüfung von Anbietern im selektiven Verfahren gemäss Art. 20 BöB                                        | Zu prüfen   |                                             |
| 15                        | Fragerunde (Clarification Round)                                                                                      | Strukturierte Q&A während Ausschreibungsphase mit anonymisierten Fragen und Antworten                           | Zu prüfen   | SIMAP-Integration                           |
| 16                        | Dialog (Dialogue)                                                                                                     | Strukturierter Dialog im Dialogverfahren gemäss Art. 24 BöB                                                     | Zu prüfen   |                                             |
| 17                        | Verhandlung (Negotiation)                                                                                             | Dokumentierte Verhandlungen im Einladungsverfahren                                                              | Zu prüfen   | Gleichbehandlungsgebot                      |
| 18                        | Akteure und Organisationen                                                                                            |                                                                                                                 |             |                                             |
| 19                        | Vergabestelle (Contracting Authority)                                                                                 | Ausschreibende Verwaltungseinheit des Bundes mit Organisationsstruktur und Zuständigkeiten                      | Zu prüfen   |                                             |
| 20                        | Anbieter (Economic Operator)                                                                                          | Wirtschaftsteilnehmer mit Qualifikationen, Zertifizierungen und Eignungsnachweisen                              | Zu prüfen   | UID-Integration mit Zefix                   |
| 21                        | Bietergemeinschaft (Consortium)                                                                                       | Zusammenschluss mehrerer Anbieter für gemeinsame Angebotsabgabe gemäss Art. 31 BöB                              | Zu prüfen   |                                             |
| 22                        | Subunternehmer (Subcontractor)                                                                                        | Unterauftragnehmer mit Angabe der übertragenen Leistungen                                                       | Zu prüfen   |                                             |
| 23                        | Evaluator (Evaluator)                                                                                                 | Bewertungsperson mit Fachexpertise und Unabhängigkeitserklärung                                                 | Zu prüfen   | Ausstandsregeln beachten                    |
| 24                        | Dokumente und Workflows                                                                                               |                                                                                                                 |             |                                             |
| 25                        | Ausschreibungsunterlagen (Tender Documents)                                                                           | Alle zur Angebotsabgabe erforderlichen Dokumente mit Versionskontrolle                                          | Zu prüfen   | PDF/A für Archivierung                      |
| 26                        | Pflichtenheft (Specifications)                                                                                        | Detaillierte Leistungsbeschreibung mit technischen und funktionalen Anforderungen                               | Zu prüfen   |                                             |
| 27                        | Angebotsformular (Bid Form)                                                                                           | Standardisiertes Formular für Angebotsabgabe mit Preisblatt                                                     | Zu prüfen   |                                             |
| 28                        | Eignungsnachweis (Qualification Evidence)                                                                             | Dokumente zum Nachweis der Eignung (Referenzen, Zertifikate, Bilanzen)                                          | Zu prüfen   |                                             |
| 29                        | Bewertungsprotokoll (Evaluation Report)                                                                               | Dokumentierte Bewertung mit Begründung und Unterschriften                                                       | Zu prüfen   |                                             |
| 30 Protocol)              | Zuschlagsprotokoll (Award                                                                                             | Formelles Protokoll der Zuschlagsentscheidung                                                                   | Zu prüfen   | GEVER-Ablage                                |
| 31                        | Debriefing-Protokoll (Debriefing Record)                                                                              | Dokumentation der Rückmeldung an nicht berücksichtigte Anbieter                                                 | Zu prüfen   |                                             |
| 32                        | Fristen und Termine                                                                                                   |                                                                                                                 |             |                                             |
| 33 Eingabefrist Deadline) | (Submission Frist für Angebotseinreichung gemäss Art. 46 BöB mit                                                      | Mindestfristen                                                                                                  | Zu prüfen   | 40 Tage im offenen Verfahren                |
| 34 Bindefrist (Validity   | Period)                                                                                                               | Gültigkeitsdauer der eingereichten Angebote                                                                     | Zu prüfen   |                                             |
| 35 Deadline)              | Beschwerdefrist (Appeal                                                                                               | 20-tägige Frist für Rechtsmittel gemäss Art. 56 BöB                                                             | Zu prüfen   | Suspensiveffekt                             |
| 36                        | Stillstandsfrist (Standstill Period)                                                                                  | Karenzfrist zwischen Zuschlag und Vertragsabschluss                                                             | Zu prüfen   |                                             |
| 37                        |                                                                                                                       | Zuschlagskriterien                                                                                              |             |                                             |
| 38                        | Preiskriterium (Price Criterion) Bewertung des Angebotspreises mit definierter                                        | Gewichtung                                                                                                      | Zu prüfen   |                                             |
| 39                        | Qualitätskriterium (Quality Criterion) Technische                                                                     | Güte, Zweckmässigkeit, Ästhetik gemäss Art. 29 BöB                                                              | Zu prüfen   |                                             |
| 40                        | Nachhaltigkeitskriterium (Sustainability Criterion)                                                                   | Ökologische, soziale und wirtschaftliche Nachhaltigkeit                                                         | Zu prüfen   | BBL-Strategie 2021-2030                     |
| 41                        | Innovationskriterium (Innovation Criterion)                                                                           | Bewertung innovativer Lösungsansätze                                                                            | Zu prüfen   |                                             |
| 42                        | Lebenszykluskosten (Life Cycle Costs)                                                                                 | Gesamtkostenbetrachtung über Nutzungsdauer                                                                      | Zu prüfen   |                                             |
| 43                        | Schwellenwerte Verfahren                                                                                              | und                                                                                                             |             |                                             |

| 44                             | Schwellenwert (Threshold)               | WTO/Staatsvertragsbereich oder Binnenbereich mit spezifischen Wertgrenzen    | Zu prüfen   | CHF 230'000 für Güter/DL         |
|--------------------------------|-----------------------------------------|------------------------------------------------------------------------------|-------------|----------------------------------|
| 45                             | Direktvergabe (Direct Award)            | Freihändige Vergabe unter Schwellenwert oder bei Ausnahmetatbestand          | Zu prüfen   | Begründungspflicht               |
| 46                             | Rahmenvertrag (Framework Agreement)     | Vereinbarung mit einem oder mehreren Anbietern für wiederkehrende Leistungen | Zu prüfen   | Max. 5 Jahre Laufzeit            |
| 47 Rechtsmittel und Compliance | 47 Rechtsmittel und Compliance          | 47 Rechtsmittel und Compliance                                               |             |                                  |
| 48                             | Beschwerde (Complaint)                  | Eingereichte Beschwerde gegen Vergabeentscheidung                            | Zu prüfen   | Bundesverwaltungsgericht         |
| 49                             | Ausschlussgrund (Exclusion Ground)      | Zwingender oder fakultativer Ausschluss gemäss Art. 44 BöB                   | Zu prüfen   | Selbstdeklaration prüfen         |
| 50                             | Sanktion (Sanction)                     | Verhängte Sanktionen bei Verstössen (Verwarnung, Ausschluss, Busse)          | Zu prüfen   | Art. 45 BöB                      |
| 51                             | Audit Trail                             | Unveränderliche Protokollierung aller Verfahrensschritte                     | Zu prüfen   | Revisionssicherheit              |
| 52                             | Reporting und Statistik                 |                                                                              |             |                                  |
| 53                             | Vergabestatistik (Award Statistics)     | Statistische Auswertung gemäss Art. 50 BöB                                   | Zu prüfen   | Jährliche Berichtspflicht        |
| 54                             | KMU-Statistik (SME Statistics)          | Anteil und Erfolgsquote von KMU in Vergabeverfahren                          | Zu prüfen   |                                  |
| 55                             | Verfahrensdauer (Procedure Duration)    | Durchschnittliche Dauer von Ausschreibung bis Zuschlag                       | Zu prüfen   | KPI für Effizienz                |
| 56                             | Beschwerdestatistik (Appeal Statistics) | Anzahl und Erfolgsquote von Beschwerden                                      | Zu prüfen   |                                  |
| 57                             | Schnittstellen und Integration          |                                                                              |             |                                  |
| 58                             | SIMAP-Integration                       | Bidirektionale Schnittstelle für Publikationen und Teilnehmerkommunikation   | Zu prüfen   | REST API v1.2, 2FA obligatorisch |
| 59                             | eIAM-Authentifizierung                  | SAML 2.0/OIDC Integration für Single Sign-On                                 | Zu prüfen   | FED-LOGIN für Bundesangestellte  |
| 60                             | GEVER-Schnittstelle                     | Dokumentenablage in Acta Nova für Vergabedossiers                            | Zu prüfen   | Métamorphose-Archivierung        |
| 61                             | SAP-Integration                         | Schnittstelle zu SAP S/4HANA für Bedarfsmeldungen und Budgetprüfung          | Zu prüfen   | RFC/OData Services               |
| 62                             | ZertES-Integration                      | Validierung qualifizierter elektronischer Signaturen                         | Zu prüfen   | Swisscom Trust Services          |
| 63                             | UID-Register                            | Validierung von Unternehmensidentifikationen                                 | Zu prüfen   | eCH-0097 Standard                |
| 64                             | CPV-Klassifikation                      | Integration des Common Procurement Vocabulary                                | Zu prüfen   | EU-Standard, SIMAP-Pflicht       |

Tabelle: Geschäftsobjekte BVML (Beschaffungs- und Vergabemanagementlösung)

## 3.21. MDG (Master Data Governance)

## Dokumentation:

- Finanzverwaltung, SuPro Übersicht MDG:  https://confluence.bit.admin.ch/x/t1E8Qw
- TBD

## Konzeptuelles Datenmodell:

|    | Geschäftsobjekt   | Beschreibung   | Geprüft   | Kommentar   |
|----|-------------------|----------------|-----------|-------------|
|  1 |                   |                |           |             |
|  2 |                   |                |           |             |
|  3 |                   |                |           |             |
|  4 |                   |                |           |             |
|  5 |                   |                |           |             |

Tabelle: Geschäftsobjekte

## 4. Externe Fachanwendungen / Geschäftsobjekte (Extern, BBL IMMO relevant)

Nicht im Scope von PI25

## 4.1. SIMAP (Beschaffungsplattform von Bund und bundesnahen Organisationen)

## Dokumentation:

- Webseite:  https://www.simap.ch/de

- REST API: https://www.simap.ch/api-doc/

## Konzeptuelles Datenmodell:

|                                     | Geschäftsobjekt (Original)                 | Geschäftsobjekt (Übersetzung)                                                                    | Beschreibung                                                        | Geprüft   |
|-------------------------------------|--------------------------------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|-----------|
| 1 Publikationen (Publications)      |                                            |                                                                                                  |                                                                     |           |
| 2 Publication                       | Publikation                                | Basiselement für alle Veröffentlichungen auf der Plattform mit Attributen wie id_simap, ob_code, | category, date, language_code                                       | OK        |
| 3 PubDraft                          | Publikationsentwurf                        | Entwurfsversion einer Publikation vor der Veröffentlichung mit Status (draft,                    | submitted, to_publish, published)                                   | OK        |
| 4 PublicationTender                 | Ausschreibung                              | Öffentliche                                                                                      | Ausschreibung mit offenen oder selektiven Verfahren                 | OK        |
| 5 PublicationAward                  | Zuschlag                                   | Vergabeentscheidung mit                                                                          | Zuschlagsinformationen                                              | OK        |
| 6 PublicationDirectAward            | Direktvergabe                              | Freihändige Vergabe ohne                                                                         | Ausschreibungsverfahren                                             | OK        |
| 7 PublicationCorrection             | Korrektur                                  |                                                                                                  | Berichtigung einer bestehenden Publikation                          | OK        |
| 8 PublicationRevocation             | Widerruf                                   |                                                                                                  | Widerruf einer Publikation                                          | OK        |
| 9 PublicationAbandonment            |                                            | Abbruch                                                                                          | Projektabbruch-Mitteilung                                           | OK        |
| 10 PublicationParticipantSelecti on |                                            | Teilnehmerauswahl                                                                                | Auswahl qualifizierter Bieter in selektiven Verfahren               | OK        |
| 11 Phase                            | PublicationSelectiveOffering Angebotsphase | (selektiv)                                                                                       | Angebotsphase im selektiven Verfahren                               | OK        |
| 12                                  | PublicationRfi                             | Informationsanfrage Request                                                                      | for Information (RFI)                                               | OK        |
| 13 PublicationCompetition           | Wettbewerb                                 |                                                                                                  | Planungs- und Projektwettbewerbe                                    | OK        |
| 14 PublicationStudyContract         |                                            | Studienauftrag                                                                                   | Studienverträge                                                     | OK        |
| 15 Projekt-Objekte                  |                                            |                                                                                                  |                                                                     |           |
| 16 Project                          | Projekt                                    |                                                                                                  | Übergeordnetes Beschaffungsprojekt mit projectId, type, status      | OK        |
| 17 ProjectHeader                    |                                            | Projektkopfdaten                                                                                 | Allgemeine Headerinformationen eines Projekts                       | OK        |
| 18                                  | ProjectDocument                            | Projektdokument                                                                                  | Dokumente zu einem Projekt mit Metadaten und Zugriffsberechtigungen | OK        |
| 19                                  | ProjectContributor                         | Projektmitarbeiter                                                                               | Beteiligte Personen am Projekt auf Beschaffungsstellenseite         | OK        |
| 20 Lot                              |                                            | Los                                                                                              | Teillos einer Ausschreibung mit lotId, lotTitle, lotDescription     | OK        |
| 21 Organisationen                   |                                            |                                                                                                  |                                                                     |           |
| 22 Institution                      |                                            | Institution                                                                                      | Hierarchische Struktur von Behörden und Organisationen              | OK        |
| 23 CompCentre                       |                                            | Kompetenzzentrum                                                                                 | Übergeordnete Verwaltungseinheit für mehrere Beschaffungsstellen    | OK        |
| 24 ProcOffice                       |                                            | Beschaffungsstelle                                                                               | Öffentliche Stelle, die Beschaffungen durchführt                    | OK        |
| 25 Vendor                           |                                            | Anbieter/Lieferant                                                                               | Unternehmen, die an Ausschreibungen teilnehmen                      | OK        |
| 26 Publisher                        |                                            | Herausgeber                                                                                      | Amtsblatt-Herausgeber für Publikationen                             | OK        |
| 27                                  |                                            |                                                                                                  |                                                                     |           |
| 28 User                             |                                            | Benutzer                                                                                         | Systembenutzer mit userId, email, firstName, lastName               | OK        |
| 29 Membership                       |                                            | Mitgliedschaft                                                                                   | Zugehörigkeit zu Organisationen mit Rollen und Status               | OK        |
| 30 Role                             | Rolle                                      |                                                                                                  | Benutzerrolle (vendor_admin, vendor_user, procurement_admin, etc.)  | OK        |
| 31 Impersonate                      |                                            | Stellvertretung                                                                                  | Funktion für Support zur temporären Übernahme einer Benutzerrolle   | OK        |
| 32 Adress- und                      | Kontaktdaten                               |                                                                                                  |                                                                     |           |
| 33 Address                          |                                            | Adresse                                                                                          | Strukturierte Adressdaten mit Strasse, PLZ, Ort, Kanton, Land       | OK        |
| 34 Contact                          |                                            | Kontakt                                                                                          | Kontaktinformationen mit Name, E-Mail, Telefon                      | OK        |
| 35                                  | InternationalPhoneNumber                   | Internationale Telefonnummer                                                                     | Telefonnummer mit Ländercode                                        | OK        |
| 36 Dokumente und                    | Dateien                                    |                                                                                                  |                                                                     |           |
| 37 Document                         |                                            | Dokument                                                                                         | Basisdokument mit Metadaten                                         | OK        |
| 38 VendorDocument                   |                                            | Anbieterdokument                                                                                 | Wiederverwendbare Dokumente eines Anbieters                         | OK        |
| 39                                  | VendorDigitalSubmission Digitale           | Angebotsabgabe                                                                                   | Elektronische Einreichung von Angeboten                             | OK        |
| 40 VendorDigitalSubmissionDoc ument | Digitales                                  | Angebotsdokument                                                                                 | Dokumente einer digitalen Angebotsabgabe                            | OK        |
| 41 DownloadToken                    |                                            | Download-Token                                                                                   | Zeitlich begrenzter Zugriffsschlüssel für Dokumentdownloads         | OK        |
| 42 Fragen und                       | Antworten                                  |                                                                                                  |                                                                     |           |
| 43 QnaRound                         | Fragerunde                                 |                                                                                                  | Organisationseinheit für Q&A mit roundId, state, deadline           | OK        |
| 44 Qna                              |                                            | Frage-Antwort-Paar                                                                               | Einzelne Frage mit Antwort und Status                               | OK        |
| 45 Question                         |                                            | Frage                                                                                            | Fragentext mit Zeitstempel und Fragensteller (anonymisiert)         | OK        |
| 46 Nachrichten und Kommunikation    |                                            |                                                                                                  |                                                                     |           |
| 47 Message                          |                                            | Nachricht                                                                                        | Nachrichten zwischen Beschaffungsstelle und Anbietern               | OK        |
| 48                                  | InvolvedVendor                             | Beteiligter Anbieter                                                                             | Anbieter mit Interesse oder Einladung zu einem Projekt              | OK        |
| 49                                  | InvolvedVendorMessage                      | Anbieternachricht                                                                                | Spezifische Nachricht an beteiligte Anbieter                        | OK        |

| 50                                 | Subscription Abonnement       | Suchabo für automatische Benachrichtigungen                      | OK   |
|------------------------------------|-------------------------------|------------------------------------------------------------------|------|
| 51 Beschaffungsspezifische Objekte |                               |                                                                  |      |
| 52 Procurement                     | Beschaffung                   | Beschaffungsinformationen mit Art, Umfang, CPV-Codes             | OK   |
| 53 Criteria                        | Kriterien                     | Zuschlagskriterien und Eignungskriterien                         | OK   |
| 54 QualificationCriterion          | Eignungskriterium             | Anforderungen an Bieter                                          | OK   |
| 55 AwardCriterion                  | Zuschlagskriterium            | Bewertungskriterien mit Gewichtung                               | OK   |
| 56 Terms                           | Bedingungen                   | Vertragsbedingungen und rechtliche Anforderungen                 | OK   |
| 57 RemediesNotice                  | Rechtsmittelbelehrung         | Information über Einspruchsmöglichkeiten                         | OK   |
| 58 Termine und                     | Fristen                       |                                                                  |      |
| 59 Dates                           | Termine                       | Strukturierte Terminangaben für Publikationen                    | OK   |
| 60 PublicationDate                 | Publikationsdatum             | Geplantes oder tatsächliches Veröffentlichungsdatum              | OK   |
| 61 Deadline                        | Frist                         | Eingabefristen für Angebote oder Fragen                          | OK   |
| 62 Appointment                     | Termin                        | Begehungen, Präsentationen oder andere Termine                   | OK   |
| 63 Codes und Klassifikationen      |                               |                                                                  |      |
| 64 CPVCode                         | CPV-Code                      | Common Procurement Vocabulary (8-stellig)                        | OK   |
| 65 CPCCode                         | CPC-Code                      | Central Product Classification                                   | OK   |
| 66 BKPCode                         | BKP-Code                      | Baukostenplan-Codes                                              | OK   |
| 67 NPKCode                         | NPK-Code                      | Normpositionen-Katalog                                           | OK   |
| 68 EBKPHCode                       | eBKP-H Code                   | Elementbasierter Baukostenplan Hochbau                           | OK   |
| 69 EBKPTCode                       | eBKP-T Code                   | Elementbasierter Baukostenplan Tiefbau                           | OK   |
| 70 OAGCode                         | OAG-Code                      | Objektarten-Gliederung                                           | OK   |
| 71 Referenzdaten                   |                               |                                                                  |      |
| 72 Canton                          | Kanton                        | Schweizer Kantone mit Code und Name                              | OK   |
| 73 Country                         | Land                          | Länder mit ISO-Code                                              | OK   |
| 74 Language                        | Sprache                       | Systemsprachen (de, fr, it, en)                                  | OK   |
| 75 MainActivity                    | Haupttätigkeit                | TED-Aktivitätskategorien (GENERAL_PUBLIC_SERVICES, HEALTH, etc.) | OK   |
| 76 Currency                        | Währung                       | Währungsangaben (CHF, EUR)                                       | OK   |
| 77 Preise und Werte                |                               |                                                                  |      |
| 78 Price                           | Preis                         | Preisangaben mit Währung und Präzision                           | OK   |
| 79 PriceWithVat                    | Preis mit MwSt                | Preis inklusive Mehrwertsteuer mit VatType                       | OK   |
| 80 PriceRange                      | Preisspanne                   | Minimaler und maximaler Preis                                    | OK   |
| 81 TotalPrice                      | Gesamtpreis                   | Aggregierte Preisangaben                                         | OK   |
| 82 Protokolle und Historie         |                               |                                                                  |      |
| 83 ParticipationProtocol           | Teilnahmeprotokoll            | Protokoll der eingegangenen Teilnahmeanträge                     | OK   |
| 84 OfferProtocol                   | Angebotsprotokoll             | Protokoll der eingegangenen Angebote                             | OK   |
| 85 BaseHistory                     | Basis-Historie                | Grundlegende Historieninformationen mit Zeitstempel              | OK   |
| 86 PublicationHistory              | Publikationshistorie          | Verlauf der Publikationen eines Projekts                         | OK   |
| 87 Vorlagen                        |                               |                                                                  |      |
| 88 PubDraftTemplate                | Publikationsvorlage           | Wiederverwendbare Vorlagen für Publikationen                     | OK   |
| 89 RemediesNoticeTemplate          | Rechtsmittelvorlage           | Vorlagen für Rechtsmittelbelehrungen                             | OK   |
| 90 Validierung                     |                               |                                                                  |      |
| 91 ValidationError                 | Validierungsfehler            | Fehler bei der Validierung von Entwürfen                         | OK   |
| 92 ValidationResults               | Validierungsergebnisse        | Gesammelte Ergebnisse einer Validierung                          | OK   |
| 93 Nachhaltigkeit                  |                               |                                                                  |      |
| 94 SustainabilityForm              | Nachhaltigkeitsformular       | Erfassung von Nachhaltigkeitsaspekten bei Vergaben               | OK   |
| 95 SustainabilityFormType          | Nachhaltigkeitsformulartyp    | Verschiedene Typen von Nachhaltigkeitsformularen                 | OK   |
| 96 Statistiken                     |                               |                                                                  |      |
| 97 WTOStatistics                   | WTO-Statistik                 | Statistische Auswertungen für WTO-Berichterstattung              | OK   |
| 98 AwardedVendorExport             | Export zugeschlagene Anbieter | Exportdaten der Zuschlagsempfänger                               | OK   |
| 99 CallForBidsExport               | Export Ausschreibungen        | Exportdaten der Ausschreibungen                                  | OK   |
| 100 TED-Integration                |                               |                                                                  |      |
| 101 TedStatus                      | TED-Status                    | Status der Übermittlung an TED (Tenders Electronic Daily)        | OK   |
| 102 TedReference                   | TED-Referenz                  | Referenznummer von TED für übermittelte Publikationen            | OK   |
| 103 Sonstige                       |                               |                                                                  |      |

|   104 | WizardState   | Wizard-Status      | Fortschrittsstatus im Erstellungsassistenten     | OK   |
|-------|---------------|--------------------|--------------------------------------------------|------|
|   105 | Translation   | Übersetzung        | Mehrsprachige Texte und Übersetzungen            | OK   |
|   106 | Weekdays      | Wochentage         | Wochentagsangaben für regelmässige Publikationen | OK   |
|   107 | CompanySize   | Unternehmensgrösse | Klassifikation der Unternehmensgrösse            | OK   |
|   108 | LegalFormCode | Rechtsformcode     | Code für die Rechtsform von Unternehmen          | OK   |

Tabelle: Geschäftsobjekte SIMAP

## 4.2. Kantonale Amtliche Vermessung (Schweiz)

## Dokumentation:

- Amtliche Vermessung Schweiz (Swisstopo): https://www.swisstopo.admin.ch/de/amtliche-vermessung
- Webseite:  https://www.geodienste.ch/services/av
- Datenmodell:  Fachanwendung - Empfehlung-AV-WMS-mit-Anhaengen.pdf
- Aktuell in Bearbeitung

## Konzeptuelles Datenmodell:

|    | Gruppe                      | Geschäftsobjekt (Feature)               | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Geprüft   |
|----|-----------------------------|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Bodenbedeckung_projekti ert | ProjBodenbedeckung (LCSFPROJ)           | Land cover surface project / Projektierte Bodenbedeckungsflächen (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | OK        |
|  2 | Bodenbedeckung              | Bodenbedeckung (LCSF)                   | 1. a. b. c. d. 2. a. b. c. 3. a. b. c. 4. a. b. c. d. 5. a. b. c. Land cover surface / Rechtsgültige Bodenbedeckungsflächen (Polygon) Ausprägung: Gebäude (TVAV Art. 14): Auf Dauer angelegte, mit dem Boden fest verbundene überdachte Bauten Definiert durch Hauptfassadenteile Muss einem bestimmten Zweck dienen Mindestfläche 6m² gemäss kantonaler Verordnung Befestigte Flächen (TVAV Art. 15): Künstlich hergerichtete Flächen Inkludiert: asphaltierte, betonierte, bekieste, gemergelte oder mit Steinen/Platten belegte Flächen Beispiele: Strassen, Trottoirs, Bahnanlagen, Flugplätze, Wasserbecken Humusierte Flächen (TVAV Art. 16): Gewachsener Boden ohne bestockte Flächen Umfasst: Acker/Wiese/Weide, Intensivkulturen, Gartenanlagen Inkludiert auch Grünstreifen bei Verkehrsanlagen oder Bachborde Bestockte Flächen (TVAV Art. 18): Basiert auf Waldgesetz (WaG Art. 2) Umfasst Wald und waldartige Flächen Inkludiert: geschlossener Wald, Wytweide, übrige bestockte Flächen Mindestbreite 12m und Mindestfläche 800m² gemäss kantonalem Waldgesetz Vegetationslose Flächen (TVAV Art. 19): Land- und forstwirtschaftlich nicht nutzbare Flächen Beispiele: Fels, Geröll, Sand, Abbauflächen, Deponien Inkludiert auch Übergangszonen bei der klimatischen Pflanzengrenze | OK        |
|  3 | Bodenbedeckung              | Bodenbedeckung farbig (LCSFC)           | Land cover surface / Rechtsgültige Bodenbedeckungsflächen (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | OK        |
|  4 | Bodenbedeckung              | BB_Nummern_Namen (LCOBJ)                | House numbers and Names / Gebäudenummern und Namen (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | OK        |
|  5 | Einzelobjekte               | Einzelobjekte (Flaechen) (SOSF)         | Single objects surface elements / Einzelobjekte Flächenelemente (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | OK        |
|  6 | Einzelobjekte               | Einzelobjekte farbig (Flaechen) (SOSFC) | Single objects surface elements / Einzelobjekte Flächenelemente (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | OK        |
|  7 | Einzelobjekte               | Einzelobjekte (Linien) (SOLI)           | Single objects linear elements / Einzelobjekte Linienelemente (Polyline)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | OK        |
|  8 | Einzelobjekte               | Einzelobjekte (Punkte) (SOPT)           | Single objects point elements / Einzelobjekte Punktelemente (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | OK        |
|  9 | Einzelobjekte               | EO_Nummern_Namen (SOOBJ)                | Numbers and Names / Nummern und Namen (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | OK        |
| 10 | Nomenklatur                 | Nomenklaturnamen (LNNA)                 | Local names and place name / Namen der Flur-, Gelände- und Ortsnamen (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | OK        |
| 11 | Liegenschaften_projektiert  | ProjLiegenschaften (RESFPROJ)           | Real estate project / Projektierte Liegenschaften (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | OK        |
| 12 | Liegenschaften_projektiert  | ProjSDRechte (DPRSFPROJ)                | DPR and mine project / Projektierte Selbständige Rechte und Bergwerke (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | OK        |
| 13 | Liegenschaften_projektiert  | ProjLiegenschaftsnummern (OSNRPROJ)     | Ownership numbers project / Nummern der proj. Liegenschaften, SDR, etc. (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | OK        |
| 14 | Liegenschaften              | Grenzpunkte (OSBP)                      | Boundary points / Grenzpunkte (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | OK        |
| 15 | Liegenschaften              | Liegenschaften (RESF)                   | Real estate / Rechtsgültige Liegenschaften (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | OK        |
| 16 | Liegenschaften              | SDRechte (DPRSF)                        | DPR and mine / Rechtsgültige SDR und Bergwerke (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | OK        |
| 17 | Liegenschaften              | Liegenschaftsnummern (OSNR)             | Ownership numbers / Nummern der rechtsgültigen Liegenschaften, SDR, etc. (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | OK        |
| 18 | Rohrleitungen               | Rohrleitungen (Flaechen) (PLSF)         | Pipelines surface elements / Rohrleitungen Flächenelemente (Polygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | OK        |
| 19 | Rohrleitungen               | Rohrleitungen (Linien) (PLLI)           | Pipelines linear elements / Rohrleitungen Linienelemente (Polyline)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | OK        |
| 20 | Rohrleitungen               | Rohrleitungsbeschriftung (PLNA)         | Pipeline labels / Beschriftungen der Rohrleitungen (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | OK        |
| 21 | Hoheitsgrenzen              | Hoheitsgrenzpunkte (TBBP)               | Boundary territorial points / Hoheitsgrenzpunkte (Point)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | OK        |

|   22 | Hoheitsgrenzen   | Gemeindegrenzen (MBSF)        | Municipal boundary / Gemeindegrenzen (Polygon)                 | OK   |
|------|------------------|-------------------------------|----------------------------------------------------------------|------|
|   23 | Hoheitsgrenzen   | Hoheitsgrenzabschnitte (TBLI) | Other Territorial boundary / Andere Grenzabschnitte (Polyline) | OK   |
|   24 | Gebaeudeadressen | Lokalisationen (LOCPOS)       | Locality labels / Beschriftung der Lokalisationen (Point)      | OK   |
|   25 | Gebaeudeadressen | Gebaeudeadressen (HADR)       | House addresses / Gebaeudeadressen (Point)                     | OK   |

Tabelle: Geschäftsobjekte Kantonale Amtliche Vermessung

## BFS E Gebäude- und Wohnungsregister GWR (Schweiz) 4.3. idgenössische

## Dokumentation:

- Webseite:  https://www.housing-stat.ch/

- Merkmalkatalog:  https://www.housing-stat.ch/de/docs/index.html

## Konzeptuelles Datenmodell:

<!-- image -->

Bild: Datenmodell GWR. https://www.housing-stat.ch/de/docs/index.html

|    | Geschäftsobjekt   | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Geprüft   |
|----|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Erhebungsstelle   | Das BFS teilt den kommunalen oder kantonalen Amtsstellen, die für die Bautätigkeit und für die Aktualisierung des eidg. GWR zuständig sind, eine Erhebungsstellennummer (PESTNR) zu. Jede Erhebungsstelle gibt eine zuständige Kontaktperson an.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | OK        |
|  2 | Bauprojekt        | Ein Bauprojekt ist ein Objekt, für das ein Baubewilligungsgesuch nach Artikel 22 des Bundesgesetzes vom 22. Juni 1979 über die Raumplanung (SR 700) erforderlich ist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | OK        |
|  3 | Arbeiten          | Gestützt auf Artikel 10 Absatz 1 der Verordnung über das eidgenössische Gebäude- und Wohnungsregister (VGWR) führen die zuständigen Stellen laufend alle Informationen zu den Merkmalen der Entität "Arbeiten" im eidg. GWR nach. Die Art der Arbeiten (Neubau, Umbau oder Abbruch) muss für jedes Gebäude eines Bauprojekts angegeben werden. Neubau bedeutet die vollständige Errichtung eines neuen Gebäudes. Abbruch hingegen den kompletten Abbruch eines bestehenden Gebäudes. Alle übrigen Arbeiten werden als Umbau bezeichnet und umfassen die Vergrösserung oder den Teilabbruch eines bestehenden Gebäudes. Wenn es sich um einen Umbau handelt, muss die Art des Umbaus präzisiert werden. | OK        |
|  4 | Gebäude           | Ein Gebäude ist ein auf Dauer angelegter, mit einem Dach versehener, mit dem Boden fest verbundener Bau, der Personen aufnehmen kann und zu Wohnzwecken oder Zwecken der Arbeit, der Ausbildung, der Kultur, des Sports oder jeglicher anderer menschlicher Tätigkeit dient; ein Doppel-, Gruppen- und Reihenhaus zählt ebenfalls als ein Gebäude, wenn es einen eigenen Zugang von aussen hat und wenn zwischen den Gebäuden eine senkrechte vom Erdgeschoss bis zum Dach reichende tragende Trennmauer besteht.                                                                                                                                                                                      | OK        |

Abbildung

2

Konzeptionelles

Datenmodell.

Datenmode D und B esch chreibung Entitaten der

|   5 | Gebäudeeingang   | Gebäudeeingang: Zugang von aussen in ein Gebäude; der Eingang ist durch eine Gebäudeadresse identifiziert. Gebäudeadresse: Adressierungsangaben nach Art. 26b der Verordnung vom 21. Mai 2008 über die geografischen Namen (GeoNV) und die Koordinaten des Gebäudeeingangs.                                                                                                                                                  | OK   |
|-----|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
|   6 | Wohnung          | 1. 2. 3. 4. 5. 6. Die Wohnung ist im eidg. GWR entsprechend Art. 2 des Zweitwohnungsgesetzes definiert: Eine Wohnung ist eine Gesamtheit von Räumen, die: für eine Wohnnutzung geeignet sind; eine bauliche Einheit bilden; einen Zugang entweder von aussen oder von einem gemeinsam mit anderen Wohnungen genutzten Bereich innerhalb des Gebäudes haben; über eine Kocheinrichtung verfügen; und keine Fahrnis darstellen | OK   |
|   7 | Grundstück       |                                                                                                                                                                                                                                                                                                                                                                                                                              | OK   |
|   8 | Strasse          | Als Strasse gilt ein Verkehrsweg für Personen oder Fahrzeuge innerhalb oder ausserhalb eines Ortes.                                                                                                                                                                                                                                                                                                                          | OK   |

Tabelle: Geschäftsobjekte BFS E idgenössische Gebäude- und Wohnungsregister GWR

## 4.4. Swisstopo APIs (Schweiz)

## Dokumentation:

- Übersicht Modelle und Anwendungen Swisstopo:  https://www.swisstopo.admin.ch/de/modelle-und-anwendungen
- API Dokumentation:  https://api3.geo.admin.ch/services/sdiservices.html
- Verfügbare VMTS Layer: https://api3.geo.admin.ch/api/faq/index.html#which-layers-have-a-tooltip

## Konzeptuelles Datenmodell:

|    | VMTS Layer                                                   | Beschreibung                              | Relevanz für BBL IMMO                               | Geprüft   |
|----|--------------------------------------------------------------|-------------------------------------------|-----------------------------------------------------|-----------|
|  1 | Gebäude und Adressen                                         |                                           |                                                     |           |
|  2 | ch.swisstopo.amtliches-gebaeudeadressverzeichnis (670)       | Amtliches Gebäudeadressverzeichnis        | Offizielle Gebäudeadressen für Stammdatenverwaltung | OK        |
|  3 | ch.bfs.gebaeude_wohnungs_register (548)                      | Eidg. Gebäude- und Wohnungsregister (GWR) | Gebäudestatus und -informationen                    | OK        |
|  4 | ch.bfs.gebaeude_wohnungs_register_waermequelle_heizung (549) | GWR: Energiequelle Heizung                | Heizungstypen für Energiemanagement                 | OK        |
|  5 | Kataster und Vermessung                                      |                                           |                                                     |           |
|  6 | ch.kantone.cadastralwebmap-farbe (595)                       | Amtliche Vermessung (Kataster)            | Grundstücksgrenzen und Eigentumsverhältnisse        | OK        |
|  7 | ch.swisstopo-vd.amtliche-vermessung (661)                    | OpenData Amtliche Vermessung              | Parzellengrenzen und Grundbuchinformationen         | OK        |
|  8 | ch.swisstopo-vd.stand-oerebkataster (669)                    | Verfügbarkeit ÖREB-Kataster               | Öffentlich-rechtliche Eigentumsbeschränkungen       | OK        |
|  9 | Zonenpläne und Raumplanung                                   |                                           |                                                     |           |
| 10 | ch.are.bauzonen (12)                                         | Bauzonen Schweiz (harmonisiert)           | Nutzungszonen für Entwicklungspotenzial             | OK        |
| 11 | ch.blw.landwirtschaftliche-zonengrenzen (585)                | Landwirtschaftliche Zonengrenzen          | Einschränkungen für Umnutzungen                     | OK        |
| 12 | Verkehr und Infrastruktur                                    |                                           |                                                     |           |
| 13 | ch.bav.haltestellen-oev (433)                                | Haltestellen öffentlicher Verkehr         | ÖV-Anbindung der Liegenschaften                     | OK        |
| 14 | ch.astra.hauptstrassennetz (30)                              | Hauptstrassennetz                         | Verkehrsanbindung                                   | OK        |
| 15 | Energie und Nachhaltigkeit                                   |                                           |                                                     |           |
| 16 | ch.bfe.solarenergie-eignung-daecher (525)                    | Solarenergie: Eignung Dächer              | Potenzial für Photovoltaikanlagen                   | OK        |
| 17 | ch.bfe.solarenergie-eignung-fassaden (526)                   | Solarenergie: Eignung Fassaden            | Potenzial für Fassaden-PV                           | OK        |
| 18 | ch.bfe.fernwaerme-angebot (500)                              | Fernwärme-Angebot                         | Anschlussmöglichkeiten Fernwärme                    | OK        |
| 19 | ch.bfe.thermische-netze (532)                                | Thermische Netze                          | Wärme-/Kälteversorgung                              | OK        |
| 20 | Naturgefahren                                                |                                           |                                                     |           |
| 21 | ch.bafu.gefahren-basiskarte (115)                            | Naturgefahren Basiskarte                  | Gefährdung durch Naturereignisse                    | OK        |
| 22 | ch.bafu.gefaehrdungskarte-oberflaechenabfluss (113)          | Oberflächenabfluss                        | Überschwemmungsrisiko                               | OK        |
| 23 | ch.bafu.gefahren-gefaehrdungszonen (117)                     | Erdbebenzonen nach SIA 261                | Gefährdungszonen für Bemessung nach SIA-Norm        | OK        |
| 24 | ch.bafu.gefahren-baugrundklassen (116)                       | Seismische Baugrundklassen                | Baugrundklassifikation für Erdbebenauslegung        | OK        |
| 25 | ch.bafu.gefahren-spektral (119)                              | Spektrale Mikrozonierung                  | Detaillierte lokale Verstärkungseffekte             | OK        |
| 26 | ch.bafu.gefahren-aktuelle_erdbeben (114)                     | Aktuelle Erdbeben                         | Monitoring aktueller seismischer Aktivität          | OK        |
| 27 | ch.bafu.gefahren-historische_erdbeben (118)                  | Historische Erdbeben                      | Historische Erdbebenaktivität                       | OK        |
| 28 | Schutzgebiete und Auflagen                                   |                                           |                                                     |           |
| 29 | ch.bafu.bundesinventare-bln (77)                             | Bundesinventar Landschaften (BLN)         | Landschaftsschutz-Auflagen                          | OK        |
| 30 | ch.bak.bundesinventar-schuetzenswerte-ortsbilder (378)       | ISOS - Ortsbildschutz                     | Denkmalschutz-Auflagen                              | OK        |
| 31 | Administrative Grenzen                                       |                                           |                                                     |           |

|   32 | ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill (783)   | Gemeindegrenzen              | Administrative Zuordnung            | OK   |
|------|--------------------------------------------------------------|------------------------------|-------------------------------------|------|
|   33 | ch.swisstopo.swissboundaries3d-kanton-flaeche.fill (784)     | Kantonsgrenzen               | Kantonale Zuständigkeiten           | OK   |
|   34 | Luftbilder und Karten                                        |                              |                                     |      |
|   35 | ch.swisstopo.lubis-luftbilder_farbe (765)                    | Luftbilder swisstopo (Farbe) | Aktuelle Luftaufnahmen              | OK   |
|   36 | ch.swisstopo.swissimage-product (789)                        | SWIssIMAGE Zeitreise         | Historische Entwicklung von Arealen | OK   |

Tabelle: Übersicht relevante VMTS Layer

## 4.5. Grundbuch (Schweiz)

## Dokumentation:

- Projekt eGRIS: https://www.egris.admin.ch/de
- eCH Fachgruppe Objektwesen: https://www.ech.ch/de/der-verein/fachgruppen/objektwesen
- eCH-0153 eGRISDM (Konzeptuelles Datenmodell Grundbuch):  https://www.ech.ch/de/ech/ech-0153/1.0

## Konzeptuelles Datenmodell:

|    | Konzept                                 | Typ                  | Beschreibung                                                                                                                                                                                                                                                                     | Geprüft   |
|----|-----------------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Hauptbuch                               | Geschäf tsobjekt     | Das Hauptbuch ist die Gesamtheit aller Daten über die rechtswirksamen und die gelöschten dinglichen Rechte, Vormerkungen und Anmerkungen an den im Grundbuch aufgenommenen Grundstücken. Hier erfolgen die Eintragungen der Rechte und der beteiligten Grundstücke und Personen. | OK        |
|  2 | Tagebuch                                | Geschäf tsobjekt     | Das Tagebuch ist ein chronologisches Protokoll über die Behandlung der Geschäftsfälle. Anmeldungen für Neueinträge, Änderungen oder Löschungen von Einträgen werden hier chronologisch nach ihrem Eintreffen im Grundbuchamt festgehalten.                                       | OK        |
|  3 | Grundstück                              | Geschäf tsobjekt     | Grundstücke sind unbewegliche Sachen (Immobilien). Es gibt vier Arten von Grundstücken: Liegenschaften, selbständige und dauernde Rechte (SDR), Miteigentumsanteile an Grundstücken und Bergwerke.                                                                               | OK        |
|  4 | Liegenschaft                            | Geschäf tsobjektt yp | Eine Liegenschaft ist eine Bodenfläche mit genügend bestimmter Grenze. Typ von Grundstück.                                                                                                                                                                                       | OK        |
|  5 | Selbständiges und dauerndes Recht (SDR) | Geschäf tsobjektt yp | Eine Grundstücksart, die in der Regel als Voraussetzung eine Dienstbarkeit hat, die das Recht definiert. Typ von Grundstück.                                                                                                                                                     | OK        |
|  6 | Miteigentumsanteil                      | Geschäf tsobjektt yp | Eine Grundstücksart, die weiter in "Stockwerkseinheit" und "Gewöhnliches Miteigentum" unterteilt wird. Typ von Grundstück.                                                                                                                                                       | OK        |
|  7 | Bergwerk                                | Geschäf tsobjektt yp | Eine Grundstücksart, ähnlich einem SDR, das aber keine Dienstbarkeit als Voraussetzung hat. Typ von Grundstück.                                                                                                                                                                  | OK        |
|  8 | Recht                                   | Geschäf tsobjekt     | Eine allgemeine Klasse für im Grundbuch eingetragene Rechte. Es gibt sechs Arten: Eigentum, Dienstbarkeiten, Grundlasten, Grundpfandrechte, Vormerkungen und Anmerkungen. Ein Recht belastet jeweils ein oder mehrere Grundstücke.                                               | OK        |
|  9 | Eigentum(santeil)                       | Geschäf tsobjektt yp | Ein Eigentumsanteil beschreibt den Anteil, den ein Eigentümer an einem Grundstück hat. Die Eigentumsformen sind Alleineigentum, Miteigentum und Gesamteigentum. Typ von Recht.                                                                                                   | OK        |
| 10 | Dienstbarkeit                           | Geschäf tsobjektt yp | Jede Verpflichtung zu einem Dulden oder Unterlassen kann Inhalt einer Dienstbarkeit sein, z.B. ein Fusswegrecht. Typ von Recht.                                                                                                                                                  | OK        |
| 11 | Grundlast                               | Geschäf tsobjektt yp | Im Gegensatz zu einer Dienstbarkeit kann eine Grundlast den Eigentümer des belasteten Grundstücks zu einer Leistung verpflichten (z. B. eine Lieferpflicht). Typ von Recht.                                                                                                      | OK        |
| 12 | Grundpfandrecht                         | Geschäf tsobjektt yp | Ein Grundpfandrecht beschreibt eine pfandgesicherte persönliche Forderung. Das belastete Grundstück dient dem Gläubiger als Sicherheit. Typ von Recht.                                                                                                                           | OK        |
| 13 | Vormerkung                              | Geschäf tsobjektt yp | Eine Vormerkung verstärkt die Wirkung eines persönlichen Rechtsverhältnisses oder Anspruchs gegenüber Dritten, z.B. ein Mietvertrag. Typ von Recht.                                                                                                                              | OK        |
| 14 | Anmerkung                               | Geschäf tsobjektt yp | Eine Anmerkung ist ein Hinweis auf eine Verpflichtung im Zusammenhang mit einem spezifischen Grundstück, deren Rechtswirkung nicht vom Grundbucheintrag abhängt (z.B. eine Denkmalschutzauflage). Typ von Recht.                                                                 | OK        |
| 15 | PersonGB                                | Geschäf tsobjekt     | Eine allgemeine Klasse für Personendaten aus Sicht des Grundbuchs. Es gibt vier Arten: natürliche Personen, juristische Personen, vermögensfähige Gesellschaften (wie Kollektiv- und Kommanditgesellschaften) und Gemeinschaften.                                                | OK        |
| 16 | Natürliche PersonGB                     | Geschäf tsobjektt yp | Eine Personenart für Menschen. Typ von PersonGB.                                                                                                                                                                                                                                 | OK        |
| 17 | Juristische PersonGB                    | Geschäf tsobjektt yp | Eine Personenart für juristische Personen und vermögensfähige Gesellschaften. Typ von PersonGB.                                                                                                                                                                                  | OK        |
| 18 | Gemeinschaft                            | Geschäf tsobjektt yp | Eine Personenart, die sich dadurch auszeichnet, dass die Mitglieder nur zusammen entscheiden können. Typ von PersonGB.                                                                                                                                                           | OK        |
| 19 | Anmeldung                               | Geschäf tsobjekt     | Ein Antrag an das Grundbuch, um etwas einzutragen, zu verändern oder zu löschen. Zu einer Anmeldung gehören auch Dokumente (Rechtsgrundausweise), mit denen die Änderungen rechtlich begründet werden.                                                                           | OK        |

Tabelle: Übersicht Konzepte Grundbuch (eGRISDM)

## 4.6. BFS Betriebs- und Unternehmensregister (Schweiz)

## Dokumentation:

- Webseite: https://www.bfs.admin.ch/bfs/de/home/register/unternehmensregister.html
- Unternehmensstammdaten: https://www.bfs.admin.ch/bfs/de/home/register/unternehmensregister/betriebs-unternehmensregister.assetdetail. 20884598.html

## Konzeptuelles Datenmodell:

|    | Konzept                    | Typ              | Beschreibung                                                                                                          | Kommentar                                                                                                     | Geprüft   |
|----|----------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------|
|  1 | Rechtliche Einheit         | Geschäfts objekt | Juristische oder natürliche Person, die als wirtschaftliche Einheit identifiziert wird. Oberste Ebene im Datenmodell. | Entspricht der UID-Einheit gemäss UIDG. Kann Einzelunternehmen oder Teil eines Mehrbetriebsunternehmens sein. | OK        |
|  2 | Unternehmen                | Geschäfts objekt | Organisatorische Einheit, die eine oder mehrere rechtliche Einheiten umfasst und wirtschaftliche Aktivitäten ausübt.  | Verbindet rechtliche Einheiten mit ihren Betrieben. Wichtig für Mehrbetriebsunternehmen.                      | OK        |
|  3 | Örtliche Einheit (Betrieb) | Geschäfts objekt | Physischer Standort, an dem wirtschaftliche Aktivitäten ausgeübt werden.                                              | Kann Hauptsitz, Zweigniederlassung oder Nebenbetrieb sein.                                                    | OK        |
|  4 | UID                        | Attribut         | Unternehmens-Identifikationsnummer - eindeutiger, nichtsprechender Identifikator                                      | Zentrale ID für rechtliche Einheiten, gesetzlich in UIDG verankert                                            | OK        |
|  5 | ENTID                      | Attribut         | Nichtsprechende Identifikationsnummer des Unternehmens                                                                | Verknüpft Unternehmensstrukturen im BUR                                                                       | OK        |
|  6 | BURNR                      | Attribut         | Nichtsprechende Identifikationsnummer des Betriebs                                                                    | Eindeutige ID für jeden Betriebsstandort                                                                      | OK        |
|  7 | Firma/Name                 | Attribut         | Offizielle Bezeichnung des Unternehmens oder Betriebs                                                                 | Aus Handelsregister oder anderen amtlichen Quellen                                                            | OK        |
|  8 | Adresse                    | Attribut         | Standortadresse (Sitz/Wohnsitz für Unternehmen, physische Adresse für Betriebe)                                       | Inkl. Gemeindenummer gemäss amtlichem Gemeindeverzeichnis                                                     | OK        |
|  9 | Rechtsform                 | Attribut         | Rechtliche Form des Unternehmens (AG, GmbH, Einzelfirma, etc.)                                                        | Gemäss Handelsregister-Klassifikation                                                                         | OK        |
| 10 | NOGA-Code                  | Attribut         | Art der wirtschaftlichen Tätigkeit gemäss Allgemeiner Systematik der Wirtschaftszweige                                | Hierarchische Klassifikation der Wirtschaftstätigkeit                                                         | OK        |
| 11 | Anzahl Beschäftigte        | Attribut         | Zahl der beschäftigten Personen nach Geschlecht und Beschäftigungsgrad                                                | Basis für Grössenklassen-Klassifikation                                                                       | OK        |
| 12 | Statusangaben              | Attribut         | Aktivitätsstatus (aktiv, in Liquidation, gelöscht, etc.)                                                              | Wichtig für Aktualität der Daten                                                                              | OK        |
| 13 | HR-Status                  | Attribut         | Status und Daten des Eintrags/Löschung im Handelsregister                                                             | Verknüpfung zum Handelsregister                                                                               | OK        |
| 14 | MWST-Status                | Attribut         | Status im Mehrwertsteuerregister mit Beginn/Ende der Steuerpflicht                                                    | Verknüpfung zur Steuerverwaltung                                                                              | OK        |
| 15 | Gebäudekoordin aten        | Attribut         | EGID und geografische Koordinaten des Standorts                                                                       | Verknüpfung zum Gebäude- und Wohnungsregister (GWR)                                                           | OK        |
| 16 | Unternehmensst ruktur      | Attribut         | Kennzeichnung als Einzelbetrieb, Hauptsitz oder Nebenbetrieb                                                          | 99% sind Einzelbetriebe, 1% Mehrbetriebsunternehmen                                                           | OK        |
| 17 | gehört zu                  | Relation         | Verknüpfung Betrieb Unternehmen                                                                                       | Hierarchische Zuordnung der Betriebe                                                                          | OK        |
| 18 | kontrolliert               | Relation         | Verknüpfung Rechtliche Einheit Unternehmen                                                                            | Eigentumsverhältnisse                                                                                         | OK        |
| 19 | REF-ENT Nummer             | Attribut         | Nichtsprechende Referenz-Identifikationsnummer                                                                        | Für spezielle Verknüpfungen und Referenzen                                                                    | OK        |
| 20 | Quellenangabe              | Attribut         | Angabe der primären Datenquelle für die Aktualisierung                                                                | Wichtig für Datenqualität und Nachvollziehbarkeit                                                             | OK        |

Tabelle: Übersicht Konzepte BFS Unternehmensregister

## 4.7. Digitaler Produktpass (EU / Schweiz)

## Dokumentation:

- GS1:  https://www.gs1.ch/de/produkte-dienstleistungen/digitaler-produktpass
- CEN/CLC/JTC 24 - Digital Product Passport - Framework and System: https://standards.cencenelec.eu/dyn/www/f?p=205:22:0::::FSP\_ORG\_ID, FSP\_LANG\_ID:3342699,25&amp;cs=12616BE69292A0FC25E5FFCFCB1205587

## Konzeptuelles Datenmodell:

<!-- image -->

Bild: Roadmap Digitaler Produktpass Kategorien. Quelle

## 5. Anhang

| Datei                                                                                                   | Geändert                       |
|---------------------------------------------------------------------------------------------------------|--------------------------------|
| Datei ~Übersicht Systeme.tmp draw.io Draft                                                              | 30.04.2026 by Rasner David BBL |
| Microsoft Excel Tabelle Archiv - Fachanwendungen zu Stammdaten.xlsx                                     | 19.02.2025 by Rasner David BBL |
| Microsoft Excel Tabelle Archiv - Fachanwendungen zu Stammdaten auf Basis RE_FX_11_02_25.xlsx            | 19.02.2025 by Rasner David BBL |
| Microsoft Excel Tabelle Bewertungskriterien_PoC_Datenkatalog_Metadaten.xlsx                             | 01.07.2025 by u80873013        |
| PNG-Datei BVML.PNG                                                                                      | 20.10.2025 by Rasner David BBL |
| PDF-Datei Datenkatalog IMMO (BBL Bauten) - ARCHIV 260801.pdf                                            | 02.08.2025 by Rasner David BBL |
| PDF-Datei Datenkatalog Toolset PoC.pdf                                                                  | 17.06.2025 by u80873013        |
| PNG-Datei Dokumentenmanagement (Vereinfachte Darst _ Mermaid Chart-2025-07-24-165853.png                | 02.08.2025 by Rasner David BBL |
| PNG-Datei EPPM Konzeptuelles Datenmodell 251029.png                                                     | 29.10.2025 by Rasner David BBL |
| PNG-Datei Erhaltungsplanung.PNG                                                                         | 04.11.2025 by Rasner David BBL |
| Microsoft Excel Tabelle Fachanwendung - 20250108_IMMO_RE- FX_Datenkatalog_WE_GR_GE_Stammdatenblatt.xlsx | 01.12.2025 by Rasner David BBL |

| Microsoft Excel Tabelle Fachanwendung - BBL GIS IMMO - Modellbeschreibung.xlsx                                                 | 18.03.2026 by Rasner David BBL   |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Microsoft Excel Tabelle Fachanwendung - BBL Korasoft DWG Layer.xlsx                                                            | 19.02.2025 by Rasner David BBL   |
| Datei Fachanwendung - BBL Korasoft DWG Vorlage.dwg                                                                             | 19.02.2025 by Rasner David BBL   |
| PDF-Datei Fachanwendung - Empfehlung-AV-WMS-mit-Anhaengen.pdf                                                                  | 19.02.2025 by Rasner David BBL   |
| PDF-Datei Fachanwendung - InterWatt - Logische Systemübersicht 19-01-2025.pdf                                                  | 19.02.2025 by Rasner David BBL   |
| Datei Fachanwendung - InterWatt - Logische Systemübersicht 19-01-2025.vsdx                                                     | 19.02.2025 by Rasner David BBL   |
| Microsoft Word Dokument Fachanwendung - K_SUPERB_Fachkonzept_ERP_IMMO_D0.21.60.10.05 _Immobiliendaten bewirtschaften V1.1.docx | 19.02.2025 by Rasner David BBL   |
| PNG-Datei Fachanwendung - K_SUPERB_Fachkonzept_ERP_IMMO Geschäftsobjekte 1.png                                                 | 06.03.2025 by Rasner David BBL   |
| PNG-Datei Fachanwendung - K_SUPERB_Fachkonzept_ERP_IMMO Geschäftsobjekte 2.png                                                 | 06.03.2025 by Rasner David BBL   |
| PNG-Datei Fachanwendung - Kalkulation kostenorientierte Miete 1.png                                                            | 06.03.2025 by Rasner David BBL   |
| PNG-Datei Fachanwendung - Kalkulation kostenorientierte Miete 2.png                                                            | 06.03.2025 by Rasner David BBL   |
| ZIP-Archiv Fachanwendung - Wüest Partner Dimensions (BBL EHP) API Dokumentation V49-0.zip                                      | 11.03.2025 by Rasner David BBL   |
| Microsoft Excel Tabelle Fachanwendung - Wüest Partner Dimensions (BBL EHP) API Geschäftsobjekte.xlsx                           | 13.03.2025 by Rasner David BBL   |
| PNG-Datei GEVER (eCH-0039) Geschäftsobjekte _ Mermaid Chart-2025-08-02-144914.png                                              | 02.08.2025 by Rasner David BBL   |
| PNG-Datei IFC_BIM_CDE Geschäftsobjekte (vereinfach _ Mermaid Chart-2025-08-02-173935.png                                       | 02.08.2025 by Rasner David BBL   |
| PNG-Datei image-2025-10-20_15-47-54.png                                                                                        | 20.10.2025 by Rasner David BBL   |
| PNG-Datei image-2025-10-29_19-25-38.png                                                                                        | 29.10.2025 by Rasner David BBL   |
| PNG-Datei image-2025-3-10_20-11-55.png                                                                                         | 10.03.2025 by Rasner David BBL   |
| PNG-Datei image-2025-3-13_9-46-31.png                                                                                          | 13.03.2025 by Rasner David BBL   |
| PNG-Datei image-2025-9-27_16-52-18.png                                                                                         | 27.09.2025 by Rasner David BBL   |
| Microsoft Excel Tabelle Lieferobjekt - Fachanwendungen zu Stammdaten auf Basis RE_FX_v_1_0.xlsx                                | 09.04.2025 by u80848903          |
| Microsoft Excel Tabelle Lieferobjekt - Fachanwendungen zu Stammdaten auf Basis RE_FX.xlsx                                      | 25.03.2025 by Rasner David BBL   |
| PNG-Datei SAP PM Geschäftsobjekte _ Mermaid Chart-2025-07-29-072510.png                                                        | 08.10.2025 by Rasner David BBL   |
| PNG-Datei SAP PS Geschäftsobjekte für Bauprojekte _ Mermaid Chart-2025-08-02-153858.png                                        | 02.08.2025 by Rasner David BBL   |

| PNG-Datei SAP RE-FX Geschäftsobjekte _ Mermaid Chart-2025-07-29-070337.png                       | 02.08.2025 by Rasner David BBL   |
|--------------------------------------------------------------------------------------------------|----------------------------------|
| PNG-Datei Tree-structure-of-the-IFC-format-Source-own-elaboration-based-on-wwwbuildbimcl (1).png | 02.08.2025 by Rasner David BBL   |
| Datei Übersicht Systeme draw.io diagram                                                          | 30.04.2026 by Rasner David BBL   |
| PNG-Datei Übersicht Systeme.png Übersicht Systeme exported to image                              | 30.04.2026 by Rasner David BBL   |

Ziehen Sie Dateien an diese Stelle, um sie hochzuladen, oder Dateien suchen Alle herunterladen