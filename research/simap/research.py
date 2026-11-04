#!/usr/bin/env python3
"""
research.py — Recherche abgeschlossener Vergaben auf simap.ch (Public API, keine Auth).

Sucht Zuschlaege (award/direct_award) per CPV-Code-Sweep und Stichwortsuche,
reichert jede Vergabe mit Zuschlagsempfaenger, Preis und Beschreibung an und
bewertet die Relevanz fuer das Profil "KI-Suche + Wissensgraph + Bauwerks-
dokumentation" (Asset Information Model BBL).

Verwendung:
  python research.py                          # Voll-Sweep seit Plattformstart
  python research.py --from 2026-01-01        # nur neuere Publikationen
  python research.py -k Neo4j -k EVANA        # zusaetzliche Stichworte
  python research.py --no-details             # ohne Detail-Anreicherung (schnell)

Ausgabe: simap_awards_all.csv (alle Zuschlaege, nach Score sortiert)
"""

import argparse
import csv
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://www.simap.ch/api"
UA = {"User-Agent": "simap-research-script/3.0 (BBL research)"}
LANG_PRIO = ("de", "fr", "it", "en")

# CPV 72 = IT-Dienste, 48 = Software. Die API matcht hierarchisch:
# 72000000 deckt alle 72er-Untercodes ab.
CPV_CODES = ["72000000", "48000000"]

# Stichworte fangen Vergaben ausserhalb der CPV-Aeste 72/48 ein.
# Die API verlangt mind. 3 Zeichen ("KI" -> HTTP 400) und sucht unscharf im
# Volltext; "BIM" allein liefert fast nur Bauauftraege und fehlt deshalb.
KEYWORDS = [
    # KI / Suche
    "künstliche Intelligenz", "intelligence artificielle", "Chatbot", "Sprachmodell",
    "Large Language Model", "generative", "Dokumentenklassifikation", "Texterkennung",
    "Machine Learning", "Wissensmanagement", "Enterprise Search",
    # Graph / Daten
    "Wissensgraph", "Knowledge Graph", "Ontologie", "Linked Data", "Datenplattform",
    "Data Lake", "Datenkatalog",
    # Immobilien-Domaene
    "CAFM", "Bauwerksdokumentation", "Objektdokumentation", "Asset Information",
    "Planarchiv", "Planverwaltung", "Immobilienportfolio", "Immobilienmanagement",
    "Digital Twin", "digitaler Zwilling", "jumeau numérique", "Lebenszykluskosten",
    "Kostenkennwerte", "Dokumentenmanagement", "gestion documentaire",
]

# Zuschlaege, wie sie im Suchresultat-Feld pubType erscheinen.
# WICHTIG: NICHT serverseitig per newestPubTypes filtern — dieser Filter
# verschluckt Los-Projekte (z.B. SPRINT 24194), deren neueste Publikation
# nachweislich ein Zuschlag ist. Stattdessen clientseitig filtern.
AWARD_PUB_TYPES = ("award", "direct_award")

# Relevanz-Muster (regex, gewicht, gruppe) — angewandt auf Titel + Beschreibung.
# Gruppen: "tech" = KI/Suche/Graph, "domain" = Immobilien/Bau-Daten.
POSITIVE = [
    (r"\brag\b|retrieval[- ]augmented|\bllm|large language|sprachmodell|generative (ki|ai|ia)|genai|\bgpt|chatbot|ki[- ]assistent|assistant (ia|virtuel)", 5, "tech"),
    (r"wissensgraph|knowledge[- ]graph|\bontolog|linked data|semanti|\brdf\b|sparql|graphdb|neo4j", 5, "tech"),
    # Kein \bai\b: trifft die italienische Praeposition "ai" (Tessiner Bauauftraege).
    (r"k[üu]nstliche intelligenz|\bki\b|intelligence artificielle|artificial intelligence|\bia\b|machine learning|maschinelles lernen", 3, "tech"),
    (r"klassifikation|klassifizierung von dokumenten|texterkennung|\bocr\b|intelligent document|extraktion|extraction", 3, "tech"),
    (r"enterprise search|suchmaschine|volltextsuche|moteur de recherche", 3, "tech"),
    (r"wissensmanagement|knowledge management|gestion des connaissances", 2, "tech"),
    (r"datenplattform|data lake|lakehouse|data platform|datenkatalog|data catalog|stammdaten", 2, "tech"),
    (r"\bcafm\b|\biwms\b|facility[- ]management[- ]?(software|system|l[öo]sung)", 5, "domain"),
    (r"asset information|bauwerksdokumentation|objektdokumentation|documentation d.ouvrage", 5, "domain"),
    (r"common data environment|\bcde\b", 4, "domain"),
    (r"digital(er)? (twin|zwilling)|jumeau num", 4, "domain"),
    (r"planarchiv|planverwaltung|archivdigitalisierung|digitalisierung (des|der) (archiv|pl[äa]ne)", 3, "domain"),
    (r"lebenszykluskosten|life[- ]?cycle cost|kostenkennwert|baukostendaten", 3, "domain"),
    (r"immobilien|liegenschaft|immobilier|geb[äa]udebestand|portfolio hochbau", 2, "domain"),
    (r"\bbim\b|\bifc\b|openbim", 2, "domain"),
    (r"dokumentenmanagement|document management|gestion documentaire|\bdms\b|\becm\b|gever\b", 2, "domain"),
    (r"open[- ]?source|souver[äa]n|on[- ]?prem", 1, "tech"),
]
NEGATIVE = [
    (r"\bbkp\b|baumeister|tiefbau|rohbau|fenster|elektroinstallation|sanit[äa]r|heizung|gesamtplaner|generalplaner|planerwahl|gesamtleistungswettbewerb|ingenieurleistungen|\bsia 14[234]", -6),
    # "Neubau" auch fuer Software ("Neubau der simap-Plattform") -> schwaecher
    (r"neubau|umbau|ersatzbau", -3),
    (r"hardware|notebook|drucker|imprimante|smartphone|tablet|fahrzeug|v[ée]hicule", -4),
    (r"netzwerk|\blan\b|wlan|firewall|telefonie|t[ée]l[ée]phonie|kabel|funksystem", -4),
    (r"rechenzentrum|datacenter|storage|backup|housing", -3),
    (r"lizenz|licence|m365|microsoft 365|office 365", -2),
]
# Bonus, wenn Technik und Immobilien-Domaene zusammenkommen (Kern des Profils).
COMBO_BONUS = 3

FRAMEWORK = re.compile(r"rahmenvertr|accord[s]?[- ]cadre|contrat[s]?[- ]cadre|r[ée]f[ée]rencement|abrufvertr", re.I)


def get_json(path, params=None, retries=3):
    url = f"{API}{path}"
    if params:
        pairs = []
        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, (list, tuple)):
                pairs += [(k, i) for i in v]
            else:
                pairs.append((k, v))
        url += "?" + urllib.parse.urlencode(pairs)
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            if attempt == retries - 1:
                print(f"WARN: {url} -> {e}", file=sys.stderr)
                return {}
            time.sleep(2 * (attempt + 1))
    return {}


def t(tr, fallback=""):
    """Translation-Objekt {de:..,fr:..} -> bester verfuegbarer String."""
    if tr is None:
        return fallback
    if isinstance(tr, str):
        return tr
    if isinstance(tr, dict):
        for lang in LANG_PRIO:
            if tr.get(lang):
                return tr[lang]
        for v in tr.values():
            if v:
                return v
    return fallback


def strip_html(s):
    return re.sub(r"<[^>]+>", " ", html.unescape(s or "")).strip()


def search(extra_params, tag, date_from, date_until=None, max_pages=400):
    """Paginierte Suche ueber /project-search (Rolling Cursor: lastItem)."""
    results, last_item = [], None
    for _ in range(max_pages):
        params = {"newestPublicationFrom": date_from, **extra_params}
        if date_until:
            params["newestPublicationUntil"] = date_until
        if last_item:
            params["lastItem"] = last_item
        data = get_json("/publications/v2/project/project-search", params)
        projects = data.get("projects") or []
        results += projects
        last_item = (data.get("pagination") or {}).get("lastItem")
        if not projects or not last_item:
            break
        time.sleep(0.2)
    print(f"  [{tag}] {len(results)} Treffer", file=sys.stderr)
    return results


def fetch_detail(project_id, publication_id):
    """Zuschlagsempfaenger, Preise, Beschreibung, CPV aus den Publikationsdetails."""
    d = get_json(f"/publications/v1/project/{project_id}/publication-details/{publication_id}")
    proc = d.get("procurement") or {}
    dec = d.get("decision") or (d.get("lot") or {}).get("decision") or {}
    vendors = []
    for v in dec.get("vendors") or []:
        name = v.get("vendorName") or ""
        city = (v.get("vendorAddress") or {}).get("city") or ""
        price = (v.get("price") or {}).get("price")
        cur = ((v.get("price") or {}).get("currency") or "CHF").upper()
        label = name + (f", {city}" if city else "")
        if price:
            label += f" ({cur} {price:,.0f})"
        vendors.append({"name": name, "city": city, "price": price, "label": label})
    return {
        "vendors": vendors,
        "decision_date": dec.get("awardDecisionDate") or "",
        "submissions": dec.get("numberOfSubmissions"),
        "cpv": (proc.get("cpvCode") or {}).get("code", ""),
        "description": strip_html(t(proc.get("orderDescription"))),
    }


def score(text):
    tl = text.lower()
    s, hits, groups = 0, [], set()
    for pattern, w, group in POSITIVE:
        m = re.search(pattern, tl)
        if m:
            s += w
            groups.add(group)
            hits.append(m.group(0).strip())
    for pattern, w in NEGATIVE:
        if re.search(pattern, tl):
            s += w
    if {"tech", "domain"} <= groups:
        s += COMBO_BONUS
    return s, hits


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("-k", "--keyword", action="append", dest="keywords", default=[],
                   help="zusaetzliches Stichwort (mehrfach moeglich, mind. 3 Zeichen)")
    p.add_argument("--from", dest="date_from", default="2024-07-01")
    p.add_argument("--until", dest="date_until", default=None)
    p.add_argument("--no-details", action="store_true")
    p.add_argument("--csv", default="simap_awards_all.csv")
    args = p.parse_args()

    print("1) Sammeln (ohne pubType-Filter, siehe Kommentar AWARD_PUB_TYPES) ...", file=sys.stderr)
    by_id = {}
    for pr in search({"cpvCodes": CPV_CODES}, "CPV 72/48",
                     args.date_from, args.date_until):
        by_id.setdefault(pr["id"], pr)
    for kw in KEYWORDS + args.keywords:
        for pr in search({"search": kw}, f"kw:{kw}",
                         args.date_from, args.date_until, max_pages=25):
            by_id.setdefault(pr["id"], pr)

    awarded = {i: pr for i, pr in by_id.items()
               if pr.get("pubType") in AWARD_PUB_TYPES}
    print(f"-> {len(by_id)} Projekte, davon {len(awarded)} Zuschlaege. "
          f"2) Details laden ...", file=sys.stderr)

    rows = []
    for n, (pid, pr) in enumerate(awarded.items(), 1):
        det = {"vendors": [], "decision_date": "", "submissions": None,
               "cpv": "", "description": ""}
        title = t(pr.get("title"))
        # Bauauftraege & Co. schon am Titel erkennbar: Detailabruf sparen.
        if not args.no_details and pr.get("publicationId") and score(title)[0] > -4:
            det = fetch_detail(pid, pr["publicationId"])
            time.sleep(0.15)
        sc, hits = score(title + " " + det["description"])
        rows.append({
            "Score": sc,
            "Datum": pr.get("publicationDate", ""),
            "Typ": pr.get("pubType", ""),
            "Verfahren": pr.get("processType", ""),
            "Auftraggeber": t(pr.get("procOfficeName")),
            "Titel": title,
            "Rahmenvertrag": "ja" if FRAMEWORK.search(title + " " + det["description"]) else "",
            "Zuschlagsempfaenger": "; ".join(v["label"] for v in det["vendors"]),
            "Preis_total": sum(v["price"] or 0 for v in det["vendors"]) or "",
            "Angebote": det["submissions"] if det["submissions"] is not None else "",
            "CPV": det["cpv"],
            "Treffer": ", ".join(sorted(set(hits))),
            "Beschreibung": det["description"][:600],
            "Link": f"https://www.simap.ch/de/project-detail/{pid}",
        })
        if n % 50 == 0:
            print(f"  ... {n}/{len(awarded)}", file=sys.stderr)

    rows.sort(key=lambda r: (r["Score"], r["Datum"]), reverse=True)
    with open(args.csv, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"FERTIG: {len(rows)} Zuschlaege -> {args.csv}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
