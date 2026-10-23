# Subscription backgrounds

One background for every subscription product image. The card in the middle changes per product (1 month, 3 months, 6 months, 12 months, renewal); the background stays the same.

- **AZ TV** (regular): white accent, white logo.
- **AZ TV Plus**: gold `#EACF69` accent, gold logo, 4K badge.

Two directions to choose from:

| | Option A: diagonal shards | Option B: spotlight burst |
|---|---|---|
| Idea | The old images' look, redrawn: dark top, one diagonal band (white or gold) with broken shards, same geometry for both tiers. | Black stage, jagged rays (the "angles" motif of the cards) bursting from behind the card, soft glow, lit floor line under the card. |
| Preview | `compare-option-a.webp` | `compare-option-b.webp` |

Each preview: top row empty backgrounds, bottom row with the current 6-month cards dropped in.

## Layout (1000 x 1000 canvas, exported at 2000 x 2000)

- Card area: x 280-720, y 150-900, corner radius 40 (the same place as in the old images, so the existing cards fit). `export/*-guide.jpg` shows it.
- Logo top centre, vertical AZTVSTORE on both sides, contact pills (WhatsApp 966509130883, AZTVSTORE.COM) at the bottom, 4K badge top right on Plus.

## Files

- `backgrounds.html`: the source. Open it with `?opt=a|b&tier=regular|plus`, add `&guide=1` for the card area or `&card=<png>` for a mock-up.
- `render.cjs`: exports everything (`node render.cjs`, needs Playwright).
- `export/`: final backgrounds, 2000 x 2000 PNG.
- `mockups/`: backgrounds with the old 6-month cards (cut from the old images, edges are approximate).
- `src/`: logo (gold and white), font, cut-out old cards.
