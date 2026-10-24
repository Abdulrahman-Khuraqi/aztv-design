# Subscription cards

The card in the middle of every subscription product image. The background around it is in `../subscription-backgrounds/` (approved: B and E); the card changes per product, the background stays the same.

**Status (2026-10-24): card 3 (`new/aztv-3m.png`, اشتراك ٣ شهور) accepted as the look for all cards. Cards 5, 7 and 8 (Plus 1 year, Plus 6 months, Plus 3 months) were rejected by the client and are now redone with new photos: 8 with 016, 5 with 017 and 018, 7 with 020 and 014. All wait for review (overview `new/all-cards.jpg`).**

Cards 5 and 7 were rebuilt (2026-10-24): card 5 with the new photos 017 and 018, card 7 with the new photo 020 and 014; card 8 with 016. The client marked ten photos as not usable: 001, 007, 008 and the stars S01, S02, S04, S05, S06, S07, S08. They are kept in `photos/rejected/` (`originals/` and `transparent/`, stars renamed with their S id) and must not be used on any card. Still free to use: 003, 012, 019 and S03 (003 and 012 were on the removed card 1).

`photos/all-photos.jpg` (`python3 photo-sheet.py`) shows every usable face photo with its id (001-015 card photos, S01-S08 latest-roles stars) and the card it is on, so the client can say which photos to drop. Our first-round cards were rejected and removed (they remain in git history). The tasks are in the workspace tab «قائمة المهام», group «إعادة تصميم بطاقات الاشتراك», from `05-design/todo.json`.

## AZ TV Plus, new design (2026-10-24)

The client kept the new AZ TV card and asked for a new Plus design. Plus is now the AZ TV card in gold, so the two tiers read as one family:

- Flat gold card and gold frame, with the same bold black zigzag burst as AZ TV (`bg/card-bg-aztv-plus.png`).
- Black header cap with the card name in gold; black side tabs with gold letters.
- Black and white photos (the same tone as AZ TV), a light gold glow at the burst centre and a gold floor under the pills.
- Black pills with gold text (duration, logos, the two-device badge); the package line has a gold «AZ TV PLUS» chip and a gold ring.
- Gone from the old Plus look: the black card, the gold dust, the corner shard and the warm sepia photos.

The older Plus notes below (black card, gold dust, warm portraits) are history.

## Header cap (2026-10-24)

The client did not like the top of the card, where the background ran into the card name (the gold corner shard on Plus, the black rays on AZ TV). New top for all cards:

- A flat **header cap** across the top of the card, black on AZ TV and gold on Plus, with a gently curved lower edge (sides at y 118, centre at y 132 on the 380 x 648 card). The card name is plain text on it (white on black, black on gold), with no pill of its own.
- Nothing reaches the cap: the top-right gold shard is gone, the rays and gold dust fade out before the cap, and the photos are clipped under its edge (`.photos` clip-path in `card.html`, same curve).
- The package line sits on the cap's edge as a badge, ringed in the card colour.
- The AZ TV card has a white frame (as Plus has its gold one), so the black cap does not merge with the dark top of the product backgrounds.
- The left side tab moved down (y 168 to 336) so it no longer touches the cap.

## Card backgrounds (2026-10-23)

What every card shares before its title, photos and duration go on. One per style, 760 x 1296, transparent rounded corners (radius 70) and a transparent hanger slot at the top, so they drop straight into the card area of the approved backgrounds.

- **AZ TV** `bg/card-bg-aztv.png`: white card, bold black zigzag burst (the old cards' black and white pattern, redrawn clean with the same jagged ray as the product background), fading to a light floor for the duration and platform logos. Black side tabs with AZTVSTORE.
- **AZ TV Plus** `bg/card-bg-aztv-plus.png`: black card with a warm gold glow, flat gold frame (no gradient, no inner line), two flat gold corner shards (top right, bottom left), faint gold burst and gold dust. Gold side tabs with AZTVSTORE.
- `bg/*-guide.png`: where the per-card content goes (title, photos, duration, platform logos). `bg/*.webp`: light copies for the workspace.
- `bg/mockups/`: each card background, blank, on approved backgrounds B (`bg-*`) and E (`option-e-*`). `preview.webp`: all four.
- Source `card-background.html` (`?tier=regular|plus`, `&guide=1`), export `node render-card-bg.cjs` (needs Playwright).

## The nine cards (card 1 was removed by the client: there is no «سنة + ٣ شهور» card; the other numbers stay as they are)

| # | Card | Product | Price today | Style | Old card | New card |
|---|---|---|---|---|---|---|
| ~~1~~ | ~~عز تي في سنة + ٣ شهور~~ removed | | | | `old/aztv-15m.png` (kept as reference) | |
| 2 | اشتراك عز تي في 6 شهور | p1133679038 | 69 SAR (was 150) | AZ TV, black and white | `old/aztv-6m.png` | `new/aztv-6m.png` |
| 3 | اشتراك عز تي في 3 شهور | p527896233 | 39 SAR (was 100) | AZ TV, black and white | `old/aztv-3m.png` | `new/aztv-3m.png` |
| 4 | اشتراك عز تي في شهر | p264351896 | 24 SAR (was 50) | AZ TV, black and white | `old/aztv-1m.png` | `new/aztv-1m.png` |
| 5 | اشتراك عز تي في بلس سنة | p331255752 | 196 SAR (was 300) | Plus, gold | `old/plus-12m.png` | `new/plus-12m.png` |
| 6 | عز تي في بلس سنة (جهازين) | p1669484767 | 400 SAR (was 500) | Plus, gold | `old/plus-12m-2dev.png` | `new/plus-12m-2dev.png` |
| 7 | اشتراك عز تي في بلس 6 شهور | p1879371242 | 150 SAR | Plus, gold | `old/plus-6m.png` | `new/plus-6m.png` |
| 8 | اشتراك عز تي في بلس 3 شهور | p1024479901 | 100 SAR (was 150) | Plus, gold | `old/plus-3m.png` | `new/plus-3m.png` |
| 9 | تجديد اشتراك عز تي في العادي | p777133688 | not shown | AZ TV renewal | `old/renew-aztv.png` | `new/renew-aztv.png` |
| 10 | تجديد اشتراك عز تي في بلس | p287657453 | not shown | Plus renewal | `old/renew-plus.png` | `new/renew-plus.png` |

The normal package has no 12-month card and, as the client says, no «سنة + ٣ شهور» card either: its longest is 6 months. "سنة" (12 months) is a Plus card.

## Photos

The face photos for the cards (cut-outs on white, delivered in batches) are in `photos/originals/`; `photos/README.md` lists them. Not yet matched to the names in `card-stars.json`.

## Trial card (2026-10-24)

(History.) `new/aztv-6m.png` was the trial for the look of all ten cards: card 2 (اشتراك ٦ شهور, regular, black and white). A first trial on the Plus 1-year card was rejected and removed (it stays in git history). What changed: big close-up faces that fill the card from under the title to the bottom (player in front, star behind), the title in a black pill, real black and white instead of a warm tint, and the duration and logo pills sitting on the photos, as on the old cards.

Built from `card.html` (`?card=aztv-6m`; each card is one entry in `CARDS`) and exported with `node render-cards.cjs aztv-6m`. The portraits are stand-ins: star `stars/latest-roles/vertical/transparent/06-antony-starr-g20.png` and player photo 010 from `photos/originals/`, cut out with `photos/cutout-white.py` (output in `photos/transparent/`, needs `pip install scipy`). Who goes on which card is not decided yet.

`new/aztv-3m.png` (card 3, اشتراك ٣ شهور) is a second trial in the same layout with photo 009 as the star (behind, right) and player photo 005 in front: `node render-cards.cjs aztv-3m`.

Round 2 on both trials: portraits about 10% smaller, a small «AZ TV SUBSCRIPTION» line under the title, a soft white light at the burst centre (hides the knot of rays between the faces) and a light floor under the duration and logo pills.

## All nine cards (2026-10-24)

Built from `card.html` in the accepted look of card 3, with the card photos 001-011 and the stars from `stars/latest-roles/`. Export all: `node render-cards.cjs` (or one: `node render-cards.cjs plus-6m`). Then `python3 contact-sheet.py` rebuilds the overview `new/all-cards.jpg`, each card with its number from the table above and its name, for review with the client.

- **AZ TV cards** (white): as card 3, unchanged.
- **AZ TV Plus cards** (`plus: true`): the black and gold card background, gold title pill with black text, gold «AZ TV PLUS SUBSCRIPTION» line, warm gold-toned portraits, a bright warm light at the burst centre (hides where the rays meet behind the faces), a dark floor, black duration and logo pills with a gold edge.
- **Renewal cards** (`renew: true`): no faces; three renewal arrows in a black disc at the burst centre (white on AZ TV, gold on Plus).
- **Package line** under the title (all cards, 2026-10-24): a black pill (no side lines) with the package name in a chip, «AZ TV» (white chip) or «AZ TV PLUS» (gold chip), then «SUBSCRIPTION», or «RENEWAL» on the renewal cards. Replaces the small spaced-out «AZ TV SUBSCRIPTION» line, which was hard to read.
- **Plus, kept flat (2026-10-24, client: too much going on):** solid gold everywhere, no gradients, outlines or shadows. Flat black background with faint flat gold rays and a few specks of dust, no grain. The package line is the same pill as on the regular cards (dark grey pill, gold «AZ TV PLUS» chip, «SUBSCRIPTION» beside it), without an outline. The duration and logo pills are dark grey with no border, the title pill is flat gold, and the centre light is softer.
- **Light on dark photos:** a photo can take `gamma` (below 1 opens the shadows of a dark face without blowing out the highlights; it also trims 1 px off the cut-out edge so no light fringe shows) next to `lift` (overall brightness). Used on cards 7 and 8, where the client found the faces too dark.
- **Two devices** (card 6): a «جهازين · 2 DEVICES» badge with a two-screens icon above the duration (`badge`); the white kit toned down and the man behind lit and enlarged so the two faces match.
- **Card backgrounds** (2026-10-24): the AZTVSTORE letters are centred on the visible part of each side tab (the tabs run 6 px past the card edge); the Plus frame, corner shards and tabs are flat gold, with no inner line.

| Card | Player (front) | Star (behind) |
|---|---|---|
| 2 `aztv-6m` | 010 | 013 |
| 3 `aztv-3m` | 005 | 009 |
| 4 `aztv-1m` | 004 | 015 |
| 5 `plus-12m` | 017 | 018 (new, 2026-10-24) |
| 6 `plus-12m-2dev` | 006 | 002 |
| 7 `plus-6m` | 020 (new, 2026-10-24) | 014 |
| 8 `plus-3m` | 011 | 016 (new, 2026-10-24) |

Numbers are the photos in `photos/` (cut-outs in `photos/transparent/`); stars are in `stars/latest-roles/vertical/transparent/`. Pairs follow `card-stars.json` where we have the photo; where we don't have that photo yet (Mbappé, Vinícius and Neymar among the players; Kit Harington, Bryan Cranston and others appear in the new photos instead), the closest photo we have stands in. Card 4 is a player (004) in front and an actor (015) behind; 014 was tried in front but the client wants one player and one actor on every card. Cards 5 and 7 follow the proportions of card 3 (pairs swapped on 2026-10-24 after the client's review): card 5 is player 017 in front of the cowboy-hat actor 018, the same pairing as card 3 (fists-clenched player, actor in a hat); the hat limits the actor's face to about 98 px so the brim stays inside the card and below the package line, and 017 fades out at the bottom because the photo ends at the thighs. Card 7 is player 020 in front of the bald actor 014 in the khaki shirt (the client asked to change the actor; 019 is now unused): he stands upright, his light shirt balances the player's dark kit, and the photo runs to the knees, so it reaches the bottom of the card with no fade. 020 looks like the same player as 010 on card 2: swap one if the client wants no repeats. 012 and 013 replaced 008 (card 5) and the dark star `06` (card 2) at the client's request. Photo 011 was cut out with `--holes 5000` to clear the white gaps between the arms and the body.

## How we work

1. **Old:** `old/` holds each card as it is on the store today, cut out of its post and enlarged 4x (`cut-old-cards.py`). `old/all-cards.png` shows all ten.
2. **New:** start from the card background in `bg/` and design each card at **760 x 1296 px** (portrait, the card area of the approved backgrounds), PNG with transparent rounded corners, and save it in `new/` under the name in the table.
3. **Product image:** place the new card on the approved background (`../subscription-backgrounds/`, B or E, white for AZ TV, gold for Plus) and export the product image to `05-design/new-design/assets/img/products/prod-<id>.png` for Salla.
4. Mark the task done in `05-design/todo.json` and run `python3 05-design/new-design/build/sync_workspace.py`.
