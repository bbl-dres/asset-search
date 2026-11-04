## Beispielarchitekturen und Referenzen

| Titel           | Beispielarchitekturen und Referenzen: Mieterportal als MVP   |
|-----------------|--------------------------------------------------------------|
| Author          | David Rasner BBL                                             |
| Status          | Entwurf                                                      |
| Stand           | 11.06.2026                                                   |
| Klassifizierung | Intern                                                       |

## Inhalte:

## Management Summary

1. Ziel des Dokuments
2. Fallbeispiele Schweiz
3. 2.1 SBB Immobilien - Mieterportal «myPortal»
4. 2.2 VBS «Immo-Portal» - das Gegenbeispiel (SharePoint-Auflösung)
5. 2.3 Mietendenportal - Stadt Zürich
6. 2.4 EPFL - Immobilien-IT (ServiceNow, Archibus, Geoportal)
7. 2.5 eBau by inosca - interkantonale Baubewilligungsplattform
8. 2.6 iGovPortal.ch - interkantonaler virtueller Schalter
9. 2.7 ETH Zürich - Real Estate Management (GMIS, ETHIS)
10. 2.8 BImA «meine BImA» - das deutsche Pendant zum BBL
11. 2.9 eBaugesucheZH - Kanton Zürich
12. 2.10 ZHAW-Studie Service-Portale (2025) - Marktüberblick CH
13. 2.11 IGE - Camunda als BPMN-Engine in einer Bundesinstitution
3. Fallbeispiele Deutschland
15. 3.1 OZG-Hub (Baden-Württemberg + Sachsen)
16. 3.2 Dataport OSI / OZG-Cloud + FIT-Connect (FITKO)
17. 3.3 GovForms 2.0 / Wirtschaftsservice-Portal.NRW
18. 3.4 Bundesagentur für Arbeit + Stadt München - Camunda
19. 3.5 Operaton &amp; CIB seven - Souveränität auf Engine-Ebene
4. Fallbeispiele Österreich
21. 4.1 oesterreich.gv.at / Digitales Amt (BRZ)
22. 4.2 aforms / AFORMSOLUTION - Formularserver CH/AT/LI
5. Internationale Benchmarks
6. Synthese: Wiederkehrende Muster
7. Abweichungen und offene Punkte
8. Verweise und Anhang

8.1 Verweise

- 8.2 Anhang

## Management Summary

Das Dokument belegt anhand produktiver Fallbeispiele (CH, DACH, international), dass das Architekturmuster des Mieterportals: geführte Formulare Prozess-Engine  eigene Datenhaltung  Fachsystem-Integration etablierte Verwaltungspraxis ist, kein Experiment. Es ergänzt Marktscreening (Produktsicht) und Referenzbericht (Beschaffungssicht) um die Architektursicht.

Die nächstliegende Open-Source-Blaupause ist der inosca/eBau-Stack (6 Kantone, PostgreSQL/Keycloak); die genaueste Validierung der PlattformAmbition der OZG-Hub (~500'000 Anträge im ersten Jahr); die fachlich identische Domäne belegen SBB und Stadt Zürich (Kibanda auf RE-FX) produktiv, aber als geschlossenes Vertikalprodukt. Das VBS-«Immo-Portal» (Word-Formulare, E-Mail-Umlauf) zeigt als Kontrastfall die Reifegradstufe, die das Vorhaben überwinden soll.

Sechs wiederkehrende Muster bestätigen die Anforderungen: Layer-Trennung, Schema statt Code, souveräne Open-Source-Engines, Keycloak + eIDBroker, Once-Only über Austauschschicht, gemeinsame Trägerschaft mit expliziter Governance. Einschränkungen: inosca ohne BPMN, einzelne Stacks nicht verifiziert, Anbieterreferenzen nur Existenzbelege. Erfahrungsaustausch mit inosca/Adfinis und SEITENBAU ist möglich und empfohlen.

<!-- image -->

Bild: Zusammenfassung Beispielarchitekturen

## 1. Ziel des Dokuments

Dieses Dokument sammelt Fallbeispiele aus der öffentlichen Verwaltung (DACH-Raum prioritär, ergänzt um internationale Referenzen), die das Architekturmuster des Mieterportals bereits produktiv umgesetzt haben: Portal mit geführten Formularen  Prozess-Engine  eigene Datenhaltung , inkl. der Querschnittsthemen IAM, Barrierefreiheit, Design-System und digitale Souveränität. Integration in bestehende Fachsysteme

Es beantwortet je Fallbeispiel drei Fragen: hat gebaut, wollte die Organisation erreichen, wurde es gelöst (Stack, Partner, Ergebnis). Das Wer was wie Dokument ergänzt das Marktscreening (Produktsicht) und den Referenzbericht Vergaben (Beschaffungssicht) um die Architektursicht umgesetzter . Der fachliche Use-Case muss dabei nicht Immobilien sein - relevant ist das wiederkehrende Muster «Antrag  Prüfung  Freigabe». Lösungen

## Lesehilfe:

<!-- image -->

| Rating   | Bedeutung                   |
|----------|-----------------------------|
|          | direkt übertragbares Muster |
|          | Teilaspekte übertragbar     |
|          | Kontext / Benchmark         |

## 2. Fallbeispiele Schweiz

## 2.1 SBB Immobilien - Mieterportal «myPortal»

| Rele   | - grösster bundesnaher Immobilienbewirtschafter mit produktivem Mieterportal auf SAP-RE-FX-Basis; dasselbe Produkt wie Stadt Zürich (Kibanda)   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| vanz   |                                                                                                                                                 |

| Links   |                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|         | Landing page: https://portal.sbb-immobilien.ch Login: https://sbb-immobilien.ch/login/ Onboarding: (Onboarding Privatkunden) https://sbb-immobilien.ch/faq/pk-onboarding/ https://sbb-immobilien.ch/faq/gk-onboarding/ (Geschäftskunden inkl. Admin-/Delegationsmodell) Fallstudie bei Kibanda: (inpeek-Fallstudie) https://kibanda.ch/mieterkommunikation-neu-gedacht/                                                                                    |
| Wer     | SBB Immobilien; Produkt Kibanda von inpeek AG - dritter öffentlicher/bundesnaher Kunde desselben Produkts neben LSZ und Stadt Bern                                                                                                                                                                                                                                                                                                                         |
| Ziel    | Self-Service für Mietende (Privat- und Geschäftskunden) im Rahmen der S/4HANA-Migration von SBB Immobilien                                                                                                                                                                                                                                                                                                                                                 |
| Lös ung | Login via SwissPass als Identity Provider; Registrierung durch Verknüpfung des SwissPass-Kontos mit Kunden-/Mietvertragsnummer; Funktionen: CFF Immobilier Schäden melden, Anfragen und Bestellungen (Rechnungen, Untermiete, Mietparteien anpassen, Schlüssel), Dokumente downloaden, Rechnungen anzeigen, Notfallkontakte pflegen; für Geschäftskunden ein Administratoren-Modell mit Selbstverwaltung der Berechtigungen pro Unternehmen CFF Immobilier |
| Les son | Zwei Muster, die das BBL Anforderungsdokument direkt bestätigen: (1) bestehendes Konzern-IAM (SwissPass) als IdP wiederverwendet statt eigene Identität gebaut - Parallele zu eIAM/AGOV; (2) das (Organisation hat Admin, der Mitarbeitende berechtigt) ist genau das Geschäftskunden-Delegationsmodell Rollenmuster, dass das BBL für mietende Verwaltungseinheiten braucht - bei LSZ (nur Privatmietende) fehlt dieses Muster, bei SBB ist es produktiv  |

<!-- image -->

<!-- image -->

Bild Links: Objektübersicht

Bild Recht: Objektkennzahlen und Karte

## 2.2 VBS «Immo-Portal» - das Gegenbeispiel (SharePoint-Auflösung)

| Relevanz   | als Kontrastfall - der direkte VILB-Schwester-BLO zeigt den Ist-Zustand ohne Prozessplattform                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links      | https://www.ar.admin.ch/de/immo-portal · Ausbildungsmodul 4 «Immo-Portal VBS» (PDF auf derselben Seite) Bedarfsformulierung/Bedarfsvoranmeldung (Word-Downloads ebd.) |

| Wer                     | armasuisse Immobilien als Eigentümervertreter; Rollenmodell mit Nutzer (Armee), Mieter (Armeestab), Betreiber, LE IKT                                                                                                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Was es ist              | Kein Software-Portal, sondern eine : Rollen-, Aufgaben- und Steuerungsmodell, Weisungen (WIRU, WIV, ZUVA), Governance- und Dokumentenseite Kostentabelle, Unterschriftenregelung                                                                                                                                       |
| Wie die Prozesse laufen | Bedarfsvoranmeldung und Bedarfsformulierung als zum Download, Raumbedarf Global 2.0 als ; Arbeitsinstrumente intern: Word-Formulare Excel-Vorlage Immo V (Intranet), ImmoGIS, IMS ar, GEVER - und «armaform» auf , also der SharePoint-Collaboration-Plattform des Bundes portal.collab.admin.ch (nur für Berechtigte) |
| Lesson                  | Das VBS wickelt die militärischen Immobilienstandards und Formularprozesse über Bundes-SharePoint und Office-Dokumente ab. Der fachlich identische Prozess zu der BBL Bedarfsmeldung (Bedarfsvoranmeldung Bedarfsformulierung Lösungsstrategie) existiert beim VBS als Word-Formular mit E-Mail- Umlauf                |

## blocked URL

Bild Links: Rollenmodell VBS

## 2.3 Mietendenportal - Stadt Zürich

| Rele vanz   | - fachlich identische Domäne (Mieterportal öffentliche Hand, RE-FX-Integration); Buy-Kontrast zur Create-Variante                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://www.stadt-zuerich.ch/de/lebenslagen/wohnen/mietendenportal.html https://kibanda.ch/zukunftsweisende-loesung-fuer-die-liegenschaftsverwaltung/ (Fallstudie mit Architekturdetails) https://kibanda.ch/was-ist-kibanda/ https://www.it-beschaffung.ch/it/1198767/lsz003-bewirtschaftungs-und-mieterportal (Zuschlag) https://www.it-beschaffung.ch/it/1167169/lsz003-bewirtschaftungs-und-mieterportal (Ausschreibung 12/2020)                                                                                           |
| Wer         | Liegenschaften Stadt Zürich (LSZ, Finanzdepartement); Produkt Kibanda von inpeek AG, Bern (SAP Gold Partner) - derselbe Anbieter wie Referenz #1 (Hochbaudepartement IMMO-Workflow)                                                                                                                                                                                                                                                                                                                                            |
| Ziel        | Professionalisierte Kommunikation Mietende Bewirtschaftung (Schadensmeldungen, Tickets), 24/7-Erreichbarkeit, Entlastung der Bewirtschaftung von Administrativaufgaben                                                                                                                                                                                                                                                                                                                                                         |
| Lös ung     | Buy: Kibanda als RE-FX-Add-On. Kibanda Go (Web-App auf Azure, Keycloak/OAuth 2.0, Login via städtisches «Mein Konto») für Mietende; Kibanda Cockpit (SAP Fiori) intern; Echtzeit-Anbindung an S/4HANA, PM/MM und RE-FX via OData Principal Propagation - keine Datenkopien, SAP-Rollenmodell nachgenutzt                                                                                                                                                                                                                       |
| Erg ebnis   | Produktiv für 20'000 Mietende und 100 Mitarbeitende. Vergabe: offene Ausschreibung 12/2020, Zuschlag CHF 650'880 exkl. MwSt. für 10 Jahre (Implementierung, Lizenz, Wartung, Support inkl. Optionen)                                                                                                                                                                                                                                                                                                                           |
| Les son     | Once-Only gegen RE-FX, Keycloak-IAM und zentrales Bürgerkonto sind produktiv belegt - aber als geschlossenes SAP-Vertikalprodukt: stark für den Ticketing- Use-Case, keine wiederverwendbare Plattform für weitere Verwaltungsleistungen. Illustriert die Buy-Grenze aus dem Marktscreening (Kap. 3.1) am fachlich nächstliegenden Fall. Funktionsumfang deutlich schmaler als unser MVP-Scope (keine geführte Bedarfsmeldung, kein Raumprogramm, keine Prüfer-Queue) - der tiefe 10-Jahres-Preis ist entsprechend einzuordnen |

Video: Mietendenportal der Stadt Zürich. Quelle

## 2.4 EPFL - Immobilien-IT (ServiceNow, Archibus, Geoportal)

| Rele vanz   | - vierter VILB-naher Immobilienakteur (ETH-Bereich); Zielmuster produktiv, aber als komponierter Stack statt Plattform; Open-Source-Geoportal als Nebenreferenz                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | DII: https://www.epfl.ch/about/vice-presidencies/fr/vice-presidences/vice-presidence-pour-les-ressources-humaines-et-operations/domaine-immobilier-et- infrastructures/ AREMIS-Fallstudie: https://www.aremis.com/fr/resultats/epfl-archibus-gestion-patrimoine-solution Camptocamp-Referenz: https://camptocamp.com/en/customer-journeys/customer-journey-epfl Routing-Architektur: https://camptocamp.com/en/news-events/route-planning-with-online-graph-editing ServiceNow-Referenz: https://www.servicenow.com/fr/customers/epfl.html                                                                                                                                  |
| Wer         | EPFL, Vice-Présidence Opérations (VPO) / Domaine Immobilier et Infrastructures (DII); Campus Lausanne ~80 Gebäude, ~700'000 m², ~10'000 Räume; Partner: AREMIS (Archibus), Camptocamp (Geoportal), PocketCampus (App)                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Ziel        | Self-Service für Schadens-/Interventionsmeldungen, Ablösung obsoleter Wartungs- und Projekt-Tools (Vergabe 2020), Flächen-/Wartungs-/Projektmanagement, Campus-Orientierung inkl. Indoor-Navigation                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Lös ung     | Komponierter Stack statt Suite: (SaaS, CH-Hosting) als Antragsportal und Workflow-Schicht für «demandes d'intervention»; (Eptura) als ServiceNow Archibus CAFM-Fachdatenhaltung (Flächen, Wartung, Projekte, Gefahrenblätter je Raum), eingeführt nach öffentlicher Ausschreibung 2020; interne Module «Cristal GMAO /Locaux» mit granularem Rollenmodell; Schnittstellen zu IS-Academia (Raumdaten) und ERP/HR. Daneben eigenes ( , seit 2001): Geoportal plan.epfl.ch GeoMapFish/c2cgeoportal (Open Source), PostgreSQL/PostGIS, pgRouting (A*-Indoor-Routing über Stockwerke/Treppen/Aufzüge), MapFish Print, FME, Docker; Routing-Graph seit 2021 webbasiert editierbar |
| Erg ebnis   | ServiceNow-Portal produktiv mit hoher Nutzerzufriedenheit (88% über drei Jahre, Anbieterquelle); Archibus zentrales Tagesinstrument der Technikteams; Geoportal 20+ Jahre produktiv; RFI zur Erneuerung/Ablösung der Geoportal-Infrastruktur publiziert (Marktabklärung, noch keine Ausschreibung)                                                                                                                                                                                                                                                                                                                                                                          |

## Les son

Die EPFL belegt das Zielmuster mit getrennten Schichten: generische Workflow-Plattform vorne (ServiceNow), spezialisiertes Fachsystem hinten (Archibus), Integration als eigene Schicht - das Portal muss nicht im CAFM gebaut werden. Zugleich Buy-Kontrast zur ETH Zürich (Planon/GMIS): gleiches Muster, anderes Produkt, kein gemeinsames ETH-Rat-System - selbst im ETH-Bereich gibt es keine erzwungene Vereinheitlichung, was die BLO-Autonomie im Lösungsentscheid stützt. Das Geoportal zeigt Open-Source-GIS mit eigener Datenhaltung (PostGIS) als langjährig tragfähige, herstellerunabhängige Option - relevant als KartenLayer-Referenz, nicht als Mietprozess-Vorbild. Kein dediziertes Mieterportal: «Mieter» sind interne Einheiten, kein AntragPrüfungFreigabe-Workflow mit Rückschreiben ins CAFM aus Primärquelle belegt

<!-- image -->

Bild: EPFL Campus App. Quelle

## 2.5 eBau by inosca - interkantonale Baubewilligungsplattform

## Rele vanz

## Links

- nächstliegende Open-Source-Blaupause für unser Zielmuster

- https://inosca.ch
- https://github.com/inosca/ebau (Quellcode)
- https://caluma.io + https://github.com/projectcaluma/caluma (Engine)
- https://www.gr.ch/DE/institutionen/verwaltung/dvs/are/projekte/Seiten/Elektronisches-Baubewilligungsverfahren-(eBBV).aspx (Einführung GR inkl. WTOVergabe)
- https://www.adfinis.com/de-ch/news/adfinis-gewinnt-ausschreibung-des-kantons-aargau-zur-implementierung-von-ebau-mit-inosca (Ablösung SAP-Lösung AG)
- https://www.bauen.dij.be.ch/de/start/baubewilligungsverfahren/eBau/betriebsseite.html (Betrieb BE)
- https://dinacon.ch/sessions/2021/inosca-die-kantonale-open-source-community/ (Community-Vortrag)

Wer inosca-Community: Kantone UR, SZ, SO, BE, GR, AG; Umsetzungs-/Betriebspartner Adfinis AG (GR: offene WTO-Submission 2022, AG: Ausschreibung 2024)

- Ziel Durchgängig digitales Baubewilligungsverfahren als gemeinsame, herstellerunabhängige, wiederverwendbare Plattform; im Aargau Ablösung einer SAP-Altlösung (Projekt DIBA)

Lös ung Ember.js-Frontends (Antragsportal + Behördenbereich); Backend Python/Django mit GraphQL; Form-/Workflow-Engine (Open Source GPL-3.0, Caluma formularzentriert - kein BPMN); ; als IAM mit kantonalen Logins (BE-Login, via Token Exchange, -Konto); document-mergePostgreSQL Keycloak my.so.ch ag.ch service für Dokumenterzeugung; GWR-Sync; eCH-0211; vollständig quelloffen

Erg ebnis Produktiv in 6 Kantonen; SZ wickelt seit 12/2022 alle &gt;2'000 Baugesuche/Jahr ausschliesslich elektronisch ab; BE verpflichtet seit 03/2022 zur OnlineEinreichung; GR-Rollout in drei Gemeindestaffeln ab 2024

## Les son

Das exakte Zielmuster (Portal + Form-Engine + PostgreSQL + Keycloak, Open Source, Schweizer Verwaltung, mehrkantonale Wiederverwendung) existiert produktiv und quelloffen. Caluma zeigt zugleich, dass eine formularzentrierte Engine eine Alternative zu BPMN ist (Abweichung von unserer BPMN-2.0-Vorgabe, siehe Kap. 8)

<!-- image -->

Video Links: Inosca für elektronische Bewilligungsprozesse. Quelle

Bild Rechts: Lösungsarchitektur. Quelle

## 2.6 iGovPortal.ch - interkantonaler virtueller Schalter

| Rele vanz   | - «Portal ohne eigene Stammdaten» + Trägerschaftsmodell                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://www.igovportal.ch https://www.igovportal.ch/de/Wer-sind-wir/Mitglieder/Mitglieder.html (Mitgliedschaftsmodell) https://www.zhaw.ch/storage/sml/News/ZHAW-Studie-Service-Portale-09_2025.pdf (Studienvergleich) https://www.sg.ch/news/sgch_allgemein/2020/05/digitalen-schalter-gemeinsam-weiterentwickeln.html (Beitritt SG inkl. Kostenmodell) https://www.inside-it.ch/auch-kanton-basel-landschaft-will-igovportal-einfuehren-20220530 (Verbreitung) |
| Wer         | Verein (gegründet 2017 durch FR/JU); heute 8 Mitgliedskantone (BL, FR, GR, JU, LU, SG, SO, VS), GL zuletzt mit Gaststatus. Nur Kantone können iGovPortal.ch beitreten; Gemeinden eines Mitgliedskantons nutzen die Lösung über ein erweitertes Lizenzrecht frei                                                                                                                                                                                                  |
| Ziel        | Gemeinsamer virtueller Amtsschalter mit SSO und Once-Only; Investitionsteilung zwischen Kantonen                                                                                                                                                                                                                                                                                                                                                                 |
| Lös ung     | Modulare, technologieoffene Architektur; On-Premises je Kanton; persönliches Cockpit mit Status-/Etappenverfolgung; keine dauerhafte Falldatenspeicherung - Daten verbleiben in den Fachsystemen; Identity Broker vorgeschaltet (SO: USP Secure Entry Server); Formular-Layer via aforms; Integratoren: Softcom, ti&m, Artionet                                                                                                                                  |

## Erg ebnis

## Les son

FR: ~60 End-to-End-Dienste. Governance als Verein mit gleichberechtigter Stimme je Kanton in technischer Kommission, Führungsausschuss und GV; jährliche Weiterentwicklungen werden durch alle Mitglieder freigegeben. Kosten (Beleg SG, 2020): CHF 20k/Jahr Vereinsbeitrag + ~CHF 68k/Jahr Wartung/Support, sinkend mit jedem Beitritt

«Einmal entwickeln, mehrfach nutzen» funktioniert mit Vereins-Governance; das Prinzip «Portal hält keine Stammdaten, Fachsysteme bleiben Leitsysteme» entspricht 1:1 unserem Once-Only-Ansatz. Das Freigabemodell (jede Weiterentwicklung braucht Konsens aller Mitglieder) zeigt zugleich den Preis gemeinsamer Trägerschaft: Geschwindigkeit gegen Mitbestimmung

## Einevolution?resSchweizerSackmesser

Digitalisierung von Verwaltungsdiensten ermoglichen:

<!-- image -->

DieseBasisdienstesindseparatverfugbarundkonnennachWunsch integriert werden.Jenachden strategischenEntscheidungenderKantonekonnen auch andereaufdemMarkterhaltlicheStandardDienstleistungen(SwisslD,Formular-Editor,Scanning-Losung,usw.) in dieLosung integriert werden. durfnissendesE-Governmentsgerechtzuwerden.

Video Links: iGovPortal.ch - Kanton St. Gallen. Quelle

Bild Rechts: IGovPortal - Modulare Onlineschalter Lösungen für Ihr iE-Government. Quelle

## 2.7 ETH Zürich - Real Estate Management (GMIS, ETHIS)

| Rele vanz   | - dritter VILB-BLO (ETH-Rat), Meldeportal-Muster produktiv, Stack nicht öffentlich                                                                                                                                                                                                                                                                                                                                                                    |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://ethz.ch/staffnet/de/service/raeume-gebaeude.html (Service-Übersicht) https://ethz.ch/de/die-eth-zuerich/organisation/abteilungen/immobilien.html https://amstein-walthert.ch/de/projekte/immobilienbewirtschaftung-eth-zuerich/ (Projekt Auftragsmanagement) ETH App: https://play.google.com/store/apps/details?id=ch.ethz.ethz&hl=de&pli=1                                                                                                  |
| Wer         | ETH Zürich Real Estate Management, Portfolio ~CHF 5 Mrd.                                                                                                                                                                                                                                                                                                                                                                                              |
| Lös ung     | Meldeportal für die Bedürfniserfassung von Mitarbeitenden und Studierenden, das Papierformulare ablöste: elektronische Formulare je Bedürfnistyp, Statuseinsicht für Meldende, einheitliche Arbeitsplanung über Abteilungen hinweg, Reports fürs Management; daneben GMIS (Gebäudedaten- Amstein-walthert Bestellung) und ETHIS (Rauminformationen je Organisationseinheit); Anträge für Flächenbedarf und bauliche Massnahmen über Staffnet-Prozesse |
| Les son     | Das Muster «geführtes Formular Status interne Queue» ist beim dritten Bundes-Immobilienorgan ebenfalls umgesetzt - allerdings fragmentiert über mehrere Tools (GMIS, ETHIS, Meldeportal) statt als Plattform. EPFL ist öffentlich nicht separat dokumentiert; der ETH-Bereich wäre ein Fall fürs Durchfragen via ETH-Rat                                                                                                                              |

<!-- image -->

Bild Links: Service Übersicht, ETH Zürich.  Quelle

Bild Rechts: ETH App. Quelle

## 2.8 BImA «meine BImA» - das deutsche Pendant zum BBL

| Rele vanz   | - der Bundes-Immobilienverwalter Deutschlands (38'300 Wohnungen) mit Konto-basiertem Serviceportal                                                                                                                                                                                                                                                                                                                                |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://meine-bima.bundesimmobilien.de https://www.bundesimmobilien.de/wohnen-d104bdac29f04109 (Reparaturservice) https://www.bundesimmobilien.de/neuer-zugang-zu-den-immobilienangeboten-ueber-das-portal-meine-bima-aaaf2821896556ba (Einführung 2024)                                                                                                                                                                          |
| Wer         | Bundesanstalt für Immobilienaufgaben (BImA), Geschäftsbereich Wohnen                                                                                                                                                                                                                                                                                                                                                              |
| Lös ung     | Zentrales Konto «meine BImA» als persönlicher Zugang zum Immobilienportal, eingeführt 2024 - auch weil der bisherige Zugang von der IT-Sicherheit als teilweise nicht sicher eingestuft wurde; Reparaturservice für Schadensmeldungen rund um die Uhr an 365 Tagen, Immobilienportal mit Bundesimmobilien Wohnungsfürsorge für Bundesbedienstete; Portalbereiche Profil, Schadenmanagement, Business-Anwendungen Bundesimmobilien |
| Les son     | Der direkte deutsche Peer macht denselben Move (zentrales Konto + Schadens-Self-Service), Antrags-/Vergabeprozesse der Wohnungsfürsorge laufen aber weiterhin formular- und vergabestellen-basiert - auch hier: Ticketing digitalisiert, Antragsworkflows nicht. Stack nicht öffentlich                                                                                                                                           |

## 2.9 eBaugesucheZH - Kanton Zürich

| Relev anz   | - Buy-Kontrast im selben Fachgebiet (proprietär vs. Open Source)   |
|-------------|--------------------------------------------------------------------|

| Links                                       |                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Wer                                         | https://www.zh.ch/de/planen-bauen/baubewilligung/elektronische-baugesuche.html https://www.axalon.ch/b/ebaugesuchezh--hier-steckt-iam-drin (IAM-Architektur) https://www.gemdat.ch/blog/stories/ebaugesuchezh-erfolgreich-produktiv/ (Hersteller) https://www.ech.ch/sites/default/files/imce/Artikel/eCH_artikel_baugesucheZH_A4_d.pdf (eCH-Standards-Bezug) |
|                                             | Baudirektion Kanton Zürich / egovpartner; Realisierung Gemdat Informatik AG                                                                                                                                                                                                                                                                                   |
| Ziel                                        | Papierloses Baubewilligungsverfahren von Eingabe bis Bauabnahme; Datendrehscheibe Gemeinden-Kanton-Dritte                                                                                                                                                                                                                                                     |
| Lösu ng                                     | Proprietäre Webapplikation mit geführtem Formular; eCH-0211; IAM via ZHservices/IDV-ZH-Broker (SAML, eCH-0107/-0167/-0170), Migration Richtung Zürikonto/AGOV; QES für Signatur. Interner Stack nicht öffentlich                                                                                                                                              |
| Ergeb                                       | Produktiv seit 02/2020, ~15'000 Baugesuche/Jahr; seit 04/2024 reicht elektronische Eingabe                                                                                                                                                                                                                                                                    |
| Lesson Funktioniert, aber Stack-Transparenz | und Nachnutzbarkeit fehlen - illustriert den Trade-off proprietär vs. Open Source im selben Fachgebiet                                                                                                                                                                                                                                                        |

Video: Erklärvideo eBaugesucheZH (Kurzversion). Quelle

## 2.10 ZHAW-Studie Service-Portale (2025) - Marktüberblick CH

| Relevanz   | - Überblick über CH-Portal-Governance und -Architekturen                                                                           |
|------------|------------------------------------------------------------------------------------------------------------------------------------|
| Links      | https://www.zhaw.ch/storage/sml/News/ZHAW-Studie-Service-Portale-09_2025.pdf https://www.ag.ch/de/smartserviceportal (Beispiel AG) |

Vergleich von Smart Service Portal AG, mein.ar.ch, iGovPortal, Digitaler Schalter Thurgau, egovpartner ZH, GemeindeConnect. Befund: alle setzen auf modulare, erweiterbare Architekturen mit eCH-Schnittstellen; Datenhoheit konsequent bei den Verwaltungen; Governance-/Finanzierungsmodelle variieren stark (Verein, öffentlich-rechtlich, Gemeindeverband). Empfehlung der Studie: auf gemeinsam Erarbeitetem aufbauen statt Eigenentwicklung von Null.

## 4. Anhang

- 4.1.ANHANG1:UBERBLICK/FRAGEKATALOG

## Tabelle 2:Systemkomponenten

<!-- image -->

| Fragon                                                                                                                         | Smart Sorvice Portal                                                                                                                                                                                                                                                                                                                               | Moin.ar.ch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | IGovPortal                                                                                                                                                                                                                                                                                                                   | Digitaler Schalter TG                                                                                                                                                  | Goplantos E-Services Portal egovpartner                                                                                                                                                                                                                                                                                                                                                    | GomeindeConnect                                                                                                                           | Amtomat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produktpalette Verwaltungspro- zesse sind aktuell abgedeckt? Wel- Monaten dazu? Welche digitalen che kommen in den nachsten 12 | 2024), davon 28 kom- Leistungen: Bescheini- gungen,Antrage,Re- gistrierungen,Reser- vationen，Zahlungen. Rund 500 digitale Ser- munal. vices(Stand Ende Bietet Formularser- Hohe Nutzung: 88'000+Bestellungen, Prozesse. vices & End-to-End- >CHF 2 Mio.Umsatz seit April 2022. Januar 2025: 4500 Bestellungen pro Mo- nat  hohe Nutzerak- zeptanz. | Pass/D,eUmzug, Einwohnermeldungen, rung. Steuerkonto), so- wie Drittservices wie Strafregisterauszug. Unterstotzt Formular- 18 Services verfugbar; Steuerservices (elekt- ronische Steuererkla- services,automat- mehrstufige Verwal- tungsintegration (Kan- sierte Ablaufe und ton, Gemeinde, Bund). In den nachsten 12 Monaten: elektronische Baubewiligung, Stras- senverkehrsportal, wei- tere Gesuche geplant. Neues Kompetenz- zentrum Digitale Transformation (Ko- DiT) geplant zur strate- gischen Weiterentwick- lung- | bilitat,Bevolkerung. Das iGovPortal bietet rund 50 End-to-End- schaft. Erganzt wird personliches Nutzer- Services in Bereichen wie Bau, Steuern, Mo- Register und Wirt- das Angebot durch ein folgung und gesicher- ter Kommunikation. cockpit mit Statusver- Zuletzt wurden vier Handelsregister-Ser- vices neu integriert. | bung,Gesundhelit, Ge werbe. dienste, Landwirt- schaft, Zivilstand. E2E-Prozesse & For- 79 Services (Stand Juni 2025), inkl. Betrei- Geplant: Einwohner- mularservices. | vice-Portal mit anfang- Steuerfristverlange- rung.Veranstaltungs- Geplant ist ein E-Ser- Behordenleistungen lung, Parkbewilligung, bewiligungen). Das lich 14 kommunalen (z. B. Urkundenbestel- gestattet und soll lang- Portal wird mit einem Benutzercockpit aus- fristig teilweise ans kantonale Zorikonto angebunden werden. Die Behordenantwort erfolgt direkt innerhalb des Portals. | moglicht die medien- gung zahlreicher kom- Bescheinigungen dienstleistungen wie GemeindeConnect er- bruchfreie Beantra- munaler Behorden- | Aktuell deckt Amtomat Wohnsitzbestatigung. Veranstaltungsgesuch, Sozialhifeantrag. Gastrobewilligung so- zentrale Prozesse wie wie einen Ratenzah- lungsservice for Steu- ern ab. In den kom- menden 12 Monaten werden weitere priori- sierte Services er- ganzt, die im Rahmen der partizipativen Roadmap erarbeitet wurden. Je nach Ska- lierung von Amtomat konnen ab 2026 poten- ziell sehr viele neue Services lanciert wer- den, da jeder von einer Gemeinde entwickelte Service automatisch auch den anderen Ge- meinden zur Verfu- gung steht. |

Bild: Anhang mit Fragenkatalog. Service-Portale im Vergleich (ZHAW, 2025). Quelle

## 2.11 IGE - Camunda als BPMN-Engine in einer Bundesinstitution

| Rele vanz   | - einziger durch eine Beschaffungsquelle belegter Camunda-Einsatz auf Bundesebene; zugleich Präzedenzfall freihändige Vergabe bei Herstellerbindung                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://camunda.com/de/case-study/swiss-federal-institute-of-intellectual-property/ (Fallstudie, Anbieterquelle) https://www.netzwoche.ch/news/2020-03-23/simap-meldungen-woche-12-zuschlaege (simap-Zuschlag) https://camunda.com/de/solutions/industry/public-sector/ |
| Wer         | Eidg. Institut für Geistiges Eigentum (IGE), Bern; dezentrale Bundesverwaltung                                                                                                                                                                                          |
| Ziel        | Ablösung einer proprietären Prozess-Engine; Kernprozesse der Schutzrechtsverwaltung (Marken, Patente, Designs) als ausführbare BPMN-Modelle, um die Kommunikation zwischen Fachseite und IT zu verbessern                                                               |

| Lös ung   | Camunda als BPMN-2.0-Engine, integriert in den bestehenden Tech-Stack; produktiv seit 2014                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Erg ebnis | Beschaffungsseitig belegt: Zuschlag an camunda services GmbH über CHF 790'000, freihändig nach Art. 13 Abs. 1 lit. c VöB (simap, publiziert 03/2020) - d.h. Folgebeschaffung über dem WTO-Schwellenwert mit Herstellerbindung als Begründung                                                                                                                                                                                                                                        |
| Les son   | BPMN-Engine-Einsatz in einer CH-Bundesinstitution ist nicht nur Anbieter-Marketing, sondern über simap verifizierbar - inkl. der TCO-Realität: Die laufenden Lizenz-/Supportkosten einer kommerziellen Engine erreichen nach wenigen Jahren WTO-Dimensionen. Stützt unseren Entscheid für einen lizenzkostenfreien Open-Source-Pfad (Operaton, Kap. 3.5) doppelt: technisch (BPMN 2.0 produktiv beim Bund etabliert) und wirtschaftlich (Vendor-Lock-in hat einen sichtbaren Preis) |

Weitere Existenzbelege Camunda im Schweizer Umfeld (Anbieter-/Partnerquellen, nur als Existenz-, nicht als Ergebnisbeleg zu lesen):

- Città di Lugano betreibt ihr Bürgerportal auf der Camunda-Engine, die Anträge ausführt und die Anbindung an Backend-Fachsysteme und Drittdienste (u.a. Payment) orchestriert - kommunal, aber fachlich exakt unser Muster Portal  Engine  Fachsystem.
- Schweizer Camunda-Partner nennen zudem SBB und Swisscom als produktive Nutzer (bundesnah).
- Das BIT schliesslich hat 2024 Lösungen für Digital/Business Process Automation und RPA inkl. Aufbau eines Center of Excellence ausgeschrieben - kein Camunda-Beleg, aber ein Indiz, dass Prozessautomatisierung beim zentralen Leistungserbringer des Bundes strategisch verankert wird.
- Das Eidg. Institut für Geistiges Eigentum setzt Camunda als BPMN-2.0-Engine ein, integriert in den bestehenden Tech-Stack - Beleg für BPMNEngine-Einsatz in einer Schweizer Bundesinstitution. (Anbieterquelle, werblich gefärbt.)

## 3. Fallbeispiele Deutschland

## 3.1 OZG-Hub (Baden-Württemberg + Sachsen)

| Rele vanz   | - strukturell genaueste Validierung unserer Plattform-Ambition                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://www.ozg-hub.de (Plattform inkl. Doku/Handbücher) https://www.ozg-hub.de/online-dienste (Formulardesigner + Prozessbausteine) https://im.baden-wuerttemberg.de/de/digitalisierung/service-bw/ozg-hub (Träger BW) https://www.digitale-verwaltung.de/SharedDocs/kurzmeldungen/Webs/DV/DE/2023/10_ozghub.html (Bund) https://im.baden-wuerttemberg.de/de/service/presse-und-oeffentlichkeitsarbeit/pressemitteilung/pid/ozg-hub-geht-an-den-start (Start/Kooperation) |
| Wer         | Länder BW und Sachsen; Entwicklungspartner SEITENBAU GmbH; Betrieb in ISO-27001-RZ (DE), BSI-Grundschutz                                                                                                                                                                                                                                                                                                                                                                   |
| Ziel        | Low-Code-Plattform für schnell entwickelbare, bundesweit nachnutzbare Onlinedienste (EfA-Prinzip «Einer für Alle»); basiert auf den Prozessplattformen von service-bw und Amt24 (600 digitale Behördengänge)                                                                                                                                                                                                                                                               |
| Lös ung     | Prozessmodellierung mit vorgefertigten Prozessbausteinen + Formulardesigner (Drag & Drop, barrierefrei) + EfA-Bausteine: BundID-Auth, ePayment, FIT- Connect-Zustellung, Kartenfunktion. Deployment je Behörde über parametrisierte Start-URLs (Behörde, Logo, Gebühren, Fristen als Konfiguration). Open-Source- Komponenten zur Reduktion von Lizenzkosten und Abhängigkeiten; konkrete Engine/DB nicht öffentlich belegt                                                |
| Erg ebnis   | Start 08/2023; Dienste in 9 Bundesländern; ~500'000 Online-Anträge in den ersten 12 Monaten; Release-Kadenz alle 3 Wochen                                                                                                                                                                                                                                                                                                                                                  |
| Les son     | Validiert unser Zielbild fast wörtlich: wiederverwendbare Plattform = Prozessmodell + Formular-Schema + Standardbausteine; neuer Dienst bzw. neue Behörde als (parametrisierte URLs). Entspricht unserer Reifegradstufe 2-3 Konfigurations-Delta                                                                                                                                                                                                                           |

## 3.2 Dataport OSI / OZG-Cloud + FIT-Connect (FITKO)

| Rele vanz   | - Integration als eigener Layer mit Standard-Contract                                                                                                                                                                                                                                                                                                                                              |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://docs.fitko.de/fit-connect/ (technische Doku inkl. APIs, SDKs Java/.NET/JS) https://docs.fitko.de/kompass/docs/it-landschaft/basisdienste/datenuebermittlung/transportsysteme/fitconnect/ (Architektur-Einordnung) https://www.onlinezugangsgesetz.de/Webs/OZG/DE/themen/foederale-architektur/fit-connect/fit-connect-node.html https://www.dataport.de/unsere-themen/onlinezugangsgesetz/ |
| Wer         | Dataport (Trägerländer HH, HB, SH, ST); FIT-Connect: FITKO im Auftrag des IT-Planungsrats                                                                                                                                                                                                                                                                                                          |
| Ziel        | Modulare Online-Service-Infrastruktur (Servicekonto, Postfach, Payment, BundID) + standardisierter, Ende-zu-Ende-verschlüsselter Antragstransport in Fachverfahren                                                                                                                                                                                                                                 |
| Lös ung     | OSI-Baukasten + OZG-Cloud mit Adaptern für Formularlösungen; FIT-Connect als offener API-Standard (REST, OAuth, Routing API, Ereignisprotokoll für Nachvollziehbarkeit); SDKs für Java/.NET/JavaScript; Self-Service-Portal für Zustellpunkte                                                                                                                                                      |
| Erg ebnis   | ~460 Onlinedienste auf OSI; ~400 Kommunen in 12 Bundesländern nutzten Ende 2022 mindestens einen OSI-Dienst                                                                                                                                                                                                                                                                                        |

Les

son Die Entkopplung «Portal sendet standardisiert, Fachverfahren empfängt» ist das deutsche Pendant zu unserem Connector-Prinzip - Integration als eigener Layer mit dokumentiertem Standard-Contract statt Punkt-zu-Punkt; das Ereignisprotokoll entspricht unserer Audit-Trail-Anforderung

## 3.3 GovForms 2.0 / Wirtschaftsservice-Portal.NRW

| Relevanz   | - mandantenfähige Formular-/Prozessplattform als Service                                                                   |
|------------|----------------------------------------------------------------------------------------------------------------------------|
| Links      | https://service.wirtschaft.nrw/hilfe/efa/nachnutzung/mitnutzung/4-dimensionen/technische-dimension-der-mitnutzungsallianz/ |

Mandantenfähige, Open-Source-basierte Microservice-Formularplattform mit FIT-Connect-Anbindung; «Digitalisierungsstrassen» als wiederverwendbares Prozessmodell; EfA-Mitnutzung durch andere Länder. Beleg für mandantenfähige Formular-/Prozessplattform als Service.

## 3.4 Bundesagentur für Arbeit + Stadt München - Camunda

| Relevanz   | - Existenzbelege BPMN in Grossverwaltungen (Anbieter-/Beraterquellen)                                                                                  |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links      | https://klardenker.kpmg.de/prozessautomatisierung-wir-begleiten-die-bundesagentur-fuer-arbeit https://camunda.com/de/solutions/industry/public-sector/ |

BA: Automatisierung der Online-Arbeitsuchendmeldung (vorher ~8 Min. manuelle Bearbeitung pro Fall), Technologiewechsel mitten im Projekt gemeistert; Change-Management als Erfolgsfaktor. München: Prozessorchestrierung zur Ablösung isolierter Altprozesse.

## 3.5 Operaton &amp; CIB seven - Souveränität auf Engine-Ebene

| Relev anz   | - externe Validierung unseres Prozess-Engine-Entscheids                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links       | https://operaton.org https://docs.operaton.org/docs/documentation/introduction/ (Doku inkl. Engine, Cockpit, Tasklist, REST API) https://github.com/operaton/operaton (Quellcode, Apache 2.0) https://github.com/operaton/operaton-keycloak (Keycloak-Integration) https://opencode.de/de/software/cib-seven-8387 (CIB seven auf openCode des Bundes DE) https://www.heise.de/news/Open-Source-Fork-CIB-seven-beerbt-Camunda-7-Community-Edition-10081700.html |
| Wer         | Operaton: Community-Konsortium (u.a. itemis, nterra), Vereinsgründung (e.V.) in Arbeit; CIB seven: CIB München                                                                                                                                                                                                                                                                                                                                                 |
| Ziel        | Reaktion auf das EOL der Camunda 7 Community Edition: souveräner, lizenzkostenfreier C7-Pfad ohne erzwungene Camunda-8-Migration                                                                                                                                                                                                                                                                                                                               |
| Lösu ng     | API-, Schema- und Modell-kompatible C7-Forks (BPMN 2.0, CMMN, DMN); Operaton mit Cockpit, Tasklist, Admin, REST API, Spring/Quarkus-Integration und ei ; halbjährliche Release-Kadenz (aktuell v2.1) gener Keycloak-Extension                                                                                                                                                                                                                                  |
| Erge bnis   | CIB seven auf gelistet - die deutsche Verwaltung führt den C7-Fork-Pfad als offizielle Souveränitätsoption openCode.de                                                                                                                                                                                                                                                                                                                                         |
| Less on     | Direkte externe Validierung unseres Prozess-Engine-Entscheids (Marktscreening Kap. 4.2); die operaton-keycloak-Extension deckt exakt unsere Auth- Architektur ab                                                                                                                                                                                                                                                                                               |

## 4. Fallbeispiele Österreich

## 4.1 oesterreich.gv.at / Digitales Amt (BRZ)

| Relevanz   | - Muster «zentrale eID + Postfach + Once-Only» auf Bundesebene                                                                                      |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Links      |                                                                                                                                                     |
|            | https://www.brz.gv.at/was-wir-tun/services-produkte/oesterreich.gv.at.html https://www.digitalaustria.gv.at/Services/ https://www.oesterreich.gv.at |

Bundesrechenzentrum als Generalunternehmer; zentrale Plattform für digitale Amtswege mit (2-Faktor-eID), SSO zu FinanzOnline/USP, ID Austria MeinP (elektronische Zustellung) und Once-Only-Datendrehscheibe für Bund/Länder/Gemeinden; &gt;2 Mio. Nutzer. Strukturell das, was eIAM/AGOV + ostkorb Notifikation + RE-FX-Anbindung bei uns leisten.

## 4.2 aforms / AFORMSOLUTION - Formularserver CH/AT/LI

| Relevanz   | - Beleg «Schema statt Code» skaliert über Mandanten; Buy-Option Form-Layer                                                                                                                                                   |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Links      | https://www.aforms.com https://aforms2web.com/formularserver/-/categories/34567 (Produktbeschreibung) https://aforms2web.com/form-solution/-/categories/29645 (Referenzen CH/AT/LI) https://de.wikipedia.org/wiki/Aforms2web |

Java-basierter, mandantenfähiger Formularserver nach (wiederverwendbare Felder, Blöcke, Validierungen - Schema statt Code); WCAGBausteinprinzip konform, mehrsprachig; produktiv in den Kantonen ZG, SZ, SO, GL, OW, SH, LU, Städten Zug/St. Gallen/Winterthur, 5 von 9 AT-Bundesländern, Liechtenstein (350+ Formulare); GEVER-Anbindung (Acta Nova). Kommerzielle Alternative zum Eigenbau des Form-Layers (vgl. BBL Formularservice /JAXForms im Referenzbericht).

## 5. Internationale Benchmarks

|    | Beispiel                                | Relevanz   | Land   | Kernmuster / Relevanz für uns                                                                                                                                                                                                             | Links                                                                                                                                                                                                      |
|----|-----------------------------------------|------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | / borger.dk MitID / Digital Post        |            | DK     | Nationales Portal, ~2'000 Self-Services, zentrales SSO (96,6% Adoption >15 J.), gesetzlich verbindliche E-Zustellung; Online-Kanal 2-3,75× günstiger - Benchmark für Adoption und Kanalkosten-Argument im Förderentscheid                 | https://en.digst.dk/digital-services/borgerdk-national- citizen-portal/ https://en.digst.dk/systems/nemlog-in/                                                                                             |
|  2 | X-Road / X-tee (RIA)                    |            | EE     | Dezentrale Datenaustauschschicht, peer-to-peer, Open Source (MIT), >3'000 Dienste - Vorbild «Integration als Austauschschicht statt Datenkopie», Bestätigung unseres Connector- /Once-Only-Ansatzes                                       | https://www.ria.ee/en/state-information-system/data- exchange-platforms/data-exchange-layer-x-tee https://x-road.global https://github.com/nordic-institute/X-Road                                         |
|  3 | GOV.UK Design System + Service Patterns |            | UK     | Wiederverwendbare, WCAG-getestete Komponenten (MIT) + ressortübergreifende Patterns («apply», «get a decision», «pay») - validiert unsere Lösungsmuster-Bibliothek: «Antrag Entscheid» ist ein dokumentiertes, generisches Pattern        | https://design-system.service.gov.uk https://github.com/alphagov/govuk-frontend · https://servic es.blog.gov.uk/2025/03/19/developing-service-patterns- reusable-designs-for-building-government-services/ |
|  4 | Common Ground + NL Design System        |            | NL     | Entkopplung Daten/Logik (5-Schichten), Daten an der Quelle abfragen; Design-Tokens für Hausstil-Theming ohne Code-Fork - Architektur-Validierung Layer-Trennung; Token-Ansatz relevant für CD-Bund-Theming wiederverwendbarer Komponenten | https://nldesignsystem.nl/handboek/developer /architectuur/ https://www.gemmaonline.nl/wiki/Thema- architectuur_Common_Ground · https://openzaak.org                                                       |

## 6. Synthese: Wiederkehrende Muster

|    | Muster                                                                                                                                                    | Belegt durch                                                       | Bezug zu unseren Dokumenten                                          |
|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
|  1 | Vier-Schichten-Trennung Portal/Formulare - Engine - Datenhaltung - Integration, jede Schicht unabhängig austauschbar                                      | inosca, OZG-Hub, OSI/FIT-Connect, Common Ground                    | Modularitätsprinzip «Stabile Layer- Verträge» (Anforderungsdok. 3.2) |
|  2 | Schema statt Code : Formulare als Schema/Bausteine, Prozesse als Modell; neuer Use-Case = Konfigurations-Delta                                            | OZG-Hub (parametrisierte Behörden- URLs), aforms, GovForms, Caluma | Plattform-Capability «Konfiguration statt Code»                      |
|  3 | Open-Source-Engine mit Souveränitätspfad : C7-Forks (Operaton, CIB seven) von Verwaltungen aktiv getragen; alternativ formularzentrierte Engines (Caluma) | openCode-Listung CIB seven, inosca                                 | Prozess-Engine-Entscheid (Marktscreening 4.2)                        |
|  4 | Keycloak + vorgeschalteter eID-Broker als IAM-Standardmuster (BE-Login, IDV-ZH, BundID, ID Austria, MitID)                                                | inosca, eBaugesucheZH, OZG-Hub, AT, DK                             | eIAM/AGOV-Architektur - unser Broker ist bereits gesetzt             |
|  5 | Once-Only über Austauschschicht : Portal hält keine Stammdaten; Fachsysteme bleiben Leitsysteme; standardisierte Contracts (eCH, FIT-Connect, X-Road)     | iGovPortal, FIT-Connect, X-Road                                    | RE-FX als Leitsystem, REST- Connector (Anforderungsdok. 5.4/5.6)     |
|  6 | Gemeinsame Trägerschaft skaliert Wiederverwendung - und braucht explizite Governance (Verein, EfA, Community)                                             | inosca (6 Kantone), iGovPortal (9 Kantone), EfA                    | Betriebs-/Trägerschaftsmodell (Anforderungsdok. 4.2)                 |

Einordnung für das Mieterportal: Jedes Element unseres Architekturzielbilds ist durch mindestens ein produktives Fallbeispiel belegt - das Vorhaben ist kein Architektur-Experiment, sondern die Anwendung eines etablierten Verwaltungsmusters. Die nächstliegende Blaupause ist der inosca/eBau-Stack (Open Source, Schweizer Verwaltung, PostgreSQL/Keycloak, mehrkantonale Wiederverwendung belegt); die strukturell genaueste Validierung der Plattform-Ambition liefert der (Prozessmodell + Formulardesigner + Standardbausteine, ~500k Anträge im ersten Jahr). OZG-Hub

## 7. Abweichungen und offene Punkte

- Caluma vs. BPMN: inosca nutzt eine formularzentrierte Engine, keine BPMN-Engine - unsere BPMN-2.0-Vorgabe (eCH-0158) bleibt davon unberührt; die inosca-Referenz trägt für Frontend-, Daten-, IAM- und Governance-Muster, nicht für den Engine-Entscheid.
- Stack-Transparenz: Beim OZG-Hub sind Engine und DB nicht öffentlich belegt («Open Source» bezieht sich auf verwendete Komponenten); bei eBaugesucheZH ist der Stack proprietär. Aussagen dazu sind als nicht verifiziert zu kennzeichnen.
- Anbieterquellen: Camunda- und KPMG-Referenzen (IGE, München, BA) sind werblich gefärbt und nur als Existenzbeleg, nicht als Ergebnisbewertung zu lesen.
- Direkter Kontakt prüfen: inosca-Community (via Adfinis, SPRINT-Los-1-Partner) und OZG-Hub/SEITENBAU für Architektur-Austausch - beide Erfahrungsträger sind erreichbar.

## 8. Verweise und Anhang

## 8.1 Verweise

- Anforderungsdokument: Lösungsarchitektur Mieterportal als MVP
- Marktscreening: Mieterportal als MVP
- Referenzbericht: Abgeschlossene IT-Vergaben für das Mieterportal
- Quellen-URLs: je Fallbeispiel in der Zeile «Links» (Stand 06/2026)

## 8.2 Anhang

| Datei                                               | Geändert                       |
|-----------------------------------------------------|--------------------------------|
| PNG-Datei ChatGPT Image 11. Juni 2026, 15_25_05.png | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-11_15-46-59.png              | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-11_15-47-48.png              | 11.06.2026 by Rasner David BBL |
| PNG-Datei Kibanda-Illu-Screen.png                   | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-11_16-14-6.png               | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-11_16-17-46.png              | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-11_16-21-24.png              | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-11_16-35-51.png              | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-11_16-47-31.png              | 11.06.2026 by Rasner David BBL |
| PNG-Datei image-2026-6-12_14-27-0.png               | 12.06.2026 by Rasner David BBL |

Ziehen Sie Dateien an diese Stelle, um sie hochzuladen, oder Dateien suchen

Alle herunterladen