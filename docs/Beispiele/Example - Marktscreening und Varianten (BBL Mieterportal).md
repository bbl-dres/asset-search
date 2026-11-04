## Marktscreening und Varianten

<!-- image -->

Arbeitsdokument

Nicht abgenommen

| Titel           | Marktscreening: Mieterportal als MVP   |
|-----------------|----------------------------------------|
| Author          | David Rasner BBL                       |
| Status          | Entwurf                                |
| Stand           | 11.06.2026                             |
| Klassifizierung | Intern                                 |

## Inhalte:

## Management Summary

1. Ziel, Zweck und Variantenlogik (Adapt / Buy / Create)
2. Übersicht der Verticals
3. Quer-Verticals
4. 3.1 SAP-native Mieterportal-Add-ons (Buy / Adapt)
5. 3.2 CAFM/IWMS mit Mieterportal-Modulen (Buy)
6. 3.3 CDE Bund / Asset-Information-Management-Plattformen (Buy / Adapt)
7. 3.3 Low-Code-/No-Code-App-Plattformen (Buy)
8. 3.4 Portal- und Workflow-/Case-Management-Plattformen (Buy)
9. 3.5 Best-of-Breed-Stack-Eigenentwicklung (Create)
10. 3.6 Standarddienste des Bundes (Adapt)
4. Optionen je Layer
12. 4.1 Frontend Layer
13. 4.2 Prozess Layer
14. 4.3 KI Layer
15. 4.4 Integration Layer
16. 4.5 Data Layer
17. 4.6 Anwendungen / Fachsysteme
5. Einordnung
6. Offene Punkte
7. Verweise und Anhang
21. 7.1 Verweise
22. 7.2 Anhang

## Management Summary

Das Marktscreening prüft die Lösungsansätze für die Plattform mit dem Mieterportal als MVP entlang Adapt / Buy / Create - wegen des spezifischen Vorgabenrahmens des Bundes (eIAM/AGOV, CD Bund, WCAG 2.1 AA, Souveränität, Open Source, BPMN 2.0, Once-Only mit SAP ERP) je Layer, nicht als Gesamtentscheid.

Kein Buy-Produkt erfüllt das Profil vollständig: CAFM scheitert an Once-Only und Plattform-Ambition, Low-Code an Souveränität und TCO, SAPnative Add-ons (Kibanda, easysquare) lösen als einzige Once-Only nativ, decken aber den MVP-Kern nicht ab und vertiefen das Lock-in; Portal-/CaseManagement-Plattformen sind fachlich das stärkste Buy-Vertical, für den Pilot aber durch den WTO-Vorlauf blockiert. Die CDE Bund ist Datenquelle per Connector, nicht Plattform-Basis.

Einzig die (Angular/Oblique, Operaton oder Flowable-Core, Schema-Formulare, PostgreSQL, Keycloak/eIAM, RHOS) erfüllt alle harten Create-Variante Anforderungen - bei interner Umsetzung ohne WTO-Vorlauf (Art. 10 BöB). Bedingung: plattform-ready by design, sonst entsteht ein Wegwerf-Pilot. Adapt liefert Bausteine, keine Lösung. Der Prozess-Engine-Entscheid (Camunda 7 EOL, Camunda 8 kommerziell  Operaton oder Flowable-Core) gehört in den Create-Umsetzungsauftrag.

<!-- image -->

Bild: Marktsegmente

## 1. Ziel, Zweck und Variantenlogik (Adapt / Buy / Create)

Dieses Dokument gibt eine Marktübersicht über mögliche Lösungsansätze für die erweiterbare Lösungsplattform mit dem Mieterportal als MVP. Es zeigt je Architektur-Layer die Optionen mit ihren Vor- und Nachteilen auf und dient als Grundlage für die Variantendiskussion und den späteren Beschaffungsentscheid. Es ist bewusst qualitativ gehalten: keine Bewertungsmatrix, keine Gewichtung, keine Produkt-Rangliste-Marktübersicht mit ehrlicher Einordnung.

Die Terminologie folgt der ABC-Analyse Lösungsarchitektur Pilot:

- Adapt -vorhandene Standarddienste des Bundes nutzen (minimaler Beschaffungs- und Entwicklungsaufwand)
- Buy -marktgängiges Produkt oder marktgängige Plattform beschaffen
- Create -Eigenentwicklung auf Basis von Standardkomponenten und Standardservices

Der Vorgabenrahmen des Bundes (eIAM/AGOV, ISG/ISDS, DSG, WCAG 2.1 AA / eCH-0059, CD Bund, digitale Souveränität, Open-Source-Präferenz, BPMN 2.0, Once-Only mit SAP ERP als Leitsystem) ist so spezifisch, dass kein einzelnes Buy-Produkt alle Anforderungen gleichzeitig erfüllt. Adapt/Buy /Create ist deshalb keine Gesamtentscheidung, sondern eine Entscheidung je Layer.

## 2. Übersicht der Verticals

|    | Vertical                                           | ABC- Variante               | Deckt ab                                                                                     | Scheitert an / Grenze                                                                                                |
|----|----------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|  1 | SAP-native Mieterportal-Add-ons                    | Buy / Adapt (SAP ERP)       | Mieter-Self-Service (Tickets, Dokumente), Once-Only nativ (RE-FX-Direktzugriff)              | MVP-Kern (Bedarfsmeldung, Prüfer-Queue), Plattform-Ambition, CD Bund / eIAM, vertieft SAP-Lock-in, Hosting zu prüfen |
|  2 | CAFM/IWMS mit Mieterportal- Modul                  | Buy                         | FM-Prozesse, Flächen, Verträge, teils Mieterportal                                           | Plattform-Ambition, CD Bund, Once-Only (Stammdaten-Doppelführung mit RE-FX), wäre neues Fachsystem                   |
|  3 | CDE Bund / Asset-Information- Management (PIMAIM)  | Buy / Adapt (in Einführung) | Dokumente, Pläne, Modelle, Bau-zu-Betrieb-Übergabe                                           | PIM-lastig (BIM-Fokus); AIM-Eignung, Modularität und API-Fähigkeit unbestätigt; Prozess-/Self-Service-Fokus fehlt    |
|  4 | Portal- und Workflow-/Case- Management-Plattformen | Buy                         | SPOC-Einstieg, rollenbasierte Navigation, Inbox /Status, Aufgabensteuerung, Audit, Reporting | Beschaffungsvorlauf (WTO), CD Bund / WCAG-Tiefe, Souveränität je Anbieter, Lizenz-TCO, Lock-in                       |
|  5 | Low-Code-/No-Code-Plattformen                      | Buy                         | Schnelle App-Erstellung, Formulare, einfache Workflows                                       | Souveränität (US-Anbieter), Lizenz-TCO, WCAG-Tiefe, eIAM, Lock-in                                                    |
|  6 | Best-of-Breed-Stack (Eigenentwicklung)             | Create                      | Alle harten Anforderungen, Plattform-Ambition                                                | Eigenleistung, Betriebsverantwortung, Integrationsrisiko                                                             |

| 7   | Standarddienste des Bundes (eIAM/AGOV, SGC, Koby)   | Adapt   | Auth, künftig Hosting und KI in CH-Hoheit   | Funktionsabdeckung nur punktuell; SGC erst ab 2027 produktiv   |
|-----|-----------------------------------------------------|---------|---------------------------------------------|----------------------------------------------------------------|

## 3. Quer-Verticals

Lesehilfe zu den Markttabellen:i Die Eignungsspalte (z.B. «Mieterportal», «AIM-Eignung») verwendet das Werteset Ja / Teilweise / Nein / zu prüfen und gibt die Positionierung des Anbieters wieder, nicht eine BBL-Evaluation.

## 3.1 SAP-native Mieterportal-Add-ons (Buy / Adapt)

Kontext: BBL ist SAP-Kunde; mit SUPERB wird S/4HANA (RE-FX, MDG) das kaufmännische Leitsystem. RE-FX-native Add-ons sind das einzige BuySegment, das Once-Only nativ erfüllt (Direktzugriff auf RE-FX, keine Stammdaten-Doppelführung) - vier öffentliche CH-Referenzen (LSZ, SBB, Stadt Bern, Kanton Luzern) nutzen dasselbe Produkt. Grenze: geschlossene Ticketing-/Self-Service-Vertikalprodukte ohne MVP-Kern (geführte Bedarfsmeldung, Prüfer-Queue) und ohne Plattform-Ambition; vertieft das SAP-Lock-in.

|    | Produkt                          | Herkunft   | Mieterportal   | Hinweis                                                                                                                                                                                                                                                                                                                                                                                         |
|----|----------------------------------|------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Kibanda (inpeek AG)              | CH         | Ja             | RE-FX-Add-on; Echtzeit-Anbindung via OData/Principal Propagation, keine Datenkopien, SAP-Rollenmodell nachgenutzt; GK- Delegationsmodell produktiv (SBB myPortal); Referenzen LSZ, SBB Immobilien, Stadt Bern (DOMUM), Kanton Luzern; Web-App (Kibanda Go) auf Azure - Hosting-Modell für Bundeskontext zu prüfen; Preisanker LSZ: CHF 650'880 / 10 Jahre bei deutlich schmalerem Scope als MVP |
|  2 | easysquare (PROMOS consult)      | DE         | Ja             | Deutsches Pendant: Mieter-App/-Portal plus easysquare workflow als RE-FX-Plug-in; Plattform auf SAP-NetWeaver-Basis, Betrieb im PROMOS-RZ (DE); Referenzen deutsche Wohnungswirtschaft und Kommunen (u.a. Stadt Mainz); kein CH-Hosting belegt                                                                                                                                                  |
|  3 | Fiori-/BTP- Eigenbau (SAP Build) | -          | Teilweise      | Kein Produkt, sondern der SAP-interne Create-Pfad: Fiori-Apps bzw. SAP Build auf BTP gegen RE-FX/MDG; im SUPERB-Kontext naheliegende Frage («warum nicht im ERP bauen?»); BTP-Lizenzkosten, Deployment-Modell und Souveränität zu klären; CD Bund /Oblique nicht nativ                                                                                                                          |

## Vorteile:

- Once-Only nativ erfüllt: Direktzugriff auf RE-FX (OData, Principal Propagation), keine Stammdaten-Doppelführung, SAP-Rollenmodell nachnutzbar - einziges Buy-Vertical ohne diesen Konflikt
- Geringster Integrationsaufwand aller Buy-Optionen; im SUPERB-Zielbild (S/4HANA) zukunftskompatibel
- Produktiv belegt im öffentlichen CH-Kontext (LSZ, SBB, Stadt Bern, Kanton Luzern) inkl. Geschäftskunden-Delegationsmodell
- Tiefer Einstiegs-TCO (Preisanker LSZ: CHF 650'880 / 10 Jahre); CH-Hersteller mit Behördenreferenzen (inpeek)

## Nachteile:

- Ticketing-/Self-Service-Fokus: MVP-Kern (geführte Bedarfsmeldung, Raumprogramm, Prüfer-Queue) nicht im Produkt-Scope - Erweiterung nur über den Hersteller
- Keine Plattform-Ambition: geschlossenes SAP-Vertikalprodukt, nicht wiederverwendbar für weitere Verwaltungs-Use-Cases
- Vertieft das SAP-Lock-in (Prozess- und Datenmodell im SAP-Ökosystem) statt es zu kapseln
- CD Bund / WCAG 2.1 AA und eIAM/AGOV nicht nativ; Theming-Spielraum produktabhängig
- Souveränität zu prüfen: Kibanda Go auf Azure, easysquare im PROMOS-RZ (DE) - kein belegtes CH-/Bundes-Hosting
- Beschaffung: WTO-pflichtig wie jedes Buy; tiefer Preisanker gilt für schmaleren Scope und ist nicht auf den MVP übertragbar

Konsequenz: Die fachlich naheliegendste Abkürzung - und das stärkste Buy-Argument gegen Create, wenn der Entscheid auf «nur Ticketing» reduziert wird. Scheitert aber an MVP-Scope und Plattform-Ambition; falls die Plattform-Ambition fällt, ist dieses Vertical neu zu bewerten, bevor Create beauftragt wird.

Bild: Kibanda. Quelle

<!-- image -->

## 3.2 CAFM/IWMS mit Mieterportal-Modulen (Buy)

Kontext: Parallel wird eine CAFM-Beschaffung diskutiert. Ein CAFM ist das richtige Werkzeug für FM-Prozesse-aber nicht für eine wiederverwendbare Verwaltungsplattform.

## Internationale IWMS-Anbieter

|    | Produkt            | Herkunft   | Mieterportal   | Hinweis                                                                     |
|----|--------------------|------------|----------------|-----------------------------------------------------------------------------|
|  1 | Planon             | NL         | Ja             | SaaS-zentriert, enterprise-schwer                                           |
|  2 | Archibus (Eptura)  | US         | Ja             | BIM/CAD-stark; seit 2022 Teil des US-Konzerns Eptura                        |
|  3 | IBM TRIRIGA        | US         | Ja             | Sehr umfangreich, hohe Komplexität                                          |
|  4 | Spacewell/Axxerion | BE         | Ja             | IoT-/Smart-Building-stark; Teil der Nemetschek Group (DE)                   |
|  5 | MRI Software       | US         | Ja             | Property-Management-Fokus                                                   |
|  6 | Yardi              | US         | Ja             | Property-Management-Fokus; eigenständiger Anbieter, nicht mit MRI verbunden |

## DACH-/CH-Anbieter

|    | Produkt                           | Herkunft               | Mieterportal   | Hinweis                                                                                                                               |
|----|-----------------------------------|------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------|
|  1 | CAMPOS (ICFM AG)                  | CH                     | Teilweise      | Eher via API als dediziertes Modul; einziger Anbieter mit explizit garantiertem CH-Hosting; Referenzen SUVA, Stadt Adliswil           |
|  2 | eTASK                             | DE                     | Ja             | Stärkstes belegtes Mieterportal; zentrales CAFM des Bundes (DE) per Rahmenvertrag, SaaS in der Bundescloud (ITZBund), Datenhaltung DE |
|  3 | Byron Informatik                  | CH                     | Zu prüfen      | Schweizer CAFM-Anbieter mit Behörden-/Werkreferenzen; relevant für CH-Souveränität                                                    |
|  4 | Axentris/Servalino                | DE (CH- Niederlassung) | Ja             | Web-Portal-Framework, On-Prem möglich (Angaben beim Anbieter zu verifizieren)                                                         |
|  5 | SPARTACUS (N+P)                   | DE                     | Teilweise      | Mieter-App, kein Self-Service-Webportal; GEFMA-444 (Zertifikatsstatus zu verifizieren)                                                |
|  6 | iTWO fm (RIB, Schneider Electric) | DE                     | Ja             | Self-Service-Portale; keine CH-Garantie                                                                                               |
|  7 | IMSWARE (IMS GmbH)                | DE                     | Ja             | Self-Service-Portale; keine CH-Garantie                                                                                               |
|  8 | waveware (Loy & Hutz)             | DE                     | Zu prüfen      | Etabliertes CAFM, Fokus Betreiberverantwortung                                                                                        |
|  9 | pit-FM (pit-cup)                  | DE                     | Zu prüfen      | CAFM mit Referenzen in der öffentlichen Verwaltung                                                                                    |

## Vorteile

- FM-Kernprozesse sofort und tief abgedeckt, kein Eigenbau
- Etablierte Mieterportal-/Self-Service-Module, mobile Apps
- Marktreife, Referenzen, Integrator-Ökosystem

## Nachteile

- FM-Vertikalprodukt, keine generische Plattform-Plattform-Ambition nicht erfüllbar
- Stammdaten-Doppelführung mit SAP ERP: verletzt Once-Only oder erzwingt aufwändige bidirektionale Synchronisation
- CD Bund / WCAG-Tiefe nicht nativ; eIAM/AGOV nicht out-of-the-box
- Souveränitätsproblem bei US-Anbietern (CLOUD Act)
- Lock-in über proprietäre Datenmodelle; Lizenzkosten triggern WTO

Konsequenz: Falls ein CAFM beschafft wird, muss es als FM-Fachsystem klar von der Plattform abgegrenzt bleiben-nicht als Plattform-Ersatz.

## 3.3 CDE Bund / Asset-Information-Management-Plattformen (Buy / Adapt)

Kontext: Nach ISO-19650-Logik geht das Projekt-Informationsmodell (PIM) bei Bauabschluss in das Asset-Informationsmodell (AIM) über (Betriebsphase: ISO 19650-3). CDE-Anbieter positionieren sich zunehmend als Betriebsphasen-Plattformen-die Abgrenzung zur CAFM verschwimmt.

Sonderfall CDE Bund: Eine CDE wurde bundesweit gemeinsam durch BBL, ASTRA und VBS beschafft und ist in Einführung-damit ist dieses Vertical nicht reines Buy, sondern Buy/Adapt: Die Frage ist nicht «beschaffen?», sondern «was kann die beschaffte Lösung, und worauf lässt sich aufbauen?». Der genaue Funktionsumfang ist aus BBL-Sicht noch nicht abschliessend bekannt. Arbeitshypothese (zu verifizieren): Alle drei beschaffenden Ämter haben einen starken BIM-Fokus, die Lösung ist entsprechend PIM-lastig; Modularität, Ausbaufähigkeit und API-First-Architektur für die Betriebsphase (AIM) sind nicht belegt und werden nicht angenommen.

## Kandidaten CDE Bund

|    | Produkt   | Herkunft   | AIM- Eignung   | Hinweis                                                                                                                                                                                                                                                                                                                                                   |
|----|-----------|------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | vrame     | DE         | Zu prüfen      | Zuschlag CDE Bund. BIM-/Informationsmanagement-Haus (Berlin) mit eigener CDE-Lösung, die «Projekte und Betrieb aus Sicht von Bauherren zusammenbringt»; positioniert für Bauherren mit grossem Bestandsportfolio; Referenzen u.a. Siemensstadt Square, SuedLink, BMW, WDR -Betriebsphasen-Tiefe (AIM) öffentlich nicht belegt. Ist zu verifizieren. vrame |

| 2   | LIBAL   | DE/CH   | Ja   | Unterlegener Kandidat CDE Bund. Dezidierter AIM-/Betriebsphasen-Fokus: Bau-zu-Betrieb-Übergabe, geprüfte Gebäudedaten (Quality Gates), KI-Gebäudeinformationssystem mit Quellenangabe; positioniert als Wissensschicht über bestehenden CDEs (Autodesk ACC, Trimble Connect, Dalux) mit Übergabe an SAP/ERP und CAFM; CH-Gesellschaft in Winterthur; Referenzen u.a. armasuisse Immobilien, Kanton Zug, Kantonsspital Aarau, Axpo -als Vergleichsmassstab für die AIM-Erwartung an die CDE Bund relevant libal-tech   |
|-----|---------|---------|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Markt (Auswahl, zum Vergleich)

|    | Produkt                              | Herkunft   | AIM-Eignung   | Hinweis                                                                                |
|----|--------------------------------------|------------|---------------|----------------------------------------------------------------------------------------|
|  1 | Autodesk Construction Cloud / Tandem | US         | Ja            | Tandem als dediziertes Digital-Twin-/Betriebsphasen-Produkt                            |
|  2 | Bentley iTwin                        | US         | Ja            | Digital-Twin-Plattform                                                                 |
|  3 | Oracle Aconex                        | US         | Nein          | Projekt-CDE (PIM-Fokus), enterprise-etabliert                                          |
|  4 | Thinkproject                         | DE         | Teilweise     | Inkl. Übernahme Conclude (5D/Kosten)                                                   |
|  5 | Dalux                                | DK         | Ja            | Dediziertes FM-Modul                                                                   |
|  6 | Catenda Hub                          | NO         | Teilweise     | openBIM/IFC-nativ, offene API-passt zur Open-Standards-Präferenz                       |
|  7 | Bricsys 24/7                         | BE         | Nein          | CDE mit Dokumenten-Workflow (Hexagon), Projektphasen-Fokus                             |
|  8 | Asite                                | UK         | Teilweise     | Projekt-CDE mit Handover-Funktionen                                                    |
|  9 | Glider TwinView                      | UK         | Ja            | Digital Twin / AIM-Fokus                                                               |
| 10 | Zutec                                | UK/IRL     | Teilweise     | Handover/O&M-Fokus; vormals BuildData Group, Marken seit 2024 unter Zutec konsolidiert |

## Vorteile

- Single Source für Dokumente, Pläne und Modelle-deckt die SOLLTE-Anforderung «Dokumente, Pläne, DMS-/CDE-Anbindung» des Anforderungsdokuments ab
- Strukturierte PIMAIM-Übergabe regelt den Datenfluss Bau  Betrieb (ISO 19650-3) statt Ad-hoc-Übergaben
- Bereits beschafft-kein zusätzlicher Beschaffungsvorlauf, Adapt-Charakter
- Vermeidet den Aufbau eines neuen Schatten-DMS für Portaldokumente

## Nachteile

- Dokument- und modellzentriert, nicht prozess- und self-service-zentriert: kein Fundament für ein Mieterportal mit geführten Anträgen, PrüferQueue und Rollenmodell
- PIM-lastig durch den BIM-Fokus der drei beschaffenden Ämter-die Betriebsphase (AIM) ist mutmasslich nicht das Designziel; AIM-Eignung unbestätigt
- Modularität, Ausbaufähigkeit und API-First-Architektur nicht belegt-als Plattform-Basis nicht annehmbar; bestenfalls Datenquelle über Connector, mit entsprechend höheren Integrationskosten
- Roadmap-Governance über drei Ämter: Selbst wenn die Lösung technisch ausbaufähig wäre, müssen Weiterentwicklungen zwischen BBL, ASTRA und VBS abgestimmt werden-BBL-spezifische AIM-/Betriebsphasen-Anforderungen konkurrieren mit den BIM-/Projektphasen-Prioritäten der anderen Ämter
- Plattform-Ambition (generische Verwaltungs-Use-Cases) nicht erfüllbar
- Drittes Stammdaten-Gravitationszentrum neben SAP ERP und CAFM-die Datenhoheit muss explizit geregelt werden: RE-FX kaufmännisch, CDE /AIM baulich-technisch und dokumentarisch, CAFM betrieblich

Konsequenz: Als Fachsystem-/Datenquellen-Vertical behandeln, nicht als Plattform-Kandidat. Die CDE Bund wird über einen Connector angebunden (Dokumente, Pläne); ihre tatsächlichen AIM- und API-Fähigkeiten sind vor dem Architekturentscheid abzuklären, die Arbeitshypothese «nicht API-first» ist bis dahin als Integrationsrisiko und Kostenfaktor einzuplanen.

## 3.3 Low-Code-/No-Code-App-Plattformen (Buy)

## Proprietäre Plattformen

|    | Produkt                  | Herkunft     | Lizenz / Modell            | Hinweis                                                                                                                             |
|----|--------------------------|--------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Microsoft Power Platform | US           | Kommerziell (SaaS)         | CH-Datenresidenz über Azure Switzerland North/West konfigurierbar; M365-Nähe; CLOUD-Act-Restrisiko bleibt (Datenresidenz Kontrolle) |
|  2 | Mendix                   | DE (Siemens) | Kommerziell                | EU-Eigentümerschaft-von der US-CLOUD-Act-Pauschale auszunehmen; Cloud-Hosting-Modell dennoch prüfen                                 |
|  3 | OutSystems               | US/PT        | Kommerziell                | Enterprise-Low-Code                                                                                                                 |
|  4 | Appian                   | US           | Kommerziell                | Low-Code + Prozess                                                                                                                  |
|  5 | Pega                     | US           | Kommerziell                | Low-Code + Case Management                                                                                                          |
|  6 | ServiceNow               | US           | Kommerziell (SaaS)         | App Engine                                                                                                                          |
|  7 | Salesforce               | US           | Kommerziell (SaaS)         | Plattform-Ökosystem                                                                                                                 |
|  8 | Oracle APEX              | US           | Kommerziell (DB- gebunden) | Bindet an Oracle-DB-Konflikt mit PostgreSQL                                                                                         |

## Open-Source-Plattformen

|    | Produkt   | Herkunft   | Lizenz / Modell         | Hinweis                                                                                    |
|----|-----------|------------|-------------------------|--------------------------------------------------------------------------------------------|
|  1 | Budibase  | UK         | Open-Core (GPLv3 + BSL) | Premium-Features unter Business Source License; self-hosted ab >20 Nutzern lizenzpflichtig |

|   2 | Appsmith   | US/IN   | Apache 2.0 + kommerzielle Editionen   | RBAC, Audit-Logs in Business/Enterprise kostenpflichtig   |
|-----|------------|---------|---------------------------------------|-----------------------------------------------------------|
|   3 | ToolJet    | US/IN   | Open-Core                             | Lizenzstand zum Stichdatum prüfen                         |
|   4 | NocoBase   | CN      | Open-Core                             | Lizenzstand prüfen                                        |
|   5 | Corteza    | EU      | Apache 2.0                            | Generische Plattform, kleine Community                    |
|   6 | Joget      | MY      | Open-Core                             | Workflow + Forms                                          |
|   7 | Baserow    | NL      | MIT/Open-Core                         | EU-Anbieter, Datenbank-/App-Fokus                         |
|   8 | n8n        | DE      | Fair-Code (nicht OSI-konform)         | Workflow-Automation, self-hostbar                         |

## Vorteile

- Sehr schnelle App-Erstellung; bei Power Platform CH-Datenresidenz und M365-Nähe; Marktstandard
- OSS-Varianten self-hosted in CH-Hoheit, PostgreSQL-kompatibel, geringe bis keine Lizenzkosten, reduzierter Lock-in

## Nachteile

- Souveränität bei US-Anbietern ungelöst (CLOUD Act-Datenresidenz  Kontrolle); hoher Lizenz-TCO bei vielen, auch externen Nutzern
- CD Bund / WCAG 2.1 AA nicht nativ; eIAM/AGOV nicht out-of-the-box; Vendor-Lock-in; APEX bindet an Oracle-DB
- OSS-Plattformen ausgelegt auf interne Tools und einfache CRUD-Apps-zu flach für langlaufende BPMN-Prozesse, feingranulare Berechtigungen und die Plattform-Ambition
- Lizenzmodelle der OSS-Plattformen teils Open-Core/BSL im Wandel-Lizenztyp je Produkt zum Stichdatum auszuweisen

Konsequenz: Als Beschleuniger für einzelne interne Tools denkbar, nicht als Plattform-Fundament. Das Vertical gehört trotzdem in die Diskussion, weil Entscheider danach fragen werden.

## 3.4 Portal- und Workflow-/Case-Management-Plattformen (Buy)

Kontext: Dies ist das Vertical, das die ABC-Analyse als Systemvariante Buy bewertet hat. Es liegt zwischen Low-Code und Eigenentwicklung: spezialisierte Plattformen für Portal-, Fall- und Workflow-Führung mit hohem Standardfunktionsumfang.

## CH-/EU-Anbieter mit Behördenfokus

|    | Produkt               | Herkunft   | Fokus                | Hinweis                                                                                                                                                                                                                                                                                                                                |
|----|-----------------------|------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Axon Ivy              | CH         | Behörden CH          | BPMN-basierte Prozessplattform, breite CH-Behördenreferenzen                                                                                                                                                                                                                                                                           |
|  2 | CMI                   | CH         | Behörden CH          | Fall-/Geschäftsverwaltung, stark in CH-Gemeinden und Kantonen                                                                                                                                                                                                                                                                          |
|  3 | Glaux Soft (Evidence) | CH         | Behörden CH          | Fall-/Geschäftsverwaltung (Bern)                                                                                                                                                                                                                                                                                                       |
|  4 | SAP Build Work Zone   | DE         | Portal / Launchpad   | Generische Portalhülle auf BTP, vollständiger Stack nur mit SAP Build Process Automation und Build Apps; Once-Only nativ, vertieft SAP- Lock-in (vgl. 3.1); KO: Betrieb nur auf BTP (Hyperscaler), kein RZ Bund/RHOS - Souveränitätsanforderung nicht erfüllbar; CD Bund nicht nativ; Referenz Kanton Zürich (Advanced Edition) &#124; |
|  5 | ti&m (channel suite)  | CH         | Behörden / Finanz    | Portal-Framework für Verwaltung und Finanzindustrie                                                                                                                                                                                                                                                                                    |
|  6 | Abraxas               | CH         | Behörden CH          | Grösster CH-GovTech-Anbieter, kantonale/kommunale Fachverfahren                                                                                                                                                                                                                                                                        |
|  7 | Fabasoft eGov-Suite   | AT         | E- Governm ent DE/AT | Referenzen Bundesverwaltung DE/AT; CH-Tochter Fabasoft Schweiz AG (vormals 4teamwork)                                                                                                                                                                                                                                                  |
|  8 | Appway (FNZ)          | CH         | Finanz               | Workflow-Plattform, seit Übernahme 2022 Fokus Finanzindustrie                                                                                                                                                                                                                                                                          |

## blocked URLblocked URL

Bild Links: Die Axon Ivy Prozessorchestrierungs-Plattform. Quelle

Bild Rechts: Deep Dive into SAP Build Work Zone. Quelle

## Internationale Anbieter

|    | Produkt           | Herkunft   | Fokus     | Hinweis                                             |
|----|-------------------|------------|-----------|-----------------------------------------------------|
|  1 | ServiceNow        | US         | Generisch | App Engine / Case Management, sehr breiter Standard |
|  2 | Pega              | US         | Generisch | Case-Management-Schwergewicht                       |
|  3 | OpenText AppWorks | CA         | Generisch | BPM/Case Management                                 |

## Vorteile

- Portal-Standardanforderungen meist out-of-the-box: SPOC-Einstieg, rollenbasierte Navigation, Wissens-/Downloadbereiche, Status-/InboxFührung, Aufgabensteuerung, Audit Trail, Reporting-deckt sich mit der Buy-Bewertung der ABC-Analyse
- Reife Produkte mit Referenzen, teils aus der Schweiz (Axon Ivy, CMI, Glaux Soft) mit Behördenfokus
- Konfigurations- statt entwicklungsgetrieben: neue Fallarten oft ohne Programmierung
- Hersteller-Support und Release-Pflege inklusive

## Nachteile

- Beschaffungsvorlauf: Lizenz- und Implementierungskosten überschreiten den WTO-Schwellenwert-für einen schnellen Piloten zeitlich ungeeignet (zentrale Begründung der ABC-Analyse gegen Buy)
- CD Bund und WCAG-2.1-AA-Tiefe nicht nativ; Theming-Spielraum produktabhängig begrenzt
- eIAM/AGOV-Integration projektspezifisch zu realisieren, nicht out-of-the-box
- Souveränität anbieterabhängig: US-Produkte (ServiceNow, Pega) mit CLOUD-Act-Problematik; CH-Produkte besser, aber Deployment-Modell zu prüfen
- Lizenz-TCO skaliert mit Nutzerzahl-kritisch bei vielen externen Portalnutzern
- Lock-in über proprietäre Prozess- und Datenmodelle; Plattform-Ambition nur innerhalb des Produkt-Ökosystems realisierbar

Konsequenz: Fachlich attraktivstes Buy-Vertical und die relevanteste Alternative zu Create-aber für den Pilot durch den Beschaffungsvorlauf blockiert. Bleibt als Option für eine spätere Konsolidierung relevant, falls die Create-Plattform die Wiederverwendungs-Erwartung nicht einlöst.

## 3.5 Best-of-Breed-Stack-Eigenentwicklung (Create)

Kontext: Entspricht der von der ABC-Analyse empfohlenen Systemvariante Create. Als Laufzeitumgebung kommt RHOS (Red Hat OpenShift) beim bundesinternen Leistungserbringer in Frage.

## Beispiel-Stack

|    | Komponente                     | Rolle                     | Hinweis                                                         |
|----|--------------------------------|---------------------------|-----------------------------------------------------------------|
|  1 | Angular + Oblique              | Frontend                  | CD Bund und WCAG nativ; Oblique 15 (02/2026)                    |
|  2 | Operaton oder Flowable-Core    | Prozess-Engine (BPMN 2.0) | Operaton 2.1, Apache 2.0; Flowable AG (Zürich), Apache-2.0-Core |
|  3 | JSON-Schema-/ Form.io-Renderer | Formulare                 | Schema statt Code                                               |
|  4 | PostgreSQL/PostGIS             | Daten                     | Gesetzt (siehe 4.5)                                             |
|  5 | MapLibre                       | Karten                    | Open Source                                                     |
|  6 | Keycloak + eIAM/AGOV           | Auth (OIDC/SAML)          | AGOV über eIAM eingebunden                                      |
|  7 | REST-Connector zu SAP ERP      | Integration               | Leichtgewichtig, Once-Only                                      |
|  8 | RHOS (BIT)                     | Laufzeitumgebung          | Bundesinterner Leistungserbringer                               |

## Vorteile

- Erfüllt als einziger Ansatz alle harten Anforderungen: CD Bund (Oblique nativ), WCAG 2.1 AA, eIAM/AGOV, CH-Hoheit, Open Source, Once-Only
- Volle Souveränität, kein Vendor-Lock-in
- Plattform-Ambition realisierbar: Komponenten nachnutzbar für Use-Case #2+-sofern der Pilot plattform-ready gebaut wird (Formulare als Schema, Prozesse als BPMN, versionierte Layer-Verträge) und nicht passgenau verdrahtet
- Bei Umsetzung durch einen bundesinternen Leistungserbringer entfällt der WTO-Beschaffungsvorlauf (In-house-/In-state-Tatbestand nach Art. 10 BöB)
- Schweizer Umsetzungspartner-Ökosystem für externe Ergänzung vorhanden (Puzzle ITC, Adfinis, Liip, VSHN, Camptocamp-insb. PostGIS/Geo, mimacom-insb. Flowable, u.a.)

## Nachteile

- Eigenleistung und Betriebsverantwortung (Integration, Wartung, Security, Releases)
- Integrationsrisiko mehrerer Komponenten; Architektur-Kompetenz nötig
- Create über externe Dienstleister triggert WTO genauso wie Buy; die interne Vergabe umgeht den Wettbewerb, nicht die KostenfrageKostentransparenz und Lieferantensteuerung müssen die Ausschreibung ersetzen
- Abhängigkeit von der Reife einzelner OSS-Projekte (insbesondere Operaton: junges Projekt, Community-Governance noch im Aufbau)

Konsequenz: Strategisch konsistenteste Variante für die Plattform-Ambition; Bedingung ist plattform-ready by design (Schema statt Code, BPMN statt Hardcoding, versionierte Layer-Verträge), sonst entsteht ein Wegwerf-Pilot statt eines Plattform-Kerns.

## 3.6 Standarddienste des Bundes (Adapt)

Kontext: Entspricht der Systemvariante Adapt der ABC-Analyse: vorhandene Standarddienste nutzen statt beschaffen oder entwickeln.

## Übersicht

|    | Dienst                        | Status 06/2026         | Deckt ab                                 | Hinweis                                                                                                                                                                        |
|----|-------------------------------|------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | eIAM/AGOV                     | Produktiv              | Auth (OIDC/SAML, SSO, passwortlos FIDO2) | eIAM bleibt zentrales IAM des Bundes; AGOV als Identity-Provider darüber eingebunden, löst CH- LOGIN ab; keine Lizenzkosten für Verwaltungseinheiten                           |
|  2 | RHOS (Red Hat OpenShift, BIT) | Produktiv              | Container- Laufzeitumgebung              | Basis für die Create-Variante beim bundesinternen Leistungserbringer                                                                                                           |
|  3 | Swiss Government Cloud (SGC)  | Realisierung 2025-2032 | Künftig Hosting in CH- Hoheit            | Erste produktive Funktionalitäten ab 2027; Verpflichtungskredit CHF 246,9 Mio. (Parlament 12 /2024); EFK-Vorbehalt zum Gesamtnutzen (12/2025)-für ein MVP 2026 nicht verfügbar |

|   4 | BIT-KI «Koby»                                                    | Rollout ab Q1 2026   | Souveräner LLM- Service       | RZ Bund, bis Klassifizierung «vertraulich», RAG vorgesehen                                               |
|-----|------------------------------------------------------------------|----------------------|-------------------------------|----------------------------------------------------------------------------------------------------------|
|   5 | Kantonale/GovTech-Anbieter (Abraxas, ti&m, ELCA, Adnovum, bedag) | Verfügbar            | Ergänzende Umsetzung /Betrieb | CH-Hoheit und Behördenerfahrung, aber teils proprietär; Eignung als generische Plattform projektabhängig |

## Vorteile

- Auth-Baustein eIAM/AGOV gesetzt, produktiv und lizenzkostenfrei für Verwaltungseinheiten
- RHOS als sofort verfügbare Laufzeitumgebung ohne Beschaffungsvorlauf
- Koby und SGC schaffen mittelfristig souveräne KI- und Hosting-Optionen, die in die Create-Variante einfliessen

## Nachteile

- Funktionsabdeckung insgesamt nur gering bis punktuell-keine fachliche Portal-, Prozess- oder Formularfunktionalität
- SGC erst ab 2027 produktiv, Ausschreibungen mehrfach verzögert; Wirtschaftlichkeitsnachweis offen (EFK)
- Koby sehr neu; Schnittstellen für die Einbettung in Fachanwendungen noch zu validieren

Konsequenz: Adapt trägt als Baustein-Lieferant, nicht als Lösungsvariante-eIAM/AGOV, RHOS und künftig Koby/SGC fliessen in die Create-Variante ein; als alleinige Variante ist die Funktionsabdeckung zu gering (Befund der ABC-Analyse, hier bestätigt).

## 4. Optionen je Layer

## 4.1 Frontend Layer

|    | Option                         | Kurzbeschreibung                                | Variante   | Vorteile                                          | Nachteile                                    | Kommentar                                                                                                 |
|----|--------------------------------|-------------------------------------------------|------------|---------------------------------------------------|----------------------------------------------|-----------------------------------------------------------------------------------------------------------|
|  1 | Angular + Oblique              | Offizielles Frontend-Ökosystem des Bundes (BIT) | Create     | CD Bund und WCAG nativ; aktiv gepflegt            | Bindung an Angular und Oblique-Releasezyklen | Oblique 15 (03.02.2026, Angular-21-kompatibel); MIT-Lizenz; direktester Weg zu CD Bund + Barrierefreiheit |
|  2 | Swiss Design System (HTML/CSS) | Framework-neutrales Design- System des Bundes   | Create     | Mit React/Vue nutzbar; CD Bund abgedeckt          | Weniger fertige Interaktionskomponenten      | Open Source; gut kombinierbar mit Option 3                                                                |
|  3 | React/Vue + SDS- Adaption      | Mainstream-Framework mit SDS-Theming            | Create     | Grosser Talentpool; MapLibre- Integration einfach | CD Bund und WCAG in Eigenverantwortung       | MIT-Lizenzen; höherer Eigenaufwand für eCH-0059-Konformität                                               |
|  4 | Vanilla JS / Web Components    | Framework-freie Standard- Webtechnologie        | Create     | Framework-unabhängig, langlebig                   | Wizards/Cockpit aufwändig im Eigenbau        | Kein Lock-in, aber höchster Eigenbau-Anteil                                                               |
|  5 | Kommerzielle UI- Suites        | Fertige proprietäre Komponentenbibliotheken     | Buy        | -                                                 | Eigene Designsprache kollidiert mit CD Bund  | Faktisch ungeeignet; nur der Vollständigkeit halber aufgeführt                                            |

Normativer Anker: eCH-0059 V3.0 (WCAG 2.1 AA, verbindlich seit 21.05.2021). Hinweis: WCAG 2.2 ist seit 10/2023 die aktuelle W3C-Recommendation; eCH-0059 referenziert weiterhin 2.1-bei Neuentwicklungen 2.2 als Zielniveau prüfen.

## 4.2 Prozess Layer

|    | Option         | Kurzbeschreibung                                 | Variante   | Vorteile                                                             | Nachteile                                                                   | Kommentar                                                          |
|----|----------------|--------------------------------------------------|------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------|
|  1 | Camunda 7      | Etablierte BPMN-Engine, Generation 7             | Buy/Create | Reif, grosse Wissensbasis                                            | CE EOL Okt. 2025 (letztes Release 7.24)- Sackgasse für Neuprojekte          | EE-Support bis Apr. 2030, Extended bis 2032; BPMN 2.0              |
|  2 | Camunda 8      | Cloud-native Nachfolge- Generation (Zeebe)       | Buy        | Aktiv weiterentwickelt, skalierbar                                   | Kommerziell; Produktionslizenz seit 8.6 (Okt. 2024); Souveränität zu klären | BPMN 2.0; Lizenz-TCO und Deployment- Modell prüfen                 |
|  3 | Operaton       | Community-Fork von Camunda 7                     | Create     | Souverän, lizenzkostenfrei; API-/Schema- kompatibel mit Camunda 7.24 | Junges Projekt; Community-Governance noch im Aufbau                         | Apache 2.0; v2.1 (04/2026), halbjährliche Release-Kadenz; BPMN 2.0 |
|  4 | CIB seven      | Vendor-getriebener Camunda-7- Fork               | Buy        | Kommerzieller Support für den C7-Pfad                                | Vendor-Abhängigkeit                                                         | CIB (DE); BPMN 2.0; belegt Marktbreite der Fork-Strategie          |
|  5 | Flowable       | BPM-Plattform mit Apache-2.0- Core               | Create/Buy | Reif; Schweizer Hersteller (Flowable AG, Zürich)                     | Open-Core: Enterprise-Features kostenpflichtig                              | Apache 2.0 (Core); BPMN 2.0 + CMMN /DMN                            |
|  6 | Kogito /jBPM   | Cloud-native Prozess-Engine im Red-Hat-Ökosystem | Create     | Apache 2.0; passt zu RHOS                                            | Fokus cloud-native, weniger klassisches Human-Task-Cockpit                  | BPMN 2.0; Red-Hat-Nähe als Plus bei RHOS-Betrieb                   |
|  7 | Bonita         | BPM-Plattform (Bonitasoft, FR)                   | Create/Buy | Etabliert                                                            | Community-Edition begrenzt                                                  | Open-Core; BPMN 2.0                                                |
|  8 | Temporal       | Workflow-as-Code-Engine                          | Create     | Sehr robust für technische Workflows                                 | Kein BPMN-scheidet bei BPMN-2.0-Vorgabe aus                                 | MIT/kommerziell; Code-first-Paradigma                              |
|  9 | SpiffWorkfl ow | Leichtgewichtige Python-BPMN- Library            | Create     | Schlank, einbettbar                                                  | Zu leichtgewichtig für Human-Task-Cockpit                                   | LGPL; BPMN 2.0                                                     |

Kernaussage: Die souveränen, lizenzkostenfreien BPMN-Kandidaten sind Operaton (C7-Erbe, nahtlose Migration ab 7.24; technische Reife durch v2.xKadenz belegt, Community-Governance zu verifizieren) und Flowable-Core (reif, aber Enterprise-Features kostenpflichtig). Camunda 7 ist EOL, Camunda 8 ein Lizenz- und Souveränitätsthema; CIB seven dokumentiert, dass der C7-Fork-Pfad marktbreit getragen wird.

## 4.3 KI Layer

| Option        | Kurzbeschreibung                  | Variante   | Vorteile                                                             | Nachteile                                                                    | Kommentar                                                                         |
|---------------|-----------------------------------|------------|----------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| BIT-KI «Koby» | Souveräner LLM-Service des Bundes | Adapt      | Maximale CH-Souveränität, RZ Bund, bis «vertraulich»; RAG vorgesehen | Sehr neu (Rollout Q1 2026); Schnittstellen für Fachanwendungen zu validieren | Quelloffenes Basismodell in geschützter Zone; bevorzugte Option bei Verfügbarkeit |

|   2 | Apertus (self- hosted)     | Offenes Schweizer LLM der Swiss AI Initiative (EPFL/ETH/CSCS)   | Create   | Vollständig offen (Gewichte, Daten, Trainingsrezepte); mehrsprachig inkl. CH- Sprachen; CH-Hoheit   | Nicht auf Niveau kommerzieller Spitzenmodelle; Hosting/GPU selbst stellen   | Apache 2.0; Modelle 8B/70B; erste Behördenreferenz Kanton Tessin   |
|-----|----------------------------|-----------------------------------------------------------------|----------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------|
|   3 | Self-hosted OSS-RAG- Stack | Eigenbetriebene Retrieval-/RAG- Pipeline                        | Create   | Volle Kontrolle; kombinierbar mit Koby/Apertus                                                      | Eigenleistung; Human-in-the-Loop zwingend                                   | Komponenten Apache-2.0-/MIT- Ökosystem                             |
|   4 | US-LLM-APIs                | Kommerzielle Cloud-LLMs                                         | Buy      | -                                                                                                   | Scheiden bei vertraulichen Mieterdaten aus Souveränitätsgründen aus         | CLOUD-Act-Problematik; nur der Vollständigkeit halber aufgeführt   |

Für den MVP optional (SOLLTE gemäss Anforderungsdokument); souverän nachrüstbar.

## 4.4 Integration Layer

|    | Option                          | Kurzbeschreibung                                        | Variante   | Vorteile                                                                         | Nachteile                                                     | Kommentar                                                  |
|----|---------------------------------|---------------------------------------------------------|------------|----------------------------------------------------------------------------------|---------------------------------------------------------------|------------------------------------------------------------|
|  1 | Eigener REST- Connector-Service | Massgeschneiderter Microservice für die RE-FX-Anbindung | Create     | Exakt zugeschnitten, minimaler Footprint; volle Kontrolle über Retry/Dead-Letter | Eigenentwicklung und Wartung                                  | Passend zur Once-Only-Architektur mit RE-FX als Leitsystem |
|  2 | Apache Camel                    | OSS-Integrationsframework mit EIP- Patterns             | Create     | Hunderte Konnektoren; souverän                                                   | Lernkurve; für ein einzelnes Interface ggf. überdimensioniert | Apache 2.0; sinnvoll ab mehreren Schnittstellen            |
|  3 | SAP Integration Suite / CPI     | SAP-eigene iPaaS auf BTP                                | Buy        | Native SAP-Unterstützung                                                         | Lizenz-/BTP-Kosten; Souveränität zu prüfen; Lock-in           | Kommerzielle Lizenz; Cloud- Deployment-Modell klären       |
|  4 | FME                             | Datentransformations-Plattform (Safe Software)          | Buy        | Stark bei Geodaten-Transformation                                                | ETL/Geo, nicht Prozessintegration                             | Kommerzielle Lizenz; ggf. Synergien mit GIS-Vorhaben       |
|  5 | WSO2-Vollstack                  | Umfassende API-Management- Plattform                    | Create/Buy | Vollständiges API-Management                                                     | Fürs MVP überdimensioniert                                    | Apache 2.0; bewusst ausgeschlossen                         |
|  6 | iPaaS (generisch)               | Cloud-Integrationsdienste                               | Buy        | Schnell einsatzbereit                                                            | Souveränität bei US-iPaaS kritisch; laufende Kosten           | CLOUD-Act-Prüfung je Anbieter                              |

## 4.5 Data Layer

PostgreSQL/PostGIS ist faktisch gesetzt. Offene Frage ist nur das Betriebsmodell:

|    | Option                          | Kurzbeschreibung                                     | Variante     | Vorteile                        | Nachteile                          | Kommentar                                                                  |
|----|---------------------------------|------------------------------------------------------|--------------|---------------------------------|------------------------------------|----------------------------------------------------------------------------|
|  1 | Self-hosted PostgreSQL /PostGIS | Eigenbetrieb im RZ Bund / bei Betriebspartner CH     | Create/Adapt | Volle Hoheit; passt zu ISG/ISDS | Betriebsverantwortung inklusive    | PostgreSQL-Lizenz (permissiv); auf RHOS beim BIT betreibbar                |
|  2 | Managed PostgreSQL in CH-Hoheit | Verwalteter DB-Dienst eines CH- souveränen Anbieters | Buy          | Weniger Betriebsaufwand         | SGC-Managed-Angebote erst ab ~2027 | Bis dahin nur CH-souveräne Anbieter; Anbieter- Souveränität je Fall prüfen |

## 4.6 Anwendungen / Fachsysteme

- SAP ERP bleibt Leitsystem. Die Plattform liest per REST und hält keine konkurrierenden Stammdaten (Once-Only).
- CDE Bund (in Einführung, gemeinsam BBL/ASTRA/VBS): Datenquelle für Dokumente, Pläne und Modelle, Anbindung über Connector; AIM- und API-Fähigkeiten vor dem Architekturentscheid abklären, siehe 3.2.
- CAFM (falls beschafft): als FM-Fachsystem abgegrenzt anbinden, siehe 3.1.

## 5. Einordnung

- Kein Buy-Produkt erfüllt das Anforderungsdokument vollständig. CAFM scheitert an Plattform-Ambition und Once-Only, Low-Code an Souveränität, TCO und Tiefe; Portal-/Case-Management-Plattformen sind fachlich das stärkste Buy-Vertical, scheitern für den Pilot aber am Beschaffungsvorlauf.
- Die Create-Variante (Best-of-Breed-Stack) ist die strategisch konsistenteste Variante für die Plattform-Ambition («Plattform-ready by design»)deckungsgleich mit der Empfehlung der ABC-Analyse. Preis: Eigenleistung, Betriebsverantwortung und-bei externer Umsetzung-WTO-pflichtige Dienstleistungsbeschaffung. Bedingung: Der Pilot muss plattform-ready gebaut werden (Schema statt Code, BPMN statt Hardcoding, versionierte Layer-Verträge), sonst entsteht ein Wegwerf-Pilot statt eines Plattform-Kerns.
- Adapt trägt als Baustein-Lieferant, nicht als Lösungsvariante-eIAM/AGOV, RHOS und künftig Koby/SGC fliessen in die Create-Variante ein; als alleinige Variante ist die Funktionsabdeckung zu gering (Befund der ABC-Analyse, hier bestätigt).
- Die Prozess-Engine-Frage ist 2024-2026 neu zu beantworten: Camunda 7 EOL, Camunda 8 kommerziell-Operaton (v2.1) und Flowable-Core sind die verbleibenden souveränen BPMN-Optionen, CIB seven der kommerzielle Fork-Pfad. Diese Entscheidung ist in der ABC-Analyse nicht adressiert und gehört in den Umsetzungsauftrag der Create-Variante.
- CAFM-Beschaffung, CDE/AIM und Plattform-Ambition sind kein Widerspruch, wenn sauber abgegrenzt: CAFM = FM-Fachsystem, CDE/AIM = Dokument-/Modell-Leitsystem (baulich-technisch), Plattform = wiederverwendbarer Use-Case-Baukasten, RE-FX = kaufmännisches StammdatenLeitsystem.

## 6. Offene Punkte

- Operaton-Governance und Support-Struktur vor Produktiventscheid verifizieren-technische Reife durch v2.x belegt, die rechtliche Verankerung der Community-Trägerschaft ist im Aufbau (Fallback: Flowable-Core)
- Plattform-Capabilities (Kap. 3 Anforderungsdokument) verbindlich in den Create-Umsetzungsauftrag aufnehmen-inkl. Prozess-Engine-Entscheid und versionierter Layer-Verträge
- Kostentransparenz der internen Vergabe sicherstellen: Pilot-Scope, Plattform-Kern und Folgekosten je Use-Case getrennt ausweisen
- Funktionsumfang der CDE Bund konkret abklären: AIM-/Betriebsphasen-Eignung, Modularität, verfügbare APIs und Export-Formate, Lizenzfolgen bei API-Nutzung, Governance der Weiterentwicklung über BBL/ASTRA/VBS-bestimmt Connector-Kosten und die Belastbarkeit der Arbeitshypothese «nicht API-first»
- CH-Hosting-Aussagen der CAFM-Anbieter im Beschaffungsfall konkret abklären (nur CAMPOS garantiert explizit); Anbieterangaben Axentris /Servalino, SPARTACUS (GEFMA-444) und die Abgrenzung IMSWARE/iTWO fm verifizieren
- Koby-Schnittstellen für die Einbettung in Fachanwendungen prüfen (Rollout ab Q1 2026)
- SGC-Zeitplan und EFK-Wirtschaftlichkeitsanalyse 2026 beobachten (produktiv ab 2027, Ausschreibungen mehrfach verzögert)
- eCH-0059-Entwicklung beobachten (mögliche Aktualisierung auf WCAG 2.2)
- Lizenzpreise wurden bewusst nicht erhoben-mengen- und beschaffungsabhängig, im WTO-Verfahren einzuholen

## 7. Verweise und Anhang

## 7.1 Verweise

TBD (mindestens aufzunehmen: Anforderungsdokument, ABC-Analyse Lösungsarchitektur Pilot, eCH-0059 V3.0, BöB Art. 10/15, InöB-Schwellenwerte 2026-2027)

## 7.2 Anhang

| Datei                             | Geändert                       |
|-----------------------------------|--------------------------------|
| PNG-Datei Management Summary.png  | 11.06.2026 by Rasner David BBL |
| PNG-Datei Marktsegemente.png      | 11.06.2026 by Rasner David BBL |
| PNG-Datei Kibanda-Illu-Screen.png | 11.06.2026 by Rasner David BBL |

Ziehen Sie Dateien an diese Stelle, um sie hochzuladen, oder Dateien suchen Alle herunterladen