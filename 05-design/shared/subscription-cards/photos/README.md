# Card photos

The photos for the subscription cards (football players and series/film stars; see `../card-stars.json` for who is planned on which card and `../README.md` for the cards). Photos arrive in batches. Each batch goes in `originals/` untouched, numbered in the order received.

## Folders

- `originals/`: files exactly as supplied. Never edit them.
- `transparent/`: cut-outs of `originals/` as PNG with a transparent background, made with `python3 cutout-white.py originals/<file>` (needs `pip install scipy`). Add `--holes 5000` when white shows through enclosed gaps (arms on hips, hands behind the back); used for 011.
- `web/`: created when we start the cards. Web versions (WebP, one size per card slot, transparent background) made from `originals/`.

## Rejected

`rejected/` holds the photos the client marked as not usable (2026-10-24): 001, 007, 008, and the latest-roles stars S01, S02, S04, S05, S06, S07, S08 (moved from `../stars/latest-roles/vertical/`, renamed with their S id). Same layout as here (`originals/`, `transparent/`). Never put them on a card.

## Naming

`NNN-short-description.ext`, where `NNN` continues from the last number (001, 002, ...). Describe what is visible (kit, pose), not who it is.

## Received

| # | File | Size | Notes |
|---|---|---|---|
| 001 | ~~`001-argentina-kit-10.jpg`~~ rejected | 896×1194 | Looking up, light-blue and white kit, captain's armband |
| 002 | `002-man-black-coat.jpg` | 1755×2000 | Bald, grey beard, black wool coat, looking over shoulder |
| 003 | `003-real-madrid-white-kit.jpg` | 896×1200 | White kit, pointing up |
| 004 | `004-barcelona-captain.jpg` | 896×1200 | Blue and garnet kit, captain's armband, arms crossed |
| 005 | `005-man-city-sky-blue-kit.jpg` | 896×1200 | Sky-blue kit, fists clenched, smiling |
| 006 | `006-yellow-navy-kit-captain.jpg` | 896×1200 | Smiling, yellow kit with navy trim, captain's armband, running |
| 007 | ~~`007-argentina-kit-10-jumping.jpg`~~ rejected | 896×1194 | Full body, mid-jump, light-blue kit and black shorts, captain's armband |
| 008 | ~~`008-man-long-hair-dark-coat-chair.jpg`~~ rejected | 896×1195 | Long hair, dark period coat, seated in a wooden chair |
| 009 | `009-man-straw-hat-pinstripe-suit.jpg` | 928×1133 | Straw boater hat, glasses, moustache, pinstripe suit, holding a chocolate bar |
| 010 | `010-barcelona-curly-hair-crossed-fingers.jpg` | 1500×2000 | Curly hair, Barcelona kit, tongue out, hands crossed on chest |
| 011 | `011-light-blue-kit-hands-behind-back.jpg` | 2000×2000 | Square studio portrait, royal-blue kit with white collar, hands behind back, looking at camera; white background, not a tight cut-out |
| 012 | `012-red-blue-spider-suit.png` | 540×740 | Red and blue spider suit, head tilted, looking at camera; already transparent (small file, fine at card size) |
| 013 | `013-blue-suit-eagle-shoulder-cape.webp` | 1350×1687 | Blue patterned suit, silver eagle on the shoulder, red cape, slicked hair; already transparent |
| 014 | `014-bald-khaki-shirt-gloves.webp` | 1126×1397 | Bald, khaki short-sleeved shirt open at the neck, fingerless black gloves, cargo trousers; white background |
| 015 | `015-flat-cap-long-coat-scar.webp` | 873×1802 | Flat cap, scar on the cheek, long dark wool coat, red tie, looking over the shoulder; white background |
| 016 | `016-man-tuxedo-456-badge.webp` | 806×980 | Dark hair, black tuxedo with bow tie, red X and «456» badges, dishes at the bottom edge; already transparent (supplied with an alpha channel) |

Batches 1 (001-005), 2 (006-009), 3 (010-011), 4 (012-013, already transparent: copied to `transparent/` as PNG without cutting) and 5 (014-015) and 6 (016, already transparent). More images to come.

## To check before the cards are built

- All eleven are cut-outs on a **white** background (JPG, no transparency). The site is dark, so the cards need a transparent version (PNG/WebP) or the images will show a white box.
- Sizes differ (001-009 are about 896×1200 except 002 at 1755×2000 and 009 at 928×1133; 010 is 1500×2000; 011 is square 2000×2000). Crop to one aspect ratio per card slot when making `web/`.
- Rights: the photos show real people and club kits. Confirm they are licensed for the store before launch.
