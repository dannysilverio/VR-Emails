"""Riche News issues, Oct 13 to Nov 7, 2026.

Data sources (pulled Oct 9, 2026): Shopify sales and inventory reports,
Klaviyo Added to Cart (300 most recent) and Viewed Product (1,000 events,
Oct 4 to 9). Refresh any stock counts the morning of each send.
"""

CDN = "https://cdn.shopify.com/s/files/1/0004/3165/2915/files/"

P = {
    "core": dict(name="CORE Hoodie Set", price="$100 · Hoodie + Pant", path="/products/core-hoodie-set",
                 img=CDN + "BLACK_77a5bfaf-9082-4092-9a6e-71f69757f5e4.jpg?v=1787716719"),
    "kids_core": dict(name="Kids CORE Hoodie Set", price="$75 · Sizes 8 to 18/20", path="/products/kids-core-hoodie-set",
                      img=CDN + "BLACK_5779d8a2-012d-4e4c-855d-0dae4102763c.jpg?v=1787706230"),
    "god_particle": dict(name="God Particle Jacket Set", price="$192", path="/products/god-particle-jacket-set",
                         img=CDN + "GREEN.jpg?v=1772151494"),
    "star_studded": dict(name="Star Studded Nylon Jacket Set", price="$198", path="/products/star-studded-nylon-jacket-set",
                         img=CDN + "1_01295691-8a6e-46b4-944b-3c70ab797d3e.jpg?v=1764170263"),
    "tribal": dict(name="Tribal Jacket Set", price="$198", path="/products/tribal-jacket-set",
                   img=CDN + "VR1874-VR1875BLKFRONT.jpg?v=1775430466"),
    "enigma": dict(name="Enigma Set", price="$200", path="/products/enigma-set",
                   img=CDN + "SET15.jpg?v=1778782439"),
    "arcangel_crew": dict(name="Mixmatch Arcangel Crew Set", price="$198", path="/products/mixmatch-arcangel-crew-set-1",
                          img=CDN + "1900668f161a6298c9.jpg?v=1763582774"),
    "crystal": dict(name="Mixmatch Crystal Set", price="$198", path="/products/mixmatch-crystal-set",
                    img=CDN + "197636923d2fb8bd98.jpg?v=1763955746"),
    "crazy_eyes": dict(name="Crazy Eyes Full Zip Hoodie Set", price="$80", path="/products/crazy-eyes-oversized-full-zip-hoodie-set",
                       img=CDN + "CF5513-BLCK1_0c3645b1-b673-4699-8533-4403b01ab882.jpg?v=1765688021"),
    "reaper": dict(name="Reaper Oversized Hoodie", price="$32", path="/products/reaper-oversized-pull-over-hoodie",
                   img=CDN + "CF5516_BLACK_1_1X1_560b641f-4ce1-4578-950b-3c5bce49ed76.jpg?v=1765425380"),
    "archangel_v": dict(name="Archangel V Tee", price="$50", path="/products/archangel_v_tee",
                        img=CDN + "magnific__generate-a-hyper-realistic-front-facing-profession__96077.png?v=1778016474"),
    "snake_eyes": dict(name="Snake Eyes Tee", price="$50", path="/products/snake_eyes_tee",
                       img=CDN + "magnific__generate-a-hyper-realistic-front-facing-profession__93840.png?v=1778038819"),
    "swamp": dict(name="Swamp Monster Tee", price="$50", path="/products/swamp_monster_t-shirt",
                  img=CDN + "VR2031-BLK1.jpg?v=1776793843"),
    "dracula": dict(name="Count Dracula Rugby", price="$50", path="/products/count_dracula_rugby",
                    img=CDN + "magnific__generate-a-hyper-realistic-front-facing-profession__93855.png?v=1778044219"),
    "lux_jersey": dict(name="Luxury Estate Jersey", price="$50", path="/products/luxury_estate_jersey",
                       img=CDN + "5_13272efb-1cbf-4e41-824d-c7f17ffc220f.jpg?v=1780631401"),
    "fearless": dict(name="Fearless Jersey", price="$25", path="/products/fearless-jersey",
                     img=CDN + "GN6270-BLACK-1_29753f46-fc63-4f54-927b-a98f8c01375b.jpg?v=1754859915"),
    "spider": dict(name="Spider Full Zip Hoodie", price="$40", path="/products/spider-oversized-full-zip-hoodie",
                   img=CDN + "CF5523-IRON1.jpg?v=1765687025"),
    "sleep": dict(name="Sleep Is The Cousin Of Death Zip", price="$40", path="/products/sleep-is-the-cousin-of-death-zip-up-hoodie",
                  img=CDN + "DS363_INDIGO_1_1X1_64d968a3-b644-42b2-8218-2835cea91a15.jpg?v=1765425055"),
    "skull": dict(name="Chosen Spiked Skull Sweatshirt", price="$32", path="/products/chosen-spiked-skull-oversized-sweatshirt",
                  img=CDN + "CF5507_ROUGE_1_1X1_6ad47209-f264-4c3d-96b9-da6c1504cb5b.jpg?v=1765425224"),
    "atlas": dict(name="Atlas Beetle Hoodie", price="$40", path="/products/atlas-beetle-pullover-hoodie",
                  img=CDN + "DS325_CREAM_1_1X1_070f573b-cd5d-4f3e-b7c9-50205257c268.jpg?v=1765424966"),
    "dragon_zip": dict(name="Dragon Zipper Hoodie", price="$79.20", path="/products/dragon_zipper_hoodie",
                       img=CDN + "STI625-BLK1.jpg?v=1771644311"),
    "digiworld": dict(name="Digiworld Zip Hoodie", price="$59.20", path="/products/digiworld_zip_hoodie",
                      img=CDN + "VR1326-OW-1_a29b7270-12c1-4f1f-89c2-08d6a2f18e15.jpg?v=1742349164"),
    "fleece_hoodie": dict(name="Garment-Dyed Heavyweight Fleece Hoodie", price="$52",
                          path="/products/garment-dyed-heavyweight-cotton-fleece-hoodie-copy", img=CDN + "image_5.png?v=1776979442"),
    "washed_hoodie": dict(name="Unknown Washed Effect Hoodie", price="$52", path="/products/unknown-washed-effect-pullover-hoodie",
                          img=CDN + "20652692dd35acc686.jpg?v=1764611730"),
    "rock_roll": dict(name="Rock & Roll Tee", price="$25", path="/products/rock-roll-t-shirt",
                      img=CDN + "GN6166-LTG1.jpg?v=1770671310"),
}


def prod(key, utm, tag=None, hot=False, blurb=None, cta=None):
    p = dict(P[key], utm=utm)
    if tag:
        p["tag"] = tag
    p["hot"] = hot
    if blurb:
        p["blurb"] = blurb
    if cta:
        p["cta"] = cta
    return p


CORE_COLORS = [("Black", "#111111"), ("Navy", "#1f2a44"), ("Dark Grey", "#4a4a4a"), ("Light Grey", "#bdbdbd"),
               ("Tone", "#b9a58a"), ("Wine", "#5e1a28"), ("Natural", "#e8dfcf"), ("Dust Lilac", "#b9a6c4"),
               ("Olive", "#5b5f3a"), ("Dust Pink", "#d8b2ad")]

ISSUES = [
    # 01 -----------------------------------------------------------------
    dict(
        slug="01-new-site", no="01", send="2026-10-13", date_label="Tuesday, October 13, 2026",
        utm_campaign="rn01_new_site", title="Did Vie Riche Just Rebuild Everything?",
        subject="Riche News: we rebuilt everything", preview="New vie-riche.com is live. Plus, new CORE colors just leaked.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="Did Vie Riche Just Rebuild <em>Everything?</em>"),
            dict(type="text", html="Short answer: yes. The new <strong>vie-riche.com</strong> is live. New look, easier to find your sets, hoodies and the drops that never come back. Everything you already love is still there."),
            dict(type="button", text="Enter the new site", href="/", utm="hero_cta"),
            dict(type="rule"),
            dict(type="section", html="What changed,<br>what didn&#39;t", sub="Three things worth knowing before you go in."),
            dict(type="cards", items=[
                ("New Look, Same DNA", "Same Riche. Cleaner pages, bigger photos, faster to the size you want."),
                ("Drops Still Don&#39;t Come Back", "Limited runs, no restocks. If it sells out on the new site, it is gone for good."),
                ("CORE Has News", "New CORE colorways are on the way. Subscribers hear first."),
            ]),
            dict(type="feature", product=prod("core", "core_feature", tag="Leak · New colors soon",
                                               blurb="10 colorways live now, XS to 3X. More coming. Want the current lineup before the new colors land?",
                                               cta="Shop CORE")),
            dict(type="button", text="Shop new arrivals", href="/collections/new-arrivals", utm="final_cta"),
        ],
    ),
    # 02 -----------------------------------------------------------------
    dict(
        slug="02-core-winter", no="02", send="2026-10-15", date_label="Thursday, October 15, 2026",
        utm_campaign="rn02_core_winter", title="Is One Set Enough For The Whole Winter?",
        subject="Is one set enough for the whole winter?", preview="The CORE math: 10 colors, 7 sizes, one $100 set.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="Is One Set Enough For The Whole <em>Winter?</em>"),
            dict(type="text", html="We think one is a start. CORE is the hoodie and pant set built to be worn on repeat, in every size and every color, all season."),
            dict(type="stats", items=[("10", "Colorways"), ("XS-3X", "Size run"), ("$100", "Full set")]),
            dict(type="image", src=P["core"]["img"], alt="Vie Riche CORE Hoodie Set in black", href=P["core"]["path"], utm="core_image"),
            dict(type="section", html="The Winter<br>Wardrobe Problem", sub="Most cold-weather fits fail the same three ways."),
            dict(type="cards", items=[
                ("Mismatched Pieces", "A hoodie from one place, sweats from another. CORE is cut as one set, one color, one fit."),
                ("Sizes Gone By November", "CORE is stocked deep across XS to 3X, so the size you need is the size you get."),
                ("Paying Twice", "Buy the set once for $100, wear it all winter. Add a second color when one is in the wash."),
            ]),
            dict(type="vote", href="/products/core-hoodie-set", options=CORE_COLORS),
            dict(type="text", html="Tap your color to shop it.", pad="0 46px 6px"),
            dict(type="button", text="Shop CORE", href="/products/core-hoodie-set", utm="core_cta"),
        ],
    ),
    # 03 -----------------------------------------------------------------
    dict(
        slug="03-sellout-report", no="03", send="2026-10-17", date_label="Saturday, October 17, 2026",
        utm_campaign="rn03_sellout", title="How Fast Does Limited Actually Sell Out?",
        subject="How fast does limited actually sell out?", preview="We pulled the numbers. Some styles are nearly gone for good.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="How Fast Does Limited Actually <em>Sell Out?</em>"),
            dict(type="text", html="We never restock a drop. So we pulled the numbers on what moved fastest in the last 30 days. These are the pieces closest to gone."),
            dict(type="chart", title="Share of stock sold, last 30 days", source="Source: Vie Riche store data, Sept 9 to Oct 9, 2026",
                 rows=[("God Particle Set", 80, "80%"), ("Spider Full Zip", 65, "65%"), ("Snake Eyes Tee", 60, "60%"),
                       ("Fearless Jersey", 57, "57%"), ("Swamp Monster Tee", 57, "57%"), ("Luxury Estate Jersey", 49, "49%")]),
            dict(type="button", text="Shop before it&#39;s gone", href="/collections/new-arrivals", utm="hero_cta"),
            dict(type="section", html="Why It<br>Disappears", sub="No restocks is not a slogan. It is the plan."),
            dict(type="cards", items=[
                ("Limited Runs", "Each drop is made in a small run. When the run is done, the style is done."),
                ("No Second Wave", "No restock, no reissue. That is what keeps it rare."),
                ("Your Size Goes First", "Popular sizes clear before the style does. Waiting usually means missing."),
            ]),
            dict(type="grid", products=[
                prod("god_particle", "grid_god_particle", tag="Almost gone", hot=True),
                prod("spider", "grid_spider", tag="Almost gone", hot=True),
                prod("snake_eyes", "grid_snake_eyes", tag="Low stock", hot=True),
                prod("swamp", "grid_swamp", tag="Low stock", hot=True),
                prod("lux_jersey", "grid_lux_jersey", tag="Selling fast"),
                prod("fearless", "grid_fearless", tag="Low stock", hot=True),
            ]),
        ],
    ),
    # 04 -----------------------------------------------------------------
    dict(
        slug="04-in-the-cart", no="04", send="2026-10-20", date_label="Tuesday, October 20, 2026",
        utm_campaign="rn04_carts", title="What Is Sitting In Everyone's Cart?",
        subject="What's sitting in everyone's cart right now?", preview="The most-carted pieces this month, and which sizes are running out.",
        audience="intent",
        blocks=[
            dict(type="headline", html="What Is Sitting In Everyone&#39;s <em>Cart?</em>"),
            dict(type="text", html="We looked at the most recent 300 add-to-carts on vie-riche.com. Same pieces, over and over. Most never made it to checkout."),
            dict(type="chart", title="Most-carted pieces, recent 300 cart adds", source="Source: Vie Riche store data, late Sept to Oct 9, 2026",
                 rows=[("CORE Set (adult + kids)", 30, "30"), ("Mixmatch Arcangel", 8, "8"), ("Archangel V Tee", 8, "8"),
                       ("Reaper Hoodie", 7, "7"), ("Tricot Track Suit", 6, "6"), ("Crazy Eyes Set", 5, "5")]),
            dict(type="section", html="Still Thinking<br>About It?", sub="Here is the thing about carts: they don&#39;t hold stock. Checkout does."),
            dict(type="grid", products=[
                prod("core", "grid_core", tag="Most carted"),
                prod("arcangel_crew", "grid_arcangel_crew", tag="Few sizes left", hot=True),
                prod("archangel_v", "grid_archangel_v", tag="Most carted"),
                prod("reaper", "grid_reaper", tag="Few sizes left", hot=True),
                prod("crazy_eyes", "grid_crazy_eyes", tag="Few sizes left", hot=True),
                prod("kids_core", "grid_kids_core", tag="Match them"),
            ]),
            dict(type="button", text="Finish your fit", href="/cart", utm="cart_cta"),
        ],
    ),
    # 05 -----------------------------------------------------------------
    dict(
        slug="05-most-viewed", no="05", send="2026-10-22", date_label="Thursday, October 22, 2026",
        utm_campaign="rn05_most_viewed", title="The Most-Viewed Pieces Nobody Has Checked Out",
        subject="Everyone's looking. Nobody's checking out.", preview="The most-viewed pieces this month. Some are down to the last sizes.",
        audience="browse",
        blocks=[
            dict(type="headline", html="Everyone&#39;s Looking. Nobody&#39;s <em>Checking Out.</em>"),
            dict(type="text", html="These are the most-viewed pieces on the site in October that people keep leaving behind. Most of them are down to their last sizes."),
            dict(type="chart", title="Product views, Oct 4 to 9", source="Source: Vie Riche site data, 1,000 recent product views",
                 rows=[("Heavyweight Fleece Hoodie", 18, "18"), ("Washed Effect Hoodie", 13, "13"), ("Mixmatch Arcangel", 12, "12"),
                       ("Rock & Roll Tee", 12, "12"), ("Dragon Zip Hoodie", 11, "11"), ("Digiworld Zip", 11, "11")]),
            dict(type="grid", products=[
                prod("fleece_hoodie", "grid_fleece", tag="Most viewed"),
                prod("washed_hoodie", "grid_washed", tag="Most viewed"),
                prod("dragon_zip", "grid_dragon_zip", tag="Last sizes", hot=True),
                prod("digiworld", "grid_digiworld", tag="Last sizes", hot=True),
                prod("crystal", "grid_crystal", tag="Last sizes", hot=True),
                prod("rock_roll", "grid_rock_roll", tag="Under $30"),
            ]),
            dict(type="section", html="Looking Is<br>Free", sub="Owning it takes one more click. Once these sizes go, they don&#39;t come back."),
            dict(type="button", text="See the hoodie rack", href="/collections/hoodies-sweatshirts", utm="hoodie_cta"),
        ],
    ),
    # 06 -----------------------------------------------------------------
    dict(
        slug="06-halloween", no="06", send="2026-10-24", date_label="Saturday, October 24, 2026",
        utm_campaign="rn06_halloween", title="Who Dresses Scarier: You Or Your Costume?",
        subject="Who dresses scarier: you or your costume?", preview="The Riche Halloween edit. Dracula, reapers, swamp monsters.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="Who Dresses Scarier: You Or Your <em>Costume?</em>"),
            dict(type="text", html="Skip the costume aisle. The scariest pieces this October are already in the Riche lineup, and they work long after the 31st."),
            dict(type="feature", product=prod("dracula", "feature_dracula", tag="Halloween pick", hot=True,
                                               blurb="Gothic energy in a premium rugby cut. Few sizes left.", cta="Shop the Count")),
            dict(type="section", html="The Halloween<br>Edit", sub="Five pieces. Zero costumes required."),
            dict(type="grid", products=[
                prod("reaper", "grid_reaper", tag="Halloween"),
                prod("swamp", "grid_swamp", tag="Low stock", hot=True),
                prod("sleep", "grid_sleep", tag="Halloween"),
                prod("skull", "grid_skull", tag="Halloween"),
            ]),
            dict(type="cards", items=[
                ("Wear It Twice", "Costumes get worn once. These get worn all season."),
                ("No Restocks", "Halloween picks are limited runs. When they are gone, they are gone."),
            ]),
            dict(type="button", text="Shop the edit", href="/collections/new-arrivals", utm="final_cta"),
        ],
    ),
    # 07 -----------------------------------------------------------------
    dict(
        slug="07-core-family", no="07", send="2026-10-27", date_label="Tuesday, October 27, 2026",
        utm_campaign="rn07_core_family", title="Does The Family That Matches Stay Together?",
        subject="Does the family that matches stay together?", preview="CORE for you, CORE for the kids. Same set, sized down.",
        audience="buyers",
        blocks=[
            dict(type="headline", html="Does The Family That Matches Stay <em>Together?</em>"),
            dict(type="text", html="We can&#39;t promise that. We can promise the fit. CORE comes in adult XS to 3X and kids 8 to 18/20, in the same colors."),
            dict(type="stats", items=[("$100", "Adult set"), ("$75", "Kids set"), ("10", "Matching colors")]),
            dict(type="feature", product=prod("core", "feature_core", tag="Adult", cta="Shop adult CORE")),
            dict(type="feature", product=prod("kids_core", "feature_kids_core", tag="Kids", cta="Shop kids CORE")),
            dict(type="section", html="Why Families<br>Pick CORE", sub=None),
            dict(type="cards", items=[
                ("Same Set, Two Sizes", "Same hoodie and pant, same colors, cut for adults and kids."),
                ("Built For Repeat Wear", "Heavyweight enough for winter, relaxed enough for every day."),
                ("Photo Ready", "Holiday cards, game days, family pics. Matching does the work."),
            ]),
            dict(type="button", text="Match the family", href="/products/kids-core-hoodie-set", utm="final_cta"),
        ],
    ),
    # 08 -----------------------------------------------------------------
    dict(
        slug="08-jacket-sets", no="08", send="2026-10-29", date_label="Thursday, October 29, 2026",
        utm_campaign="rn08_jacket_sets", title="Why Is The $190 Set Outselling The Hoodie?",
        subject="Why is the $190 set outselling everything?", preview="The jacket set index: what Riche buyers actually spend on.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="Why Is The $190 Set Outselling <em>Everything?</em>"),
            dict(type="text", html="The best-selling pieces on vie-riche.com right now are not tees. They are full jacket sets. Here is where Riche buyers spent the last 60 days."),
            dict(type="chart", title="Top sellers by revenue, last 60 days", source="Source: Vie Riche store data, Aug 10 to Oct 9, 2026",
                 rows=[("God Particle Set", 10573, "$10.6K"), ("Star Studded Set", 6367, "$6.4K"), ("CORE Set", 5745, "$5.7K"),
                       ("Enigma Set", 3540, "$3.5K"), ("Viking Panel Set", 3120, "$3.1K")]),
            dict(type="section", html="One Purchase,<br>Full Fit", sub="A set answers the whole outfit in one move."),
            dict(type="grid", products=[
                prod("god_particle", "grid_god_particle", tag="Almost gone", hot=True),
                prod("star_studded", "grid_star_studded", tag="Top seller"),
                prod("tribal", "grid_tribal", tag="Jacket set"),
                prod("enigma", "grid_enigma", tag="Jacket set"),
            ]),
            dict(type="button", text="Shop the sets", href="/collections/new-arrivals", utm="final_cta"),
        ],
    ),
    # 09 -----------------------------------------------------------------
    dict(
        slug="09-last-call-halloween", no="09", send="2026-10-31", date_label="Saturday, October 31, 2026",
        utm_campaign="rn09_halloween_last", title="Still Haven't Picked Your Fit For Tonight?",
        subject="Still no fit for tonight?", preview="Last call on the Halloween edit before the night starts.",
        audience="clickers",
        blocks=[
            dict(type="headline", html="Still Haven&#39;t Picked Your Fit For <em>Tonight?</em>"),
            dict(type="text", html="Happy Halloween from Riche. If you need something dark to wear tonight or all season, these are the last of the edit."),
            dict(type="grid", products=[
                prod("dracula", "grid_dracula", tag="Last sizes", hot=True),
                prod("reaper", "grid_reaper", tag="Halloween"),
                prod("swamp", "grid_swamp", tag="Last sizes", hot=True),
                prod("sleep", "grid_sleep", tag="Halloween"),
            ]),
            dict(type="button", text="Shop the edit", href="/collections/new-arrivals", utm="final_cta"),
        ],
    ),
    # 10 -----------------------------------------------------------------
    dict(
        slug="10-core-vote", no="10", send="2026-11-03", date_label="Tuesday, November 3, 2026",
        utm_campaign="rn10_core_vote", title="Which CORE Color Wins November?",
        subject="Vote: which CORE color wins November?", preview="10 colors. One winner. Your click is your vote.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="Which CORE Color Wins <em>November?</em>"),
            dict(type="text", html="Ten colorways. One winner. Tap a color to cast your vote and shop it. We will publish the results in the next Riche News."),
            dict(type="vote", href="/products/core-hoodie-set", options=CORE_COLORS),
            dict(type="image", src=P["core"]["img"], alt="Vie Riche CORE Hoodie Set", href=P["core"]["path"], utm="core_image",
                 caption="CORE Hoodie Set. $100. XS to 3X."),
            dict(type="cards", items=[
                ("How Voting Works", "Every tap counts as a vote. Tap as many as you like."),
                ("New Colors Incoming", "The leaked CORE colorways land soon. Voters hear first."),
            ]),
            dict(type="button", text="Shop CORE", href="/products/core-hoodie-set", utm="final_cta"),
        ],
    ),
    # 11 -----------------------------------------------------------------
    dict(
        slug="11-gone-forever", no="11", send="2026-11-05", date_label="Thursday, November 5, 2026",
        utm_campaign="rn11_gone_forever", title="What Did You Miss In October?",
        subject="Gone forever: what you missed in October", preview="The October sell-out report, plus what is still standing.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="Gone Forever: What Did You Miss In <em>October?</em>"),
            dict(type="text", html="Every month some styles sell out and never come back. Here is what is still standing from the fastest movers, for now."),
            dict(type="section", html="Still Standing", sub="The fastest movers that have not sold out yet."),
            dict(type="grid", products=[
                prod("god_particle", "grid_god_particle", tag="Last units", hot=True),
                prod("atlas", "grid_atlas", tag="Last units", hot=True),
                prod("lux_jersey", "grid_lux_jersey", tag="Selling fast"),
                prod("snake_eyes", "grid_snake_eyes", tag="Last units", hot=True),
            ]),
            dict(type="cards", items=[
                ("Why We Don&#39;t Restock", "Limited runs keep Vie Riche from looking like everything else. The tradeoff: when it is gone, it is gone."),
                ("Never Miss The Next One", "Riche News lands Tuesday, Thursday and Saturday. New drops hit the inbox before anywhere else."),
            ]),
            dict(type="button", text="Shop what&#39;s left", href="/collections/new-arrivals", utm="final_cta"),
        ],
    ),
    # 12 -----------------------------------------------------------------
    dict(
        slug="12-early-access", no="12", send="2026-11-07", date_label="Saturday, November 7, 2026",
        utm_campaign="rn12_early_access", title="Do You Want In Before Everyone Else?",
        subject="Do you want in before everyone else?", preview="Black Friday early access list is open. One tap to get on it.",
        audience="engaged_all",
        blocks=[
            dict(type="headline", html="Do You Want In Before <em>Everyone Else?</em>"),
            dict(type="text", html="Black Friday at Riche means limited runs moving faster than ever. The early access list gets in first. One tap puts you on it."),
            dict(type="button", text="I&#39;m in. Add me.", href="/", utm="bfcm_optin"),
            dict(type="cards", items=[
                ("First Access", "Early access list members shop before the public."),
                ("Limited Runs", "No restocks, Black Friday included. Early means your size."),
                ("One Tap", "Tap the button above. That&#39;s it. You&#39;re on the list."),
            ]),
            dict(type="section", html="Warm Up<br>With CORE", sub="The set that is stocked deep for the whole season."),
            dict(type="feature", product=prod("core", "feature_core", tag="All sizes live", cta="Shop CORE")),
        ],
    ),
]


# ---- clickable product imagery everywhere ---------------------------------

CHART_PRODUCTS = {
    "God Particle Set": "god_particle", "Spider Full Zip": "spider", "Snake Eyes Tee": "snake_eyes",
    "Fearless Jersey": "fearless", "Swamp Monster Tee": "swamp", "Luxury Estate Jersey": "lux_jersey",
    "CORE Set (adult + kids)": "core", "Mixmatch Arcangel": "arcangel_crew", "Archangel V Tee": "archangel_v",
    "Reaper Hoodie": "reaper", "Crazy Eyes Set": "crazy_eyes", "Heavyweight Fleece Hoodie": "fleece_hoodie",
    "Washed Effect Hoodie": "washed_hoodie", "Rock & Roll Tee": "rock_roll", "Dragon Zip Hoodie": "dragon_zip",
    "Digiworld Zip": "digiworld", "Star Studded Set": "star_studded", "CORE Set": "core", "Enigma Set": "enigma",
}

# Products shown under each issue's card section (3-up clickable strip).
CARD_STRIPS = {
    "01-new-site": ["god_particle", "star_studded", "arcangel_crew"],
    "02-core-winter": ["core", "kids_core", "crazy_eyes"],
    "03-sellout-report": ["god_particle", "spider", "snake_eyes"],
    "06-halloween": ["dracula", "reaper", "skull"],
    "07-core-family": ["core", "kids_core", "reaper"],
    "10-core-vote": ["core", "kids_core", "fleece_hoodie"],
    "11-gone-forever": ["god_particle", "atlas", "spider"],
    "12-early-access": ["god_particle", "star_studded", "enigma"],
}

MOST_WANTED = {
    "01-new-site": ["core", "god_particle", "arcangel_crew"],
    "02-core-winter": ["god_particle", "star_studded", "arcangel_crew"],
    "03-sellout-report": ["core", "arcangel_crew", "crazy_eyes"],
    "04-in-the-cart": ["god_particle", "star_studded", "fleece_hoodie"],
    "05-most-viewed": ["core", "god_particle", "reaper"],
    "06-halloween": ["core", "god_particle", "arcangel_crew"],
    "07-core-family": ["god_particle", "star_studded", "enigma"],
    "08-jacket-sets": ["core", "arcangel_crew", "crystal"],
    "09-last-call-halloween": ["core", "god_particle", "skull"],
    "10-core-vote": ["god_particle", "star_studded", "arcangel_crew"],
    "11-gone-forever": ["core", "star_studded", "arcangel_crew"],
    "12-early-access": ["kids_core", "arcangel_crew", "reaper"],
}

for _iss in ISSUES:
    _new = []
    for _b in _iss["blocks"]:
        if _b["type"] == "chart":
            _b["rows"] = [r + (prod(CHART_PRODUCTS[r[0]], CHART_PRODUCTS[r[0]]),) if r[0] in CHART_PRODUCTS else r
                          for r in _b["rows"]]
        _new.append(_b)
        if _b["type"] == "cards" and _iss["slug"] in CARD_STRIPS:
            _new.append(dict(type="strip", products=[prod(k, k) for k in CARD_STRIPS[_iss["slug"]]]))
    _iss["blocks"] = _new
    _iss["most_wanted"] = [prod(k, k) for k in MOST_WANTED[_iss["slug"]]]
