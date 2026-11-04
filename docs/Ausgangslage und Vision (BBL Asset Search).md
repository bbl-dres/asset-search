## Ausgangslage und Vision

## Ausgangslage

Der Bereich Bauten des BBL ist das Immobilien-Kompetenzzentrum der zivilen Bundesverwaltung und verantwortet über 2'700 Objekte im In- und Ausland - von Verwaltungs-, Regierungs- und Gerichtsgebäuden über Zollanlagen und Forschungsanstalten bis zu Botschaften. Die Informationen zu diesen Objekten sind auf über 20 interne Fachanwendungen und mehrere externe Register verteilt. SAP RE-FX führt die Immobilienstammdaten von der Wirtschaftseinheit bis zum Raum, SAP PS die Bauprojekte. Pläne und Dokumente liegen in FileNet DALA, ActaNova GEVER und der CDE-Bund, die Instandhaltung in SAP PM, Energiedaten in InterWatt, die Erhaltungsplanung in Wüest Dimensions und Geodaten in BBL GIS IMMO. Externe Register wie GWR, amtliche Vermessung und Grundbuch liefern die amtlichen Identifikatoren (EGID, EGRID).

Mit der Übersicht Systeme IMMO wurde im Rahmen des Programms SUPERB eine physische Datenarchitektur erstellt, die diese Systeme und ihre Geschäftsobjekte inventarisiert. Sie zeigt: Die strukturierten Stammdaten sind mit SAP RE-FX klar geführt und werden in die künftige S/4HANA-Landschaft des Bundes überführt. Für Dokumente gibt es dagegen kein gemeinsames Modell. DALA, GEVER und CDE-Bund haben je eigene Dokument- und Dossierstrukturen, eine einheitliche Klassifikation nach Dokumenttyp fehlt, und die Verknüpfung eines Dokuments mit Gebäude, Geschoss, Raum oder Anlage ist nicht durchgängig vorhanden.

Eine Bedarfsmeldung aus dem Projektmanagement bestätigt das aus Sicht der Nutzenden. Die Projektdokumentation wird in ActaNova nach Projekten abgelegt, nicht nach Gebäuden. Wer für ein neues Projekt wissen muss, welche Bauprojekte und Analysen in einem Gebäude bereits durchgeführt wurden, ist auf das Gedächtnis von Projektleitenden oder Objektverantwortlichen angewiesen oder muss die Unterlagen jedes früheren Projekts einzeln durchsuchen. Ähnlich bei strukturierten Daten: Zu abgeschlossenen BBL-Projekten liegen umfangreiche Daten zu Kosten und Terminen vor, die heute kaum systematisch für die Schätzung neuer Projekte genutzt werden.

Eine Recherche zu ontologiegestützter KI-Suche (Oktober 2026) kommt zum Schluss, dass die Bausteine dafür ausgereift sind: IFC 4.3 und W3C BOT als Strukturmodell, der KBOB-Dokumenttypenkatalog als Klassifikationsvokabular, offene Dokumentparser wie Docling und souveräne Sprachmodelle wie Apertus oder der geplante KI-Service des BIT. Ein fertiges Produkt, das Asset-Wissensgraph, Klassifikation nach KBOB und KI-Suche für ein öffentliches Immobilienportfolio kombiniert, gibt es jedoch nicht. Kommerzielle Lösungen klassifizieren nach eigenen Taxonomien und werden meist in Deutschland oder der EU gehostet.

## Vision

Das BBL verfügt über ein gebäudebezogenes Asset Information Model (AIM), das alle relevanten Informationen zu einem Objekt über seinen gesamten Lebenszyklus auffindbar macht - unabhängig davon, in welchem System sie liegen. Einstieg ist das Gebäude, identifiziert über SAP-ID, EGID oder Adresse. Das AIM verbindet drei Arten von Informationen: die Dokumente, Pläne und Modelle aus den Quellsystemen, die Historie der Bauprojekte und Arbeiten an einem Gebäude sowie strukturierte Daten wie Flächen, Erstellungs- und Betriebskosten, Termine, Energieverbrauch und Zustand. Kern ist ein schlanker Wissensgraph, der diese Informationen über die Objekthierarchie (Grundstück, Gebäude, Geschoss, Raum, Anlage) zusammenführt. Dokumente werden automatisiert nach dem KBOB-Dokumenttypenkatalog klassifiziert und dem richtigen Objekt und Bauprojekt zugeordnet; unsichere Fälle prüfen Fachpersonen.

Über eine KI-Suche stellen Mitarbeitende aus Projekt-, Objekt- und Portfoliomanagement Fragen in natürlicher Sprache. Fragen nach Dokumenten beantwortet die Dokumentensuche, Fragen nach Zahlen eine Abfrage auf die strukturierten Daten. Kosten und Kennwerte stammen damit immer aus den Quellsystemen und werden nicht vom Sprachmodell erzeugt. Jede Antwort nennt ihre Quelle.

Dabei bleiben die Quellsysteme führend: SAP RE-FX bzw. künftig S/4HANA für Immobilienstammdaten, SAP PS und die Finanzmodule für Projekt- und Kostendaten, CDE-Bund, DALA und GEVER für Dokumente, das EDM für Energiedaten. Das AIM ersetzt keine Ablage, sondern bildet einen semantischen Index darüber. Es folgt den Prinzipien Once-Only, offene Standards (IFC, BOT, SKOS, DCAT-AP CH) und amtliche Identifikatoren (EGID, EGRID, SAP-Objekt-ID) als Verknüpfungsschlüssel. Betrieben wird es auf Bundesinfrastruktur mit austauschbaren Sprachmodellen, damit die Daten in der Schweiz bleiben und keine Abhängigkeit von einzelnen Herstellern entsteht. Entscheidend sind nachvollziehbare Antworten, eine sichtbare Datenqualität und der Schutz sensibler Inhalte gemäss DSG und ISG.

## Zielbild

Wenn die Vision umgesetzt ist, gilt:

- **Ein Einstieg pro Gebäude.** Über SAP-ID, EGID oder Adresse lassen sich alle Dokumente, Pläne, Modelle und Daten zu einem Gebäude, Geschoss oder Raum finden, ohne die Quellsysteme zu kennen.
- **Nachvollziehbare Gebäudehistorie.** Abgeschlossene Bauprojekte und Arbeiten (z.B. Neubau, Umbau, Instandsetzung) sind dem Gebäude zeitlich zugeordnet, samt ihrer Bauwerksdokumentation und den durchgeführten Analysen. Als Modell dienen die GWR-Objekte Bauprojekt und Arbeiten. Das Wissen hängt nicht mehr an einzelnen Personen.
- **Kennwerte aus eigenen Projekten.** Erstellungs-, Betriebs- und Lebenszykluskosten sowie Termine abgeschlossener Projekte stehen als vergleichbare Kennwerte zur Verfügung und unterstützen die Schätzung neuer Projekte - vergleichbar mit Produkten wie KeeValue, aber auf Basis der BBL-Projekte.
- **Einheitliche Dokumenttypen.** Jedes Dokument trägt einen KBOB-Dokumenttyp (z.B. O14019 Betriebsbewilligung, O15002 Abnahmeprotokoll). Daraus leiten sich Aufbewahrungsfristen und Dokumentationspflichten ab. Der Katalog von 2016 wird um BIM-Dokumenttypen ergänzt und versioniert.
- **Verlässlicher Objektbezug.** Dokumente und Projekte sind über EGID, EGRID sowie SAP-Objekt- und Projekt-IDs mit RE-FX, SAP PS, GWR und GIS verknüpft.
- **Nachvollziehbare Antworten.** Jede Antwort nennt Quelldokument oder Quellsystem, Objekt und Konfidenz und stützt sich nur auf belegte Fakten.
- **Sichtbare Lücken.** Fehlende Pflichtdokumente oder ablaufende Garantien lassen sich je Objekt und über das ganze Portfolio auswerten.

Typische Fragen, die das AIM beantworten soll:

- «Welche Bauprojekte und Analysen wurden im Gebäude X seit 2000 durchgeführt, und wo liegen die Berichte?»
- «Zeige alle Prüfberichte und Abnahmeprotokolle der Lüftungsanlagen im Gebäude X.»
- «Was kosteten vergleichbare Gesamtsanierungen von Bürogebäuden pro m² Geschossfläche, und wie lange dauerten sie?»
- «Wie haben sich die Betriebskosten von Gebäude X seit der letzten Sanierung entwickelt?»
- «Für welche Gebäude fehlt eine gültige Betriebsbewilligung?»

## Ausbau in Stufen

| Stufe             | Ziel                                           | Inhalte im AIM                                                                   | Wichtigste Quellen                                        |
|-------------------|------------------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------|
| 1 - Gebäudeakte   | Dokumente und Baugeschichte pro Gebäude finden | Grundstück, Gebäude, Geschoss, Raum, Bauprojekt, Arbeiten, Dokument              | SAP RE-FX, SAP PS, GWR, ActaNova GEVER, DALA, CDE-Bund    |
| 2 - Daten und Technik | Kennwerte und Anlagen                      | zusätzlich Flächen, Kosten, Termine, Anlage, Komponente, Nachweis, Messpunkt     | RE-FX Bemessung, SAP PS/IM/FI/CO, SAP PM, EDM, Wüest EHP  |
| 3 - Lebenszyklus  | Lebenszykluskosten und Benchmarks              | zusätzlich Mangel, Garantie, Vertrag, Lebenszykluskosten                         | CDE-Bund, SAP PM, SAP FI/CO                               |

## Abgrenzung

- Kein neues führendes System und keine neue Dokumentablage; CDE-Bund, DALA und GEVER werden nicht abgelöst. Projekt- und Kostendaten werden weiterhin in den SAP-Modulen geführt.
- Gebäudeautomation (Domotik, BMS) und Echtzeitdaten sind in den ersten Stufen nicht enthalten.
- Kostenkennwerte nach eBKP-H setzen voraus, dass die Lizenzfrage mit CRB geklärt ist.

## Nächster Schritt

Empfohlen wird ein Pilot über 3-4 Monate mit 3-5 Gebäuden, an denen bereits mehrere Bauprojekte abgeschlossen wurden: mindestens ein aktuelles BIM-Projekt aus der CDE-Bund und ein Bestandsgebäude mit gescannten Unterlagen. Der Pilot umfasst Stufe 1 mit Gebäudeakte und Projekthistorie, die Klassifikation nach KBOB mit Prüfung durch Fachpersonen und die Verknüpfung zu SAP RE-FX, SAP PS, GWR und GIS. Die Testfragen kommen aus dem Projektmanagement; gemessen werden Klassifikationsgenauigkeit, Trefferqualität der Suche und Belegtreue der Antworten. Die Anforderungen werden mit der laufenden Business-Analyse zu CAFM/AIM im Objektmanagement abgestimmt.

## Grundlagen

- Ontology-Aligned AI Search over an Asset Information Model (Recherche, Oktober 2026)
- Übersicht Systeme IMMO (Arbeitsdokument, Programm SUPERB)
- Bedarfsmeldung BBL Projektmanagement (E-Mail, Oktober 2026)
- Bereich Bauten BBL: https://www.bbl.admin.ch/de/bauten
