# Riche News: 30-day email plan (Oct 13 to Nov 7, 2026)

Goal: grow Klaviyo-attributed revenue from about 6.8% of Vie Riche store revenue to 20 to 30% ($15k to $24k per month at the current run rate).

Status: every email below is an unsent DRAFT in Klaviyo. Nothing is scheduled. Flow changes are recommendations only; no live flow was edited.

## 1. Diagnosis

Based on Klaviyo and Shopify data pulled Oct 9, 2026:

- **Email share is about 6.8% of revenue.** The gap to the target is roughly $10k to $18k per month.
- **Checkout abandonment is the biggest leak.** The current flow recovers about $540 a month against roughly $64k of started-but-unfinished checkouts.
- **Pixel-based flows (browse and cart) are set to manual,** so most site intent never triggers an email.
- **Winback shows zero conversions** in the reporting window.
- **Campaign click rate is about 0.5%.** The Klaviyo 2026 benchmark average is 1.69% (top 10%: 3.38%). The old layout was image-heavy and offer-led, with no recurring format.
- **Inventory is two-sided.**
  - CORE Hoodie Set is stocked deep (10 colors, XS to 3X) and needs demand.
  - Limited drops (God Particle, Spider, Snake Eyes, Swamp Monster, jerseys) sell through and are never restocked, which is a real scarcity story.
- **Site intent is concentrated.**
  - The most-carted items in the recent 300 cart adds are CORE (30), Mixmatch Arcangel (8), Archangel V Tee (8) and Reaper Hoodie (7).
  - The most-viewed items without matching checkouts are the Heavyweight Fleece Hoodie, the Washed Effect Hoodie, Mixmatch Arcangel, Rock & Roll Tee, Dragon Zip and Digiworld Zip.

## 2. The format: Riche News

Each email matches the Brand Exclusivity reference:

- cream page, Playfair masthead, one question as the headline;
- a data chart or stat block built from real store data;
- dark story cards, then product grids;
- the black RICHE footer with VR CORE / NEW ITEMS / ON SALE buttons, plus an Afterpay strip.

Every product image is clickable. Every link carries `utm_source=klaviyo&utm_medium=email&utm_campaign=rnXX_slug&utm_content=<block>`, so clicks can be read by block. Text is live HTML (not image-only), and each email is 15 to 22 KB, well under Gmail's 102 KB clip limit.

Source: `build.py` (blocks and layout) and `issues.py` (content). Run `python3 build.py` to rebuild `out/`.

## 3. Calendar (3 sends per week: Tue, Thu, Sat)

| # | Send | Theme | Focus | Subject |
|---|---|---|---|---|
| 01 | Tue 10/13 | New site live | Launch, CORE tease | Riche News: we rebuilt everything |
| 02 | Thu 10/15 | CORE winter math | CORE | Is one set enough for the whole winter? |
| 03 | Sat 10/17 | Sell-out report | Never-restocked items | How fast does limited actually sell out? |
| 04 | Tue 10/20 | What is in everyone's cart | Cart abandonment | What is sitting in everyone's cart? |
| 05 | Thu 10/22 | Most viewed, not bought | Browse abandonment | Everyone's looking. Nobody's checking out. |
| 06 | Sat 10/24 | Halloween edit | Seasonal, low-stock graphics | Who dresses scarier: you or your costume? |
| 07 | Tue 10/27 | CORE family | CORE + Kids CORE | Does the family that matches stay together? |
| 08 | Thu 10/29 | Jacket set index | High-AOV sets | Why is the $190 set outselling everything? |
| 09 | Sat 10/31 | Halloween last call | Seasonal urgency | Still no fit for tonight? |
| 10 | Tue 11/3 | CORE color vote | CORE engagement | Vote: which CORE color wins November? |
| 11 | Thu 11/5 | Gone forever | Sell-outs, what remains | Gone forever: what you missed in October |
| 12 | Sat 11/7 | BFCM early access | List building for BFCM | Do you want in before everyone else? |

Audience for all sends: engaged segments (QVqxML, R2Tfci, TKSfnM, UVh6gD, VFF9GA, WHGXM8, S6PnFC), excluding XgG26H. Smart Sending is on. Klaviyo IDs are in `klaviyo_ids.md`.

### Before each send

1. **Refresh stock tags** ("Almost gone", "Last sizes", "Low stock") against Shopify inventory on send day. Remove any item that has sold out, or move it into issue 11.
2. **Narrow 09 to clickers of 06** if the segment is large enough (recommended; 09 is a last call).
3. **Build two segments from click data:**
   - for 10, a "clicked `vote_*` in rn10" segment, so the result can be published in the next issue;
   - for 12, a "clicked `bfcm_optin`" segment as the BFCM early-access list.

   The copy in 12 promises early access, so that list must actually get it.
4. **Review the old drafts dated 10.11, 10.13 and 10.15.** They overlap this calendar. Danny should decide whether to archive them. They were not deleted.

## 4. Flow fixes (recommendations, not changed)

Flows earn about 41% of email revenue from about 5% of sends (Klaviyo benchmarks). These carry most of the gap to 20 to 30%.

| Priority | Flow | Recommendation | Metric to watch |
|---|---|---|---|
| 1 | Checkout abandonment | First email at 30 to 60 minutes (not hours). Show cart contents with live stock: "Your size is one of the last". Then send #2 at 24h and #3 at 48h. Use the Riche News styling. | Recovery rate on Checkout Started; target $3k+/month vs about $540 now |
| 2 | Browse + cart abandonment (pixel) | Switch the manual pixel flows to live. 2 emails: product viewed or carted plus "Most wanted right now". | Revenue per recipient; placed order rate |
| 3 | Low stock / back in stock | Repair the Low Stock flow so people who viewed an item get "last sizes" when inventory drops below a threshold. | Click rate; sell-through on flagged SKUs |
| 4 | New: Sold out, gone forever | When a viewed item sells out, send "That one is gone for good. Here is the closest thing still standing." | Conversion from sold-out viewers |
| 5 | Winback | Rebuild with a "what you missed" format (the same structure as issue 11) at 60, 90 and 120 days. | Reactivation orders (currently 0) |
| 6 | Welcome | 3 to 4 emails covering the no-restock story, CORE and the best sellers, with the Riche News look. | Welcome placed order rate |

## 5. Test plan

Run one variable at a time. Judge on click rate, placed order rate and revenue per recipient, not opens.

| Test | Where | Variable | Success metric |
|---|---|---|---|
| Question headline vs statement | 02 vs 07 subjects | Subject format | Click rate |
| Data chart vs no chart | 03 / 04 / 05 | Chart block present | Click rate on chart thumbnails (`chart_*`) |
| Clickable thumbnails in charts | 03, 04, 05, 08 | `chart_*` vs `grid_*` clicks | Share of clicks |
| "Most wanted" strip | All | `strip_*` clicks | Footer and strip click share |
| Animated GIF hero (next step) | 1 send | Static vs GIF hero | Click rate, RPR |

### Month-end targets

| Metric | Current | Target |
|---|---|---|
| Campaign click rate | 0.5% | 1.5%+ |
| Checkout flow monthly revenue | about $540 | $3k+ |
| Email share of revenue | 6.8% | 15% (month 1), then 20 to 30% |

## 6. Next upgrades offered

- An animated GIF hero (frame 1 must be a complete static message for Outlook).
- Universal Content blocks for the footer and "Most wanted" strip, so one edit updates every template.

## Sources

- Klaviyo email benchmarks (2026): https://www.klaviyo.com/marketing-resources/email-benchmarks
- eightx, darkroom and redefineweb on DTC send cadence and flow share
- Attribuly ecommerce email playbook
- Vie Riche Shopify and Klaviyo data pulled Oct 9, 2026 (events: Placed Order, Checkout Started, Added to Cart, Viewed Product)
