# Subscription backgrounds

One background for every subscription product image. The card in the middle changes per product (1 month, 3 months, 6 months, 12 months, renewal); the background stays the same.

**Approved 2026-10-23: spotlight burst** (was "Option B"). Black stage, jagged rays (the "angles" motif of the cards) bursting from behind the card, soft glow. Other options (diagonal shards, halo, stadium) were rejected and removed; they remain in git history.

- **AZ TV**: white accent, white logo. `export/bg-aztv.png`
- **AZ TV Plus**: gold `#EACF69` accent, gold logo, 4K badge. `export/bg-aztv-plus.png`

Preview: `preview.webp` (top row the backgrounds, bottom row with the current 6-month cards).

## Also approved: Option E "split" (2026-10-23)

The old images' look, redrawn clean: black top, one light plane under a sharp diagonal (white for AZ TV, gold for Plus), the zigzag rays pressed into the plane tone on tone, one clean edge line. No loose shards, no grey strip (removed at the client's request). Same card area, logo, side text and contact pills as B. Both B and E are approved and saved; pick per use.

- Preview: `preview-option-e.webp`
- Files: `export/option-e-aztv.png`, `export/option-e-aztv-plus.png`, mock-ups `mockups/option-e-*-6m.jpg`
- Source: `backgrounds.html?opt=e&tier=regular|plus`

## Layout (1000 x 1000 canvas, exported at 2000 x 2000)

- Card area: x 310-690, y 204-852 (380 x 648; 760 x 1296 in the export), corner radius 35. Same proportions as the current cards. `export/*-guide.jpg` shows it.
- Logo top centre, vertical AZTVSTORE on both sides, contact pills (WhatsApp 966509130883, AZTVSTORE.COM) at the bottom, 4K badge top right on Plus.

## Files

- `backgrounds.html`: the source. Open it with `?opt=b|e&tier=regular|plus` (b is the default), add `&guide=1` for the card area or `&card=<png>` for a mock-up.
- `render.cjs`: exports everything (`node render.cjs`, needs Playwright).
- `export/`: final backgrounds (PNG) and card-area guides.
- `mockups/`: backgrounds with the old 6-month cards (cut from the old images, edges are approximate).
- `src/`: logo (gold and white), font, cut-out old cards.
