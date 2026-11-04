## Anforderungen Lösungsarchitektur - Arbeitsdokument nicht abgenommen (löschen)

<!-- image -->

Dokument löschen

| Titel           | Lösungsarchitektur: Mieterportal als MVP   |
|-----------------|--------------------------------------------|
| Author          | David Rasner BBL                           |
| Status          | Entwurf                                    |
| Stand           | 11.06.2026                                 |
| Klassifizierung | Intern                                     |

## Inhalte:

Management Summary

1. Zweck, Scope und Entscheidungslogik

2. Normativer Rahmen und handlungsleitende Prinzipien

- 2.1 Zentrale Grundlagen

- 2.2 Tragende Architekturprinzipien

3. Architekturleitbild: Plattform by design

- 3.1 Plattform Module und Anwendungsfall spezifische Anforderungen

- 3.2 Modularitätsprinzipien

- 3.3 Wiederverwendbarkeit über Lösungsmuster

- 3.4 Reifegrad-Roadmap - nicht geprüft

- 3.5 Plattform-Capabilities

4. Querschnitt für alle Layer

- 4.1 Übergreifende Anforderungen

- 4.2 Betriebs- und Trägerschaftsmodell

5. Layer-Capabilities

- 5.1 Frontend Layer

- 5.2 Prozess Layer

- 5.3 KI Layer

- 5.5 Data Layer

- 5.6 Anwendungen / Systeme Layer

6. MVP-Scope und bewusste Abgrenzung - nicht geprüft

- 6.1 MVP-Scope

- 6.2 Nicht Teil des MVP

7. Verweise und Anhang

7.1 Verweise

7.2 Anhang

## Management Summary

Dieses Dokument definiert die Anforderungen an eine erweiterbare Lösungsarchitektur mit dem Mieterportal als produktivem MVP. Das Mieterportal ist nicht als Einzelanwendung konzipiert, sondern als erste Instanz einer wiederverwendbaren Plattform für weitere digitale Leistungen im Immobilienmanagement des Bundes. Es dient als gemeinsame Anforderungsbasis für Auftraggeber, Entwicklung, Betrieb und den Förder/Investitionsentscheid.

Leitsatz ist : Kernfunktionen (Prozess-Engine, Form-Engine, Auth/Audit, Datenhaltung, Connectors / Integration in Fachsysteme, «Plattform by design» Frontend-Shell) sind modular aufgebaut, mit stabilen, versionierten Nahtstellen gebaut; neue Anwendungsfälle entstehen danach aus Anwendungsfall spezifischen Anforderungen wie BPMN-Prozesse, Formular-Schema und Datenobjekte / Attribute - mit deutlich tieferen Entwicklungskosten je zusätzlicher Anwendungsfall. Die Anforderungen sind durchgängig priorisiert (MUSS/SOLLTE/KANN/WIRD NICHT), Plattform-Capabilities zusätzlich nach MVP und Zielbild getrennt.

Der verbindliche Vorgabenrahmen des Bundes (EMBAG/DigiV, ISG/ISDS, DSG, eIAM/AGOV, WCAG 2.1 AA, BPMN 2.0, Once-Only mit SAP ERP als Leitsystem, CH-Souveränität) ist als Querschnitt über alle Layer verankert. Der MVP umfasst den Plattform-Kern und dem Mieterportal als MVP Anwendungsfall: geführte Bedarfsmeldung, rollenbasierte Sichten, Statuspipeline mit Prüfer-Queue, Prozess-Engine mit BFF-Abstraktion, PostgreSQL und SAP RE-FX-Anbindung.

Bewusst ausgeschlossen sind Mobile-App, Enterprise Service Bus-Vollstack, No-/Low-Code-Frontend Lösung und autonome KI-Agents.

Entscheidungsreif wird das Vorhaben erst mit geklärtem Betriebs- und Trägerschaftsmodell: interne Product Ownership, Betrieb in CH-Hoheit, Prüfung des 5-Jahres-TCO gegen die Beschaffungsschwellenwerte sowie Trägerschaft für Weiterentwicklung und Use-Case #2+ sind als MUSS-Anforderungen definiert - ohne diese Nachweise bleibt die Architektur fachlich plausibel, aber organisatorisch nicht umsetzbar.

<!-- image -->

## 1. Zweck, Scope und Entscheidungslogik

Dieses Dokument bündelt die Anforderungen an eine erweiterbare Lösungsarchitektur mit dem Mieterportal als produktiver MVP-Umsetzung. Das Mieterportal ist dabei nicht als isolierte Einzelanwendung zu verstehen, sondern als erste Instanz einer wiederverwendbaren Lösungsplattform für weitere digitale Leistungen im Immobilienmanagement des Bundes.

Das Dokument dient als gemeinsame Anforderungsbasis für Auftraggeber, Architektur, Entwicklung, Betrieb und Förder-/Investitionsentscheidung. Es beschreibt:

- den normativen und architektonischen Vorgabenrahmen,
- das Plattform-Leitbild und die Wiederverwendbarkeit,
- die übergreifenden Querschnittsanforderungen,
- das Betriebs- und Trägerschaftsmodell,
- die benötigten Capabilities je Architektur-Layer,
- den MVP-Scope sowie bewusst ausgeschlossene Themen.

Die Layer-Gliederung orientiert sich am Referenzmodell Informatikarchitektur Bund RIAB sowie an TOGAF. Die Architekturarbeit folgt den Architekturprinzipien des Bundes. Querschnitt, Plattform-Logik und Betriebsmodell stehen bewusst vor den Layern, weil sie für alle Layer gelten.

## Priorisierung:

| Priorität   | Bedeutung                            |
|-------------|--------------------------------------|
| MUSS        | MVP-kritisch oder rechtlich zwingend |
| SOLLTE      | wichtig, früh nach MVP umzusetzen    |
| KANN        | Mehrwert, spätere Ausbaustufe        |
| WIRD NICHT  | bewusst ausserhalb des Scope         |

Plattform-Capabilities tragen zusätzlich eine zweite Priorität für das Zielbild. Damit wird sichtbar, was im MVP zwingend gebaut wird und was zur längerfristigen Plattform-Ambition gehört.

## 2. Normativer Rahmen und handlungsleitende Prinzipien

Das Vorhaben bewegt sich im verbindlichen Vorgabenrahmen der zentralen Bundesverwaltung. Das anwendbare Recht hat Vorrang gegenüber Architekturprinzipien. Die Prinzipien helfen jedoch, die rechtlichen, organisatorischen und technischen Anforderungen konsistent in eine Lösungsarchitektur zu übersetzen.

## 2.1 Zentrale Grundlagen

- Verordnung über das Immobilienmanagement und die Logistik des Bundes (VILB): https://www.fedlex.admin.ch/eli/cc/2008/857/de
- Bundesgesetz über den Einsatz elektronischer Mittel zur Erfüllung von Behördenaufgaben (EMBAG):  https://www.fedlex.admin.ch/eli/cc/2023/682 /de
- Verordnung über die digitalen Dienste und die digitale Transformation in der Bundesverwaltung (DigiV):  https://www.fedlex.admin.ch/eli/cc/2025 /235/de
- Vorgaben zur digitalen Transformation und IKT-Lenkung der Bundesverwaltung (DTI): https://www.bk.admin.ch/de/vorgaben

|    | Thema                   | Relevante Vorgaben / Standards                                                           | Konsequenz für die Architektur                                             |
|----|-------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
|  1 | Digitale Verwaltung     | EMBAG, DigiV, Strategie Digitale Bundesverwaltung, Strategie Digitale Verwaltung Schweiz | Leistungen werden digital, medienbruchfrei und wiederverwendbar konzipiert |
|  2 | Datenschutz             | DSG, DSV                                                                                 | Datenklassifikation, Bearbeitungsverzeichnis, Retention, ggf. DSFA         |
|  3 | Informationssicher heit | ISG, ISV, Schutzbedarfsanalyse, ISDS-Konzept, IKT-Grundschutz                            | Schutzbedarf, Verschlüsselung, Audit, sichere Betriebsumgebung             |
|  4 | Identität / Zugang      | IAMV, IAM-Strategie, eIAM/AGOV                                                           | SSO, Rollen, Berechtigungen, Zero Trust                                    |
|  5 | Interoperabilität       | eCH-Standards, I14Y, Interoperabilitätsstandards                                         | offene APIs, standardisierte Schnittstellen, Anschlussfähigkeit            |
|  6 | Barrierefreiheit        | BehiG/BehiV, eCH-0059, WCAG 2.1 AA                                                       | barrierefreie Oberflächen als Muss-Anforderung                             |
|  7 | Prozessmodellieru ng    | BPMN 2.0, eCH-0158, eCH-0074                                                             | standardisierte, nachvollziehbare Prozessmodelle                           |
|  8 | Geodaten                | eCH-0056, eCH-0031, OGC API                                                              | Karten, Objektbezug und Geodatenintegration                                |
|  9 | Stammdaten              | SB018, Once-Only                                                                         | Daten aus Leitsystemen lesen statt mehrfach erfassen                       |
| 10 | Aktenführung / GEVER    | eCH-0002, eCH-0038, GEVER-Vorgaben                                                       | geschäftsrelevante Vorgänge nachvollziehbar ablegen                        |
| 11 | Cloud / Souveränität    | Cloud-Strategie, Cloud-Prinzipien, Digitale Souveränität                                 | Betrieb und Datenhaltung in CH-Hoheit; Cloud nur regelkonform              |

|   12 | KI                     | Strategie Einsatz von KI-Systemen   | KI nur mit Governance, Datenklassifikation und Human-in-the- Loop   |
|------|------------------------|-------------------------------------|---------------------------------------------------------------------|
|   13 | Open Data / Offenheit  | EMBAG, OGD-Strategie                | offene, dokumentierte APIs; Open Source wo möglich                  |
|   14 | Architektur / Methodik | RIAB, TOGAF, W010, SOA, HERMES      | Layer-Modell, stabile Verträge, methodisches Vorgehen               |

## 2.2 Tragende Architekturprinzipien

Für dieses Vorhaben sind insbesondere fünf Prinzipien tragend:

|    | Prinzip                                      | Bedeutung für das Vorhaben                                                                                                                           |
|----|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Verwaltung als Plattform / Interoperabilität | Das Mieterportal ist die erste Instanz eines wiederverwendbaren Plattform-Kerns. Weitere Anwendungsfälle sollen mit geringem Grenzaufwand entstehen. |
|  2 | Datengetrieben / Once-Only                   | Stammdaten werden aus SAP ERP und weiteren Leitsystemen gelesen, nicht erneut erfasst.                                                               |
|  3 | Sicherheit und Souveränität                  | eIAM/AGOV, Zero Trust, ISDS, Audit-Trail und Betrieb in CH-Hoheit sind Grundanforderungen.                                                           |
|  4 | Nutzerzentrierung und Inklusion              | Rollenbasierte Sichten, geführte Prozesse, Barrierefreiheit und Mehrsprachigkeit sind Teil des Zielbilds.                                            |
|  5 | Offenheit und Nachhaltigkeit                 | Offene Standards, Open Source und Wiederverwendung senken Abhängigkeiten, Kosten und Grenzaufwand.                                                   |

## 3. Architekturleitbild: Plattform by design

Das Mieterportal ist die erste Ausprägung einer wiederverwendbaren Lösungsplattform. Ziel ist nicht, sofort eine vollständige Plattform zu bauen, sondern den MVP so zu gestalten, dass spätere Anwendungsfälle den gleichen Kern nutzen können.

## Leitsatz:

<!-- image -->

Plattform by design, nicht platform-built upfront.

## 3.1 Plattform Module und Anwendungsfall spezifische Anforderungen

- Ein Anwendungsfall kann spezifische Anforderungen haben
- Kernfunktionen der Plattform sind aber modular und können wiederverwendet werden

|    | Plattform-Kern                          | Use-Case-Delta                         |
|----|-----------------------------------------|----------------------------------------|
|  1 | Prozess-Engine                          | BPMN-Prozessmodell                     |
|  2 | Form-Engine                             | Formular-Schema                        |
|  3 | Cockpit-/Inbox-Pattern                  | Datenobjekt und Statuslogik            |
|  4 | Auth, Audit, Berechtigungen             | Rollen-Mapping und Navigation          |
|  5 | Connector-Baukasten                     | benötigte Fachsystem-Anbindungen       |
|  6 | Frontend-Shell, Listen, Details, Karten | Texte, leichte UI-Anpassungen, Theming |
|  7 | Suche, i18n, Notifikation               | use-case-spezifische Inhalte           |

Konsequenz für den MVP: Der Kern wird schlank gebaut, aber mit stabilen Nahtstellen. Der erste Use-Case wird vollständig verdrahtet. Der Mehraufwand gegenüber einem Wegwerf-MVP bleibt begrenzt, schafft aber die Grundlage für Wiederverwendung.

## 3.2 Modularitätsprinzipien

- W010 - Architekturprinzipien: https://www.bk.admin.ch/de/w010-architekturprinzipien

|    | Prinzip                | Anforderung                                                          | Wirkung                              |
|----|------------------------|----------------------------------------------------------------------|--------------------------------------|
|  1 | Stabile Layer-Verträge | Versionierte REST-/API-Contracts; Frontend kennt Engine nicht direkt | Engine bleibt austauschbar           |
|  2 | Schema statt Code      | Formulare als JSON-Schema, Prozesse als BPMN                         | neue Anwendungsfälle ohne Kern-Umbau |

|   3 | Lose Kopplung                  | einheitliches Status-, Event- und Audit-Modell   | geringere Integrationskosten     |
|-----|--------------------------------|--------------------------------------------------|----------------------------------|
|   4 | Connector statt Punkt-zu-Punkt | Fachsysteme über wiederverwendbare Konnektoren   | einmal anbinden, mehrfach nutzen |
|   5 | Offene APIs                    | dokumentierte, nachnutzbare Schnittstellen       | anschlussfähig für andere Ämter  |

## 3.3 Wiederverwendbarkeit über Lösungsmuster

Die meisten Fachthemen lassen sich auf wenige wiederkehrende Muster zurückführen. Je Muster können Prozess-, Formular- und Datenobjekt-Templates entstehen.

|    | Lösungsmuster                                                                              | Beispiel-Anwendungsfälle                            | Gemeinsame Bausteine                                     |
|----|--------------------------------------------------------------------------------------------|-----------------------------------------------------|----------------------------------------------------------|
|  1 | Antrag Prüfung Freigabe/ Statusanzeige                                                     | Mieterportal, Möbel-Shop, Bauprojekt-Antrag         | Form-Engine, Prozess-Engine, DMN, Cockpit, Rollen, Audit |
|  2 | Ticket Triage Bearbeitung erledigt / Statusanzeige                                         | Support, Schadensmeldung, Instandhaltung, Reinigung | Formular, Queue, Fristen, Eskalation, Audit              |
|  3 | Stammdaten / Inventar Mutation Validierung Übernahme BBL interner Prozess sonst via Ticket | Stammdaten, Grünflächeninventar, Workspace          | Formular, Prozess, SAP-/Inventar-Connector, Audit        |
|  4 | Katalog Auswahl Bestellung Lieferung Portal Shop in Verantwortung LOG BBL                  | Möbel- und Ausstattungs-Shop                        | Katalog, Suche, Genehmigung, Connector                   |
|  5 | Portfolio-/Objektsicht Suche Details Information                                           | alle Anwendungsfälle mit Objektbezug                | Liste, Karte, Detail, Dokumente, Suche                   |

## 3.4 Reifegrad-Roadmap nicht geprüft

| Stufe                                    | Inhalt                                                            | Zeitpunkt              |
|------------------------------------------|-------------------------------------------------------------------|------------------------|
| 0 - MVP                                  | Plattform-Kern schlank angelegt, Mieterportal verdrahtet          | jetzt                  |
| 1 - Zweiter Use-Case                     | z. B. Schadensmeldung auf gleichem Kern                           | nach MVP               |
| 2 - Konfigurationsgetriebenes Onboarding | neuer Use-Case über Prozess, Formular, Datenobjekt und Navigation | mittelfristig          |
| 3 - Self-Onboarding                      | Fachseite legt neue Lösungen mit No-/Low-Code-Studio selbst an    | strategisches Zielbild |

Daraus ergibt sich die gewünschte Kostenstruktur: moderater Einmalaufwand für den Kern, danach deutlich tiefere Grenzkosten je weiterem Use-Case.

## 3.5 Plattform-Capabilities

|    | Capability                           | MVP        | Zielbild   | Kurzanforderung                                                                      |
|----|--------------------------------------|------------|------------|--------------------------------------------------------------------------------------|
|  1 | Wiederverwendbare Frontend-Bausteine | MUSS       | MUSS       | Shell, Form-Renderer, Cockpit, Listen, Details und Karten als gemeinsame Komponenten |
|  2 | Plattform-Services                   | MUSS       | MUSS       | Auth, Audit, Berechtigungen; später i18n, Suche, Notifikation                        |
|  3 | Stabile Layer-Verträge               | MUSS       | MUSS       | versionierte APIs; Engine nie direkt am Frontend                                     |
|  4 | Once-Only                            | MUSS       | MUSS       | Stammdaten aus Leitsystemen lesen                                                    |
|  5 | Harmonisierte Daten                  | SOLLTE     | MUSS       | use-caseübergreifende Datenharmonisierung an der Quelle                              |
|  6 | Multi-Use-Case-Fähigkeit             | SOLLTE     | MUSS       | Trennung von Daten, Rollen und Navigation je Use-Case                                |
|  7 | Connector-Baukasten                  | SOLLTE     | MUSS       | SAP ERP, DMS/CDE, Geo, Mail als wiederverwendbare Konnektoren                        |
|  8 | Konfiguration statt Code             | SOLLTE     | MUSS       | neuer Use-Case über Prozess, Formular, Datenschema und Navigation                    |
|  9 | Offene Standards / Nachnutzbarkeit   | SOLLTE     | MUSS       | offene, dokumentierte APIs; Open Source wo möglich                                   |
| 10 | Lösungsmuster-Bibliothek             | KANN       | SOLLTE     | Templates je Archetyp                                                                |
| 11 | No-/Low-Code-Studio                  | WIRD NICHT | KANN       | strategisches Endbild, nicht MVP                                                     |

## 4. Querschnitt für alle Layer

Der Querschnitt umfasst Anforderungen, die unabhängig vom einzelnen Layer gelten. Sie sind nicht optional, sondern bestimmen, ob die Lösung produktions-, betriebs- und entscheidungsfähig ist.

## 4.1 Übergreifende Anforderungen

|    | Capability             | Priorität   | Anforderung                                                                                 |
|----|------------------------|-------------|---------------------------------------------------------------------------------------------|
|  1 | Zero Trust             | MUSS        | eIAM/AGOV-SSO, Rollen und Berechtigungen über alle Layer                                    |
|  2 | Informationssicherheit | MUSS        | Schutzbedarfsanalyse, ISDS-Konzept, IKT-Grundschutz, Verschlüsselung at-rest und in-transit |
|  3 | Datenschutz            | MUSS        | Datenklassifikation, Bearbeitungsverzeichnis, Retention, ggf. DSFA                          |
|  4 | Observability / Audit  | MUSS        | Logs, Metriken, Audit-Trail und Nachweise                                                   |
|  5 | Interoperabilität      | MUSS        | offene APIs, eCH-Standards, Anschlussfähigkeit an I14Y                                      |
|  6 | Accessibility          | MUSS        | WCAG 2.1 AA, Tastaturbedienung, ARIA, Kontrast, Fokus-Management                            |
|  7 | Governance / Ownership | MUSS        | Rollen, Verantwortlichkeiten, Change Management, Kosten, Risiken, Qualitätssicherung        |
|  8 | Aktenführung / Records | SOLLTE      | geschäftsrelevante Vorgänge nachvollziehbar ablegen; GEVER-Anbindung prüfen                 |
|  9 | Digitale Souveränität  | SOLLTE      | Datenhaltung und Betrieb in CH-Hoheit; Cloud nur regelkonform                               |
| 10 | Findability            | SOLLTE      | Metadaten, Lineage, Directories, Datenkatalog                                               |
| 11 | Reusability            | SOLLTE      | modulare, entkoppelte und wiederverwendbare Bausteine                                       |

## 4.2 Betriebs- und Trägerschaftsmodell

Das Vorhaben dient der Förder- und Investitionsentscheidung. Die offene Frage ist nicht nur, was gebaut werden soll, sondern wer baut, wer betreibt, wer trägt und wer die Weiterentwicklung verantwortet.

|    | Aspekt                        | Priorität   | Anforderung                                                                                                                    |
|----|-------------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------|
|  1 | Product Ownership             | MUSS        | interne Product Ownership für Backlog, Prozessdefinitionen, Stakeholder-Koordination und Lieferantensteuerung                  |
|  2 | Umsetzungsmodell              | MUSS        | Make-/Best-of-Breed-Ansatz als Primärvariante; realistisch als Blend aus interner Ownership und externer Entwicklungskapazität |
|  3 | Betrieb / Hosting             | MUSS        | Private Cloud oder Betriebspartner in CH-Hoheit                                                                                |
|  4 | Beschaffungsweg               | MUSS        | 5-Jahres-TCO prüfen; bei Überschreitung der Schwellenwerte rechtskonformen Beschaffungsweg festlegen                           |
|  5 | Projektmethodik               | MUSS        | HERMES-Rollen und -Phasen verbindlich klären                                                                                   |
|  6 | Support / SLA                 | SOLLTE      | Verfügbarkeit, Incident-, Change- und Release-Prozess definieren                                                               |
|  7 | Lifecycle / Weiterentwicklung | SOLLTE      | Trägerschaft für Use-Case #2+ und Plattform-Pflege klären                                                                      |

Damit wird das Dokument entscheidungsreif: Ohne geklärte Trägerschaft, Betrieb und Ownership bleibt die Architektur fachlich plausibel, aber organisatorisch nicht umsetzbar.

## 5. Layer-Capabilities

## 5.1 Frontend Layer

Zweck : Interaktion und Self-Service für mietende Verwaltungseinheiten, GS-Prüfer:innen, BBL-PFM, BBL-Campus und Auditoren.

|    | Capability                | Priorität   | Anforderung                                                                                                   |
|----|---------------------------|-------------|---------------------------------------------------------------------------------------------------------------|
|  1 | Geführte Bedarfsmeldung   | MUSS        | 5-Schritt-Wizard mit Validierung, Autosave, NAW-Klassifikation, m²/FTE-Berechnung und Validierungsübersicht ? |
|  2 | Self-Service-Katalog      | MUSS        | Einstieg in die verfügbaren Leistungen                                                                        |
|  3 | Authentisierung           | MUSS        | eIAM/AGOV-Login                                                                                               |
|  4 | Rollenbasierte Navigation | MUSS        | Sichten und Funktionen je Rolle                                                                               |
|  5 | Antragsverfolgung         | MUSS        | Statuspipeline, Inbox, Prüfer-Queue, Detailansicht mit Anhängen und Historie                                  |
|  6 | Barrierefreiheit          | MUSS        | WCAG 2.1 AA                                                                                                   |
|  7 | Erscheinungsbild          | MUSS        | CD-Bund-Konformität                                                                                           |
|  8 | Objektportfolio           | SOLLTE      | Galerie, Liste und Karte                                                                                      |
|  9 | Objekt-Detailseite        | SOLLTE      | Vertrag, Kennzahlen, Mietverhältnis, Anträge, Dokumente und Kontakte                                          |
| 10 | Pläne und Dokumente       | SOLLTE      | Anzeige und Download ? Abgrenzung zu CDE/AC klären                                                            |

|   11 | Volltextsuche     | SOLLTE          | Suche über Portalinhalte                                                                     |
|------|-------------------|-----------------|----------------------------------------------------------------------------------------------|
|   12 | Mehrsprachigkeit  | SOLLTE          | DE/FR/IT/EN                                                                                  |
|   13 | Notifikation      | SOLLTE          | E-Mail-Benachrichtigungen                                                                    |
|   14 | Inhalte           | SOLLTE          | Info-, Hilfe- und News-Inhalte                                                               |
|   15 | Erweiterte Viewer | KANN            | Grundriss-Viewer, Dokumentenvorschau                                                         |
|   16 | Geosuche          | KANN            | Standort-/Geosuche                                                                           |
|   17 | Komfortfunktionen | KANN            | Deep-Linking, Teilen, Drucken, Tastatur-Shortcuts, Wiki                                      |
|   18 | Native Mobile-App | WIRD NICHT KANN | responsive Web genügt je nach use case könnte eine Mobile APP Sinn machen z.B. Störmeldungen |

## 5.2 Prozess Layer

Zweck : Orchestrierung der Geschäftsprozesse, insbesondere Bedarfsmeldung, Prüfung, Freigabe und Mutationen.

|    | Capability                | Priorität   | Anforderung                                             |
|----|---------------------------|-------------|---------------------------------------------------------|
|  1 | Prozessausführung         | MUSS        | zustandsbehaftete, langlaufende Prozesse                |
|  2 | Human Tasks               | MUSS        | Aufgaben-Inbox für manuelle Schritte                    |
|  3 | Status-Bereitstellung     | MUSS        | Prozessstatus für das Frontend                          |
|  4 | BFF-Abstraktion           | MUSS        | REST-/BFF-Schicht; Frontend kennt Engine nicht direkt   |
|  5 | Prozess-Logging           | MUSS        | Logging der Prozessereignisse                           |
|  6 | Prozessversionierung      | SOLLTE      | parallele Versionen laufender Prozessmodelle            |
|  7 | Prozessmonitoring         | SOLLTE      | Cockpit für laufende Instanzen                          |
|  8 | Fachliche Modellierung    | KANN        | No-/Low-Code-BPMN-Modellierung durch Fachanwender:innen |
|  9 | Direkte Engine-Exposition | WIRD NICHT  | Engine nie direkt am Frontend                           |

## 5.3 KI Layer

Zweck : Kognitive Assistenz für Suche, Verstehen und Automatisierung.

|    | Capability               | Priorität   | Anforderung                                                                                 |
|----|--------------------------|-------------|---------------------------------------------------------------------------------------------|
|  1 | RAG-Wissenssuche         | SOLLTE      | Suche über Portalinhalte und Dokumente                                                      |
|  2 | LLM-Ausfüllhilfe         | SOLLTE      | Unterstützung bei geführten Bedarfsmeldungen                                                |
|  3 | Auswertungen             | KANN        | Zusammenfassungen und Analysen                                                              |
|  4 | Agents/Actions           | KANN        | MCP-Anbindung, eng abgegrenzt, mit Human-in-the-Loop                                        |
|  5 | Autonome Automatisierung | WIRD NICHT  | keine Prozessautomatisierung ohne Governance, Datenklassifikation und menschliche Kontrolle |

## 5.4 Integration Layer

Zweck : Kontrollierter Datenfluss zwischen Plattform und Leitsystemen - Befüllung und Aktualisierung des Leitsystem-Caches (lesend) sowie kontrollierte Rückschreibung einzelner Geschäftsvorfälle (schreibend). Abgrenzung: Das BFF bedient das Frontend und setzt fachliche Berechtigungen durch; der Integration Layer spricht mit Fachsystemen. Beide sind getrennte Verantwortlichkeiten, auch wenn sie im MVP im selben Backend-Service liegen können.

|    | Capability                         | Priorität   | Anforderung                                                                                                                           |
|----|------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------|
|  1 | RE-FX-Connector                    | MUSS        | REST-Anbindung für AO-Objekte, Mietobjekte und Mietverhältnisse; lesend in den Cache, schreibend nur für definierte Geschäftsvorfälle |
|  2 | Synchronisation / Cache- Befüllung | MUSS        | definierte Aktualisierungsstrategie je Datenobjekt (Pull-Intervall, On-Demand, Invalidierung); konsistent mit Data Layer Cap. 2       |
|  3 | Fehlerbehandlung                   | MUSS        | Retry, Dead-Letter und Alarmierung; idempotente Verarbeitung bei Wiederholung                                                         |
|  4 | Schnittstellen-Verträge            | MUSS        | versionierte, dokumentierte API-Contracts je Connector (Modularitätsprinzip 1)                                                        |
|  5 | MDG-Connector                      | SOLLTE      | Geschäftspartner (Kontakte, Adressen, IDs) lesend in den Cache                                                                        |
|  6 | HR-Connector                       | SOLLTE      | Personal- und Organisationsdaten für Rollen-Mapping und Zuordnung zu Verwaltungseinheiten, lesend                                     |
|  7 | DMS-/CDE-Connector                 | SOLLTE      | Dokumente und Pläne referenzieren statt kopieren; Ablage geschäftsrelevanter Vorgänge (GEVER) prüfen                                  |

|   8 | Konfigurierbarkeit   | SOLLTE     | Connectors parametrisierbar (Endpunkte, Mapping, Intervalle) statt hartcodiert - Basis für den Connector-Baukasten (Plattform-Capability 7)      |
|-----|----------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|   9 | Metadaten / Lineage  | SOLLTE     | Herkunfts- und Verarbeitungsnachweise je Datenobjekt (Quelle, Stand, Transformation)                                                             |
|  10 | API-Gateway          | KANN       | separates Gateway erst bei mehreren Consumern; Aufgabe dann technisch (Token-Validierung, Routing, Rate Limiting), nicht fachliche Autorisierung |
|  11 | ESB-Vollstack        | WIRD NICHT | kein schwergewichtiger WSO2-ESB im MVP                                                                                                           |

## 5.5 Data Layer

Zweck : Persistenz für portaleigene Daten ohne Leitsystem (Anträge, Entwürfe, Statusverläufe, Kommentare) sowie Caching von Leitsystem-Daten für Performance und Entkopplung. Die Datenhaltung konkurriert nicht mit den Leitsystemen: Stammdaten bleiben read-only-Replikate, das Portal ist nur für seine eigenen Fachdaten System of Record.

|    | Capability                | Priorität   | Anforderung                                                                                                                                                                           |
|----|---------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Portaleigene Datenhaltung | MUSS        | PostgreSQL als System of Record für Anträge, Entwürfe, Statusverläufe und Prozess-Fachdaten; transaktionale CRUD- Operationen                                                         |
|  2 | Leitsystem-Cache          | SOLLTE      | Read-only-Replika von RE-FX-/MDG-Daten mit definierter Aktualisierungsstrategie (Refresh, Invalidierung, Stale- Kennzeichnung); keine eigenständige Pflege - Once-Only bleibt gewahrt |
|  3 | Berechtigungen            | MUSS        | Durchsetzung der fachlichen Zugriffslogik im Backend/BFF (siehe Hinweis); DB-Zugriff nur über Service-Konten mit minimalen Rechten                                                    |
|  4 | Mandantentrennu ng        | SOLLTE      | Datentrennung je Verwaltungseinheit bzw. Use-Case; Row-Level Security als zweite Verteidigungslinie prüfen                                                                            |
|  5 | Backup / Recovery         | MUSS        | Sicherung und Wiederherstellbarkeit                                                                                                                                                   |
|  6 | Geodaten                  | SOLLTE      | PostGIS für Objektkarte, Geodaten und Grundriss-Viewer                                                                                                                                |
|  7 | Skalierung                | KANN        | Load Balancing und Hochverfügbarkeit                                                                                                                                                  |
|  8 | API-Gateway               | WIRD NICHT  | kein separates WSO2 API Gateway im MVP                                                                                                                                                |

## 5.6 Anwendungen / Systeme Layer

Zweck : Bestehende Fachsysteme als Datenquellen und -senken anbinden.

|    | Capability                      | Priorität   | Anforderung                                                                                                    |
|----|---------------------------------|-------------|----------------------------------------------------------------------------------------------------------------|
|  1 | SAP ERP / RE-FX                 | MUSS        | AO-Objekte, Mietobjekte und Mietverhältnisse lesen und ggf. schreiben; Once-Only                               |
|  2 | SAP MDG                         | SOLLTE      | Geschäftspartner als führende Quelle für Kontakte, Adressen und IDs lesen; keine Doppelerfassung im Portal     |
|  3 | HR-Integration (Bundespersonal) | SOLLTE      | Personal- und Organisationsdaten für Nutzerprofile, Rollen-Mapping und Zuordnung zu Verwaltungseinheiten lesen |
|  4 | DMS / CDE                       | SOLLTE      | Dokumente und Pläne anbinden; GEVER-/Aktenführungsanforderungen prüfen                                         |
|  5 | Weitere Fachsysteme             | KANN        | nach Bedarf                                                                                                    |
|  6 | Schattenregister                | WIRD NICHT  | keine Neuanlage für bereits vorhandene Stammdaten                                                              |

## 6. MVP-Scope und bewusste Abgrenzung - nicht geprüft

## 6.1 MVP-Scope

Der MVP umfasst den schlanken Plattform-Kern und genau einen produktiv verdrahteten Use-Case: das Mieterportal. Enthalten sind:

- Frontend-Shell mit CD-Bund-Konformität,
- geführte Bedarfsmeldung,
- rollenbasierte Sichten,
- Statuspipeline, Inbox und Prüfer-Queue,
- Prozess-Engine mit BFF-Abstraktion,
- PostgreSQL-Datenhaltung,
- SAP-RE-FX-Anbindung für zentrale Stammdaten,
- Auth, Audit, Rollen und grundlegende Observability,
- wiederverwendbare Nahtstellen für spätere Anwendungsfälle.

## 6.2 Nicht Teil des MVP

Nicht Bestandteil des MVP sind:

- native Mobile-App,
- schwergewichtiger ESB-Vollstack,
- separates API-Gateway ohne mehrere Consumer,
- vollständiges No-/Low-Code-Studio,
- autonome KI-Agents ohne klare Governance,
- vollständiges Self-Onboarding durch Fachbereiche,
- voll ausgebaute Plattform-Governance für beliebig viele Anwendungsfälle.

Diese Themen bleiben Teil des Zielbilds oder späterer Reifegradstufen.

## 7. Verweise und Anhang

## 7.1 Verweise

- TBD

## 7.2 Anhang

| Datei                                                | Geändert                       |
|------------------------------------------------------|--------------------------------|
| PNG-Datei Lösungsarchitektur mit Capabilities V2.png | 11.06.2026 by Rasner David BBL |
| PNG-Datei Lösungsarchitektur mit Capabilities V1.png | 11.06.2026 by Rasner David BBL |
| PNG-Datei ChatGPT Image 15. Juni 2026, 11_18_19.png  | 15.06.2026 by Rasner David BBL |

Ziehen Sie Dateien an diese Stelle, um sie hochzuladen, oder Dateien suchen Alle herunterladen