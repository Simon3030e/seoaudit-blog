# -*- coding: utf-8 -*-
"""
Audit niche configuration for seoaudit.blog, then run
`python3 build_site.py` from the repo root.

Keywords grounded in Marketing Miner data (2026-09):
SK: seo audit 440, audit seo 530 (diff 97!), seo online audit 220, seo audits 260.
CZ: seo audit 640, seo audity 220, seo audit online 140, seo audit webu 50.
Note: head terms are tool-dominated (diff 92+). Win via guides + free audit offer.
"""
import engine

BASE = "https://seoaudit.blog"
BRAND = "SEO audit"
BRAND_TAGLINE = "SEO audit webu. Nokto Studio."

NICHE_KEY = "audit"
MAIN_DOMAIN = "seoaudit.blog"

KW_PROOF_SK = [
    ("seo audit", 440),
    ("audit seo", 530),
    ("seo online audit", 220),
    ("seo audits", 260),
    ("seo audit webu", 50),
]
KW_PROOF_CZ = [
    ("seo audit", 640),
    ("seo audity", 220),
    ("seo audit online", 140),
    ("seo audit webu", 50),
]

SERVICES = [
    ("sluzby/seo-audit/", "sluzby/seo-audit/",
     "SEO audit webu", "SEO audit webu"),
    ("sluzby/technicky-audit/", "sluzby/technicky-audit/",
     "Technický SEO audit", "Technický SEO audit"),
    ("sluzby/obsahovy-audit/", "sluzby/obsahovy-audit/",
     "Obsahový audit", "Obsahový audit"),
    ("sluzby/eshop-audit/", "sluzby/eshop-audit/",
     "SEO audit e-shopu", "SEO audit e-shopu"),
]

NICHE_NAV_SVC = {
    "sk": [(p_sk, lbl_sk) for (p_sk, _p_cz, lbl_sk, _lbl_cz) in SERVICES],
    "cz": [(p_cz, lbl_cz) for (_p_sk, p_cz, _lbl_sk, lbl_cz) in SERVICES],
}
engine.NICHE_NAV_SVC = NICHE_NAV_SVC

SK_PATHS = {
    "", "sluzby/", "cennik/", "jak-pracujeme/", "blog/", "kontakt/",
    "privacy/", "terms/",
} | {s[0] for s in SERVICES}
CZ_PATHS = {
    "", "sluzby/", "cenik/", "jak-pracujeme/", "blog/", "kontakt/",
    "privacy/", "terms/",
} | {s[1] for s in SERVICES}
engine.LANG_PATHS = {"sk": SK_PATHS, "cz": CZ_PATHS}

HREFLANG_PAIR = {
    "": "",
    "sluzby/": "sluzby/",
    "cennik/": "cenik/",
    "jak-pracujeme/": "jak-pracujeme/",
    "blog/": "blog/",
    "kontakt/": "kontakt/",
    "privacy/": "privacy/",
    "terms/": "terms/",
}
for s in SERVICES:
    HREFLANG_PAIR[s[0]] = s[1]
    HREFLANG_PAIR[s[1]] = s[0]
engine.HREFLANG_PAIR = HREFLANG_PAIR

engine.BASE = BASE
engine.BRAND = BRAND
engine.LOGO = ('<span class="logo-n">S</span><span class="logo-o">E</span>'
               '<span class="logo-k">O</span> <span class="logo-t">audit</span>')

engine.GSC_TOKEN = ""
engine.BING_TOKEN = "3b43ea1af0ee49f082ab3c4e94ed5f4f"
