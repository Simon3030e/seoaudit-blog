# -*- coding: utf-8 -*-
"""
Audit niche content for seoaudit.blog (SK + CZ).

Keywords grounded in Marketing Miner (2026-09):
SK seo audit 440, audit seo 530 (diff 97), seo online audit 220, seo audits 260.
CZ seo audit 640, seo audity 220, seo audit online 140, seo audit webu 50.
Head terms are tool-dominated: the play is guides + real human audit offer.
"""

from engine import _VIOLET, _ORANGE, _CERULEAN, _VIOLET_L, _sparkline, _bars

SERVICE_DEFS = [
    ("sluzby/seo-audit/", "sluzby/seo-audit/",
     "SEO audit webu", "SEO audit webu"),
    ("sluzby/technicky-audit/", "sluzby/technicky-audit/",
     "Technický SEO audit", "Technický SEO audit"),
    ("sluzby/obsahovy-audit/", "sluzby/obsahovy-audit/",
     "Obsahový audit", "Obsahový audit"),
    ("sluzby/eshop-audit/", "sluzby/eshop-audit/",
     "SEO audit e-shopu", "SEO audit e-shopu"),
]
SERVICE_DEFS_TEXT = [
    ("Kompletný audit: technika, obsah, pozície aj AI viditeľnosť. S plánom podľa priorít, ktorému rozumiete.",
     "Kompletní audit: technika, obsah, pozice i AI viditelnost. S plánem podle priorit, kterému rozumíte."),
    ("Indexácia, rýchlosť, Core Web Vitals, presmerovania a štruktúra. Čo brzdí web v Google na technickej úrovni.",
     "Indexace, rychlost, Core Web Vitals, přesměrování a struktura. Co brzdí web v Google na technické úrovni."),
    ("Ktoré stránky majú potenciál, ktoré chýbajú a kde sa dá posunúť rýchlo. Plán obsahu na reálne hľadania.",
     "Které stránky mají potenciál, které chybí a kde se dá posunout rychle. Plán obsahu na reálná hledání."),
    ("Kategórie, produkty, filtre a feedy. Audit navrhnutý pre e-shopy na Shoptet, Upgates a WooCommerce.",
     "Kategorie, produkty, filtry a feedy. Audit navržený pro e-shopy na Shoptet, Upgates a WooCommerce."),
]
SERVICE_DEFS_ICON = ["audit", "bolt", "mail", "shop"]
SERVICE_DEFS_COLOR = ["#6A3FC4", "#F75940", "#1DACD6", "#1DACD6"]
SERVICE_DEFS_TAG = ["tag-violet", "tag-orange", "tag-cerulean", "tag-cerulean"]

SLIDES = [
    {"client": "Firemný web (klient)", "chip": "SEO od nuly",
     "period": "posledné 3 mesiace",
     "nums": [{"big": "250", "color": _VIOLET, "label": "klikov za 3 mesiace (+355 %)"},
              {"big": "8 950", "color": _CERULEAN, "label": "zobrazení (+246 %)"},
              {"big": "5", "color": _ORANGE, "label": "násobný rast klikov"}],
     "chart": _bars([68, 92, 130, 171, 250], _ORANGE, ["mesiac 1", "mesiac 2", "mesiac 3", "mesiac 4", "teraz"]),
     "caption": "Rast po audite a náprave. Audit ukázal, čo brzdí; náprava každý mesiac posúva web vyššie. Rast každý mesiac, žiadny skok, ktorý sa nedá opakovať."},
    {"client": "Rast po pridaní obsahu", "chip": "Obsah na 6 stránkach",
     "period": "28 dní + posledný týždeň",
     "nums": [{"big": "11 000", "color": _CERULEAN, "label": "zobrazení mesačne (+14 %)"},
              {"big": "+43 %", "color": _VIOLET, "label": "klikov posledný týždeň"},
              {"big": "6", "color": _ORANGE, "label": "stránok, na ktorých sa to stalo"}],
     "chart": _sparkline([30, 38, 42, 50, 55, 62, 66, 72, 78, 84, 92, 102], _CERULEAN),
     "caption": "Obsahový audit ukázal 6 stránok s najväčším potenciálom. Pridaný obsah na reálne dopyty posunul celý web."},
]

PROCESS = {
    "sk": {
        "s1_t": "Bezplatný vstupný audit", "s1_x": "Začneme 30-minútovým hovorom a bezplatným auditom. Uvidíte presne, čo brzdí váš web v Google, ešte pred prvou faktúrou.",
        "s2_t": "Plný audit s plánom", "s2_x": "Kompletný audit so zoznamom opráv podľa priorít: čo opraviť ako prvé, koľko to trvá a čo to prinesie.",
        "s3_t": "Náprava v dávkach", "s3_x": "Opravím to aj za vás: technika, obsah, štruktúra. Vždy viete, čo sa stalo v predchádzajúcom týždni.",
        "s4_t": "Meranie a report", "s4_x": "Mesačný report vám dám osobne: 30-minútový telefonát. Pozície, kliky z Google, čo sa urobilo a čo nasleduje.",
    },
    "cz": {
        "s1_t": "Bezplatný vstupní audit", "s1_x": "Začneme 30minutovým hovorem a bezplatným auditem. Uvidíte přesně, co brzdí váš web v Google, před první fakturou.",
        "s2_t": "Plný audit s plánem", "s2_x": "Kompletní audit se seznamem oprav podle priorit: co opravit jako první, kolik to trvá a co to přinese.",
        "s3_t": "Naprava v dávkách", "s3_x": "Opravím to i za vás: technika, obsah, struktura. Vždy víte, co se stalo v předchozím týdnu.",
        "s4_t": "Měření a report", "s4_x": "Měsíční report vám dám osobně: 30minutový telefonát. Pozice, kliky z Google, co se udělalo a co následuje.",
    },
}

FAQ = {
    "sk": {
        "common": [
            ("Koľko stojí SEO audit?",
             "Bezplatný vstupný audit je zadarmo. Plný audit začina na 5 hodinách (60 EUR) pre malý web, e-shop zvyčajne 10 až 15 hodín (120 až 180 EUR). V pláne vidíte presne, čo dostanete."),
            ("Ako dlho trvá SEO audit?",
             "Plný audit zvyčajne 5 až 10 pracovných dní od hovoru. Dostanete ho v čitateľnej podobe, nie ako surový výpis z nástrojov."),
            ("Čo dostanem v audite?",
             "Zoznam problémov s prioritami: technika, obsah, pozície. Ku každému bodu čo to znamená, koľko trvá oprava a čo môže priniesť. Bez technickej reči, ktorá nič nevraví."),
            ("Je audit SEO online dostupný zdarma?",
             "Základné nástroje (Search Console, PageSpeed Insights) sú zdarma a odporúčam ich. Rozdiel je v interpretácii: ja vám poviem, čo čísla znamenajú pre váš predaj a v akom poradí to riešiť."),
            ("Pomôže mi audit aj v ChatGPT viditeľnosti?",
             "Áno, súčasťou auditu je aj AI viditeľnosť: či vás ChatGPT, Gemini a AI Overviews odporúčajú a čo na to chýba."),
        ],
        "sluzby": [
            ("Aký rozdiel je medzi auditmi?", "Technický audit rieši to, či Google web vidí a rýchlo načítava. Obsahový rieši, čo web pokrýva a čo nie. Kompletný audit oboje aj AI viditeľnosť."),
            ("Robíte audit aj pre e-shopy?", "Áno, e-shop audit je špecifický: kategórie, produkty, filtre, XML feedy a riešenie duplicit."),
        ],
        "cennik": [
            ("Prečo je vstupný audit bezplatný?", "Lebo rozhodnutie o spolupráci potrebujete podložené číslami, nie sľubmi. Ak vám čísla nebudú dávať zmysel, nič neplatíte."),
            ("Koľko stojí plný audit?", "Malý web 5 hodín (60 EUR), firemný web 8 hodín (96 EUR), e-shop 10 až 15 hodín (120 až 180 EUR)."),
        ],
        "proces": [
            ("Čo potrebujem na audit?", "Adresu webu a 30-minútový hovor. Prístup k Search Console a analytics pomáha, ale nie je podmienkou."),
            ("Dostanem audit aj v PDF?", "Áno, audit prijímate v čitateľnej podobe s prioritami. PDF aj prehľadný zoznam bodov."),
        ],
    },
    "cz": {
        "common": [
            ("Kolik stojí SEO audit?",
             "Bezplatný vstupní audit je zdarma. Plný audit začíná na 5 hodinách (60 EUR) pro malý web, e-shop zpravidla 10 až 15 hodin (120 až 180 EUR). V plánu vidíte přesně, co dostanete."),
            ("Jak dlouho trvá SEO audit?",
             "Plný audit zpravidla 5 až 10 pracovních dnů od hovoru. Dostanete ho v čitelné podobě, ne jako surový výpis z nástrojů."),
            ("Co dostanu v auditu?",
             "Seznam problémů s prioritami: technika, obsah, pozice. Ke každému bodu co to znamená, kolik trvá oprava a co může přinést. Bez technické řeči, která nic neříká."),
            ("Je audit SEO online dostupný zdarma?",
             "Základní nástroje (Search Console, PageSpeed Insights) jsou zdarma a doporučuji je. Rozdíl je v interpretaci: já vám řeknu, co čísla znamenají pro váš prodej a v jakém pořadí to řešit."),
            ("Pomůže mi audit i v ChatGPT viditelnosti?",
             "Ano, součástí auditu je i AI viditelnost: zda vás ChatGPT, Gemini a AI Overviews doporučují a co na to chybí."),
        ],
        "sluzby": [
            ("Jaký rozdíl je mezi audity?", "Technický audit řeší, zda Google web vidí a rychle načítá. Obsahový řeší, co web pokrývá a co ne. Kompletní audit obojí i AI viditelnost."),
            ("Děláte audit i pro e-shopy?", "Ano, e-shop audit je specifický: kategorie, produkty, filtry, XML feedy a řešení duplicit."),
        ],
        "cennik": [
            ("Proč je vstupní audit bezplatný?", "Protože rozhodnutí o spolupráci potřebujete podložené čísly, ne sliby. Když vám čísla nebudou dávat smysl, nic neplatíte."),
            ("Kolik stojí plný audit?", "Malý web 5 hodin (60 EUR), firemní web 8 hodin (96 EUR), e-shop 10 až 15 hodin (120 až 180 EUR)."),
        ],
        "proces": [
            ("Co potřebuji na audit?", "Adresu webu a 30minutový hovor. Přístup k Search Console a analytics pomáhá, ale není podmínkou."),
            ("Dostanu audit i v PDF?", "Ano, audit přebíráte v čitelné podobě s prioritami. PDF i přehledný seznam bodů."),
        ],
    },
}

DETAIL = [
    {  # 0: seo-audit webu
        "sk": {
            "h1": '<span class="hl-violet-light">SEO audit</span> webu: presný obraz toho, čo vás brzdí',
            "sub": "15-bodová kontrola techniky, obsahu, pozícií aj AI viditeľnosti. S plánom podľa priorít, nie s výpisom z nástrojov.",
            "title": "SEO audit webu | SEO audit",
            "desc": "SEO audit webu: technika, obsah, pozície aj AI viditeľnosť. Plán podľa priorít. Bezplatný vstupný audit. Nokto Studio, SEO špecialista.",
            "b1_t": "Čo auditom zistím", "b1_x": "Ktoré stránky Google vidí a ktoré nie, kde stráca web rýchlosť, čo brzdí obsah, na ktorých kľúčových slovách sa dá posunúť ako prvé a či vás AI nástroje odporúčajú.",
            "b2_t": "Čo dostanete", "b2_x": "Čitateľný audit so zoznamom bodov podľa priorít. Ku každému bodu čo znamená, koľko trvá oprava a čo môže priniesť. Bez technickej reči.",
            "what_t": "Ako audit prebieha",
            "what_x": "Najprv 30-minútový hovor a bezplatný vstupný audit. Plný audit potom beží 5 až 10 pracovných dní. Výsledok dostanete v podobe, ktorú aj neprogramátor rozumie.",
        },
        "cz": {
            "h1": '<span class="hl-violet-light">SEO audit</span> webu: přesný obraz toho, co vás brzdí',
            "sub": "15 bodová kontrola techniky, obsahu, pozic i AI viditelnosti. S plánem podle priorit, ne s výpisem z nástrojů.",
            "title": "SEO audit webu | SEO audit",
            "desc": "SEO audit webu: technika, obsah, pozice i AI viditelnost. Plán podle priorit. Bezplatný vstupní audit. Nokto Studio, SEO specialista.",
            "b1_t": "Co auditom zjistím", "b1_x": "Které stránky Google vidí a které ne, kde ztrácí web rychlost, co brzdí obsah, na kterých klíčových slovech se dá posunout jako první a zda vás AI nástroje doporučují.",
            "b2_t": "Co dostanete", "b2_x": "čitelný audit se seznamem bodů podle priorit. Ke každému bodu co znamená, kolik trvá oprava a co může přinést. Bez technické řeči.",
            "what_t": "Jak audit probíhá",
            "what_x": "Nejdřív 30minutový hovor a bezplatný vstupní audit. Plný audit potom běží 5 až 10 pracovních dní. Výsledek dostanete v podobě, které rozumí i neprogramátor.",
        },
    },
    {  # 1: technicky audit
        "sk": {
            "h1": 'Technický SEO audit: <span class="hl-orange">indexácia</span>, rýchlosť a štruktúra',
            "sub": "Čo Google z vášho webu vidí, ako rýchlo sa načítava a kde stráca. Základy, ktoré rozhodujú o pozíciách.",
            "title": "Technický SEO audit | SEO audit",
            "desc": "Technický SEO audit: indexácia, Core Web Vitals, presmerovania, sitemap, robots.txt. Nokto Studio, 12 EUR za hodinu.",
            "b1_t": "Čo riešim", "b1_x": "Indexáciu a crawl budget, rýchlosť a Core Web Vitals, presmerovania a 404, sitemap a robots.txt, canonical adresy a štruktúrované dáta.",
            "b2_t": "Prečo to rozhoduje", "b2_x": "Ak Google nevidí stránku alebo sa načítava pomaly, obsah ani odkazy nepomôžu. Technika je základ, na ktorom všetko ostatné stojí.",
            "what_t": "Ako technický audit prebieha",
            "what_x": "Crawl webu, Search Console, PageSpeed Insights a ručná kontrola kľúčových šablón. Výsledok: zoznam opráv v poradí, ktoré dáva zmysel.",
        },
        "cz": {
            "h1": 'Technický SEO audit: <span class="hl-orange">indexace</span>, rychlost a struktura',
            "sub": "Co Google z vašeho webu vidí, jak rychle se načítá a kde ztrácí. Základy, které rozhodují o pozicích.",
            "title": "Technický SEO audit | SEO audit",
            "desc": "Technický SEO audit: indexace, Core Web Vitals, přesměrování, sitemap, robots.txt. Nokto Studio, 12 EUR za hodinu.",
            "b1_t": "Co řeším", "b1_x": "Indexaci a crawl budget, rychlost a Core Web Vitals, přesměrování a 404, sitemap a robots.txt, canonical adresy a strukturovaná data.",
            "b2_t": "Proč to rozhoduje", "b2_x": "Když Google nevidí stránku nebo se načítá pomalu, obsah ani odkazy nepomohou. Technika je základ, na kterém vše stojí.",
            "what_t": "Jak technický audit probíhá",
            "what_x": "Crawl webu, Search Console, PageSpeed Insights a ruční kontrola klíčových šablon. Výsledek: seznam oprav v pořadí, které dává smysl.",
        },
    },
    {  # 2: obsahovy audit
        "sk": {
            "h1": 'Obsahový audit: čo pokrývate a <span class="hl-cerulean-light">čo chýba</span>',
            "sub": "Ktoré stránky majú potenciál posunúť sa hore, ktoré témy chýbajú a kde sa dá rýchlo vyhrať. Plán obsahu na reálne hľadania.",
            "title": "Obsahový SEO audit | SEO audit",
            "desc": "Obsahový audit webu: ktoré stránky majú potenciál, ktoré témy chýbajú, plán obsahu na reálne hľadania. Nokto Studio.",
            "b1_t": "Čo auditom zistím", "b1_x": "Ktoré stránky majú najväčší potenciál (striking distance), ktoré obsahové témy konkurencia pokrýva a vy nie, kde sa dá posunúť v týždňoch, nie v mesiacoch.",
            "b2_t": "Čo dostanete", "b2_x": "Plán obsahu: zoznam tém s objemom hľadania, prioritami a navrhnutými stránkami. Buď na nové články, alebo na vylepšenie existujúcich.",
            "what_t": "Ako obsahový audit prebieha",
            "what_x": "Porovnám váš obsah s konkurenciou a dátami z Google. Výstupom je plán obsahu, ktorý sa dá rovno realizovať, nielen zoznam odporúčaní.",
        },
        "cz": {
            "h1": 'Obsahový audit: co pokrýváte a <span class="hl-cerulean-light">co chybí</span>',
            "sub": "Které stránky mají potenciál posunout se výš, která témata chybí a kde se dá rychle vyhrát. Plán obsahu na reálná hledání.",
            "title": "Obsahový SEO audit | SEO audit",
            "desc": "Obsahový audit webu: které stránky mají potenciál, která témata chybí, plán obsahu na reálná hledání. Nokto Studio.",
            "b1_t": "Co auditom zjistím", "b1_x": "Které stránky mají největší potenciál (striking distance), která témata konkurence pokrývá a vy ne, kde se dá posunout v týdnech, ne měsících.",
            "b2_t": "Co dostanete", "b2_x": "Plán obsahu: seznam témat s objemem hledání, prioritami a navrhnutými stránkami. Buď na nové články, nebo na vylepšení existujících.",
            "what_t": "Jak obsahový audit probíhá",
            "what_x": "Porovnám váš obsah s konkurencí a daty z vyhledávání. Výstupem je plán obsahu, který jde rovnou realizovat, ne jen seznam doporučení.",
        },
    },
    {  # 3: eshop audit
        "sk": {
            "h1": 'SEO audit e-shopu: <span class="hl-violet-light">kategórie</span>, produkty a filtre',
            "sub": "Audit navrhnutý pre e-shopy: kde strácajú kategórie, čo chýba produktom, či filtre vytvárajú duplicity a čo chýba vo feede.",
            "title": "SEO audit e-shopu | SEO audit",
            "desc": "SEO audit e-shopu: kategórie, produkty, filtre, XML feedy, riešenie duplicit. Shoptet, Upgates, WooCommerce. Nokto Studio.",
            "b1_t": "Čo auditom zistím", "b1_x": "Ktoré kategórie Google vidí a kde stoja, čo brzdí produkty, či filtre a varianty vytvárajú duplicity, čo chýba vo feede pre Merchant Center.",
            "b2_t": "Čo dostanete", "b2_x": "Zoznam opráv s prioritami: kategórie na kľúčové slová, systémová náprava produktov, čisté URL a správne feedy. S odhadom hodín.",
            "what_t": "Ako e-shop audit prebieha",
            "what_x": "Crawl e-shopu, Search Console, kontrola feedov a šablón. Práce priamo vo vašom eshopovom systéme (Shoptet, Upgates, WooCommerce).",
        },
        "cz": {
            "h1": 'SEO audit e-shopu: <span class="hl-violet-light">kategorie</span>, produkty a filtry',
            "sub": "Audit navržený pro e-shopy: kde ztrácejí kategorie, co chybí produktům, zda filtry vytvářejí duplicity a co chybí ve feedu.",
            "title": "SEO audit e-shopu | SEO audit",
            "desc": "SEO audit e-shopu: kategorie, produkty, filtry, XML feedy, řešení duplicit. Shoptet, Upgates, WooCommerce. Nokto Studio.",
            "b1_t": "Co auditom zjistím", "b1_x": "Které kategorie Google vidí a kde stojí, co brzdí produkty, zda filtry a varianty vytvářejí duplicity, co chybí ve feedu pro Merchant Center.",
            "b2_t": "Co dostanete", "b2_x": "Seznam oprav s prioritami: kategorie na klíčová slova, systémová náprava produktů, čisté URL a správné feedy. S odhadem hodin.",
            "what_t": "Jak e-shop audit probíhá",
            "what_x": "Crawl e-shopu, Search Console, kontrola feedů a šablon. Práce přímo ve vašem eshopovém systému (Shoptet, Upgates, WooCommerce).",
        },
    },
]

DETAIL_FAQ = {
    0: {
        "sk": [("Koľko stojí kompletný audit?", "Malý web 5 hodín (60 EUR), firemný 8 hodín (96 EUR), e-shop 10 až 15 hodín. Vstupný audit a hovor sú bezplatné."),
               ("Audit aj pre AI viditeľnosť?", "Áno, súčasťou je kontrola toho, či vás ChatGPT, Gemini a AI Overviews odporúčajú a čo na to chýba.")],
        "cz": [("Kolik stojí kompletní audit?", "Malý web 5 hodin (60 EUR), firemní 8 hodin (96 EUR), e-shop 10 až 15 hodin. Vstupní audit a hovor jsou bezplatné."),
               ("Audit i pro AI viditelnost?", "Ano, součástí je kontrola toho, zda vás ChatGPT, Gemini a AI Overviews doporučují a co na to chybí.")],
    },
    1: {
        "sk": [("Dostanem aj opravy, alebo len odporúčania?", "Oboje. Audit vám dá plán, nápravu urobím za vás v dávkach za 12 EUR za hodinu, ak chcete."),
               ("Musím mať prístup ku kódu?", "Väčšina technických zistení sa dá urobiť bez prístupu ku kódu. Prístup pomáha pri náprave, nie pri audite.")],
        "cz": [("Dostanu i opravy, nebo jen doporučení?", "Obojí. Audit vám dá plán, nápravu udělám za vás v dávkách za 12 EUR za hodinu, když chcete."),
               ("Musím mít přístup ke kódu?", "Většina technických zjištění jde udělat bez přístupu ke kódu. Přístup pomáhá při nápravě, ne při auditu.")],
    },
    2: {
        "sk": [("Znamená obsahový audit aj napísanie obsahu?", "Nie, audit je plán. Obsah píšem ako samostatnú službu na základe plánu, ktorý audit vyprodukuje."),
               ("Na akých dátach je audit postavený?", "Google Search Console, Marketing Miner a porovnanie s konkurenciou. Reálne hľadania, nie odhady.")],
        "cz": [("Znamená obsahový audit i napsání obsahu?", "Ne, audit je plán. Obsah píšu jako samostatnou službu na základě plánu, který audit vyprodukuje."),
               ("Na jakých datech je audit postavený?", "Google Search Console, Marketing Miner a porovnání s konkurencí. Reálná hledání, ne odhady.")],
    },
    3: {
        "sk": [("Pre ktoré platformy robíte e-shop audit?", "Shoptet, Upgates, WooCommerce aj PrestaShop. Štruktúra sa rieši podobne, rozdiely sú v detailoch."),
               ("Koľko trvá audit veľkého e-shopu?", "10 až 15 hodín práce, výsledok do 10 pracovných dní. Pri e-shopoch s desiatkami tisíc produktov viem rozsah upraviť.")],
        "cz": [("Pro které platformy děláte e-shop audit?", "Shoptet, Upgates, WooCommerce i PrestaShop. Struktura se řeší podobně, rozdíly jsou v detailech."),
               ("Kolik trvá audit velkého e-shopu?", "10 až 15 hodin práce, výsledek do 10 pracovních dní. U e-shopů s desítkami tisíc produktů rozsah upřesním.")],
    },
}

BLOG_POSTS = {
    "sk": [
        {"href": "blog/seo-audit-navod/", "title": "SEO audit krok za krokom: ako si audit urobiť sám (2026)",
         "desc": "Bezplatný návod: 15 bodov, ktoré skontrolovať v Search Console a PageSpeed. Kedy si audit nechať urobiť.", "tag": "Návod"},
        {"href": "blog/seo-audit-online/", "title": "SEO audit online: ktoré nástroje skutočne potrebujete",
         "desc": "Search Console, PageSpeed, crawl nástroje. Čo je zdarma, čo stojí za to a čo je len marketing.", "tag": "Nástroje"},
        {"href": "blog/seo-audit-cena/", "title": "Koľko stojí SEO audit a čo za to dostanete",
         "desc": "Cena auditu od 60 EUR. Čo je v cene, čo nie a ako spoznať audit, ktorý nič nevraví.", "tag": "Cena"},
        {"href": "blog/audit-eshopu/", "title": "SEO audit e-shopu: čo skontrolovať ako prvé",
         "desc": "Kategórie, produkty, filtre a feedy. 15 bodov špecifických pre e-shopy na Shoptet a Upgates.", "tag": "E-shop"},
    ],
    "cz": [
        {"href": "blog/seo-audit-navod/", "title": "SEO audit krok za krokem: jak si audit udělat sám (2026)",
         "desc": "Bezplatný návod: 15 bodů, které zkontrolovat v Search Console a PageSpeed. Kdy si audit nechat udělat.", "tag": "Návod"},
        {"href": "blog/seo-audit-online/", "title": "SEO audit online: které nástroje opravdu potřebujete",
         "desc": "Search Console, PageSpeed, crawl nástroje. Co je zdarma, co stojí za to a co je jen marketing.", "tag": "Nástroje"},
        {"href": "blog/seo-audit-cena/", "title": "Kolik stojí SEO audit a co za to dostanete",
         "desc": "Cena auditu od 60 EUR. Co je v ceně, co ne a jak poznat audit, který nic neříká.", "tag": "Cena"},
        {"href": "blog/audit-eshopu/", "title": "SEO audit e-shopu: co zkontrolovat jako první",
         "desc": "Kategorie, produkty, filtry a feedy. 15 bodů specifických pro e-shopy na Shoptet a Upgates.", "tag": "E-shop"},
    ],
}


# ---------------------------------------------------------------- blog articles
BLOG_ARTICLES = {
    "seo-audit-navod": {
        "sk": {
            "label": "Návod",
            "h1": "SEO audit krok za krokom: ako si audit urobiť sám (2026)",
            "title": "SEO audit krok za krokom: návod 2026 | SEO audit",
            "desc": "SEO audit webu sám: 15 kontrolných bodov z Search Console, PageSpeed a obsahu. Kedy si audit nechať urobiť profesionálne.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO audit sám urobíte za 30 minút: 15 bodov v Google Search Console (indexácia, kliky, pozície), PageSpeed Insights (LCP, INP, CLS) a kontrola obsahu. Cieľ je zistiť tri veci: čo Google vidí, čo je pomalé a na ktoré dopyty sa už zobrazujete. Komplexný audit s plánom opráv od 96 EUR.",
            "sections": """
<h2>Čo je SEO audit a čo vám povie</h2>
<p>SEO audit je kontrola webu z pohľadu Google. Odpovie na tri otázky: vidí Google všetky vaše stránky, ako rýchlo sa web načítava a na ktoré dopyty sa už zobrazujete. Bez auditu robíte SEO naslepo: meníte veci, ktoré možno nie sú problém, a necháte problém, ktorý brzdí celý web.</p>

<h2>Krok 1: Google Search Console (10 minút)</h2>
<ul>
<li><strong>Performance</strong>: kliky, zobrazenia, pozície, CTR. Ktoré dopyty prinášajú návštevnosť a kde stojíte.</li>
<li><strong>Pages</strong>: koľko stránok je indexovaných. "Crawled, currently not indexed" znamená problém s kvalitou stránok.</li>
<li><strong>Core Web Vitals</strong>: rýchlosť na reálnych používateľoch.</li>
</ul>

<h2>Krok 2: PageSpeed Insights (5 minút)</h2>
<p>Zadajte adresu a pozrite tri metriky: LCP (pod 2,5 s), INP (pod 200 ms), CLS (pod 0,1). Ak je LCP nad 4 sekundy, web stráca zákazníkov aj pozície. Prvá oprava: cache, WebP obrázky, menej pluginov.</p>

<h2>Krok 3: Obsahová kontrola (15 minút)</h2>
<ul>
<li><strong>Titulky</strong>: má každá stránka jedinečný meta titulok s kľúčovým slovom?</li>
<li><strong>Nadpisy</strong>: jeden H1 na stránku, H2 podľa podotázok?</li>
<li><strong>Interné odkazy</strong>: odkazujú stránky navzájom, alebo sú izolované?</li>
<li><strong>Starý obsah</strong>: články staršie ako rok obnovte.</li>
</ul>

<h2>Kedy si dať audit urobiť profesionálne</h2>
<p>Samoaudít zistí zjavné problémy. Nezistí: čo konkurencia robí lepšie, na ktorých dopytoch sa dá rýchlo posunúť (striking distance), duplicitné URL, štruktúrované dáta, AI viditeľnosť (či vás ChatGPT odporúča). Kompletný audit s plánom podľa priorít: firemný web 8 hodín = 96 EUR, e-shop 10 až 15 hodín = 120 až 180 EUR. Vstupný audit je bezplatný.</p>
""",
            "faq": [
                ("Je bezplatný SEO audit skutočne zdarma?", "Áno. Vstupný audit a 30-minútový hovor sú bezplatné. Plný audit s plánom od 96 EUR."),
                ("Aké nástroje na audit potrebujem?", "Google Search Console a PageSpeed Insights, obe zdarma. Na dopyty a objemy Marketing Miner. Súbor nástrojov neznamená znalosti: rozhoduje interpretácia."),
                ("Ako dlho trvá profesionálny audit?", "Plný audit 5 až 10 pracovných dní. Dostanete čitateľný zoznam bodov s prioritami, nie surový výpis z nástrojov."),
            ],
            "related": [
                ("seo-audit-online", "SEO audit online: ktoré nástroje potrebujete"),
                ("seo-audit-cena", "Koľko stojí SEO audit"),
            ],
        },
        "cz": {
            "label": "Návod",
            "h1": "SEO audit krok za krokem: jak si audit udělat sám (2026)",
            "title": "SEO audit krok za krokem: návod 2026 | SEO audit",
            "desc": "SEO audit webu sám: 15 kontrolních bodů ze Search Console, PageSpeed a obsahu. Kdy si audit nechat udělat profesionálně.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO audit zvládnete sám za 30 minut: 15 bodů v Google Search Console (indexace, pozice), PageSpeed Insights (LCP, INP, CLS) a kontrola obsahu. Komplexní audit s plánem oprav od 96 EUR (12 EUR za hodinu). Vstupní audit je bezplatný.",
            "sections": """
<h2>Co je SEO audit a co vám řekne</h2>
<p>SEO audit odpovídá na tři otázky: vidí Google všechny vaše stránky, jak rychle se web načítá a na které dotazy se už zobrazujete. Bez auditu měníte věci, které možno nejsou problém, a necháte problém, který brzdí celý web.</p>

<h2>Krok 1: Google Search Console (10 minut)</h2>
<ul>
<li><strong>Performance</strong>: kliky, zobrazení, pozice, CTR.</li>
<li><strong>Pages</strong>: kolik stránek je indexovaných. "Crawled, currently not indexed" = problém s kvalitou stránek.</li>
<li><strong>Core Web Vitals</strong>: rychlost na reálných uživatelích.</li>
</ul>

<h2>Krok 2: PageSpeed Insights (5 minut)</h2>
<p>Tři metriky: LCP (pod 2,5 s), INP (pod 200 ms), CLS (pod 0,1). První oprava: cache, WebP obrázky, méně pluginů.</p>

<h2>Krok 3: Obsahová kontrola (15 minut)</h2>
<ul>
<li><strong>Titulky</strong>: jedinečný meta titulek s klíčovým slovem na každé stránce.</li>
<li><strong>Nadpisy</strong>: jeden H1, H2 podle podotázek.</li>
<li><strong>Interní odkazy</strong>: stránky propojené, nebo izolované?</li>
<li><strong>Starý obsah</strong>: články starší rok obnovte.</li>
</ul>

<h2>Kdy si dát audit profesionálně</h2>
<p>Samoaudit najde zjevné problémy. Ne najde: co dělá konkurence lépe, kde se dá rychle posunout, strukturovaná data a AI viditelnost. Kompletní audit: firemní web 8 hodin = 96 EUR, e-shop 10 až 15 hodin = 120 až 180 EUR.</p>
""",
            "faq": [
                ("Je bezplatný SEO audit opravdu zdarma?", "Ano, vstupní audit a hovor jsou bezplatné. Plný audit od 96 EUR."),
                ("Jaké nástroje na audit potřebuji?", "Search Console a PageSpeed Insights, obě zdarma. Rozhoduje interpretace dat, ne počet nástrojů."),
                ("Jak dlouho trvá profesionální audit?", "5 až 10 pracovních dní. Dostanete čitelný seznam bodů s prioritami."),
            ],
            "related": [
                ("seo-audit-online", "SEO audit online: které nástroje potřebujete"),
                ("seo-audit-cena", "Kolik stojí SEO audit"),
            ],
        },
    },
    "seo-audit-online": {
        "sk": {
            "label": "Nástroje",
            "h1": "SEO audit online: ktoré nástroje skutočne potrebujete",
            "title": "SEO audit online: ktoré nástroje potrebujete | SEO audit",
            "desc": "Bezplatné nástroje na SEO audit online: Search Console, PageSpeed Insights, crawl nástroje. Čo je zdarma, čo stojí za to a čo je len marketing.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "Na SEO audit online potrebujete tri bezplatné nástroje: Google Search Console (indexácia, pozície), PageSpeed Insights (rýchlosť) a crawl nástroj (Screaming Frog, 500 URL zdarma). Platene nástroje (Marketing Miner na SK/CZ objemy, Ahrefs na odkazy) majú zmysel pri systematickej práci, nie pri jednorazovom audite.",
            "sections": """
<h2>Základná trojica (všetko zdarma)</h2>
<ul>
<li><strong><a href="https://search.google.com/search-console" target="_blank" rel="noopener noreferrer">Google Search Console</a></strong>: jediný nástroj, ktorý ukazuje reálne dáta o vašom webe v Google. Indexácia, kliky, pozície, Core Web Vitals.</li>
<li><strong><a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a></strong>: rýchlosť a Core Web Vitals. Aj s dátami reálnych používateľov (CrUX).</li>
<li><strong>Crawl nástroj</strong>: Screaming Frog (500 URL zdarma) odhalí 404, presmerovania, chýbajúce titulky, duplicitný obsah.</li>
</ul>

<h2>Platené nástroje: kedy majú zmysel</h2>
<p><strong>Marketing Miner</strong> (SK/CZ objemy dopytov, difficulty): potrebný pri plánovaní obsahu. <strong>Ahrefs alebo Semrush</strong> pri analýze odkazov a konkurencie. Pre jednorazový audit nepotrebujete ani jedno: Search Console dáva 80 percent toho, čo potrebujete.</p>

<h2>Online SEO testy: pozor</h2>
<p>Stránky typu "SEO analyzer zdarma" dajú skóre 45/100 a zoznam všeobecných rád. Skóre je marketingový nástroj, nie audit. Reálny audit odpovedá na otázky špecifické pre váš web: prečo táto kategória nestojí, ktoré dopyty sa dajú dobyť, čo konkurencia robí lepšie.</p>

<h2>Audit nástrojom vs audit človekom</h2>
<p>Nástroj nájde technické chyby (404, presmerovania, pomalé stránky). Človek interpretuje: čo ta chyba znamená pre váš predaj, v akom poradí to riešiť a čo to prinesie. Súrod sa robí: nástroje na dáta, človek na plán. Plný audit s plánom: od 96 EUR, vstupný audit bezplatný.</p>
""",
            "faq": [
                ("Je SEO audit online zdarma možný?", "Áno, základný audit urobíte zdarma cez Search Console a PageSpeed Insights. Rozdíl je v interpretácii a pláne opráv."),
                ("Aký crawl nástroj použiť?", "Screaming Frog (500 URL zdarma) pre menšie weby. Pre e-shopy platná licencia, lebo filtrujú tisíce URL."),
                ("Veriť online SEO testom so skóre?", "Nie. Skóre je marketingový nástroj. Reálny audit odpovedá na otázky špecifické pre váš web."),
            ],
            "related": [
                ("seo-audit-navod", "SEO audit krok za krokom: návod 2026"),
                ("seo-audit-cena", "Koľko stojí SEO audit"),
            ],
        },
        "cz": {
            "label": "Nástroje",
            "h1": "SEO audit online: které nástroje opravdu potřebujete",
            "title": "SEO audit online: které nástroje potřebujete | SEO audit",
            "desc": "Bezplatné nástroje na SEO audit online: Search Console, PageSpeed Insights, crawl nástroje. Co je zdarma, co stojí za to.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "Na SEO audit online potřebujete tři bezplatné nástroje: Google Search Console (indexace, pozice), PageSpeed Insights (rychlost) a crawl nástroj (Screaming Frog, 500 URL zdarma). Placené nástroje mají smysl při systematické práci, pro jednorazový audit stačí Search Console.",
            "sections": """
<h2>Základní trojice (vše zdarma)</h2>
<ul>
<li><strong><a href="https://search.google.com/search-console" target="_blank" rel="noopener noreferrer">Google Search Console</a></strong>: jediný nástroj s reálnými daty o vašem webu: indexace, kliky, pozice.</li>
<li><strong><a href="https://pagespeed.web.dev/" target="_blank" rel="noopener noreferrer">PageSpeed Insights</a></strong>: rychlost a Core Web Vitals.</li>
<li><strong>Crawl nástroj</strong>: Screaming Frog (500 URL zdarma): 404, přesměrování, chybějící titulky, duplicity.</li>
</ul>

<h2>Placené nástroje: kdy mají smysl</h2>
<p>Marketing Miner (CZ/SK objemy dotazů) při plánování obsahu. Ahrefs nebo Semrush při analýze odkazů a konkurence. Pro jednorazový audit nepotřebujete ani jedno: Search Console dáva 80 procent toho, co potřebujete.</p>

<h2>Online SEO testy: pozor</h2>
<p>Stránky typu "SEO test zdarma" dají skóre 45/100 a seznam obecných rad. Skóre je marketing, audit odpovídá na otázky specifické pro váš web: proč tato kategorie nestojí, kde se dá rychle posunout.</p>

<h2>Nástroj vs člověk</h2>
<p>Nástroj najde technické chyby. Člověk interpretuje: co chyba znamená pro váš prodej, v jakém pořadí to řešit. Plný audit s plánem: od 96 EUR, vstupní audit bezplatný.</p>
""",
            "faq": [
                ("Je SEO audit online zdarma možný?", "Ano, základní audit zdarma přes Search Console a PageSpeed. Rozdíl je v interpretaci a plánu oprav."),
                ("Jaký crawl nástroj použít?", "Screaming Frog (500 URL zdarma) pro menší weby. E-shopy potřebují placenou licenci."),
                ("Věřit online SEO testům?", "Ne, skóre 45/100 je marketing. Reálný audit odpovídá na otázky vašeho webu."),
            ],
            "related": [
                ("seo-audit-navod", "SEO audit krok za krokem: návod 2026"),
                ("seo-audit-cena", "Kolik stojí SEO audit"),
            ],
        },
    },
    "seo-audit-cena": {
        "sk": {
            "label": "Cena",
            "h1": "Koľko stojí SEO audit (2026)? Ceny a čo za ne dostanete",
            "title": "Koľko stojí SEO audit | SEO audit",
            "desc": "Cena SEO auditu: vstupný audit zdarma, plný od 96 EUR (firemný web) po 180 EUR (e-shop). Čo je v cene a ako spoznať audit, ktorý nič nevraví.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO audit stojí od 96 EUR: firemný web 8 hodín (96 EUR), e-shop 10 až 15 hodín (120 až 180 EUR) pri hodinovej sadzbe 12 EUR. Vstupný audit je bezplatný. Agentúry účtujú za audit 300 až 1000 EUR, často za vygenerovaný výpis z nástroja, ktorý si môžete urobiť zdarma.",
            "sections": """
<h2>Cenová stupnica SEO auditu</h2>
<ul>
<li><strong>Vstupný audit</strong>: bezplatný. 30-minútový hovor a rýchla kontrola webu, odhad čo by SEO u vás znamenalo.</li>
<li><strong>Plný audit: malý web</strong>: 5 hodín = 60 EUR. Technika, obsah, pozície, plán opráv.</li>
<li><strong>Plný audit: firemný web</strong>: 8 hodín = 96 EUR. Plus konkurencia a obsahový plán.</li>
<li><strong>Plný audit: e-shop</strong>: 10 až 15 hodín = 120 až 180 EUR. Plus kategórie, produkty, filtre, feedy.</li>
</ul>

<h2>Čo má byť v audite</h2>
<p>Zoznam bodov s prioritami: čo opraviť ako prvé, koľko to trvá a čo to prinesie. Ku každému bodu vysvetlenie bez technickej reči. Ak dostanete PDF so skóre 62/100 a desiatich všeobecných rád, to nie je audit, to je marketingový materiál.</p>

<h2>Ako spoznať predražený audit</h2>
<p>Príznaky: cena bez rozsahu (čo presne dostanete?), výstup ako PDF so skóre, žiadna prioritizácia, žiadne čísla z Search Console (reálne dáta vášho webu). Dobrý audit cituje vaše dáta, porovnáva s konkurenciou a končí plánom, ktorý sa dá rovno realizovať.</p>

<h2>Prečo je vstupný audit bezplatný</h2>
<p>Lebo rozhodnutie o spolupráci potrebujete podložené číslami, nie sľubmi. Ak vám čísla nebudú dávať zmysel, nič neplatíte. Prvý hovor je tiež zdarma: 30 minút o vašom webe bez predaja.</p>
""",
            "faq": [
                ("Je vstupný audit naozaj zdarma?", "Áno, bez záväzku. Platíte až za plný audit alebo následnú prácu po pláne."),
                ("Prečo je váš audit lacnejší ako agentúry?", "Hodinová sadzba 12 EUR bez prémiových kancelárií. Kvalita je v interpretácii a pláne, nie v cene."),
                ("Dostanem audit aj v PDF?", "Áno, audit prijímate v čitateľnej podobe s prioritami. PDF aj prehľadný zoznam bodov."),
            ],
            "related": [
                ("seo-audit-navod", "SEO audit krok za krokom: návod 2026"),
                ("audit-eshopu", "SEO audit e-shopu: čo skontrolovať ako prvé"),
            ],
        },
        "cz": {
            "label": "Cena",
            "h1": "Kolik stojí SEO audit (2026)?",
            "title": "Kolik stojí SEO audit | SEO audit",
            "desc": "Cena SEO auditu: vstupní zdarma, plný od 96 EUR (firemní web) po 180 EUR (e-shop). Co je v ceně a jak poznat audit, který nic neříká.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO audit stojí od 96 EUR: firemní web 8 hodin (96 EUR), e-shop 10 až 15 hodin (120 až 180 EUR) při hodinové sazbě 12 EUR. Vstupní audit je bezplatný. Agentury účtují za audit 300 až 1000 EUR, často za vygenerovaný výpis, který zvládnete zdarma.",
            "sections": """
<h2>Cenová stupnice SEO auditu</h2>
<ul>
<li><strong>Vstupní audit</strong>: bezplatný. 30minutový hovor a rychlá kontrola webu.</li>
<li><strong>Plný audit: malý web</strong>: 5 hodin = 60 EUR.</li>
<li><strong>Plný audit: firemní web</strong>: 8 hodin = 96 EUR. Plus konkurence a obsahový plán.</li>
<li><strong>Plný audit: e-shop</strong>: 10 až 15 hodin = 120 až 180 EUR. Plus kategorie, produkty, filtry, feedy.</li>
</ul>

<h2>Co má být v auditu</h2>
<p>Seznam bodů s prioritami: co opravit jako první, kolik to trvá a co to přinese. Vysvětlení bez technické řeči. Dobrý audit končí plánem, který jde rovnou realizovat, ne skóre 62/100.</p>

<h2>Jak poznat předražený audit</h2>
<p>Příznaky: cena bez rozsahu, výstup jako skóre bez priorit, žádná data z Search Console, žádné srovnání s konkurencí. Dobrý audit odpovídá na otázky vašeho webu, ne obecně.</p>

<h2>Proč je vstupní audit bezplatný</h2>
<p>Protože rozhodnutí o spolupráci potřebujete podložené čísly. Když vám čísla nebudou dávat smysl, nic neplatíte.</p>
""",
            "faq": [
                ("Je vstupní audit opravdu zdarma?", "Ano, bez závazku. Platíte za plný audit nebo následnou práci po plánu."),
                ("Proč je váš audit levnější než agentury?", "Hodinová sazba bez prémiových kancelárií. Kvalita je v interpretaci a plánu, ne v ceně."),
                ("Dostanu audit v PDF?", "Ano, v čitelné podobě s prioritami."),
            ],
            "related": [
                ("seo-audit-navod", "SEO audit krok za krokem: návod 2026"),
                ("audit-eshopu", "SEO audit e-shopu: co zkontrolovat jako první"),
            ],
        },
    },
    "audit-eshopu": {
        "sk": {
            "label": "E-shop",
            "h1": "SEO audit e-shopu: čo skontrolovať ako prvé",
            "title": "SEO audit e-shopu | SEO audit",
            "desc": "SEO audit e-shopu: kategórie, produkty, filtre, XML feedy a riešenie duplicit. 15 bodov špecifických pre Shoptet a Upgates. Od 120 EUR.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO audit e-shopu kontroluje 15 bodov, ktoré bežný audit nepokrýva: duplicitné URL z filtrov, kanonické adresy produktov, XML feed pre Google Merchant Center, texty kategórií na reálne hľadania, štruktúrované dáta produktov a dostupnosť vo feede. E-shop audit trvá 10 až 15 hodín = 120 až 180 EUR.",
            "sections": """
<h2>Prečo je e-shop audit iný</h2>
<p>E-shop má tisíce stránok, filtre a varianty. Každá technická chyba sa násobí: jedna zlá šablóna popisu = 5 000 slabých produktových stránok. Preto e-shop audit začína systémom (šablóny, pravidlá, feedy), nie jednotlivými stránkami.</p>

<h2>15 bodov e-shop auditu (výber)</h2>
<ul>
<li><strong>Filte a duplicitné URL</strong>: či Google indexuje každú kombináciu filtra.</li>
<li><strong>Kanonické adresy</strong>: produktov, variantov, kategórií.</li>
<li><strong>Texty kategórií</strong>: či kategórie majú text na reálne hľadania.</li>
<li><strong>Popisy produktov</strong>: vlastné, alebo duplicitné s dodávateľom?</li>
<li><strong>XML feed</strong>: názvy, ceny, dostupnosť, GTIN v Merchant Center.</li>
<li><strong>Schema</strong>: Product, Offer, Review. Ceny a hodnotenia v SERP.</li>
<li><strong>Rýchlosť</strong>: LCP kategórií a produktových stránok.</li>
<li><strong>Vnútorné prepojenie</strong>: či kategórie odkazujú medzi sebou a na blog.</li>
</ul>

<h2>Koľko trvá e-shop audit</h2>
<p>10 až 15 hodín práce = 120 až 180 EUR pri hodinovej sadzbe 12 EUR. Výsledok do 10 pracovných dní: zoznam opráv s prioritami a odhadom hodín. Vstupný audit (bezplatný) ukáže prvé zistenia ešte pred objednaním plného auditu.</p>
""",
            "faq": [
                ("Pre ktoré platformy robíte e-shop audit?", "Shoptet, Upgates, WooCommerce aj PrestaShop. Štruktúra je podobná, rozdiely sú v nastaveniach platformy."),
                ("Koľko trvá audit veľkého e-shopu?", "10 až 15 hodín práce, výsledok do 10 pracovných dní. Rozsah upresním podľa počtu produktov."),
                ("Dostanem aj nápravu, alebo len odporúčania?", "Oboje. Audit dáva plán, nápravu urobím v dávkach za 12 EUR za hodinu, ak chcete."),
            ],
            "related": [
                ("seo-audit-navod", "SEO audit krok za krokom: návod 2026"),
                ("seo-audit-cena", "Koľko stojí SEO audit"),
            ],
        },
        "cz": {
            "label": "E-shop",
            "h1": "SEO audit e-shopu: co zkontrolovat jako první",
            "title": "SEO audit e-shopu | SEO audit",
            "desc": "SEO audit e-shopu: kategorie, produkty, filtry, XML feedy, řešení duplicit. 15 bodů pro Shoptet a Upgates. Od 120 EUR.",
            "date_display": "17. 9. 2026", "date_iso": "2026-09-17",
            "answer": "SEO audit e-shopu řeší, co běžný audit nevidí: duplicitní URL z filtrů, kanonické adresy produktů, XML feed pro Merchant Center, texty kategorií na reálná hledání a strukturovaná data. E-shop audit trvá 10 až 15 hodin = 120 až 180 EUR (12 EUR za hodinu).",
            "sections": """
<h2>Proč je e-shop audit jiný</h2>
<p>E-shop má tisíce stránek a jedna šablona popisu = 5000 slabých produktových stránek. Proto e-shop audit začíná systémem (šablony, pravidla, feedy), ne jednotlivými stránkami.</p>

<h2>15 bodů e-shop auditu (ukázka)</h2>
<ul>
<li><strong>Filtry a duplicitní URL</strong>: zda Google indexuje každou kombinaci.</li>
<li><strong>Kanonické adresy</strong>: produktů, variant, kategorií.</li>
<li><strong>Texty kategorií</strong>: na reálná hledání, ne generické fráze.</li>
<li><strong>Popisy produktů</strong>: vlastní, nebo duplicitní s dodavatelem?</li>
<li><strong>XML feed</strong>: názvy, ceny, dostupnost, GTIN v Merchant Center.</li>
<li><strong>Schema</strong>: Product, Offer, Review. Ceny a hodnocení ve výsledcích.</li>
<li><strong>Rychlost</strong>: LCP kategorií i produktů.</li>
</ul>

<h2>Kolik trvá e-shop audit</h2>
<p>10 až 15 hodin = 120 až 180 EUR (12 EUR za hodinu). Výsledek do 10 pracovních dní: seznam oprav s prioritami a odhadem hodin. Vstupní audit je bezplatný.</p>
""",
            "faq": [
                ("Pro které platformy děláte e-shop audit?", "Shoptet, Upgates, WooCommerce i PrestaShop."),
                ("Kolik trvá audit velkého e-shopu?", "10 až 15 hodin, výsledek do 10 pracovních dní. Rozsah upřesním podle počtu produktů."),
                ("Dostanu i nápravu?", "Ano, audit dá plán, nápravu udělám v dávkách za 12 EUR za hodinu."),
            ],
            "related": [
                ("seo-audit-navod", "SEO audit krok za krokem: návod 2026"),
                ("seo-audit-cena", "Kolik stojí SEO audit"),
            ],
        },
    },
}
