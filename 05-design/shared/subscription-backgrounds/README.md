# Subscription backgrounds

One background for every subscription product image. The card in the middle changes per product (1 month, 3 months, 6 months, 12 months, renewal); the background stays the same.

- **AZ TV** (regular): white accent, white logo.
- **AZ TV Plus**: gold `#EACF69` accent, gold logo, 4K badge.

Two directions to choose from (dropped on 2026-10-23: Option A diagonal shards, too busy; Option C halo, too quiet):

| | Option B: spotlight burst | Option D: stadium night |
|---|---|---|
| Idea | Black stage, jagged rays (the "angles" motif of the cards) bursting from behind the card, soft glow. Approved by the client. | Match night: two floodlight towers with a broadcast lens flare cross their beams behind the card, camera flashes in the stands, halfway line and centre circle on the pitch under the card. |
| Preview | `compare-option-b.webp` | `compare-option-d.webp` |

Each preview: top row empty backgrounds, bottom row with the current 6-month cards dropped in.

## Layout (1000 x 1000 canvas, exported at 2000 x 2000)

- Card area: x 310-690, y 204-852 (380 x 648), corner radius 35. Same proportions as the current cards, a little smaller than in the old images. `export/*-guide.jpg` shows it.
- Logo top centre, vertical AZTVSTORE on both sides, contact pills (WhatsApp 966509130883, AZTVSTORE.COM) at the bottom, 4K badge top right on Plus.

## Files

- `backgrounds.html`: the source. Open it with `?opt=b|d&tier=regular|plus`, add `&guide=1` for the card area or `&card=<png>` for a mock-up.
- `render.cjs`: exports everything (`node render.cjs`, needs Playwright).
- `export/`: final backgrounds, 2000 x 2000 PNG.
- `mockups/`: backgrounds with the old 6-month cards (cut from the old images, edges are approximate).
- `src/`: logo (gold and white), font, cut-out old cards.
