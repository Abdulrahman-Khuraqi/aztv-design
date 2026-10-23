# Subscription backgrounds

One background for every subscription product image. The card in the middle changes per product (1 month, 3 months, 6 months, 12 months, renewal); the background stays the same.

- **AZ TV** (regular): white accent, white logo.
- **AZ TV Plus**: gold `#EACF69` accent, gold logo, 4K badge.

Two directions to choose from (Option A, the diagonal shards, was dropped on 2026-10-23: too busy):

| | Option B: spotlight burst | Option C: halo |
|---|---|---|
| Idea | Black stage, jagged rays (the "angles" motif of the cards) bursting from behind the card, soft glow. | Light falling from above through the logo onto the card, soft light shafts, two thin rings with a glowing top arc, a little dust in the beam. Calm but dramatic. |
| Preview | `compare-option-b.webp` | `compare-option-c.webp` |

Each preview: top row empty backgrounds, bottom row with the current 6-month cards dropped in.

## Layout (1000 x 1000 canvas, exported at 2000 x 2000)

- Card area: x 310-690, y 204-852 (380 x 648), corner radius 35. Same proportions as the current cards, a little smaller than in the old images. `export/*-guide.jpg` shows it.
- Logo top centre, vertical AZTVSTORE on both sides, contact pills (WhatsApp 966509130883, AZTVSTORE.COM) at the bottom, 4K badge top right on Plus.

## Files

- `backgrounds.html`: the source. Open it with `?opt=b|c&tier=regular|plus`, add `&guide=1` for the card area or `&card=<png>` for a mock-up.
- `render.cjs`: exports everything (`node render.cjs`, needs Playwright).
- `export/`: final backgrounds, 2000 x 2000 PNG.
- `mockups/`: backgrounds with the old 6-month cards (cut from the old images, edges are approximate).
- `src/`: logo (gold and white), font, cut-out old cards.
