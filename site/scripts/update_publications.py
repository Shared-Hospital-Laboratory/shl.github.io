#!/usr/bin/env python3
"""Refresh _data/publications_all.json from Europe PMC.

Reads the search for each team member from _data/publication_authors.yml, keeps only
papers with "Shared Hospital Laboratory" in an author affiliation, merges the results, and records which SHL team members are on each paper and whether they are
first or last (senior) author.

Usage (from the site/ folder):  python3 scripts/update_publications.py
Needs only the Python standard library and an internet connection.
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.error
import urllib.request
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
CONFIG = SITE / "_data" / "publication_authors.yml"
TEAM_DIR = SITE / "_team"
OUT = SITE / "_data" / "publications_all.json"
API = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
SHL_AFFILIATION = "Shared Hospital Laboratory"

# Skip things that are not papers in their own right.
SKIP_TITLE = re.compile(
    r"^(correction|erratum|publisher correction|author correction|retraction|oral presentations?|poster)"
    r"|annual conference|conférence annuelle|abstracts?$",
    re.I,
)


def read_config():
    """Tiny parser for the simple YAML list in publication_authors.yml (no PyYAML needed)."""
    people, cur = [], None
    for line in CONFIG.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^(-\s+|\s+)(\w+):\s*(.*)$", line)
        if not m:
            continue
        if m.group(1).startswith("-"):
            cur = {}
            people.append(cur)
        key, val = m.group(2), m.group(3).strip()
        if val.startswith("["):
            cur[key] = [v.strip().strip("\"'") for v in val.strip("[]").split(",") if v.strip()]
        else:
            cur[key] = val[1:-1] if val[:1] in "'\"" else val
    return people


def team_title(slug):
    text = (TEAM_DIR / f"{slug}.md").read_text()
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', text, re.M)
    return m.group(1) if m else slug


def get_json(url, tries=6):
    """GET with retries: Europe PMC sometimes answers 503 when busy."""
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0", "Accept": "*/*"})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            if attempt == tries - 1:
                raise
            wait = 2 ** attempt * 3
            print(f"  {e} for {url[:160]}; retrying in {wait}s", file=sys.stderr)
            time.sleep(wait)


def fetch(query):
    results, cursor = [], "*"
    while True:
        params = urllib.parse.urlencode({
            # SHL-affiliated, peer-reviewed records only (SRC filter also drops preprint duplicates)
            "query": f'({query}) AND AFF:"{SHL_AFFILIATION}" AND (SRC:MED OR SRC:PMC)',
            "format": "json", "resultType": "lite", "pageSize": 100, "cursorMark": cursor,
        }, quote_via=urllib.parse.quote)  # %20 for spaces: Europe PMC rejects "+"
        data = get_json(f"{API}?{params}")
        batch = data["resultList"]["result"]
        results += batch
        nxt = data.get("nextCursorMark")
        # Stop once everything is fetched: asking Europe PMC for a page past the end returns 503.
        if not batch or nxt == cursor or len(results) >= int(data.get("hitCount", 0)):
            return results
        cursor = nxt
        time.sleep(0.3)


def clean(s):
    s = html.unescape(s or "")
    s = re.sub(r"<[^>]+>", "", s)
    return s.strip().rstrip(".")


def main():
    people = read_config()
    papers, found_by = {}, {}
    for p in people:
        print(f"Searching for {p['team']}…", file=sys.stderr)
        for r in fetch(p["query"]):
            title = clean(r.get("title"))
            if not title or SKIP_TITLE.search(title):
                continue
            key = (r.get("doi") or "").lower() or re.sub(r"\W+", "", title.lower())
            papers.setdefault(key, r)
            found_by.setdefault(key, set()).add(p["team"])

    out = []
    for key, r in papers.items():
        authors = [a.strip() for a in clean(r.get("authorString")).split(",") if a.strip()]
        if not authors:
            continue
        members = []
        for p in people:
            # Only credit people whose own (affiliation-restricted) search returned this paper,
            # so a namesake on someone else's paper is not highlighted.
            if p["team"] not in found_by[key]:
                continue
            names = set(p["names"])
            idx = [i for i, a in enumerate(authors) if a in names]
            if not idx:
                continue  # search hit on someone else (e.g. a namesake in another author slot)
            i = idx[0]
            role = "first" if i == 0 else ("last" if i == len(authors) - 1 and len(authors) > 1 else "")
            members.append({"team": p["team"], "name": team_title(p["team"]), "author": authors[i], "role": role})
        if not members:
            continue
        out.append({
            "title": clean(r.get("title")),
            "authors": authors,
            "journal": clean(r.get("journalTitle")) or clean(r.get("bookOrReportDetails", {}).get("publisher")),
            "year": int(r.get("pubYear") or (r.get("firstPublicationDate") or "0")[:4] or 0),
            "date": r.get("firstPublicationDate") or "",
            "doi": r.get("doi") or "",
            "pmid": r.get("pmid") or "",
            "members": members,
        })

    out.sort(key=lambda x: (x["date"], x["title"]), reverse=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(f"Wrote {len(out)} publications to {OUT.relative_to(SITE)}", file=sys.stderr)


if __name__ == "__main__":
    main()
