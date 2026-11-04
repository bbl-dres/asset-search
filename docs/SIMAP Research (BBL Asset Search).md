## SIMAP Research

| Titel           | Referenzbericht: Abgeschlossene Vergaben für KI-Suche und Asset Information Model |
|-----------------|-----------------------------------------------------------------------------------|
| Author          | David Rasner BBL                                                                  |
| Status          | Entwurf                                                                           |
| Stand           | 02.11.2026                                                                        |
| Klassifizierung | Intern                                                                            |

## Inhalt:

Management Summary

1. Ziel von Dokument
2. Referenz-Vergaben (funktionale Treffer)
3. Abrufbare Rahmenverträge (Beschaffungsweg ohne neue Ausschreibung)
4. Track-Record der in der Recherche genannten Anbieter
5. Verweise und Anhang

## Management Summary

Das Vorhaben sieht ein gebäudebezogenes Asset Information Model (AIM) vor: einen Wissensgraphen über die bestehenden Quellsysteme mit Klassifikation der Dokumente nach KBOB und einer KI-Suche mit Quellenangabe (siehe Ausgangslage und Vision). Dieser Bericht wertet sämtliche seit Plattformstart von simap.ch publizierten Zuschläge aus (07/2024-11/2026, 3'711 Datensätze aus CPV 72/48 und 33 Stichwortsuchen) und beantwortet drei Beschaffungsfragen:

1. Das Zielbild ist am Markt angekommen, aber nur in Teilen. Den nächsten Treffer liefert Swissgrid: Im Februar 2026 wurde der «Aufbau eines RDF-basierten Asset Information Models (AIM)» als Knowledge Graph im offenen Verfahren vergeben (Ontotext/Graphwise, CHF 6,9 Mio., 4 Angebote). Das Vorhaben ist fast deckungsgleich mit der Graph-Schicht des Zielbilds. Die KI-Schicht wird in der Verwaltung bereits als eigenständige Plattform beschafft, mit grossem Wettbewerb: Private LLM der SSGI (CHF 249k, 20 Angebote), RAG-Chatbots der HUG (CHF 1,0 Mio. für 3 Partner, 21 Angebote), KI-Plattform der Zürcher Gemeinden (CHF 4,0 Mio., 20 Angebote). Keine Vergabe verbindet KI-Suche mit Bauwerksdokumentation oder Immobiliendaten. Damit bestätigt sich der Befund der Recherche: Das BBL wäre hier früh dran.
2. Ein Beschaffungsweg für den Pilot existiert, ein KI-spezifischer Rahmenvertrag des Bundes dagegen nicht. Mit SPRINT (bis 2033, BBL abrufberechtigt) ist ein Pilot unter CHF 1 Mio. als Mini-Tender in Los 1 möglich, ein Ausbau als Mini-Tender in Los 2. Der CDE-Bund-Vertrag mit Zühlke (bis 2032, inkl. Entwicklung und Integration) kommt für die Anbindung der CDE-Bund an das AIM in Frage. Die gefundenen KI-Rahmenverträge (Kanton Zürich, HUG) sind kantonal und für das BBL nicht abrufbar.
3. Die Anbieter von Dokumenten-KI aus der Recherche haben keine Schweizer Referenz auf simap. Für EVANA, Architrave, Findable, sd-solution (TwinEstate), Neo4j, Palantir und Stardog findet sich seit 07/2024 kein Zuschlag. Von den Graph-Plattformen ist einzig Ontotext (Swissgrid) belegt. Schweizer RAG-Referenzen haben dagegen kleinere Häuser wie Artificialy, Deeplink, Liip, BEGASOFT und AlpineAI.

Empfehlung: Pilot (Stufe 1) über einen SPRINT-Mini-Tender in Los 1, mit RAG-, Graph- und KBOB-Erfahrung sowie souveränem Betrieb als Zuschlagskriterien. Die Referenzen der SSGI und der HUG dienen als Preisanker für die KI-Schicht (rund CHF 250-350k). Parallel einen Erfahrungsaustausch mit Swissgrid zum AIM-Projekt suchen (Ontologie, Object Type Library, Vorgehen, Kosten). Den Plattformausbau später über SPRINT Los 2 oder eine eigene Ausschreibung nach dem Muster von Swissgrid beschaffen.

## 1. Ziel von Dokument

Dieser Bericht schafft die vergaberechtliche und marktliche Evidenzbasis für den Beschaffungsentscheid zur KI-Suche über das Asset Information Model. Er beantwortet auf Grundlage abgeschlossener Vergaben (simap.ch, 07/2024-11/2026) drei Fragen:

1. Marktnachweis: Welche vergleichbaren Vorhaben (AIM, Wissensgraph, KI-/RAG-Plattform, CDE, CAFM, Erschliessung von Bauakten) wurden in der Schweiz bereits vergeben - zu welchen Preisen, in welchen Verfahren, an welche Anbieter?
2. Beschaffungsweg: Welche bestehenden Rahmenverträge erlauben den Abruf externer Kapazität ohne neue WTO-Ausschreibung?
3. Anbieterlage: Welche der in der Recherche genannten Anbieter haben Schweizer Referenzen im öffentlichen Sektor?

Anforderungsprofil (aus Ausgangslage und Vision): gebäudebezogenes AIM als Wissensgraph über die Quellsysteme (SAP RE-FX, SAP PS, GEVER, DALA, CDE-Bund, GWR), Klassifikation der Dokumente nach KBOB-Dokumenttypenkatalog, KI-Suche (RAG) mit Quellenangabe, Gebäudehistorie und strukturierte Daten (z.B. Kosten), offene Standards, souveräner Betrieb auf Bundesinfrastruktur.

## Match-Rating:

| Rating | Bedeutung                                                                                |
|--------|------------------------------------------------------------------------------------------|
| A      | nahezu deckungsgleich: AIM als Wissensgraph oder KI-Suche über Asset- und Bauwerksdaten   |
| B      | stark verwandt: KI-/RAG-Plattform, CDE, CAFM oder Erschliessung von Bauakten              |
| C      | Kontext: Marktevidenz, Datenquelle oder Governance-Baustein, fachlich weiter entfernt     |

## 2. Referenz-Vergaben (funktionale Treffer)

|    | Datum   | Auftraggeber                              | Gegenstand (was wurde gemacht)                                                                 | Verfahren  | Volumen CHF        | Zuschlagsempfänger                          | Match | Kommentar |
|----|---------|-------------------------------------------|------------------------------------------------------------------------------------------------|------------|--------------------|---------------------------------------------|-------|-----------|
| 1  | 2026-02 | Swissgrid AG                              | RDF Knowledge Graph implementation - Aufbau eines systemunabhängigen AIM als RDF-Graph mit Object Type Library, ETL, Validierung (SHACL), Triplestore/Editor | offen      | 6'891'774          | Ontotext AD, Sofia                          | A     | Fast identisch mit der Graph-Schicht des Zielbilds, inkl. «Data AI-Readiness» und LLM als Folge-Use-Case. Ontotext ist Teil von Graphwise (Muster B der Recherche). Preisreferenz für die Plattform-Variante inkl. Consulting; nur 4 Angebote. [simap](https://www.simap.ch/de/project-detail/9b0a21e8-2802-4e80-ae81-14a3d9948d22) |
| 2  | 2026-03 | CAIB Vaud-Genève (für HUG)                | Référencement chatbots RAG - Konzeption, Entwicklung, Wartung von RAG-Chatbots für interne und externe Nutzende | offen      | 996'681 (3 × 332'227) | Artificialy SA, Lugano; Deeplink SA, Lausanne; Liip SA, Lausanne | B | RAG-Architektur als Rahmenvertrag mit drei Partnern; Preisanker rund CHF 330k pro Partner. Liip ist SPRINT-Los-2-Partner. 21 Angebote. [simap](https://www.simap.ch/de/project-detail/6bf75694-cfca-422e-a849-4944e5378955) |
| 3  | 2026-03 | Verein SSGI (ZG, OW, NW, AR, SH, SZ)      | Datenschutzkonforme KI-Plattform - Private LLM als Mandant für Gemeinde- und Kantonsverwaltungen | offen      | 248'952            | BEGASOFT AG, Bern                           | B     | Souveräne LLM-Basisplattform unter CHF 250k; 20 Angebote zeigen einen breiten Markt. [simap](https://www.simap.ch/de/project-detail/c51dd1f2-9f2d-423b-bcea-73a2d2d93f1b) |
| 4  | 2026-02 | Staatskanzlei Kanton Zürich (egovpartner) | Nutzung und Skalierung KI-Basisdienste - Rahmenvertrag KI-Plattform für Zürcher Gemeinden und Städte | offen      | 4'021'189          | AlpineAI AG, Davos                          | B     | Gemeinsame Beschaffung, um Datenschutz- und Sicherheitsabklärungen zentral zu machen; Muster für einen KI-Basisdienst. Für das BBL nicht abrufbar. 20 Angebote. [simap](https://www.simap.ch/de/project-detail/bbf9f3ec-9a68-4eea-a288-7eacbcb418ad) |
| 5  | 2025-08 | BBL                                       | Common Data Environment «CDE-Bund» 2025-2032 - Entwicklung, Integration, Betrieb, Support      | offen      | 14'981'038         | Zühlke Engineering AG, Bern                 | B     | Wichtigste Quelle für BIM- und Projektdokumente im Zielbild. Stundenpool für Entwicklung und Integration bis 2032: Anbindung an das AIM darüber prüfen. [simap](https://www.simap.ch/de/project-detail/3f3aedc0-e34a-4f03-93ee-be2af772b6f5) |
| 6  | 2026-05 | Stadt Zürich, Amt für Hochbauten          | CDE Stadt Zürich - CDE für alle Phasen öffentlicher Bau- und Infrastrukturprojekte, 5 Jahre     | offen      | 2'485'511          | B3 digital AG, Gossau SG                    | B     | Kommunales Gegenstück zur CDE-Bund. Weitere CDE-Vergaben: Universitätsspital Zürich (Kaulquappe AG, 648'723), Generalsekretariat P+I (BuildingPoint Schweiz AG, 911'175). [simap](https://www.simap.ch/de/project-detail/5a741790-739b-4c12-8605-e600d9cbb599) |
| 7  | 2026-09 | Immobilien Aargau                         | Vertragsdatenerfassung - Identifikation, Abgleich und Eingabe von FM-Verträgen in ein CAFM-System, Digitalisierung und strukturierte Ablage | offen      | 176'403            | Cadmec AG, Kemptthal                        | B     | Genau der manuelle Erfassungsaufwand, den KI-Extraktion reduzieren soll; Preisreferenz für ein kantonales Hochbauportfolio. Cadmec pflegt dort auch die digitalen Architekturpläne (618'332, 2025-11). [simap](https://www.simap.ch/de/project-detail/d66eabae-30de-4861-ab5c-575570704c9f) |
| 8  | 2025-09 | ASTRA                                     | Strukturierung und Metadatenerfassung Archivakten Nationalstrassen                             | offen      | 219'789            | GBL Gubler AG, Frauenfeld                   | B     | Erschliessung von Altakten mit Metadaten bei einem Bundesamt; Vorstufe zur Klassifikation nach KBOB. Nur 1 Angebot. [simap](https://www.simap.ch/de/project-detail/b686ee26-4b31-4578-ab04-aafc329cc79b) |
| 9  | 2025-09 | Stadt Biel                                | Digitalisierung Baugesuche - Übernahme, Archivierung und Digitalisierung des Baugesuchsarchivs  | offen      | 734'097            | GBL Gubler AG, Frauenfeld                   | B     | Preisreferenz für die Digitalisierung eines Bauakten-Backlogs als Dienstleistung; 9 Angebote. [simap](https://www.simap.ch/de/project-detail/cc29b89e-ec64-4222-9f0d-c92a1641a7f0) |
| 10 | 2025-12 | Universität Zürich                        | CAFM-Software Planon - Vertragsverlängerung Lizenzen, Dienstleistungen, Weiterentwicklung      | freihändig | 1'346'000          | Planon GmbH, Zürich                         | B     | CAFM als Standardprodukt mit freihändigen Folgekosten; Planon war in der Recherche nur «nicht verifiziert». [simap](https://www.simap.ch/de/project-detail/06a29bfe-af4a-4560-bcca-1fbd6a059807) |
| 11 | 2026-05 | Aargauische Gebäudeversicherung           | Agent BSV 2026 - Überführung einer KI-Lösung zu den Brandschutzvorschriften vom PoC in den Betrieb | freihändig | 700'000            | Public Cloud Group AG, Baar                 | C     | KI über Bauvorschriften in einer Gebäudeversicherung; zeigt den Weg PoC und danach freihändiger Folgeauftrag (Art. 21 Abs. 2 Bst. e IVöB). [simap](https://www.simap.ch/de/project-detail/0d1888ca-4b71-49f0-becc-c48c36062b1e) |
| 12 | 2025-03 | BBL                                       | LINDASnext - Linked-Data-Infrastruktur des Bundes                                              | offen      | 17'230'598         | Cognizone, Bruxelles                        | C     | Zielplattform, um den KBOB-Katalog als SKOS-Vokabular zu publizieren (Recherche, Kap. 2.4). Dazu passt armasuisse/swisstopo «Semantic Web Linked Data» (kontrollierte Vokabulare, EPSILON Italia, 2024-11). [simap](https://www.simap.ch/de/project-detail/02b41468-3518-4dc6-a263-895afccd2f3d) |
| 13 | 2026-09 | Kanton Aargau, Statistik Aargau           | Metadatenkatalog kantonale Verwaltung                                                          | offen      | 404'321            | dataspot. ag, Basel                         | C     | Datenkatalog als Governance-Baustein (entspricht dem «Datenverzeichnis» der Recherche). [simap](https://www.simap.ch/de/project-detail/a5185d07-d7f7-4738-afa6-828e8f39dcf8) |
| 14 | 2025-05 | BBL                                       | SUPERB Immobilien Projektmanagement - SAP-Erweiterung «Projektmanagement-Cockpit» für Bau- und Liegenschaftsprojekte | freihändig | 1'011'848          | emineo AG, Baar                             | C     | Kontext: Quelle der Projekt- und Kostendaten für Gebäudehistorie und Kennwerte (Stufe 2). [simap](https://www.simap.ch/de/project-detail/0d7a5954-0bff-463c-8a9d-b85c51a389ea) |

## 3. Abrufbare Rahmenverträge (Beschaffungsweg ohne neue Ausschreibung)

|   | Rahmenvertrag | Vergabestelle | Partner | Abruf | Eignung für die KI-Suche / das AIM |
|---|---------------|---------------|---------|-------|------------------------------------|
| 1 | SPRINT (24194) 104 «Software-Projekte realisieren und integrieren», bis 2033 | BBL | Los 1 (< 1 Mio., 12 Partner): u.a. queo/Adfinis/Limetree, Softcom, Sopra Steria, Orange Business, linkyard, MindNow, Intersim, TXT e-Swiss · Los 2 (1-5 Mio.): u.a. Liip, ti&m, IPT, LHIND, European Dynamics | Mini-Tender unter den Partnern | Primärer Weg: Pilot Stufe 1 als Los-1-Mini-Tender, Ausbau als Los-2-Mini-Tender. Entwicklung und Cloud-Leistungen abgedeckt. KI-, Graph- und KBOB-Erfahrung im Mini-Tender als Referenz abfragen; über simap ist sie bei den Partnern nicht belegt. [simap](https://www.simap.ch/de/project-detail/72a0615f-d406-417f-a61f-35024a71b809) |
| 2 | CDE-Bund 2025-2032 (24245) | BBL | Zühlke Engineering AG | Abruf aus Stundenpool (Entwicklung, Integration) | Anbindung der CDE-Bund an das AIM (Schnittstelle, Metadaten-Export). Nicht für den AIM-Kern; Abdeckung im Vertrag prüfen. [simap](https://www.simap.ch/de/project-detail/3f3aedc0-e34a-4f03-93ee-be2af772b6f5) |
| 3 | Public Clouds Bund (F25228, Verlängerung) | BBL | IBM, Microsoft, AWS, Oracle, Alibaba | Abruf (Restvolumen rund CHF 49 Mio.) | Nur für nicht sensitive Daten; KI-Dienste der Hyperscaler als Option für Tests. Für den Kern gilt die Vorgabe zum souveränen Betrieb. [simap](https://www.simap.ch/de/project-detail/38bbb542-257a-4449-99cf-4aa2abb022cf) |
| 4 | PM Inland - externe Unterstützung für Bauherrenleistungen (b24036, Nachtrag Fb26053) | BBL | EBP Schweiz, siworks immo, Techdata | Abruf | Mögliche Fachunterstützung aus der Baudomäne, z.B. für das Labeln des Testsets nach KBOB; Leistungsumfang prüfen. [simap](https://www.simap.ch/de/project-detail/d83b6205-b19c-4413-ab50-77642c2724a9) |
| 5 | Nicht abrufbar, nur als Muster | - | - | - | KI-Basisdienste Kanton Zürich (AlpineAI) und RAG-Référencement HUG sind kantonal. FileNet-Dienstleistungen (25106, IBM) und SAP Consulting 2026-2030 (25171) sind auf die ESTV beschränkt, DigiSanté (24061) auf das Programm DigiSanté. |

## 4. Track-Record der in der Recherche genannten Anbieter

Alle Zuschläge seit 07/2024 im ausgewerteten Datensatz; 4 von 12 genannten Anbietern sind vergaberechtlich belegt:

|    | Anbieter                          | Rolle in der Recherche                 | Zuschläge (Auswahl)                                                                                          | Volumen sichtbar |
|----|-----------------------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------|
| 1  | Ontotext (Graphwise)              | Muster B: Graph-Plattform              | Swissgrid AIM als RDF Knowledge Graph (6,89 Mio.)                                                            | 6,9 Mio.         |
| 2  | Zühlke Engineering AG             | Integrator CDE-Bund (mit vrame)        | BBL CDE-Bund (14,98 Mio.); Swissgrid Outage Planning Platform (10,27 Mio. Anteil); ASTRA Fachapplikation Trassee (3,85 Mio.); BAG-Rahmen Dashboards (Partner) | ~29 Mio. + Rahmen |
| 3  | IBM Schweiz AG                    | FileNet (DALA)                         | FileNet-Dienstleistungen ESTV (33,5 Mio.); BBL Passport Advantage 2026-2028 (22,4 Mio.); Public Clouds Bund   | > 55 Mio.        |
| 4  | Planon                            | CAFM (nicht verifiziert)               | Universität Zürich, CAFM-Vertragsverlängerung (1,35 Mio.)                                                    | 1,3 Mio.         |
| 5  | EVANA, Architrave, Findable       | Muster A: Dokumenten-KI für Immobilien | keine Zuschläge im Zeitraum                                                                                  | -                |
| 6  | sd-solution (TwinEstate)          | KBOB-konforme Ablage                   | keine Zuschläge im Zeitraum                                                                                  | -                |
| 7  | Neo4j, Palantir, Stardog          | Muster B: Graph-Plattformen            | keine Zuschläge im Zeitraum                                                                                  | -                |
| 8  | vrame                             | Produkt CDE-Bund                       | kein eigener Zuschlag (über Zühlke)                                                                          | -                |

Weitere Anbieter mit passenden Referenzen aus dem Datensatz:

|   | Anbieter                    | Zuschläge (Auswahl)                                                                                         | Volumen sichtbar |
|---|-----------------------------|-------------------------------------------------------------------------------------------------------------|------------------|
| 1 | Artificialy SA, Lugano      | HUG RAG-Chatbots (Rahmen, 332k); ECA Vaud, Consulting KI (800k)                                             | ~1,1 Mio.        |
| 2 | Liip AG                     | HUG RAG-Chatbots (Rahmen, 332k); SPRINT Los 2; BBL NUX Statistikportal (1,76 Mio.); DigiAgriFoodCH           | > 2 Mio. + Rahmen |
| 3 | BEGASOFT AG, Bern           | SSGI KI-Plattform (249k); BBL Medienplattformen DMA (1,84 Mio.)                                              | ~2,1 Mio.        |
| 4 | AlpineAI AG, Davos          | KI-Plattform Zürcher Gemeinden (4,02 Mio.)                                                                  | 4,0 Mio.         |
| 5 | Cadmec AG, Kemptthal        | Immobilien Aargau: Vertragsdatenerfassung CAFM (176k), Pflege digitale Architekturpläne (618k)              | ~0,8 Mio.        |
| 6 | B3 digital AG, Gossau SG    | CDE Stadt Zürich (2,49 Mio.); ASTRA Westumfahrung Zürich (1,26 Mio.)                                         | ~3,7 Mio.        |
| 7 | GBL Gubler AG, Frauenfeld   | ASTRA Archivakten Nationalstrassen (220k); Stadt Biel Baugesuche (734k); Stiftsarchiv St. Gallen (929k)      | ~1,9 Mio.        |
| 8 | Cognizone, Bruxelles        | LINDASnext, Linked-Data-Infrastruktur des Bundes (17,2 Mio.)                                                | 17,2 Mio.        |

Hinweis: Fehlende Zuschläge bedeuten nicht, dass ein Anbieter keine Schweizer Kunden hat. Aufträge unter den Schwellenwerten, Abrufe aus Rahmenverträgen und Lieferungen über Wiederverkäufer erscheinen nicht auf simap.

## 5. Verweise und Anhang

## 5.1 Verweise

- Quelle: simap.ch Public API (vollständig seit Plattformstart 01.07.2024, Abfrage vom 02.11.2026)
- Datenbasis: 3'711 Zuschläge aus 5'671 Projekten (CPV 72000000 IT-Dienste / 48000000 Software und 33 Stichwortsuchen zu KI, Graph/Daten und Immobilien-Domäne), je angereichert mit Zuschlagsempfänger, Preis und Auftragsbeschreibung.
- Rohdaten: research/simap/simap_awards_all.csv
- Skript: research/simap/research.py
- Grundlagen: Ausgangslage und Vision (BBL Asset Search); Ontology-Aligned AI Search over an Asset Information Model (Recherche, Oktober 2026)

## Methodik

- Relevanz-Score aus gewichteten Mustern in drei Gruppen (KI/Suche, Graph/Daten, Immobilien-Domäne), Bonus von 3 Punkten, wenn Technik und Domäne zusammen vorkommen, Abzüge für Bauleistungen, Hardware, Netzwerk und Lizenzen. Der Score sortiert nur vor; die Auswahl in Kapitel 2 bis 4 ist manuell.
- Der Score in der CSV wurde nach der Abfrage mit korrigierten Mustern neu berechnet (Titel und erste 600 Zeichen der Beschreibung).
- Die Stichwortsuche von simap ist unscharf: Mehrwortige Begriffe wie «Data Lake» oder «Digital Twin» erreichen die Obergrenze von 500 Treffern, Begriffe unter 3 Zeichen («KI») lehnt die API ab. Vergaben ausserhalb von CPV 72/48 sind deshalb nur über die Stichworte und nicht vollständig erfasst.

## 5.2 Anhang

| Datei                                 | Geändert   |
|---------------------------------------|------------|
| research/simap/research.py            | 02.11.2026 |
| research/simap/simap_awards_all.csv   | 02.11.2026 |
