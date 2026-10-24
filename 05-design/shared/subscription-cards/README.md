# Subscription cards

The card in the middle of every subscription product image. The background around it is in `../subscription-backgrounds/` (approved: B and E); the card changes per product, the background stays the same.

**Status (2026-10-23): card backgrounds done, per-card content not started.** Our first-round cards were rejected and removed (they remain in git history). The tasks are in the workspace tab «قائمة المهام», group «إعادة تصميم بطاقات الاشتراك», from `05-design/todo.json`.

## Card backgrounds (2026-10-23)

What every card shares before its title, photos and duration go on. One per style, 760 x 1296, transparent rounded corners (radius 70) and a transparent hanger slot at the top, so they drop straight into the card area of the approved backgrounds.

- **AZ TV** `bg/card-bg-aztv.png`: white card, bold black zigzag burst (the old cards' black and white pattern, redrawn clean with the same jagged ray as the product background), fading to a light floor for the duration and platform logos. Black side tabs with AZTVSTORE.
- **AZ TV Plus** `bg/card-bg-aztv-plus.png`: black card with a warm gold glow, gold frame, two clean gold corner shards (top right, bottom left), faint gold burst and gold dust. Gold side tabs with AZTVSTORE.
- `bg/*-guide.png`: where the per-card content goes (title, photos, duration, platform logos). `bg/*.webp`: light copies for the workspace.
- `bg/mockups/`: each card background, blank, on approved backgrounds B (`bg-*`) and E (`option-e-*`). `preview.webp`: all four.
- Source `card-background.html` (`?tier=regular|plus`, `&guide=1`), export `node render-card-bg.cjs` (needs Playwright).

## The ten cards

| # | Card | Product | Price today | Style | Old card | New card |
|---|---|---|---|---|---|---|
| 1 | عز تي في سنة + ٣ شهور | p930436127 | 96 SAR (was 238) | AZ TV, black and white | `old/aztv-15m.png` | `new/aztv-15m.png` |
| 2 | اشتراك عز تي في 6 شهور | p1133679038 | 69 SAR (was 150) | AZ TV, black and white | `old/aztv-6m.png` | `new/aztv-6m.png` |
| 3 | اشتراك عز تي في 3 شهور | p527896233 | 39 SAR (was 100) | AZ TV, black and white | `old/aztv-3m.png` | `new/aztv-3m.png` |
| 4 | اشتراك عز تي في شهر | p264351896 | 24 SAR (was 50) | AZ TV, black and white | `old/aztv-1m.png` | `new/aztv-1m.png` |
| 5 | اشتراك عز تي في بلس سنة | p331255752 | 196 SAR (was 300) | Plus, gold | `old/plus-12m.png` | `new/plus-12m.png` |
| 6 | عز تي في بلس سنة (جهازين) | p1669484767 | 400 SAR (was 500) | Plus, gold | `old/plus-12m-2dev.png` | `new/plus-12m-2dev.png` |
| 7 | اشتراك عز تي في بلس 6 شهور | p1879371242 | 150 SAR | Plus, gold | `old/plus-6m.png` | `new/plus-6m.png` |
| 8 | اشتراك عز تي في بلس 3 شهور | p1024479901 | 100 SAR (was 150) | Plus, gold | `old/plus-3m.png` | `new/plus-3m.png` |
| 9 | تجديد اشتراك عز تي في العادي | p777133688 | not shown | AZ TV renewal | `old/renew-aztv.png` | `new/renew-aztv.png` |
| 10 | تجديد اشتراك عز تي في بلس | p287657453 | not shown | Plus renewal | `old/renew-plus.png` | `new/renew-plus.png` |

The normal package has no 12-month card: its longest is سنة + ٣ شهور (15 months), shown today as a 12-month card plus a free 3-month card. "سنة" (12 months) is a Plus card.

## Photos

The face photos for the cards (cut-outs on white, delivered in batches) are in `photos/originals/`; `photos/README.md` lists them. Not yet matched to the names in `card-stars.json`.

## Trial card (2026-10-24)

`new/aztv-6m.png` is the trial for the look of all ten cards: card 2 (اشتراك ٦ شهور, regular, black and white). A first trial on the Plus 1-year card was rejected and removed (it stays in git history). What changed: big close-up faces that fill the card from under the title to the bottom (player in front, star behind), the title in a black pill, real black and white instead of a warm tint, and the duration and logo pills sitting on the photos, as on the old cards.

Built from `card.html` (`?card=aztv-6m`; each card is one entry in `CARDS`) and exported with `node render-cards.cjs aztv-6m`. The portraits are stand-ins: star `stars/latest-roles/vertical/transparent/06-antony-starr-g20.png` and player photo 010 from `photos/originals/`, cut out with `photos/cutout-white.py` (output in `photos/transparent/`, needs `pip install scipy`). Who goes on which card is not decided yet.

`new/aztv-3m.png` (card 3, اشتراك ٣ شهور) is a second trial in the same layout with photo 009 as the star (behind, right) and player photo 005 in front: `node render-cards.cjs aztv-3m`.

Round 2 on both trials: portraits about 10% smaller, a small «AZ TV SUBSCRIPTION» line under the title, a soft white light at the burst centre (hides the knot of rays between the faces) and a light floor under the duration and logo pills.

## How we work

1. **Old:** `old/` holds each card as it is on the store today, cut out of its post and enlarged 4x (`cut-old-cards.py`). `old/all-cards.png` shows all ten.
2. **New:** start from the card background in `bg/` and design each card at **760 x 1296 px** (portrait, the card area of the approved backgrounds), PNG with transparent rounded corners, and save it in `new/` under the name in the table.
3. **Product image:** place the new card on the approved background (`../subscription-backgrounds/`, B or E, white for AZ TV, gold for Plus) and export the product image to `05-design/new-design/assets/img/products/prod-<id>.png` for Salla.
4. Mark the task done in `05-design/todo.json` and run `python3 05-design/new-design/build/sync_workspace.py`.
