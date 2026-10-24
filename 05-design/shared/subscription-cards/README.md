# Subscription cards

The card in the middle of every subscription product image. The background around it is in `../subscription-backgrounds/` (approved: B and E); the card changes per product, the background stays the same.

**Status (2026-10-24): card 3 (`new/aztv-3m.png`, اشتراك ٣ شهور) accepted as the look for all cards. Cards 5, 7 and 8 (Plus 1 year, Plus 6 months, Plus 3 months) were rejected by the client and are now redone with new photos: 8 with 016, 5 with 017 and 018, 7 with 020 and 014. All wait for review (overview `new/all-cards.jpg`).**

Cards 2, 5, 7 and 8 were rebuilt (2026-10-24): card 5 with the new photos 017 and 018, card 7 with 020 and 014, card 8 with 021 and 016, card 2 with 022 and 013. The client marked ten photos as not usable: 001, 007, 008 and the stars S01, S02, S04, S05, S06, S07, S08. They are kept in `photos/rejected/` (`originals/` and `transparent/`, stars renamed with their S id) and must not be used on any card. Still free to use: 003, 010, 011 (hands behind his back), 012, 019 and S03 (003 and 012 were on the removed card 1).

`photos/all-photos.jpg` (`python3 photo-sheet.py`) shows every usable face photo with its id (001-015 card photos, S01-S08 latest-roles stars) and the card it is on, so the client can say which photos to drop. Our first-round cards were rejected and removed (they remain in git history). The tasks are in the workspace tab «قائمة المهام», group «إعادة تصميم بطاقات الاشتراك», from `05-design/todo.json`.

## Actor behind: no early fade (2026-10-24)

The client said the second person (the actor behind) faded out too early, so the burst showed through his body. The actors on cards 2, 3, 5, 6 and 8 now stay solid down to the floor and the pills and fade only in the last few percent (`fadeBottom: [86-92, 100]` in `card.html`, under the floor gradient). Two photos were too short to get there and were enlarged a little: 002 on card 6 (it ended at y 455, now 560) and 016 on card 8 (it ended at y 493, now 545; its dishes at the bottom stay hidden under the floor, and the «456» badge is kept clear of the right side tab). Rule for a new actor photo: it must reach y 560 or more on the 648 px card.

## Players changed on cards 2 and 8 (2026-10-24)

The client asked to change the player on card 2 and to fix card 8, where the player had no visible hands. After two tries with the photos we had (003 with a raised arm, which forced a mirrored card, and 010, the same player as card 7), the client sent two new player photos, already transparent:

- **021** (white Real Madrid kit, arms crossed over the chest, smiling; 488 x 650, small, so it is used at the card's size with no more enlargement) is now the player on **card 8** (`plus-3m`), in front of the actor 016. It is darkened a little (`lift: .9`) so the white kit does not wash out into the gold.
- **022** (red Bayern kit, looking up, one hand hanging; 895 x 1608) is now the player on **card 2** (`aztv-6m`), in front of the actor 013. The card is back to the normal layout (player front left, actor behind right).
- Not used on any card now: 003, 010 (the same player as 020 on card 7, so he is no longer repeated), 011 (hands behind his back).
- Seven cards, seven players: 022, 005, 004, 017, 006, 020, 021. No repeats.

## Plus design: the AZ TV card in gold (chosen 2026-10-24)

The client chose **option F** from the Plus options and it is now the design of all five Plus cards (5, 6, 7, 8, 10). It is the layout of the AZ TV card, recoloured:

- Flat gold card, the bold black zigzag burst running up to the top behind the title, a gold floor for the pills (`bg/card-bg-aztv-plus.png`).
- The card name in gold on a black title pill, the package line under it with a gold «AZ TV PLUS» chip.
- Black and white photos, a light gold glow at the burst centre.
- Black pills with gold text (duration, logos, the two-device badge); black side tabs with gold letters.
- No header cap, no frame, no diagonal split.

The other options (the gold card with a black header cap, the black-card options, the diagonal split, the gold disc, the screen) were dropped and their files removed; they are in the git history.

**beIN logo on every card (2026-10-24):** the outline beIN SPORTS logo the client supplied («bein» with «SPORTS» under it, one colour) replaces the old beIN logo in the logo strip of all nine cards, regular and Plus (`LOGOS` in `card.html`). It is shown white like the other logos, so the strip stays black and white (`05-design/new-design/assets/img/logos/bein-sports-outline.svg`; original in `05-design/sections/02-platform-logos/originals/`).

**Logo balance (2026-10-24):** the four logos are sized for the same visual weight, not the same height: Netflix 56 px wide, SSC 50, beIN 50 (it has two lines, so it is taller), Shahid 56 (`LOGOS` in `card.html`), with equal gaps. Before, Netflix was the biggest and SSC the smallest, and beIN stood out.

## History: earlier Plus designs (2026-10-24)

Everything from here to «How we work» describes earlier Plus looks (the gold card with a black header cap, the header cap itself, the black Plus card with gold dust and warm portraits). The design in use is the one above.

### AZ TV Plus, gold card with a header cap

The client asked for a new Plus design, and then for the AZ TV cards to go back to their old design (black title pill, rays up to the top, white card with no frame; the header cap below was tried on them and dropped). So only Plus has the new look: the AZ TV burst in gold, with a black header cap:

- Flat gold card and gold frame, with the same bold black zigzag burst as the AZ TV card (`bg/card-bg-aztv-plus.png`).
- Black header cap with the card name in gold; black side tabs with gold letters.
- Black and white photos (the same tone as AZ TV), a light gold glow at the burst centre and a gold floor under the pills.
- Black pills with gold text (duration, logos, the two-device badge); the package line has a gold «AZ TV PLUS» chip and a gold ring.
- Gone from the old Plus look: the black card, the gold dust, the corner shard and the warm sepia photos.

The older Plus notes below (black card, gold dust, warm portraits) are history.

### Header cap (Plus only, dropped)

The client did not like the top of the card, where the background ran into the card name. The header cap below was made for all cards; the AZ TV cards went back to their old top afterwards, so it is now on the Plus cards only (black cap, gold name):

- A flat **header cap** across the top of the card, black on AZ TV and gold on Plus, with a gently curved lower edge (sides at y 118, centre at y 132 on the 380 x 648 card). The card name is plain text on it (white on black, black on gold), with no pill of its own.
- Nothing reaches the cap: the top-right gold shard is gone, the rays and gold dust fade out before the cap, and the photos are clipped under its edge (`.photos` clip-path in `card.html`, same curve).
- The package line sits on the cap's edge as a badge, ringed in the card colour.
- The left side tab moved down (y 168 to 336) so it no longer touches the cap.
- In `card.html` the base styles are the AZ TV top (title pill, package line at y 114, no photo clip); the `.plus` rules add the cap layout.

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
| 2 `aztv-6m` | 022 (new, 2026-10-24) | 013 |
| 3 `aztv-3m` | 005 | 009 |
| 4 `aztv-1m` | 004 | 015 |
| 5 `plus-12m` | 017 | 018 (new, 2026-10-24) |
| 6 `plus-12m-2dev` | 006 | 002 |
| 7 `plus-6m` | 020 (new, 2026-10-24) | 014 |
| 8 `plus-3m` | 021 (new, 2026-10-24) | 016 (new, 2026-10-24) |

Numbers are the photos in `photos/` (cut-outs in `photos/transparent/`); stars are in `stars/latest-roles/vertical/transparent/`. Pairs follow `card-stars.json` where we have the photo; where we don't have that photo yet (Mbappé, Vinícius and Neymar among the players; Kit Harington, Bryan Cranston and others appear in the new photos instead), the closest photo we have stands in. Card 4 is a player (004) in front and an actor (015) behind; 014 was tried in front but the client wants one player and one actor on every card. Cards 5 and 7 follow the proportions of card 3 (pairs swapped on 2026-10-24 after the client's review): card 5 is player 017 in front of the cowboy-hat actor 018, the same pairing as card 3 (fists-clenched player, actor in a hat); the hat limits the actor's face to about 98 px so the brim stays inside the card and below the package line, and 017 fades out at the bottom because the photo ends at the thighs. Card 7 is player 020 in front of the bald actor 014 in the khaki shirt (the client asked to change the actor; 019 is now unused): he stands upright, his light shirt balances the player's dark kit, and the photo runs to the knees, so it reaches the bottom of the card with no fade. 020 looks like the same player as 010 on card 2: swap one if the client wants no repeats. 012 and 013 replaced 008 (card 5) and the dark star `06` (card 2) at the client's request. Photo 011 was cut out with `--holes 5000` to clear the white gaps between the arms and the body.

## How we work

1. **Old:** `old/` holds each card as it is on the store today, cut out of its post and enlarged 4x (`cut-old-cards.py`). `old/all-cards.png` shows all ten.
2. **New:** start from the card background in `bg/` and design each card at **760 x 1296 px** (portrait, the card area of the approved backgrounds), PNG with transparent rounded corners, and save it in `new/` under the name in the table.
3. **Product image:** place the new card on the approved background (`../subscription-backgrounds/`, B or E, white for AZ TV, gold for Plus) and export the product image to `05-design/new-design/assets/img/products/prod-<id>.png` for Salla.
4. Mark the task done in `05-design/todo.json` and run `python3 05-design/new-design/build/sync_workspace.py`.
