#!/usr/bin/env python3
"""
research.py — Recherche abgeschlossener IT-Vergaben auf simap.ch (Public API, keine Auth).

Sucht Zuschlaege (award/direct_award) per CPV-Code-Sweep und Stichwortsuche,
reichert jede Vergabe mit Zuschlagsempfaenger, Preis und Beschreibung an und
bewertet die Relevanz fuer das Profil "Prozess-Engine + Formulare + Portal"
(Mieterportal BBL). Details: README.md.

Verwendung:
  python research.py                          # Voll-Sweep seit Plattformstart
  python research.py --from 2026-01-01        # nur neuere Publikationen
  python research.py -k Camunda -k Formular   # zusaetzliche Stichworte
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
KEYWORDS = [
    "Camunda", "Flowable", "Workflow", "Formularservice", "Fachanwendung",
    "Individualentwicklung", "Webapplikation", "Onlineschalter",
    "Geschäftsverwaltung", "guichet virtuel",
]

# Zuschlaege, wie sie im Suchresultat-Feld pubType erscheinen.
# WICHTIG: NICHT serverseitig per newestPubTypes filtern — dieser Filter
# verschluckt Los-Projekte (z.B. SPRINT 24194), deren neueste Publikation
# nachweislich ein Zuschlag ist. Stattdessen clientseitig filtern.
AWARD_PUB_TYPES = ("award", "direct_award")

# Relevanz-Muster (regex, gewicht) — angewandt auf Titel + Beschreibung.
POSITIVE = [
    (r"camunda|flowable|operaton|activiti|jbpm|bpmn", 5),
    (r"prozess[- ]?engine|process[- ]?engine|workflow[- ]?engine|moteur de processus", 5),
    (r"workflow|prozessautomatis|automatisation des processus", 3),
    (r"formular|formulaire|\bforms?\b", 3),
    (r"antrags|gesuchs|self[- ]?service|onlineschalter|guichet", 3),
    (r"portal|portail", 2),
    (r"individualentwicklung|individual[- ]?software|d[ée]veloppement sp[ée]cifique", 3),
    (r"fachanwendung|fachapplikation|application m[ée]tier", 2),
    (r"gesch[äa]ftsverwaltung|gever\b", 2),
    (r"e[- ]?government|egov|digitale verwaltung|cyberadministration", 2),
    (r"webapplikation|webanwendung|web[- ]?app|application web", 2),
    (r"neuentwicklung|weiterentwicklung|agile|scrum|devops", 1),
    (r"\bjava\b|angular|react|vue|spring|\.net|typescript|open[- ]?source", 1),
]
NEGATIVE = [
    (r"lizenz|licence[s]? (microsoft|sap|oracle)|m365|microsoft 365|office 365", -4),
    (r"hardware|notebook|drucker|imprimante|smartphone|tablet", -4),
    (r"netzwerk|lan\b|wlan|firewall|telefonie|t[ée]l[ée]phonie|kabel", -4),
    (r"rechenzentrum|datacenter|storage|backup|housing", -3),
    (r"\bsap\b|abacus|navision|dynamics 365|erp[- ]einf", -2),
    (r"scanning|digitalisierung von akten|num[ée]risation", -2),
]


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
    s, hits = 0, []
    for pattern, w in POSITIVE + NEGATIVE:
        if re.search(pattern, tl):
            s += w
            if w > 0:
                hits.append(pattern.split("|")[0].replace("\\b", ""))
    return s, hits


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("-k", "--keyword", action="append", dest="keywords", default=[],
                   help="zusaetzliches Stichwort (mehrfach moeglich)")
    p.add_argument("--from", dest="date_from", default="2024-07-01")
    p.add_argument("--until", dest="date_until", default=None)
    p.add_argument("--no-details", action="store_true")
    p.add_argument("--csv", default="simap_awards_all.csv")
    args = p.parse_args()

    print("1) Sammeln (ohne pubType-Filter, siehe README) ...", file=sys.stderr)
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
        if not args.no_details and pr.get("publicationId"):
            det = fetch_detail(pid, pr["publicationId"])
            time.sleep(0.15)
        title = t(pr.get("title"))
        sc, hits = score(title + " " + det["description"])
        rows.append({
            "Score": sc,
            "Datum": pr.get("publicationDate", ""),
            "Typ": pr.get("pubType", ""),
            "Verfahren": pr.get("processType", ""),
            "Auftraggeber": t(pr.get("procOfficeName")),
            "Titel": title,
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
