# Ontology-aligned AI search over an Asset Information Model for BBL Bauten – research report (October 2026)

Building an ontology-aligned RAG over BBL's AIM is feasible with today's components, but no product delivers it ready-made: the realistic path is a composable architecture in which a small, IFC/BOT-aligned asset graph (site, parcel, building, storey, space, document) acts as the backbone, the KBOB Dokumenttypenkatalog and eBKP-H are loaded as controlled vocabularies, and LLM/VLM classification plus hybrid vector-graph retrieval run on Swiss-hosted or on-prem infrastructure.

## TL;DR

- The building blocks are mature individually (IFC 4.3, W3C BOT, bSDD, GraphRAG-capable graph stores, open document parsers such as Docling, open-weight LLMs such as Apertus), and peer-reviewed work since 2025 shows LLM + knowledge graph querying of IFC data works on small models\[1\] – but there is no published, evaluated end-to-end system that combines asset KG, document classification against a national taxonomy and RAG for a public real estate portfolio. BBL would be at the frontier, not following a template.
- Commercial document-AI for real estate (EVANA, Architrave, Findable) already classifies building documents into 400+ proprietary classes; EVANA claims a hit rate of "over 98 percent" and Architrave claims "98% accuracy: verified by Human QA" (vendor claims, not independently tested). None was found that uses the KBOB catalog natively; the one Swiss product aligned with KBOB (sd-solution TwinEstate) is a structured filing system, not an AI classifier. Classification against KBOB DTC codes will need either vendor customisation or an in-house LLM pipeline using the official XLSX version of the catalog.
- Recommended next step: a 3–4 month pilot on 3–5 buildings, using the minimal ontology described below, KBOB DTC classification with human-in-the-loop, Swiss identifiers (EGID, EGRID) as join keys to SAP RE-FX, GWR and GIS, and a sovereign LLM option (Apertus or the BIT AI service)\[2\] – evaluated on classification accuracy per document group, retrieval precision, and answer faithfulness.

## Key Findings

1. **Maturity of the field.** Ontology-grounded and graph-based RAG is an active research area (2024–2026) with consistent evidence that grounding LLMs in a schema reduces errors,\[3\]\[4\] but evidence in the built environment comes mostly from single-building IFC demos (e.g. Graph-RAG over IFC presented at EC3 2025, multi-agent text-to-Cypher evaluated on an IFC-derived graph).\[5\]\[6\] Portfolio-scale, multi-source, multilingual evaluations are missing.
2. **Taxonomy fit.** The KBOB-IPB Anhang C catalog is well suited as a classification target: each document type has a stable 6-character code (e.g. O01001 Immobilienhandbuch, O15002 Abnahmeprotokoll, B17012 Fotodokumentation), a description usable as a zero-shot label definition, and attributes (documentation type PD/OD, file format, retention, SIA phases) that can drive governance rules.\[7\] An editable XLSX and a French version exist, which makes machine import and FR prompts straightforward.\[8\]\[9\]
3. **Ontology fit.** IFC 4.3 covers site, building, storey, space, systems, elements, documents, costs and classification references; W3C BOT gives a lightweight RDF backbone; bSDD provides the documented mechanism to attach external classifications (IfcClassification / IfcClassificationReference).\[10\]\[11\]\[12\] Parcel (EGRID) and building/dwelling identifiers (EGID/EWID) are not first-class IFC entities and must be modelled as identifiers or external references.
4. **eBKP-H is not openly machine-readable.** No public evidence was found that CRB publishes eBKP-H in bSDD, LINDAS or I14Y; CRB distributes the eBKP-H–IFC4 rule set as Excel and licenses data use (eBKP-Gate).\[13\]\[14\] Licensing must be clarified before eBKP-H is loaded into a graph or used for training.
5. **Swiss federal building blocks are emerging.** KBOB itself now runs public repositories that validate data dictionaries against ISO 23386/23387/12006 and DCAT and transform them into RDF/Turtle for LINDAS and JSON for I14Y;\[15\]\[16\] CDE-Bund (Vrame) is live for ASTRA, BBL and armasuisse;\[17\]\[18\] BIT has piloted an on-prem open-source LLM assistant with RAG; Apertus is available with open weights.\[19\]\[20\]
6. **Reference projects are partial.** The closest analogues are US GSA (deployed RAG chatbot and portfolio LLM, 2025 AI inventory),\[21\] Statsbygg (AI classification of FDV documents by NS 3451 via Findable, per vendor sources),\[22\] SBB (AIM-CDE under construction, FDK data catalog)\[23\]\[24\] and BImA/Bundeswehr (Objektkatalog Bundesbau mapped to IFC and SAP).\[25\] None publishes accuracy figures or architecture details sufficient to copy.

## 1. Reference architecture by layer

The layering requested by BBL matches the pattern found in the literature on knowledge-graph-based digital twins of built assets, where a central knowledge graph acts as a semantic index over heterogeneous stores rather than as the single storage location.\[26\] The table lists options per layer; they can be mixed.

| Layer | Function | Open-source / self-hosted options | Commercial / platform options | Notes for BBL |
|---|---|---|---|---|
| Data – documents | Original files, versions, renditions | Object storage (S3-compatible), existing CDE-Bund as source of truth | CDE-Bund (Vrame), EVANA 360, Architrave data rooms | Keep originals in source systems; store extracted text and renditions in the lake |
| Data – graph | Asset hierarchy, classifications, links document↔asset | Apache Jena / Fuseki (RDF), Neo4j Community (property graph) | Graphwise GraphDB, Neo4j Enterprise/Aura, Stardog, Palantir Foundry ontology | RDF favours standards (BOT, SKOS, DCAT, SHACL); property graph favours developer tooling and text-to-Cypher |
| Data – vector / search | Embeddings, full-text, hybrid search | pgvector, Qdrant, Weaviate, OpenSearch | Azure AI Search, Elastic | Hybrid (BM25 + vector) matters for codes, room numbers and German compounds |
| Data – structured | Master and process data snapshots | PostgreSQL / lakehouse (Parquet, Delta/Iceberg) | Databricks, Snowflake, Microsoft Fabric | Mirror SAP RE-FX, GWR, EDM; do not replace them |
| Integration | Ingestion, mapping, identity resolution | Python ETL, Apache NiFi / Airflow, IfcOpenShell for IFC, GDAL for GIS | Vendor connectors, Foundry pipelines | Use EGID, EGRID, SAP object IDs and CDE document IDs as join keys |
| AI – parsing | OCR, layout, tables, figures | Docling (MIT, IBM Research Zurich), Unstructured, Tesseract\[27\] | Azure Document Intelligence, Autodesk drawing extraction | Plans need title-block extraction; Autodesk's feature works on PDFs only\[28\]\[29\] |
| AI – classification / extraction | KBOB DTC, eBKP-H, metadata, asset links | Open-weight LLM/VLM (Apertus, other open models) with schema-constrained output | EVANA AI, Architrave, Findable | Zero-/few-shot with label descriptions first; fine-tune only if needed |
| AI – retrieval / answer | GraphRAG, text-to-SPARQL/Cypher, agents | Microsoft GraphRAG, LightRAG, LlamaIndex property graphs, LangChain, Haystack | Graphwise GraphRAG, Neo4j GraphRAG, Azure AI Search + GraphRAG | Route structured questions to graph queries, open questions to hybrid RAG |
| Governance | Catalog («Datenverzeichnis»), lineage, access, quality | OpenMetadata, DataHub, CKAN; SHACL for graph validation; I14Y / DCAT-AP CH for publication | Collibra, Atlan, Purview | BBL prototype data-catalog-immo (DCAT-AP CH) can serve as seed\[30\] |
| Frontend | Search, chat, exploration, maps, 3D | Web app with xeokit / That Open (IFC viewer), MapLibre/OpenLayers | ArcGIS Enterprise (until open-source GIS migration), vendor UIs | Answers must show source document, KBOB type, asset and confidence |

Three architectural patterns emerged from the screening:

| Pattern | Description | Strengths | Weaknesses |
|---|---|---|---|
| A – Vendor document-AI + integration | Real estate document-AI (e.g. EVANA, Architrave) on top of documents, integrated with SAP/GIS | Fast start, proven classification on real estate documents | Proprietary taxonomies, KBOB mapping effort, SaaS hosting in Germany/EU, limited ontology control |
| B – Semantic platform | Enterprise KG platform (e.g. GraphDB/PoolParty, Neo4j, Foundry) with GraphRAG | Strong ontology governance, reasoning, out-of-the-box GraphRAG | Licence cost, specialist skills, document AI still needs to be built or bought |
| C – Composable open source on federal infrastructure | Docling + open LLM + RDF/property graph + vector store, run by BIT or on Swiss Government Cloud | Sovereignty, no lock-in, aligned with KBOB RDF work | Highest internal effort, operations burden, BBL must own MLOps |

A hybrid of B or C for the graph and governance layers, with optional vendor document-AI for the bulk legacy backlog, is the most defensible option.

## 2. Ontology and classification

### 2.1 How the standards fit together

| Concern | Standard / artefact | Role in the AIM |
|---|---|---|
| Information management process | ISO 19650 (AIM/PIM, CDE), DIN SPEC 91391 | Defines the AIM as the operational information container;\[31\]\[32\] Bauen digital Schweiz notes that an AIM is in practice a collection of documents, plans, models and databases rather than one file\[33\] |
| Data schema | ISO 16739-1 (IFC 4.3) | Spatial structure, systems, elements, documents, costs, classification references |
| Lightweight RDF backbone | W3C LBD: BOT (Site, Building, Storey, Space, Element, Zone, Interface), plus PRODUCT, BEO, MEP\[34\] | Graph backbone that is easy to query and extend; ifcOWL only if full IFC semantics are needed |
| Properties and dictionaries | bSDD, ISO 23386/23387, ISO 12006-3, KBOB data dictionary repos, KBOB Fachdatenkatalog\[35\] | Property definitions and classification links\[36\] |
| Element classification | CRB eBKP-H (SN 506 511) | Classify construction elements; attach via IfcClassificationReference\[37\] |
| Document classification | KBOB-IPB Anhang C Dokumenttypenkatalog 2016 | Controlled vocabulary for document type (DTC code) |
| Requirements | IDS, EN 17412 (LOIN), COBie | Validate deliveries; COBie for handover data incl. warranties |
| Sensors / measurements | Brick, SOSA/SSN, RealEstateCore\[34\] | Link EDM meters and time series to spaces and systems\[38\] |
| Swiss identifiers | GWR (EGID, EWID), amtliche Vermessung (EGRID), eCH standards | Join keys to registers, SAP RE-FX and GIS |
| Metadata publication | DCAT-AP CH, I14Y, LINDAS | Publish catalog entries and vocabularies |
| Lifecycle record | EU Digital Building Logbook (EPBD recast 2024/1275, Art. 2(41)) | Reference concept; DBL is defined as a common repository for all relevant building data\[39\] |

### 2.2 IFC mapping of the required asset hierarchy

| BBL concept | IFC 4.3 | BOT / RDF | Identifier / classification |
|---|---|---|---|
| Parcel | No dedicated entity; IfcSite or external reference | bot:Site (or custom class) | EGRID from amtliche Vermessung |
| Site | IfcSite | bot:Site | SAP RE-FX economic unit / site ID |
| Building | IfcBuilding | bot:Building | EGID (GWR), SAP building ID |
| Storey | IfcBuildingStorey | bot:Storey | Storey code |
| Space / room | IfcSpace (dwellings via IfcZone or IfcSpace) | bot:Space | Room number, EWID where applicable |
| Technical system | IfcSystem / IfcDistributionSystem | bot:Zone or Brick system | Anlagekennzeichnung, eBKP-H D-group |
| Component | IfcDistributionElement subtypes, IfcTypeObject | bot:Element, Brick equipment | Product data templates (ISO 23387) |
| Construction element | IfcBuiltElement (renamed from IfcBuildingElement in 4.3) | bot:Element | eBKP-H via IfcClassificationReference |
| Document | IfcDocumentInformation / IfcDocumentReference via IfcRelAssociatesDocument | dcterms / schema.org document class | KBOB DTC code |
| Certificate | IfcDocumentInformation (with type) | Document subclass | KBOB type (e.g. Bewilligungen O14xxx, Prüfberichte B17013) |
| Measurement | IfcPerformanceHistory, property values | SOSA Observation / Brick Point | EDM meter ID |
| Construction cost | IfcCostSchedule, IfcCostItem | Custom cost class | eBKP-H cost groups |
| Operating cost | Not well covered in IFC | Custom class linked to SAP cost objects | SAP RE-FX / FI |
| Issue / defect | BCF topics; IfcTask partly | Custom Issue class | KBOB O15005 Mängelliste, O10012 Mängelrüge |
| Guarantee / warranty | Pset_Warranty; COBie Warranty | Custom class | KBOB O15010 Schlussprotokoll (end of guarantee) |

The bSDD documentation specifies how dictionaries map into IFC: dictionary name to IfcClassification.Name, dictionary URI to IfcClassification.Specification in IFC4x3_ADD2 (Location in IFC4), version to Edition, owner to Source, and IDS uses classification.system and classification.uri.\[10\]\[12\] The same pattern can carry both eBKP-H and the KBOB document catalog if they are published as dictionaries – which neither currently is, as far as could be verified.

### 2.3 Structure of the KBOB Dokumenttypenkatalog (Anhang C)

- Four document categories (Dokumentarten) based on SIA 112: O Organisation und Administration, K Kosten und Verträge, B Beschriebe und Konzepte, V Visualisierungen.\[40\]
- Groups below each category (e.g. O01 Stammorganisation, O05 Informationsmanagement, O10 Korrespondenz und Protokolle, O13 Gesuche, O14 Bewilligungen, O15 Technische Protokolle, B17 reports).\[7\]
- Document types with 6-character codes and descriptions (e.g. O14019 Betriebsbewilligung, O15004 Inbetriebnahmeprotokoll, B17005 Energiebericht).\[7\]
- Attribute columns: documentation type (Projektdokumentation, Objektdokumentation, Prozess-, Fach-, Anlagedokumentation), file format (DWG, PDF-A, Office, andere), quality reference (CAD-, CAFM-, BIM-Richtlinie), retention (none, 5 years, 12 years, until replacement, until purpose lapses), SIA phases 11–53, and a mapping column to BDM15 codes.\[7\]

Implications: the description column is directly usable as a label definition for zero-shot LLM classification; retention and PD/OD attributes can be inherited as governance metadata once a document is classified; the 2016 catalog predates BIM-centric deliverables and has no explicit types for IFC models, IDS files or sensor data, so extensions will be needed and should be versioned.

### 2.4 Recommended starting ontology and extension path (options)

| Phase | Scope | Classes | Vocabularies |
|---|---|---|---|
| 1 – Minimal | Find documents per asset | Parcel, Site, Building, Storey, Space, Document, Organisation | KBOB DTC (as SKOS), EGID/EGRID/SAP IDs |
| 2 – Technical | Systems and evidence | + System, Component, Certificate, Measurement point | eBKP-H (licence permitting), KBOB FDK / data dictionary properties, Brick for EDM points |
| 3 – Process and cost | Lifecycle questions | + Issue, Warranty, Product, CostItem, Contract | eBKP-H cost groups, COBie, BCF |

Options for the backbone: (a) BOT + SKOS + DCAT in RDF with SHACL shapes, aligning with KBOB's RDF/LINDAS direction; (b) a property graph whose labels mirror IFC entity names, which current text-to-Cypher research uses; (c) a relational semantic layer over the lakehouse. Option (a) best fits federal publication via I14Y; option (b) has the most LLM tooling.

The requester's open KBOB Fachdatenkatalog mockup (davras5/kbob-fdk: classifications, LOI attributes, IFC mappings for building elements) and the official KBOB-admin data dictionary repositories (templates and validation aligned with ISO 23386, ISO 23387, ISO 12006 and DCAT; SchemaForge producing RDF/Turtle for LINDAS INT and an I14Y JSON bundle, under a provisional namespace) are directly reusable as the property layer for Phase 2.\[15\]\[16\]\[30\]

## 3. Academic literature

| Title | Authors | Year | Venue / ID | Relevance |
|---|---|---|---|---|
| BOT: The Building Topology Ontology of the W3C Linked Building Data Group | Rasmussen, Lefrançois, Schneider, Pauwels | 2021 | Semantic Web 12(1):143–161, DOI 10.3233/SW-200385 | Core lightweight ontology for site–building–storey–space–element backbone\[41\]\[42\] |
| Knowledge Graphs and Linked Data for the Built Environment | Pauwels et al. | 2022 | Book chapter (Springer) | Foundational overview of LBD, IFC-to-RDF conversion and KG use in AECO\[43\] |
| Knowledge graph-based data integration system for digital twins of built assets | Ramonell et al. (authors to verify) | 2023 | Automation in Construction, ScienceDirect S0926580523003692 | Neo4j KG as semantic index over asset information model, IFC-to-property-graph; closest architectural analogue\[26\] |
| A Survey on Semantic Modeling for Building Energy Management | multiple | 2024 | arXiv 2404.11716 | Compares BOT, SAREF, SSN/SOSA, Brick for measurement and energy data\[34\] |
| From Local to Global: A Graph RAG Approach to Query-Focused Summarization | Edge et al. (Microsoft) | 2024 | arXiv 2404.16130 | Original GraphRAG method; entity graph + community summaries\[6\] |
| Docling Technical Report / Docling toolkit | IBM Research | 2024–2025 | arXiv 2408.09869; AAAI 2025 version | Open document parsing with layout, OCR and tables; ingestion candidate\[44\]\[45\] |
| Automation of text document classification in the budgeting phase of the construction process: SLR | multiple | 2024 | Construction Innovation 24(7), Emerald | Pre-LLM baseline for construction document classification; notes small training sets\[46\] |
| LLM-assisted Graph-RAG Information Extraction from IFC Data | Iranmanesh, Vakaj et al. | 2025 | EC3 2025, DOI 10.35490/EC3.2025.366; arXiv 2504.16813 | IFC → graph → LLM-generated Cypher with GPT-4o; reports limits from IFC hierarchy complexity\[1\]\[47\] |
| Natural Language Information Retrieval from BIM Models: An LLM-Based Multi-Agent System Approach | Borrmann group (TUM) | 2025 | EC3 2025, DOI 10.35490/EC3.2025.265 | Agentic querying of BIM models\[48\] |
| Advancing BIM information retrieval with an LLM-based query-domain-specific language | Cheng et al. | 2025 | Automation in Construction 178, 106374 | DSL-mediated BIM retrieval, alternative to free text-to-query\[48\] |
| BIM-based semantic enrichment and knowledge graph generation via geometric relation checking | multiple | 2025 | Automation in Construction 173, 106081 | Deriving graph relations from geometry\[48\] |
| Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs | multiple | 2025 | arXiv 2511.08274 | Evaluated on CypherBench and IFC-derived graphs; agentic correction improves accuracy\[6\] |
| Enhancing IFC Model Interpretability Using Knowledge Graphs (MSc thesis) | Ata (TUM) | 2025 | mediaTUM 1782062 | Uses IFC KG as constraint for LLM answers\[49\] |
| RAG and Ontologies for Information Retrieval: A Literature Review | Univ. of Toronto EIL | 2025 | ONTOLLM 2025, CEUR-WS Vol-4176 | Taxonomy of ontology-driven RAG patterns\[50\] |
| Next-generation language-based data mining techniques for smart construction documentation | multiple | 2025 | Canadian Journal of Civil Engineering, DOI 10.1139/cjce-2025-0329 | Review of NLP/LLM on construction documents incl. RFI classification (88.5 % accuracy)\[51\] |
| Envisaging a European Digital Building Renovation Logbook: Proposal of a Data Model | multiple | 2024 | Applied Sciences 14, 8903 | Conceptual DBL data model; reference for lifecycle record structure\[52\] |
| Towards the definition of a European Digital Building Logbook: A survey | multiple | 2023 | (see ResearchGate 373355160) | Argues for an EU semantic data model of DBL core elements\[53\] |
| Leveraging large language models for document classification in the banking sector | multiple | 2026 | Int. J. of Data Science and Analytics, Springer | Zero-shot classification from label descriptions – directly transferable to KBOB DTC\[54\] |
| OntoLLM: Enhancing LLM grounding and digression prevention with ontologies and knowledge graphs | multiple | 2026 | Expert Systems with Applications | Dual structured/unstructured handlers, evaluated on industrial manuals\[4\] |
| Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations | multiple | 2026 | arXiv 2605.26874 | Typed asset KG (site, location, equipment, work order) for LLM operations; transferable to FM\[55\] |
| Review of automated code compliance with ML/LLM | Alnuzha et al. | 2026 | ITcon 2026_38 | Notes LLMs still weak on spatial reasoning (20–60 %) and points to Graph RAG over IFC\[56\] |

Assessment: evidence quality is mostly conference papers and preprints with small test buildings. No peer-reviewed study was found on LLM classification of Swiss or German-language building documentation, or on KBOB/eBKP-H as KG vocabularies.

## 4. Market screening

Verification status: "Verified" means the capability was confirmed on the vendor's own documentation or a primary source during this research; "Vendor claim" means a marketing figure not independently tested; "Not verified" means listed from general market knowledge and must be checked before shortlisting.

### 4.1 CDE and document management with AI

| Product | Vendor | Layer | IFC / bSDD | Document classification | Custom taxonomy | Deployment | References | Status |
|---|---|---|---|---|---|---|---|---|
| CDE-Bund (Vrame CDE) | vrame consult GmbH (Berlin), with Zühlke | Data / CDE | BIM/IFC exchange (2D and 3D) | Not documented | Project structures | Federal operation | ASTRA, BBL, armasuisse | Verified as federal CDE; AI features not found\[17\]\[18\] |
| Autodesk Docs / Construction Cloud – Automated Drawing Extraction | Autodesk | AI parsing | Autodesk BIM | OCR of title block attributes, splits multi-page PDFs; PDF only, DWG not supported (open user request 2025)\[29\] | Custom attributes via title block templates\[28\]\[57\] | SaaS (US/EU regions) | Broad market | Verified (feature); no taxonomy classification |
| ProjectWise / iTwin, Thinkproject, Dalux, Oracle Aconex, Nemetschek dTwin | various | CDE / twin | IFC support varies | AI features announced by several vendors | varies | Mostly SaaS | varies | Not verified in this research |

### 4.2 Real estate document-AI and FM platforms

| Product | Vendor | Classification capability | Custom taxonomy | Deployment | References | Status |
|---|---|---|---|---|---|---|
| EVANA AI / EVANA 360 / EVA | EVANA AG (Saarbrücken, DE) | 400+ real estate document types, extraction, AI assistant over data room\[58\]\[59\] | Own schema; mapping to customer structure stated | EVANA Secure Cloud\[60\] | HIH Real Estate, Mann Immobilien\[61\]\[62\] | Vendor claim: >98 % hit rate (a third-party listing cites 95 %)\[58\]\[63\] |
| Architrave | Architrave (DE) | "Architrave Standard": its homepage states "468 document classes. 1,361 data fields. 7 country versions.", while its AV Standard page states "450+ document classes, 2,000+ data fields, 7 languages" – the vendor's own figures are inconsistent | Proprietary standard | SaaS | Commercial real estate | Vendor claim: "98% accuracy: verified by Human QA" (architrave.de) |
| Findable | Findable AS (Oslo) | Classifies building/FDV documents by NS 3451; chat search over documents\[22\]\[64\] | National Norwegian standard (proof that national taxonomies work) | SaaS | Statsbygg (per vendor and trade press) | Vendor/trade press |
| TwinEstate | sd-solution (CH) | Structured filing following KBOB processes and document type catalog; M365 integration | KBOB-native | M365-based | Public owners (claims a BBL-recommended filing structure)\[65\] | Verified as KBOB-aligned; no AI classification found |
| Planon, Spacewell, MRI | various | CAFM/IWMS with document modules | varies | SaaS / on-prem varies | many | Not verified in this research |

### 4.3 Knowledge graph and semantic platforms

| Product | Vendor | Model | GraphRAG / LLM | Deployment | Status |
|---|---|---|---|---|---|
| GraphDB + PoolParty (Graphwise platform) | Graphwise (merger of Ontotext and Semantic Web Company, 2024)\[66\]\[67\] | RDF, SPARQL, OWL 2 RL/QL reasoning, SHACL; SKOS taxonomy management\[68\] | GraphRAG (hybrid graph + vector + full-text), MCP support, "Talk to Your Graph"\[69\]\[70\] | GraphDB Free; Enterprise on-prem, AWS, Azure\[70\]\[71\] | Verified; Graphwise's press release of 16 February 2026 claims its semantic layer "moves AI accuracy from 60% to 90%+" and that adding an ontology-based KG to HippoRAG more than halves inaccurate answers on MuSiQue – vendor claims |
| Neo4j | Neo4j | Property graph, Cypher | Largest GraphRAG ecosystem, MCP server | Aura cloud, self-managed\[66\] | Secondary sources |
| Palantir Foundry | Palantir | Ontology over data | Ontology exposed to agents via MCP\[66\] | SaaS / dedicated | Secondary sources; cost and sovereignty to assess |
| Timbr | Timbr | SQL-native ontology over warehouses | GraphRAG, MCP\[66\] | varies | Secondary sources |
| Stardog, metaphactory, Microsoft Fabric / Azure AI Search, Databricks, Snowflake, AWS Neptune, Google | various | varies | varies | Mostly hyperscaler cloud | Not verified in this research |

### 4.4 Open-source building blocks

| Component | Purpose | Notes |
|---|---|---|
| Docling | PDF/Office/image parsing, layout, tables, OCR; Granite-Docling VLM (258M parameters)\[72\]\[73\] | MIT licence; started by IBM Research Zurich; hosted in LF AI & Data\[27\] |
| IfcOpenShell | IFC parsing; built-in bSDD client to search dictionaries and apply classification properties\[74\] | Mature, widely used |
| Microsoft GraphRAG, LightRAG, LlamaIndex property graph, LangChain, Haystack | Retrieval orchestration | Rapidly evolving; pin versions |
| Apache Jena / Fuseki | RDF store and SPARQL | Stable, no GraphRAG features built in |
| pgvector, Qdrant, Weaviate, OpenSearch | Vector / hybrid search | All self-hostable |
| OpenMetadata, DataHub, CKAN | Data catalog | CKAN closest to DCAT publishing |
| xeokit, That Open Company | Web IFC viewers | Licence terms differ (xeokit AGPL / commercial) |
| Apertus 8B / 70B | Open LLM (Swiss AI Initiative) | Open weights, data and recipes\[20\]\[75\] |

## 5. Reference projects and examples

| Organisation | What was built | Standards | Technology | Outcomes / lessons |
|---|---|---|---|---|
| ASTRA, BBL, armasuisse – CDE-Bund | Joint federal CDE for construction projects, separate environments per owner | BIM/IFC, 2D plans | Vrame CDE, Zühlke | In operation since go-live on 15 July; BBL manages around 2,700 objects; positioned as the basis for lifecycle BIM\[17\]\[76\] |
| armasuisse Immobilien | BIM as standard for large projects from 2025; information requirements for construction and FM; prototype and requirements for a "CDE AIM"\[77\]\[78\] | open BIM | digitalbau.ch support | Harmonisation study of data catalogs with SBB; portfolio of about 7,000 buildings and installations\[77\]\[79\] |
| SBB | Fachdatenkatalog (FDK) and SpecData-Tool for project data requirements; AIM-CDE under construction | IFC, FDK | in-house | SBB states the AIM-CDE "aktuell noch nicht zur Verfügung steht"\[23\]\[24\] |
| Kanton Basel-Stadt, Städtebau & Architektur | BWD checklists built on the KBOB Dokumenttypenkatalog\[80\] | KBOB BWD | – | Only verified public-sector reuse of the KBOB catalog found; manual, not AI |
| BImA / Bundeswehr (DE) | Objektkatalog Bundesbau V1.0 (Dec 2024) mapping object types to SAP operating systems and IFC\[25\]\[81\] | IFC | – | Shows the master-data-to-IFC mapping pattern BBL needs for SAP RE-FX |
| Statsbygg (NO) | AI classification of FDV documentation by NS 3451 (Findable); SIMBA BIM requirements as mvdXML for IFC4\[22\]\[82\] | NS 3451, IFC4 | Findable SaaS | Evidence that national element classification can drive document AI; customer-side metrics not published |
| Senaatti-kiinteistöt (FI) | Portfolio-wide lifecycle document management since 2004, about 1,800 active projects\[83\] | CAD/BIM/PDF | Buildercom BEM | No AI project found |
| Rijksvastgoedbedrijf (NL) | RVB BIM Specificatie; element information linked to external sources as linked data; data ecosystem combining sensor data with BIM database and ML\[84\]\[85\] | IFC, linked data | in-house | ML on sensor/energy data, not document LLM |
| Rijkswaterstaat (NL) | Object type library published as W3C linked data\[86\] | RDF/OWL | GitHub | Model for publishing a national vocabulary openly |
| US GSA PBS | Leasing Desk Guide RAG chatbot (deployed), Portfolio Analysis LLM (deployed), Maximo chatbot (pre-deployment)\[21\] | COBie in P100\[87\] | GenAI, RAG, IBM Maximo | Most mature public LLM deployment found; focus on policy documents, not drawings |
| Germany ITZBund – KIPITZ | Federal AI platform with on-prem LLM apps (chat, document Q&A, redaction)\[88\] | – | Sovereign data-centre operation | Analogue for running LLMs for a federal office in-house |

No reference was found from BIM Deutschland, Deutsche Bahn, Network Rail, Crown Estate, NHS, Singapore or Swiss airports in the time available; these remain open.

## 6. Prior work on KBOB document types and eBKP-H in AI or knowledge graphs

- No academic paper or product was found that uses the KBOB Dokumenttypenkatalog as a classification target for machine learning or LLMs, or as a vocabulary in a knowledge graph.
- Practical reuse exists in non-AI form: TwinEstate (sd-solution) and Kanton Basel-Stadt's BWD checklists.\[65\]\[80\]
- eBKP-H appears in the CH national glossary as an example of a national classification system and has an official eBKP-H–IFC4 rule set (Excel, first published 2018),\[13\]\[89\] but no bSDD, LINDAS or I14Y publication was found. This is a gap BBL could address together with KBOB and CRB, subject to licensing.

## 7. Swiss federal constraints and implications

| Constraint | Implication | Options |
|---|---|---|
| DSG and ISG | Documents may contain personal data (tenant correspondence, Personalakten-like content) and classified information (security plans, embassies); classification must also tag sensitivity | Sensitivity classifier as first pipeline step; exclude or isolate classified content; access control inherited from source systems |
| Cloud policy (Public Clouds Bund, Swiss Government Cloud) | SaaS document-AI hosted in Germany/EU may be acceptable only for non-sensitive data | Use vendor SaaS for low-sensitivity backlog only; run core graph and LLM on BIT or SGC |
| LLM choice | BIT piloted an on-prem open-source LLM assistant with RAG in its own data centres, planned as a service for 2026;\[19\] Apertus 8B/70B is fully open | Apertus or other open-weight models on BIT infrastructure; keep model-agnostic interfaces |
| Apertus limitations | Swiss German output was weak in independent tests: 20 Minuten found the dialect "oft zusammengewürfelt und gekünstelt", and watson.ch described the 70B model as "ein Plappermaul, das sich im Dialekt-Kauderwelsch äussert". Multimodality and agentic workflows were not the focus of the first generation | Use a separate VLM/OCR stack (Docling, Granite-Docling) for images and plans; benchmark DE/FR/IT before committing |
| Procurement (BöB/VöB, WTO) | Platform licences and integration services above thresholds require public tenders | Pilot with open source and existing frame contracts; write tender criteria around open standards (IFC, RDF, DCAT, SKOS) and exportability |
| Licensing of vocabularies | eBKP-H data use is licensed by CRB\[14\] | Clarify whether BBL's licence covers loading into a KG and LLM prompts |
| Federal AI governance | The Federal Council's press release of 18 September 2026 ("Bundesverwaltung priorisiert KI-Strategiemassnahmen") reports 116 AI projects across all departments and the Federal Chancellery; 6 of the 8 AI strategy measures continue under a "Roadmap 2026 bis 2028" funded with CHF 2 million per year | Register the pilot with the federal AI competence network; reuse federal guidance\[90\] |

## 8. Gaps, risks and open questions

- **Classification accuracy on legacy material.** Vendor claims of 95–98 % refer to their own taxonomies and mostly digital documents. Scanned, handwritten or multi-document PDFs, and 2016-era plan sets without title-block standards, are likely to perform worse; there is no published benchmark for KBOB classes.
- **Granularity mismatch.** Many KBOB types differ only by context (e.g. Gesuch vs. Bewilligung for the same utility, Vorabnahme vs. Abnahme). Expect confusion within groups; evaluate at group level (e.g. O14) and type level separately.
- **Plans and images.** Drawings need title-block extraction and drawing-type recognition (floor plan, section, schematic); photos need asset linkage via metadata or location, which is harder than classification.
- **Asset linking.** Linking a document to the right building or room depends on reliable identifiers in file names, CDE metadata or text; EGID and SAP IDs should be enforced at ingestion.
- **Ontology maintenance.** KBOB 2016 lacks BIM-era types; eBKP-H versions change; ownership of extensions (BBL vs. KBOB) must be decided and versioned.
- **Multilingual content.** DE/FR/IT documents require multilingual embeddings and label definitions; only DE and FR versions of the KBOB catalog were confirmed.
- **Hallucination and trust.** Answers must cite documents and graph facts; text-to-query should be validated against SHACL shapes or schema constraints.
- **GIS migration.** The planned move from ArcGIS Enterprise to open-source GIS around 2027 argues for keeping spatial joins on open identifiers (EGRID, EGID) rather than platform-specific IDs.

## 9. Suggested next steps

1. **Pilot scope (3–4 months):** 3–5 buildings with mixed document backlogs (one recent BIM project from CDE-Bund, one legacy building with scans), Phase 1 ontology, KBOB DTC classification, links to SAP RE-FX, GWR (EGID) and GIS (EGRID).
2. **Build a labelled test set:** 500–1,000 documents labelled by KBOB group and type by domain experts, stratified by format (scan, digital PDF, Office, plan, photo) and language.
3. **Compare three classification approaches:** zero-shot LLM using KBOB descriptions, few-shot with examples, and a vendor service (e.g. EVANA, Architrave or Findable mapped to KBOB) on non-sensitive data.
4. **Evaluation criteria:** macro-F1 per KBOB group and type, asset-link accuracy, retrieval precision@k, answer faithfulness and citation correctness, latency, cost per 1,000 pages, share of documents routed to human review.
5. **Standards work in parallel:** publish the KBOB catalog as SKOS (with KBOB) and seek clarity from CRB on eBKP-H machine-readable use; reuse KBOB data dictionary pipelines for LINDAS/I14Y.
6. **Governance:** register datasets and vocabularies in BBL's «Datenverzeichnis» (seeded from data-catalog-immo, DCAT-AP CH) and define sensitivity rules before ingesting real documents.
7. **Market dialogue:** an RFI to CDE, real estate document-AI and KG vendors asking explicitly for KBOB mapping, on-prem/Swiss hosting, export formats and accuracy evidence on customer data.

## Caveats

- Several market entries rely on secondary sources or vendor marketing; all accuracy figures are vendor claims.
- The year of CDE-Bund go-live was not stated explicitly in the sources reviewed; the 15 July date is from the ASTRA blog.\[76\]
- The eBKP-H non-publication finding is based on absence of evidence; the bSDD search index and I14Y were not queried directly.
- Several literature entries are preprints; author lists marked "multiple" were not fully verified.

## Quellen

1. [(PDF) LLM-assisted Graph-RAG Information Extraction from IFC Data](https://www.researchgate.net/publication/391057960_LLM-assisted_Graph-RAG_Information_Extraction_from_IFC_Data)
2. [The Swiss open source LLM is live](https://www.startupticker.ch/en/news/the-swiss-open-source-llm-is-live)
3. [RAG and Ontologies for Information Retrieval: A Literature Review](https://eil.mie.utoronto.ca/wp-content/uploads/2025/09/ONTOLLM_2025_Aug20v11.pdf)
4. [OntoLLM: Enhancing LLM grounding and digression prevention with ontologies and knowledge graphs - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417426004185)
5. [LLM-assisted Graph-RAG Information Extraction from IFC Data](https://www.alphaxiv.org/abs/2504.16813v1)
6. [Multi-Agent GraphRAG: A Text-to-Cypher Framework for Labeled Property Graphs](https://arxiv.org/html/2511.08274v1)
7. [Dokumenttypenkatalog](https://www.kbob.admin.ch/dam/de/sd-web/rVvtgYM1wFVT/20171024_KBOB-IPB_Anhang_C_-_Dokumenttypenkatalog_2016_DE.pdf)
8. [Bauwerksdokumentation im Hochbau - KBOB](https://www.kbob.admin.ch/de/bauwerksdokumentation-im-hochbau)
9. [Documents d’ouvrage du bâtiment](https://www.kbob.admin.ch/fr/documents-douvrage-du-batiment)
10. [bSDD/Documentation/bSDD-IFC documentation.md at master · buildingSMART/bSDD · GitHub](https://github.com/buildingSMART/bSDD/blob/master/Documentation/bSDD-IFC%20documentation.md)
11. [\[PDF\] BOT: The building topology ontology of the W3C linked building data group](https://www.semanticscholar.org/paper/BOT:-The-building-topology-ontology-of-the-W3C-data-Rasmussen-Lefran%C3%A7ois/789d0b45f15e364885043fab0a26eef726bd076e)
12. [Referencing bSDD in IDS and IFC - buildingSMART Technical](https://technical.buildingsmart.org/services/bsdd/referencing-bsdd-in-ids-and-ifc/)
13. [Regelsatz eBKP.](https://www.crb.ch/de/aktuelles/regelsatz-ebkp)
14. [Baukostenplan eBKP-Gate](https://www.crb.ch/de/normen-standards/baukostenplane/baukostenplan-ebkp-gate)
15. [GitHub - KBOB-admin/KBOB-data-dictionary-schemaforge · GitHub](https://github.com/KBOB-admin/KBOB-data-dictionary-schemaforge)
16. [GitHub - KBOB-admin/KBOB-data-dictionary · GitHub](https://github.com/KBOB-admin/KBOB-data-dictionary)
17. [Frank Müller - Zühlke Group](https://www.linkedin.com/in/frank-mueller-zuehlke/)
18. [CDE-Bund](https://www.bbl.admin.ch/de/cde-bund)
19. [KI als Schlüsseltechnologie für die öffentliche Verwaltung](https://www.bit.admin.ch/de/aus-der-gl-83)
20. [swiss-ai/Apertus-70B-2509 · Hugging Face](https://huggingface.co/swiss-ai/Apertus-70B-2509)
21. <https://www.gsa.gov/system/files/GSA-AI-use-case-inventory-2025.csv>
22. [\- Vi ser bare starten på potensialet innen kunstig intelligens - FDVhuset AS](https://www.fdvhuset.no/en/blogg/vi-ser-bare-starten-pa-potensialet-innen-kunstig-intelligens/)
23. [BIM Common Data Environment](https://company.sbb.ch/de/bahnentwicklung/zukunft-bahn/bim/planen/common-data-environment.html)
24. [Wegleitung BIM-Leistungen SBB](https://company.sbb.ch/content/dam/internet/corporate/downloads/de/sbb-als-geschaeftspartner/einkauf/bim/wegleitung-bim-leistungen-sbb.pdf.sbbdownload.pdf)
25. [Neues aus der Geschäftsstelle BIM Bundesbau](https://www.bimdeutschland.de/neues-aus-der-geschaeftsstelle-bim-bundesbau)
26. [Knowledge graph-based data integration system for digital twins of built assets - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0926580523003692)
27. [github.com](https://github.com/ceberam/docling)
28. [Automated Drawing Extraction](https://help.autodesk.com/cloudhelp/ENU/Docs-Files/files/Automated_Drawing_Extraction.html)
29. [ACC Docs Settings - Allow “Automated drawing extraction” to extract pages and attributes from AutoCA... - Autodesk Community](https://forums.autodesk.com/t5/acc-ideas/acc-docs-settings-allow-automated-drawing-extraction-to-extract/idi-p/13773526)
30. [davras5 (David Rasner) · GitHub](https://github.com/davras5)
31. [What is the Asset Information Model (AIM)?](https://www.thenbs.com/knowledge/what-is-the-asset-information-model-aim)
32. [Asset information model AIM - Designing Buildings](https://www.designingbuildings.co.uk/wiki/Asset_information_model_AIM)
33. [Asset Information Model (AIM) Grundlagen](https://bauen-digital.ch/wp/wp-content/uploads/dlm_uploads/2023-12-Asset-Information-Model-Grundlagen-DE.pdf)
34. [A Survey on Semantic Modeling for Building Energy Management](https://arxiv.org/pdf/2404.11716)
35. [What is the BuildingSMART data dictionary? - NBS](https://www.thenbs.com/knowledge/what-is-the-buildingsmart-data-dictionary)
36. [buildingSMART Data Dictionary - buildingSMART International](https://www.buildingsmart.org/users/services/buildingsmart-data-dictionary-old/)
37. [Anwenderhandbuch eBKP-H](https://www.crb.ch/de/normen-standards/baukostenplane/anwenderhandbuch-ebkp-h)
38. [SIGMUS: Semantic Integration for Knowledge Graphs in Multimodal Urban Spaces](https://arxiv.org/pdf/2509.00287)
39. [Vienna’s mandatory electronic Bauwerksbuch: lessons for Europe’s Digital Building Logbooks](https://build-up.ec.europa.eu/en/resources-and-tools/articles/viennas-mandatory-electronic-bauwerksbuch-lessons-europes-digital)
40. [Bauwerksdokumentation](https://fachglossar.platinus.at/docs/Glossar/B-Glossar/Bauwerksdokumentation/)
41. [BOT: The Building Topology Ontology of the W3C Linked Building Data Group](https://publica.fraunhofer.de/handle/publica/268735)
42. [BOT: The building topology ontology of the W3C linked building data group - Research portal Eindhoven University of Technology](https://research.tue.nl/en/publications/bot-the-building-topology-ontology-of-the-w3c-linked-building-dat/)
43. [Knowledge Graphs and Linked Data for the Built Environment](https://www.researchgate.net/publication/356758057_Knowledge_Graphs_and_Linked_Data_for_the_Built_Environment)
44. [(PDF) Docling Technical Report](https://www.researchgate.net/publication/383236441_Docling_Technical_Report)
45. [(PDF) Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion](https://www.researchgate.net/publication/388529387_Docling_An_Efficient_Open-Source_Toolkit_for_AI-driven_Document_Conversion)
46. [Automation of text document classification in the budgeting phase of the Construction process: a Systematic Literature Review](https://www.emerald.com/ci/article/24/7/292/1230787/Automation-of-text-document-classification-in-the)
47. [LLM-assisted Graph-RAG Information Extraction from IFC Data](https://arxiv.org/pdf/2504.16813)
48. [Automating Geometry-Intensive Compliance Checking in BIM: Graph-Based Semantic Reasoning Framework](https://arxiv.org/pdf/2606.12065)
49. [Enhancing IFC Model Interpretability Using Knowledge ...](https://mediatum.ub.tum.de/doc/1782062/ls0kfav1uhl700783e2ykjkt6.redacted_m_thesis_Ata_onlyNames.pdf)
50. [RAG and Ontologies for Information Retrieval: A Literature Review](https://ceur-ws.org/Vol-4176/ontollm-2.pdf)
51. [Next-generation language-based data mining techniques for smart construction documentation: challenges and opportunities](https://cdnsciencepub.com/doi/10.1139/cjce-2025-0329)
52. [(PDF) Envisaging a European Digital Building Renovation Logbook: Proposal of a Data Model](https://www.researchgate.net/publication/384583096_Envisaging_a_European_Digital_Building_Renovation_Logbook_Proposal_of_a_Data_Model)
53. [(PDF) Towards the definition of a European Digital Building Logbook: A survey](https://www.researchgate.net/publication/373355160_Towards_the_definition_of_a_European_Digital_Building_Logbook_A_survey)
54. [Leveraging large language models for document classification in the banking sector](https://link.springer.com/article/10.1007/s41060-026-01077-x)
55. [Knowledge Graphs as the Missing Data Layer for LLM-Based Industrial Asset Operations](https://arxiv.org/pdf/2605.26874)
56. [Itcon](https://www.itcon.org/papers/2026_38-ITcon-Alnuzha.pdf)
57. [Data Management Help](https://help.autodesk.com/view/DOCS/ENU/?guid=Automated_Drawing_Extraction_Authoring_Guide)
58. [Automatische Dokumentenklassifizierung mit KI](https://evana.ai/eng/produkte/evana-ai/)
59. [KI-Dokumentenmanagement für Immobilien](https://evana.ai/eng/produkte/?lang=en)
60. [KI Dokumentenmanagement für Immobilien](https://evana.ai/eng/produkte/evana-360/)
61. [EVANA](https://www.airframe.ai/product/evana-ai/analysis)
62. [Mann Immobilien: Next-Level DMS mit EVANA KI](https://evana.ai/eng/mann-immobilien/)
63. [Evana.ai - IDP Software Vendor](https://idp-software.com/vendors/evana/)
64. [Suksess med bruk av kunstig intelligens for håndtering av FDV-dokumentasjon - Elektro24-7](https://www.elektro247.no/suksess-med-bruk-av-kunstig-intelligens-for-haandtering-av-fdv-dokumentasjon.6621983-567787.html)
65. [Bauherren](https://sd-solution.ch/Bauherren/)
66. [Top Knowledge Graph Platforms for Enterprise Data (2026)](https://www.getgalaxy.io/articles/top-knowledge-graph-platforms-enterprise-data-intelligence-2026)
67. [Graphwise: Transforming Enterprise AI with Knowledge Graphs](https://www.rws.com/content-management/blog/how-graphwise-is-transforming-the-graph-ai-landscape/)
68. [Ontotext GraphDB vs a Context Layer: Where Each Fits \[2026\]](https://atlan.com/know/ai-agent/knowledge-graph/ontotext-graphdb-vs-atlan/)
69. [Introducing GraphRAG: The Trust Layer of the Graphwise Platform](https://graphwise.ai/blog/introducing-graphrag-the-trust-layer-of-the-graphwise-platform/)
70. [Graphwise GraphDB](https://graphwise.ai/components/graphdb/)
71. [\[Galaxy\] 7 Best Graph Databases for 2026: Founder's Guide to ...](https://www.getgalaxy.io/articles/best-graph-databases-2026)
72. [ibm docling](https://github.com/fkatada/ibm-docling)
73. [Docling Documentation - IBM Docling Technical Manual ...](https://docling.org/doc/)
74. [bSDD - IfcOpenShell 0.9.0post1 documentation](https://docs.ifcopenshell.org/bsdd.html)
75. [Apertus: a fully open, transparent, multilingual language model](https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html)
76. [CDE-Bund: Gemeinsame Plattform, gemeinsam bauen](https://blog.astra.admin.ch/cde-bund-gemeinsame-plattform-gemeinsam-bauen/)
77. [BIM: Digitale Bauwerksinformationen](https://www.ar.admin.ch/de/bim-de)
78. [armasuisse Immobilien](https://digitalbau.ch/referenz/armasuisse-immobilien/)
79. [Geodaten untermauern das digitale Bauen](https://www.swisstopo.admin.ch/de/geodaten-untermauern-digitales-bauen)
80. [Bau- und Verkehrsdepartement des Kantons Basel-Stadt Städtebau & Architektur](https://media.bs.ch/original_file/b825dc9e0373003ab210cb2bfed8679ff2c0fc53/2-3412-richtlinie-bauwerksdokumentation.pdf)
81. [Bundesministerium der Verteidigung, Postfach 13 28, 53003 Bonn](https://bundesbau.de/fileadmin/user_upload/241212_BIM_Lenkungsgruppe_Ver%C3%B6ffentlichung_Objektkatalog_V1.0.pdf)
82. [SIMBA - Statsbygg's BIM requirements - Use Case Management](https://ucm.buildingsmart.org/en/use-cases/2565/en)
83. [Case Senaatti: keskitetty rakentamisen tiedonhallinta - Buildercom](https://buildercom.fi/referenssi/rakennuttaminen/case-senaatti-keskitetty-rakentamisen-tiedonhallinta/)
84. [‘Als je vastgoeddata combineert, kom je tot inzichten’](https://www.rijksvastgoedbedrijf.nl/actueel/nieuws/2023/12/28/als-je-vastgoeddata-combineert-kom-je-tot-inzichten)
85. [RVB BIM Specificatie v1.1-c](https://www.rijksvastgoedbedrijf.nl/documenten/2019/04/01/rvb-bim-specificatie-v1.1-c)
86. [GitHub - RWS-NL/rws-otl: Repository for the Rijkswaterstaat OTL modelled in Linked Data · GitHub](https://github.com/RWS-NL/rws-otl)
87. [COBie Data Handoff from the Construction Record](https://www.specset.com/use-cases/cobie-handoff)
88. [. - Die KI-Plattform der Bundesverwaltung: KIPITZ - ITZBund](https://www.itzbund.de/DE/itloesungen/egovernment/kipitz-ki-plattform/kipitz-ki-plattform.html)
89. [Glossar - Bauen digital Schweiz / buildingSMART Switzerland BIM Glossar](https://bauen-digital.ch/publikationen/glossar/)
90. [Künstliche Intelligenz](https://www.bk.admin.ch/de/ki)
