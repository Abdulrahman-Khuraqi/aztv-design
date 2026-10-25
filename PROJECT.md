# AZ TV Store — New Store Design

Single source of truth for the redesign of [aztvstore.com](https://aztvstore.com/).
The visual version of this file is **Our Workspace**: [our workspace.html](our%20workspace.html). Keep the two in sync. Its tab «قائمة المهام» is the image to-do list (`05-design/todo.json`), and «ملفات التسليم» embeds every deliverable (refresh with `python3 05-design/new-design/build/sync_workspace.py`).

Last updated: 2026-10-24

## 1. Project in one paragraph

Redesign the AZ TV Store homepage (عز تي في) into a shorter, clearer page that is more focused on conversion, while keeping services easy to reach. The store runs on **Salla**, so every section must be buildable as a Salla theme block. We design the sections in the agreed order below, 01 to 17.

- Live store: https://aztvstore.com/
- Agreed plan, full original Arabic text: [01-brief/homepage-plan.md](01-brief/homepage-plan.md), also inside the workspace (tabs "الخطة" and "ملاحظات التصميم"). Work from these, not from the Google Doc.
- Original Google Doc (`AZTV_Homepage_New_Order_v3`), reference only: https://docs.google.com/document/d/1F0vgi7_V4gwE4v3klXzwdz6QhVmNvYYqwonBPe1vdEs/edit?tab=t.0
- Platform: Salla (Twilight theme engine)
- Theme: **ملاك (Malak)** by AfterAds, the name it has on Salla. In the code it is called `ANGEL` (v1.174.0).
- Language and direction: Arabic first, RTL

## 2. Brand

| Role | Hex | Use |
|---|---|---|
| Primary (gold) | `#EACF69` | Accent: buttons, highlights, key numbers. Use sparingly so it stays premium. |
| Secondary (black) | `#0D0D0D` | Page background. |
| Surface | `#1A1A1A` | Cards, raised blocks, alternating section bands. |

Rules agreed in the plan:

- Dark mode is the core identity of the site.
- Dark backgrounds with clear contrast for text and buttons.
- Gold `#EACF69` is the main accent, black `#0D0D0D` the main secondary colour.
- Keep clear space and do not overuse gold.

Contrast (WCAG): gold on `#0D0D0D` ≈ 12.6:1, gold on `#1A1A1A` ≈ 11.3:1, white on `#0D0D0D` ≈ 19.4:1. White text on gold fails (≈ 1.5:1), so text on gold buttons must be `#0D0D0D`.

Not decided yet: typeface (the current store uses `PingARLT`), supporting neutrals for text and borders.

## 3. Homepage order (agreed)

| # | Section | القسم | Content | On the store today |
|---|---|---|---|---|
| 01 | Hero | Hero Section | Short black-and-white background video (players + shows, series, TV content). Clear headline, short description of the service, CTA such as "تصفح الباقات" or "اشترك الآن". Video must be light and compressed for web. | Image slider. Changes to video. |
| 02 | Platform and channel logos | شعارات المنصات والقنوات | Available platforms and services (Netflix, beIN Sports, other channels) as a moving logo strip. | New |
| 03 | Main categories | التصنيفات الرئيسية | Quick access to: تجديد الاشتراك, AZ TV, AZ TV Plus, beIN Sports, AZ TV Box. | New (categories are only in the menu) |
| 04 | beIN world | عالم beIN | Devices, subscriptions, renewals. | Exists. To be redesigned. |
| 05 | AZ TV Box | AZ TV Box | The device and its features, shown clearly and directly. | Exists (featured product with countdown) |
| 06 | Season-start offers | عروض بداية الموسم | Top current offers and discounts, direct links to key offers and products. | Exists as "عروض اليوم الوطني" |
| 07 | AZ TV subscriptions | اشتراكات AZ TV | The basic AZ TV packages. | Exists, lower on the page. Moves up. |
| 08 | Supported apps and devices (AZ TV) | التطبيقات والأجهزة المدعومة | Apple, Android, Smart TV, Samsung. | Exists |
| 09 | Why our store | مميزات متجرنا | Fast activation, support, payment methods, device compatibility. | Exists |
| 10 | Testimonials | قالوا عن عز تي في | Customer ratings and reviews. Builds trust before the second package. | Exists |
| 11 | AZ TV Plus subscriptions | اشتراكات AZ TV Plus | AZ TV Plus packages and their key features. | Exists |
| 12 | Supported apps and devices (Plus) | التطبيقات والأجهزة المدعومة | Apple, Android, Smart TV, Samsung, LG. | Exists |
| 13 | AZ TV vs AZ TV Plus | مقارنة AZ TV وAZ TV Plus | Simple, clear comparison that helps the customer pick a package. | New |
| 14 | Second store offer | عرض متجرنا الثاني | "2 والثالث مجانًا". Promo banner leading to the second store. | Exists |
| 15 | For loyal customers | لعملائنا الأوفياء | Subscription renewal, offers or options for existing customers. | Exists |
| 16 | FAQ | الأسئلة الشائعة | Answers to the questions that could stop a customer from completing the order. | New |
| 17 | Final CTA | CTA نهائي | تصفح الباقات, اشترك الآن, جدد اشتراكك. | New |

### Proposal still open: one apps section instead of two

- Merge sections 08 and 12 into a single apps and devices section.
- Give it two clear buttons: "تفعيل AZ TV" and "تفعيل AZ TV Plus".
- Place access to activation after the AZ TV and AZ TV Plus subscription sections.
- Why: customers look for apps and activation after buying, not before. Less repetition makes the page shorter and keeps attention on the purchase decision. Competitor sites give apps little homepage space, some only link to them.
- Other places to reach activation: main menu, FAQ, categories and quick access, post-purchase page or message.

**Decision needed from the client:** keep 17 sections, or merge to 16.

## 4. Design and development notes (agreed)

- **Direction:** dark mode, gold accent, generous spacing.
- **Logo:** animated AZ TV logo. Preferably plays when the site opens, then settles without distracting the user.
- **beIN Sports section:** reorder and redesign. Use the beIN section on KoorPlanet as a visual and structural reference. Make devices, subscriptions and renewals clearer to browse.
- **Main menu:** review and fix the menu list. Fix the card that appears without an image.

## 5. Salla: what it means for the design

Confirmed from Salla's Twilight documentation and from the live store:

- The homepage is a stack of blocks the merchant enables and fills in the theme customizer. Built-in blocks are listed in the theme's `twilight.json`; custom blocks are declared there with their fields and built as Twig files.
- Product data, prices, discounts, countdowns, cart and reviews come from Salla (the store uses `salla-products-list`, `salla-products-slider`, `salla-count-down`, `salla-add-product-button`, `salla-rating-stars`).
- Cart and checkout belong to Salla. They are out of scope for the homepage design.

Design rules that follow:

1. Design every section as a block with editable fields (image, title, text, link, product or category picker). No one-off layouts that only work with one piece of content.
2. Design the product card once and reuse it everywhere products appear.
3. Arabic and RTL first. The header also carries a language and a currency switch.
4. The hero video needs a poster image, muted autoplay and a mobile fallback, and must stay small.

### The theme: ملاك (Malak) by AfterAds

On Salla the store uses the theme **ملاك**. Its code name is **ANGEL**, so the page and CSS say ANGEL; both names mean the same theme.

Read from the saved page: `<meta name="theme:name" content="ANGEL">`, `theme:developer` AfterAds, CSS `themes/1034648396/1.174.0/app.css`. (`salla-1130931637` on `<body>` is the store id, not the theme.) The AfterAds site is blocked from this work environment, so the block list below comes from the theme's own markup and CSS.

ANGEL blocks **in use on the homepage today**: hero slider (`s-block--hero-slider`, full width), section title / divider (`s-angel--divider`: title, subtitle, image or GIF, countdown, one button), banners (`s-block--banners`), featured product (`s-block--special-product`: product, features, countdown), products grid (`s-block--angel-products`), products slider (`s-block--best-offers`), categories / links slider (`s-block--categories`: image + title + link), store features (`s-block--features`), testimonials (`s-block--testimonials`).

ANGEL blocks **in the theme CSS but not used yet**: FAQ (`s-block--faqs`), moving strip (`angel-ad`, marquee with small images and text, pauses on hover), video in the hero slider (`responsive-video`, `video-swiper`), slider with background (`s-block--slider-with-bg`), stories (`angel-stories`, YouTube/TikTok), discount coupon (`angel-discountcoupon`).

**Build map: each section on ANGEL, with as little extra code as possible.**

| # | Section | ANGEL block | Extra code |
|---|---|---|---|
| 01 | Hero | Hero slider with a video slide | CSS. Headline and buttons over the video may not be a slider field: either bake them into the poster or add a small custom block. To check in the theme settings. |
| 02 | Logos strip | Moving strip `angel-ad` (images) | CSS only (bigger logos, dark tiles) |
| 03 | Main categories | Categories block (image + title + link) | CSS only. The second line under each name is not a field; drop it. |
| 04 | beIN world | Divider (title + "تصفح العروض") + banners (two devices) + categories (packages and renewal) | CSS only. The three-column layout in the draft becomes three stacked blocks. |
| 05 | AZ TV Box | Featured product | CSS only |
| 06 | Season offers | Divider with countdown and button + products grid | CSS only. Banner and cards stack instead of sitting side by side. |
| 07 / 11 | Packages | Divider + products slider | CSS only (product card restyled once) |
| 08 / 12 | Apps and devices | Divider with "تفعيل" button + categories block with icon images | CSS only. Icons uploaded as images. |
| 09 | Why us | Store features | CSS only. Payment logos already sit in the footer. |
| 10 | Testimonials | Testimonials | CSS only |
| 13 | Comparison | **No ANGEL block.** Banners block with a designed comparison image (desktop and phone) + divider buttons | Image instead of code. A real table needs a custom block. |
| 14 | Second store | Divider + full-width banner | CSS only |
| 15 | Loyal customers | Divider with button + products grid (renewals) | CSS only |
| 16 | FAQ | FAQ block `s-block--faqs` | CSS only |
| 17 | Final CTA | Divider (title, subtitle, one button) | CSS only, with one button; three buttons need three banners or a custom block |

So with ANGEL kept, almost everything is block settings plus one custom CSS file. Only the comparison table, the three-button final CTA and text over the hero video would need code; each has a no-code fallback above.

**Decision needed:** how we build it.

- Route A: keep the current theme and restyle it through its settings and custom CSS. Faster, limited.
- Route B: build custom blocks or a custom Twilight theme. Full control. Needs a Salla Partners account, the Salla CLI and Twig development.
- **Decided 2026-10-22: Route A.** The page is built from ملاك blocks with one custom CSS file; step-by-step setup in `05-design/SALLA-SETUP.md`.
- Earlier note, 2026-10-22: the theme is ملاك (ANGEL in the code), and it already covers the video hero, the logo strip and the FAQ (map above). **Route A is now the recommended fit**: keep ANGEL, set the blocks in the order of the plan, and add one custom CSS file. Route B only if the client wants the comparison table or the three-button final CTA as real HTML.

## 6. Current store snapshot (homepage, 2026-10-14)

- Theme: ملاك (Malak, code name ANGEL) by AfterAds, v1.174.0 (theme files id `1034648396`; `1130931637` is the store id). Font `PingARLT`. Theme primary colour `#000000`.
- Desktop homepage is about 8,000 px tall once products load.
- Order today: header → hero slider (Saudi win offer) → عالم بي ان → banners → عز تي في بوكس (featured product) → عروض اليوم الوطني → 2 والثالث مجانا → مميزات متجرنا → لعملائنا الأوفياء → تطبيقات الباقة العادية → Az TV → قالوا عن عز تي في → تطبيقات باقة البلس → Az TV Plus → newsletter → footer.
- Menu: أجهزة بي ان 4K, أجهزة بي ان PVR, تجديد اشتراك بي ان الرسمي, قمة عربي, قمة خليجي, تميز عربي, تميز خليجي, باقات الاشتراك (الباقة العادية, باقة البلس), تفعيل اشتراك عز تي في, تفعيل اشتراك عز تي في بلس.
- Footer: المدونة, من نحن, app download pages, activation guides, سياسة الاستبدال والإسترجاع, customer service +966 50 913 0883 (phone and WhatsApp), Telegram.

Things noticed:

- The apps block appears twice (normal and Plus), as the plan's proposal says.
- The features block reads "+ 0 طلب". Check whether the order counter is working.
- Product names and prices were not captured (the product cards did not expose their text). To be listed.
- Viewed from outside Saudi Arabia: the store showed prices in EUR and first showed Salla's human-verification page.

## 7. Assets

Have (paths from the client folder root):

- Logo: `01-brand/aztv/` (transparent 367×400 AVIF, 7338 px JPG on dark). No vector file.
- Brand pattern: `01-brand/aztv/angles-pattern (1).svg`
- Sister store logos: `01-brand/sister-stores/`
- Player and show photos: `02-assets/player-photos/`
- Stock textures and effects: `02-assets/stock/`
- Subscription cards (3 months, 12 months, Plus): `03-product-cards/subscription-cards/`
- Card images (player and show cut-outs, arriving in batches): `05-design/shared/subscription-cards/photos/` (`originals/`, README with the list and checks)
- Past campaigns for reference: `04-campaigns/`
- Activation guide: `05-guides/device-activation-steps/`
- Designs the client liked: `07-client/designs-client-liked/`

Missing for this plan:

- Confirmation in the Salla customizer that the moving strip and FAQ blocks exist on the homepage (see `05-design/SALLA-SETUP.md`, section 6).
- Official vector logo (AI or SVG). A traced SVG now exists (see log, 2026-10-22); the official file is still better if the client has it.
- Hero video footage, black and white, licensed for web use.
- AZ TV Box product photos.
- App and device icons.
- Comparison data for AZ TV vs AZ TV Plus.
- FAQ questions and answers.
- KoorPlanet beIN section screenshots (reference).

## 8. Open questions

1. Merge the two apps sections into one (16 sections) or keep both (17)?
2. ~~Which Salla theme does the store own?~~ ملاك (Malak) by AfterAds, code name ANGEL, v1.174.0. Still open: confirm Route A (keep ANGEL + custom CSS), and where the store adds custom CSS (theme settings or Salla's custom code).
3. Typeface for the new design: keep `PingARLT` or change?
4. Is a vector version of the logo available?
5. Who supplies the hero video footage?
6. Does the redesign cover only the homepage, or also category, product and activation pages?
7. Are the comparison rows (section 13) and the FAQ answers (section 16) right? Both are drafts written from the store's own pages.

## 9. Folder map

```
new store design/
├── our workspace.html  Our Workspace, the project page (open in a browser)
├── PROJECT.md          this file
├── 01-brief/           homepage-plan.md (the agreed plan, full text), client brief, meeting notes
├── 02-references/      competitor and inspiration screenshots (KoorPlanet etc.)
├── 03-current-site/    old-design/ (frozen copy of the live homepage + screens/)
├── 04-wireframes/      layout before visuals
├── open old design.bat / open new design.bat   run the two designs locally
├── 05-design/          new-design/ (the homepage on ملاك blocks + malak-custom.css), sections/01-hero … 17-final-cta, SALLA-SETUP.md (how to apply it on Salla), IMAGE-PROMPTS.md
├── 06-assets/          images, video, icons made for the new design
└── 07-exports/         final files handed to the client or to development
```

## 10. Log

- 2026-10-25: Background F (straight split) chosen by the client for the website: all ten product images on the website now use it (`build_page.py` default `PRODUCT_BG=f`).
- 2026-10-25: New product background option F, «تقسيم مستقيم» (straight split): option E with a straight horizontal line instead of the diagonal (`subscription-backgrounds/export/option-f-*.png`). All ten product images rendered on it for review (`subscription-cards/product-images/f/`, overview `overview-f.jpg`). The website still uses B; `PRODUCT_BG=f` on `build_page.py` previews F.
- 2026-10-25: Offer of the week reorganised (client: the discount column took too much space): the right column removed; the gift set centred and a little larger; the discount is one white circle «خصم 60%» on the 3-month card's corner.
- 2026-10-25: Offer of the week: the price taken off the image (the store's product card already shows it) and the discount «خصم 60%» made the highlight on the right, above «+ ٣ شهور مجانًا»; the small «خصم ٦٠٪» seal on the card removed as redundant.
- 2026-10-25: Offer of the week redesigned to be more elegant (client): black and white, the two regular cards as a gift set (1-year card in front, 3-month card behind, both tilted) wrapped in a black satin ribbon with thin white edges and a bow; «OFFER OF THE WEEK» / «عرض الأسبوع» heading; a white «خصم ٦٠٪» seal; «96 ريال فقط», «بدل ٢٣٨ ريال» struck through and «+ ٣ شهور مجانًا» on the right; on the dark stage (background B), which the website now uses for the offer too.
- 2026-10-25: Offer of the week redone in black and white only (client: no gold): white title plate, white 3D «96» with the old price «٢٣٨» struck through, white coupon and arrow, black satin ribbon and bow, the small 3-month card tilted 5 degrees.
- 2026-10-25: Offer of the week («عرض الأسبوع») for the old «سنة + ٣ شهور» product (96 SAR, 3 months free), on the old offer image's layout: a big title («عرض» on a gold plate, «الأسبوع» in white), a big gold 3D «96» with «ريال فقط», a dashed coupon «٣ شهور مجانًا» with an arrow, the cards smaller, a gold gift ribbon and bow on the small card. It is the regular line, so both cards are regular: the existing AZ TV 3-month card and a **new regular 1-year card** (`aztv-12m`, made at the client's request, players 003 behind on the right and 012 in front on the left, arranged with similar face sizes) because the regular line had no 12-month card. Earlier tries with Plus cards and a new «offer of the month» card were rejected and removed. `product-images/e/offer-week.jpg` (website), also on B. On the website it replaces the national-day image in the offers and AZ TV packages.
- 2026-10-24: All nine subscription cards accepted by the client. Each card is now a product image on the approved background (B, the black spotlight burst, on the website; E, the diagonal split, as an alternative): `05-design/shared/subscription-cards/product-images/` (2000 x 2000 JPG). The website preview shows them on the nine product cards (offers, AZ TV packages, Plus packages, loyal customers): `build_page.py` now swaps the images. The old «سنة + ٣ شهور» product still shows its old image in the preview (the client says that card does not exist).
- 2026-10-24: Card 5 (Plus 1 year): the actor behind also replaced with a black-and-white version with better lighting sent by the client (024, same framing as 018). 018 is unused now.
- 2026-10-24: Card 5 (Plus 1 year): the player photo replaced with a black-and-white version with better lighting sent by the client (023, same framing as 017). 017 is unused now.
- 2026-10-24: The actor behind no longer fades out early (client: the background showed through his body). Cards 2, 3, 5, 6 and 8: the actor stays solid down to the floor and the pills; the short photos 002 (card 6) and 016 (card 8) were enlarged a little to reach the bottom.
- 2026-10-24: Cards 2 and 8 redone with two new player photos from the client (already transparent): 022 (red Bayern kit) in front of the actor on card 2, back to the normal layout; 021 (white Real Madrid kit, arms crossed) in front of the Squid Game actor on card 8. 003, 010 and 011 are no longer used, so no player appears twice (seven cards, seven players).
- 2026-10-24: Logo strip balanced on all nine cards: Netflix, SSC, beIN and Shahid are sized for the same visual weight (widths 56, 50, 50, 56 px on the 380 px card) with even gaps.
- 2026-10-24: Card 2: player changed to 003 (Real Madrid kit), the card mirrored (player front right, actor behind left) so his raised arm does not cross the actor. Card 8: player 011 (no visible hands) replaced by 010 (crossed hands); 010 and 020 (card 7) are the same player, so he is on cards 7 and 8: there are only six usable players for seven cards. The outline beIN SPORTS logo is now on all nine cards, regular and Plus.
- 2026-10-24: Plus design F chosen by the client and applied to all five Plus cards (5, 6, 7, 8, 10): the AZ TV card in gold (gold card, black burst up to the top, gold name on a black title pill, black pills with gold text), with the outline beIN SPORTS logo. The other options and their code are removed. Overview `new/all-cards.jpg`.
- 2026-10-24: Plus options C and F rendered on all five Plus cards (card 5 was the only one before), with an overview of each option on the five cards: `05-design/shared/subscription-cards/new/options/plus-all-c.jpg` and `plus-all-f.jpg`. The Plus cards in `new/` keep the old gold design until the client picks C or F.
- 2026-10-24: Plus options: D and E dropped. C improved (the black burst now runs up to the top behind the title pill, as on the AZ TV card) and a new option F added: the AZ TV card in gold (gold card, black burst up to the top, gold name on a black pill). The Plus cards now use the outline beIN SPORTS logo the client supplied, shown white like the other logos. Overview `05-design/shared/subscription-cards/new/options/plus-12m-options.jpg`.
- 2026-10-24: Plus options: A and B dropped by the client, C kept, two new designs added on card 5: D (black card, big gold disc behind the faces) and E (gold card with a black screen; the heads rise out of its top). The stacked beIN logo on the Plus cards is now black and white. Overview `05-design/shared/subscription-cards/new/options/plus-12m-options.jpg`.
- 2026-10-24: Plus cards: the stacked beIN SPORTS logo supplied by the client replaces the old white beIN logo in the logo strip (Plus only). Three Plus design options made on card 5 for the client to choose from: A gold card (current), B black card with a gold burst and gold cap, C gold and black diagonal split with a black title pill. Overview `05-design/shared/subscription-cards/new/options/plus-12m-options.jpg`.
- 2026-10-24: AZ TV (regular) cards back to their old design at the client's request: black title pill, rays up to the top, white card with no frame (the cards are pixel-identical to the earlier export). The header cap and the new gold design stay on the Plus cards only.
- 2026-10-24: New AZ TV Plus card design (the client kept the new AZ TV card): Plus is now the AZ TV card in gold. Flat gold card and frame with the same black zigzag burst, black header cap with the name in gold, black side tabs and pills with gold text, black and white photos. The black card, gold dust, corner shard and sepia photos are gone. All Plus cards re-exported.
- 2026-10-24: Subscription cards, new top (client did not like the background running into the card name): a flat header cap, black on AZ TV and gold on Plus, with a curved lower edge holds the card name as plain text. The top-right gold shard is gone, rays and dust fade out before the cap, photos are clipped under it, the package line sits on its edge as a badge, the AZ TV card gets a white frame so the cap stays clear on the dark product backgrounds, and the left side tab moved down. All nine cards and the card backgrounds re-exported; details in `05-design/shared/subscription-cards/README.md`.
- 2026-10-24: Card 7 (Plus 6 months): actor changed at the client's request. The bald actor in the khaki shirt (photo 014) replaces 019 behind player 020: upright, light shirt against the dark kit, reaching the bottom of the card with no fade. 019 is unused for now.
- 2026-10-24: Cards 5 and 7 pairs swapped (client did not like the previous layouts). Card 5 (Plus 1 year): Messi photo 017 in front of the cowboy-hat actor 018, the same pairing as the accepted card 3; the brim stays inside the card and below the package line. Card 7 (Plus 6 months): Barcelona player 020 in front of the long-haired actor 019, his chair hidden under the duration pills.
- 2026-10-24: Cards 5 and 7 re-balanced (client: the photos are good but the layout is not). Placed to the proportions of the accepted card 3, measured with face detection: the actor behind has the larger face (about 114 px on the 380 px card) with its centre at about x 275, y 245; the player in front has a slightly smaller face, a little lower, at about x 130. The cowboy hat now clears the package line and the card edge, the long-haired actor no longer touches the right edge, and Messi's photo (cut at the thighs) fades out at the bottom instead of being enlarged.
- 2026-10-24: Cards 5 and 7 (Plus 1 year, Plus 6 months) built with four new photos, supplied already transparent: 017 (Argentina kit 10, fists out) in front of 019 (long hair, black period coat) on card 5, matching the planned Messi and Kit Harington pair; 020 (Barcelona kit, fist pump) in front of 018 (cowboy hat, blue suit, bolo tie) on card 7. The chairs and the cane are faded out. All eight face cards now have photos; overview `new/all-cards.jpg`. Note: 020 and 010 (card 2) look like the same player. Waiting for review.
- 2026-10-24: Merged site-dev (the 6-month trial card was removed there as unapproved, and the star photos were cleaned up) into the card work. Kept the rebuilt card 2 (`new/aztv-6m.png`: photos 010 and 013, built after the client asked for new photos on it) and the rejected-photos folder (`photos/rejected/`, which also holds S02, S05, S06 and S08); remove card 2 again if it is not wanted.
- 2026-10-24: Card 8 (Plus 3 months) rebuilt with the new photo 016 (the Squid Game actor in the tuxedo, supplied transparent) behind player 011. Waiting for review.
- 2026-10-24: Card 1 (عز تي في سنة + ٣ شهور) removed: the client says there is no such card. Nine cards left, numbers unchanged (2-10). Photos 003 and 012 are free again.
- 2026-10-24: Card 4 (AZ TV 1 month) now has a player (004) in front and an actor (015) behind, as every card should (one player, one actor); 014 is free again.
- 2026-10-24: Plus cards simplified at the client's request (too much going on): flat gold instead of gradients, no outlines or shadows, plain package line (gold chip, white text, no box), dark grey duration and logo pills, flat black background with faint gold rays.
- 2026-10-24: Client also rejected star S05 (Tom Holland, card 1); card 1 now has photo 012 (same actor) behind the player as a stand-in until another star is chosen.
- 2026-10-24: Client marked ten photos as not usable: 001, 007, 008 and the latest-roles stars S01, S02, S04, S05, S06, S07, S08. Moved to `05-design/shared/subscription-cards/photos/rejected/`; never use them on a card. Cards 5, 7 and 8 are empty until new photos are chosen.
- 2026-10-24: Client rejected cards 5, 7 and 8 (Plus 1 year, Plus 6 months, Plus 3 months). Sheet of all face photos with ids made for the client to pick which to drop: `05-design/shared/subscription-cards/photos/all-photos.jpg`.
- 2026-10-24: Card round with the client: Plus frame and shards flat gold without the inner line; AZTVSTORE letters centred in the side tabs (both styles); Plus 1 year rebuilt with photo 008 and Morte (two actors); two-device card polished (two-screens icon in the badge, faces matched in size and light). Plus 3 months rejected: waiting for two new photos (a player and a star).
- 2026-10-24: Plus 3 months and Plus 6 months cards: faces relit (client: the light was poor). Shadows opened with a gamma lift on both photos of Plus 3 months and on the player of Plus 6 months.
- 2026-10-24: AZ TV 1 month card: client found its photos weak; now photos 014 (front) and 015 (behind), two actors, instead of 007 and the latest-roles star `07`.
- 2026-10-24: Cards, client edits: AZ TV 6 months now has photo 013 behind the player (was the dark star photo), AZ TV Plus 1 year has photo 012 behind the player (was 008). The «AZ TV SUBSCRIPTION» line under the title on every card is now a clear pill: the package name in a chip («AZ TV» white, «AZ TV PLUS» gold) and «SUBSCRIPTION» or «RENEWAL» beside it.
- 2026-10-24: All ten subscription cards built in the accepted look (`05-design/shared/subscription-cards/new/`, overview `new/all-cards.jpg`), using the card photos 001-011 and the latest-roles stars. Plus cards get a gold version of the look (gold title pill, warm portraits, dark floor); the two renewal cards show renewal arrows instead of faces; the two-device Plus card has a «جهازين» badge. Card 3 is unchanged. Waiting for review; who is on which card is in the folder README.
- 2026-10-24: Subscription card look accepted: `05-design/shared/subscription-cards/new/aztv-3m.png` (اشتراك ٣ شهور). White card with the black burst, black title pill with an «AZ TV SUBSCRIPTION» line under it, two large black-and-white portraits (player in front, star behind), a soft light at the burst centre, a light floor under the duration and logo pills. Built from `card.html`, exported with `node render-cards.cjs <card>`; player photos cut out with `photos/cutout-white.py`. The 6-month trial was rejected and removed; portraits remain stand-ins until photos are matched to the name list.
- 2026-10-24: Card photos batch 3 (010 and 011: Barcelona kit with crossed fingers, royal-blue kit studio portrait) added to `05-design/shared/subscription-cards/photos/originals/`. Eleven photos in total. 011 is a square studio shot, not a tight cut-out like the rest.
- 2026-10-24: Card images batch 2 (four more cut-outs, 006 to 009: yellow-and-navy kit, Argentina kit jumping, man in dark period coat seated, man in straw hat and pinstripe suit) added to `05-design/shared/subscription-cards/photos/originals/`. Nine images in total, still all on white backgrounds.
- 2026-10-24: Place for the card images created: `05-design/shared/subscription-cards/photos/`. Batch 1 (five cut-outs: Argentina kit, man in black coat, Real Madrid, Barcelona, Man City) saved untouched in `originals/` with numbered names; more batches to follow, then we start on the cards. All five are on a white background (no transparency), so transparent versions are needed for the dark site; rights to be confirmed. Listed under shared elements in the workspace.

- 2026-10-23: Who appears on the subscription cards: top 10 football players (Ronaldo, Messi, Mbappé, Haaland, Vinícius, Bellingham, Yamal, Salah, Neymar, Benzema) and top 10 series and film stars (Game of Thrones, Breaking Bad, Peaky Blinders, Spider-Man, The Boys, Squid Game, Money Heist, Stranger Things, Vikings, Wednesday), picked for a Saudi and Arab audience by fame, not a live ranking. Source `05-design/shared/subscription-cards/card-stars.json`; shown in the workspace «ملفات التسليم» (نجوم البطاقات) with a suggested split across the eight cards that carry faces (the two renewal cards have none). Image rights to check before publishing.

- 2026-10-23: Subscription card backgrounds, one per style, in `05-design/shared/subscription-cards/bg/` (760 x 1296, transparent corners and hanger slot): AZ TV white with a bold black zigzag burst, AZ TV Plus black with a gold frame, gold corner shards and gold dust; both with AZTVSTORE side tabs and the same jagged ray as the approved product backgrounds. Content guides, mock-ups on B and E, source `card-background.html`, export `render-card-bg.cjs`. Also in the workspace «ملفات التسليم» under «خلفيات بطاقات الاشتراك».

- 2026-10-23: New first tab "نظرة عامة" in the workspace: a grid of large tiles, one icon and a short title each, in groups: tabs, to-do list, tasks and decisions, delivery files, plan and design, brand, Salla, current store, files and links. Each tile opens its tab and scrolls straight to that part (tasks, open questions, colours, Salla rules, footer links, etc.), plus the old design, new design and live store. The workspace now opens on it.

- 2026-10-23: Subscription cards organised in one folder, `05-design/shared/subscription-cards/` (README lists the ten cards, products, prices, old and new file names and the steps): `old/` the store's cards cut out of their posts, 4x, transparent corners (`cut-old-cards.py`, `old/all-cards.png` for all ten); `new/` empty, for the redesign, each card 760 x 1296 to fit the card area of the approved backgrounds. Our first-round cards were rejected (not good enough, will not go on the site) and removed: `assets/img/products/`, `build/make_products.js`, `cat-renewal-3d-bw.png`; the preview shows the store's own product images again and SALLA-SETUP.md no longer lists them. Tasks: «إعادة تصميم بطاقات الاشتراك» in «قائمة المهام», ten close-ups, not started.
- 2026-10-23: Subscription backgrounds merged into `site-dev`. Both approved backgrounds (B and E, white and gold) are in the workspace: «لوحة التصميم» shared-elements card, sections 07 and 11, and a new «خلفيات بطاقات الاشتراك» block in «ملفات التسليم» with downloads (WebP copies in `05-design/shared/subscription-backgrounds/export/`; `sync_workspace.py` embeds them).
- 2026-10-23: Option E approved by the client after removing the grey strip and thin line above the diagonal. B and E are both saved as usable subscription backgrounds (`bg-aztv*.png` = B, `option-e-aztv*.png` = E). Workspace shared-elements card shows both.
- 2026-10-23: Subscription background, new option to try next to the approved B: Option E "split", the old images' black / light diagonal redrawn clean (white or gold plane, zigzag rays tone on tone, fine double edge line, no loose shards). B stays the approved background until the client decides. Preview `05-design/shared/subscription-backgrounds/preview-option-e.webp`.
- 2026-10-23: **Subscription background approved: Option B** (spotlight burst). Option D (stadium) rejected as childish; all other options removed. Final files `05-design/shared/subscription-backgrounds/export/bg-aztv.png` (white) and `bg-aztv-plus.png` (gold, 4K badge), 2000 x 2000. Card area 380 x 648 at x 310, y 204 (of 1000). Added to the workspace: shared elements card, sections 07 and 11, log.
- 2026-10-23: Subscription backgrounds, round 3. Client: Option B is good, Option C is bad. C replaced by Option D "stadium night" (floodlight towers crossing beams behind the card, crowd camera flashes, pitch lines under the card), to feel epic and fun: TV shows and football. Preview `compare-option-d.webp`.
- 2026-10-23: Subscription backgrounds, round 2 after client feedback. Option A dropped (too busy). Option B kept without the floor light and the corner frames. New Option C "halo": light from above, soft shafts, two thin rings, dust in the beam. Card made smaller in both: 380 x 648 at x 310, y 204 (of 1000). Previews `compare-option-b.webp`, `compare-option-c.webp`.
- 2026-10-23: Subscription product backgrounds, two options for the client to pick (sections 07 and 11). One background for all subscription cards, the card in the middle changes per product. AZ TV uses white, AZ TV Plus uses gold with a 4K badge. Option A redraws the old diagonal look (dark top, one white or gold band with shards); Option B is a black stage with jagged rays from behind the card and a lit floor. Card area kept where it was in the old images (x 280-720, y 150-900 of 1000) so the current cards fit. Files in `05-design/shared/subscription-backgrounds/` (previews `compare-option-a.webp`, `compare-option-b.webp`; finals 2000 x 2000 in `export/`).
- 2026-10-23: Task list: new group «إعادة تصميم بطاقات الاشتراك» at the top of the «قائمة المهام» tab, all ten subscription cards marked to redesign. AZ TV (black and white): سنة + ٣ شهور p930436127, ٦ شهور p1133679038, ٣ شهور p527896233, شهر p264351896. AZ TV Plus (gold): سنة p331255752, سنة جهازين p1669484767, ٦ شهور p1879371242, ٣ شهور p1024479901. Renewals: العادي p777133688, البلس p287657453. Each shows today's card, current price and the new file name (`prod-*-v2.png`). The normal package has no 12-month card; its longest is سنة + ٣ شهور.
- 2026-10-23: Header logo changed again at the client's request, to `assets/img/logo/aztv-logo-stroke.svg`: one slow 10 s loop, a gold stroke draws around each shape (frame first, then the line, A, Z and TV), the logo fills in, rests, a soft shine passes across, rests, fades out gently, and the loop starts again. Still under reduced motion. The shine, loop and play-once versions stay as alternatives. Frames: `05-design/shared/logo/logo-stroke-frames.png`.
- 2026-10-23: New header logo `assets/img/logo/aztv-logo-shine.svg`, at the client's request (keep it moving and shining): no drawing intro, the logo is always visible; a wide bright shine sweeps across every 3 s, it floats gently, a gold glow breathes behind it, and four small sparkles twinkle in turn. CSS inside the SVG (works as a plain image / uploaded logo), still under reduced motion. Header (logo-light and logo-dark) now uses it; the loop and play-once versions stay as alternatives. Frames: `05-design/shared/logo/logo-shine-frames.png`.
- 2026-10-23: Hero video in place of the Gemini poster (poster files removed). Source `05-design/sections/01-hero/hero-video-source.mp4` (19.5 s, 1920x1080, already black and white, 13 MB with sound). Cropped to the 2.39:1 area because most clips carry 138 px cinema bars; encoded without sound to `assets/video/hero.mp4` (1280x536, 2.3 MB) and `hero-phone.mp4` (600x798, centre 3:4 crop, 1.4 MB), with VP9 WebM fallbacks and first-frame posters. Hero slider markup now a video slide (`responsive-video`, `video-swiper`; rebuilt from the theme CSS, to check in the customizer); the CSS makes it fill the hero like a background. Checked playing at 1440 and 390.
- 2026-10-22: Section 04 rebalanced: the row of five package tiles is gone, renewal moved up, so the section is three equal cards in one banners block (4K receiver, PVR receiver, official beIN renewal), swiping sideways on phones; the beIN icon above the title is dropped (the cards carry the logo). Cards composed by `build/make_bein.js` (beIN logo + Arabic title in PingARLT), temporarily with the devices cut out of the old banners. Prompts for the three 3D renders, with reference images (the real devices cut out, `assets/img/bein/ref-bein-*-device.png`, plus the section 03 style renders), are in the to-do list; when `bein-4k-3d.png`, `bein-pvr-3d.png`, `bein-renew-3d.png` land in `assets/img/bein/`, re-running `make_bein.js` swaps them in.
- 2026-10-22: The ten product card images are done (`assets/img/products/prod-*.png` for Salla, `.webp` for the page), composed by `build/make_products.js` in the browser so the Arabic is shaped in PingARLT: the section 03 3D card (black and white for AZ TV, gold for Plus with a 4K badge, the renewal arrow for renewals), the duration large, the package name small, on black with a soft glow. The two «اليوم الوطني» images are gone. In the preview via `build_page.py`; upload list in `SALLA-SETUP.md`; to-do items marked done.
- 2026-10-22: Image to-do list. `05-design/todo.json` lists the 23 old or placeholder images still in the new page, grouped: 10 product cards (I compose them from the section 03 3D renders, with the duration in Arabic; two still say «اليوم الوطني»), beIN world (4K and PVR receivers, قمة and تميز packages, renewal), the AZ TV Box card, the second-store banner, the three old GIF title icons, an optional 3D upgrade of the flat icons, and the hero video. Each has the image used today, the new file name, who makes it and a ready prompt in the section 03 style. `sync_workspace.py` (with `build/todo_panel.py`) turns it into the workspace tab «قائمة المهام» and `05-design/TODO.md`.
- 2026-10-22: Section 03, AZ TV card: black-and-white version of the 3D render (`cat-aztv-3d-bw.png/.webp`, silver frame, white logo) so the regular package reads black and white and Plus stays gold, as on the store's product cards. The gold original is kept.
- 2026-10-22: Full review of the new page, section by section, with the next edit for each and the top five priorities: stale «اليوم الوطني» product images (06, 07, 11), the beIN section (04), the AZ TV Box image (05), a shorter page by merging 08 and 12 (page is 10,826 px vs about 9,500 today), and renewal prices showing «-» (15). In `05-design/REVIEW.md`, full-page screenshots in `05-design/review/`.
- 2026-10-22: Section 03 uses the five 3D renders (transparent PNG, `cat-*-3d.png`, WebP copies for the page). CSS for the first categories block only (`section:nth-child(1 of .s-block--categories)`): the card is drawn behind the lower two thirds of the tile so the object rises out of it, floats gently and lifts with a gold glow on hover. The theme's own dark background on category links is removed for all category blocks.
- 2026-10-22: Second logo, `assets/img/logo/aztv-logo-loop.svg`: the same intro, then a quiet loop (signal waves from the antenna tip, a breathing gold glow, a shine every 7 s); taller canvas for the waves. Now in the header (logo-light and logo-dark). `aztv-logo-animated.svg` (plays once) stays as the calmer option the plan described. Frames: `05-design/shared/logo/logo-loop-frames.png`.
- 2026-10-22: Fix: the header logo disappeared with dark mode on. ملاك hides `.logo-light` in a dark header and shows `.logo-dark`, the dark-mode logo field, which the store never filled. The preview now carries the animated logo in both; `SALLA-SETUP.md` says to upload it in the dark-mode logo field too.
- 2026-10-22: Main menu fixed (plan note «مراجعة وإصلاح Menu List، إصلاح الكرت الذي يظهر بدون صورة»). Found in the saved page: the "card without an image" is the menu banner slider at the top of the drawer, enabled with one slide and no image; and «تجديد اشتراك بي ان الرسمي» has an empty image circle next to the 4K and PVR items that have images. New menu, no item images: باقات الاشتراك (العادية، البلس) · تجديد الاشتراك · عالم beIN (4K، PVR، قمة وتميز عربي وخليجي، تجديد beIN الرسمي) · AZ TV Box · العروض · تفعيل الاشتراك (AZ TV، AZ TV Plus). beIN packages were filed under renewal; renewal, the Box and offers were missing. Built into the preview by `build/build_page.py`, steps in `SALLA-SETUP.md` section 5, screenshots in `05-design/shared/menu/`.
- 2026-10-22: Workspace tab «ملفات التسليم» holds a copy of every deliverable, embedded so nothing depends on the folder: SALLA-SETUP.md (rendered), malak-custom.css (with copy button), both logo SVGs, all block images, IMAGE-PROMPTS.md and this file, each with a download button. Refresh after any change with `python3 05-design/new-design/build/sync_workspace.py`.
- 2026-10-22: **New design rebuilt on ملاك blocks (Route A).** `05-design/new-design/index.html` is now generated by `build/build_page.py` from the saved live page: the theme's own block markup, in the plan's 17-section order, refilled the way the merchant would in Salla's customizer. The earlier custom-markup draft (`new-design.css`, `az-` sections) is removed.
  - Theme settings do most of the work: ملاك has a dark mode (`.dark`, `--dark-bg-main` etc.) and colour settings (`--color-primary`, `--text-btn`, `--bg-color`, header/footer). Gold `#EACF69`, black `#0D0D0D`, surface `#1A1A1A` there turn the page black and gold with no CSS.
  - One CSS file for the store: `assets/css/malak-custom.css` (about 180 lines). It uses theme classes and block order, never component ids. Two order rules matter: the title block right after the first slider becomes the hero text (01), and the title block right after the FAQ becomes the final CTA box (17).
  - `assets/css/preview-only.css` is for the local copy only (stands in for Swiper and the FAQ toggle, since the saved page has no scripts).
  - New images made locally in `assets/img/malak/`: gold icons for the apps and features blocks, five beIN package tiles, the comparison image (desktop and phone), and the eight platform logos in white on one canvas size. Scripts in `build/`.
  - Not used on the store yet, so rebuilt from the theme CSS and to be checked in the Salla customizer: the moving strip (`angel-ad`, section 02) and the FAQ block (`s-block--faqs`, 16).
  - 13 Comparison is an image (no ملاك block for tables). 17 has one button (the title block holds one).
  - Section screenshots: `05-design/sections/*/…-malak-desktop.png|webp` and `…-malak-mobile.webp`, also in the workspace board.

- 2026-10-22: Animated logo. The store logo PNG (`S29idagq…png`, 1284×1397) traced into an SVG of five flat shapes (TV frame with antennas, top line, A, Z, TV), 98.9% overlap with the original. Two files in `05-design/new-design/assets/img/logo/`: `aztv-logo.svg` (static, 1.4 KB, now in the footer) and `aztv-logo-animated.svg` (4.3 KB, now in the header). The animation plays once, about 2.6 s: the frame and top line draw in, the frame fills, A and Z rise, TV pops, one gold shine passes, then the logo stays still. No motion for visitors who ask for reduced motion. The animation is CSS inside the SVG file, so it also runs as a plain image: on Salla it can be uploaded as the store logo with no theme code, if Salla's logo field accepts SVG (to check; if not, it goes in the header through the theme's custom code). Frames preview: `05-design/shared/logo/logo-animation-frames.png`. The original's slight dark shading inside the Z is flattened to the gold gradient.

- 2026-10-22: Sections 04 to 17, first draft, in `05-design/new-design/index.html`, in plan order. They replace the old theme blocks below the categories (the old design keeps them). Styles in `new-design.css`, all `az-`. What changed:
  - Shared: one product card (`.az-card`) for every product row (06, 07, 11, 15), a shared section shell (`.az-sec`, `--band` for the `#1A1A1A` ground), a `--line` button, and the footer restyled dark with the same links. The page ground is black from the hero to the footer.
  - 04 beIN world: three columns, devices (4K c757128774, PVR c1398521669), subscriptions (قمة عربي c1147218769, قمة خليجي c415231319, تميز عربي c374229586, تميز خليجي c1787038800), renewals (c899162953). Offers link c1461115041. Device images are the store's banners for now.
  - 05 AZ TV Box: features with gold icons, Plus year as a gift, 299 instead of 400, countdown. The countdown date is a placeholder; on Salla it comes from the product.
  - 06 Season offers: text banner ("خصم حتى 60٪") beside the two products of the offers category c1510593888.
  - 07 and 11: four packages each from the product data captured on 2026-10-21 (names, prices, discounts, ratings).
  - 08 and 12: kept as two sections (17 total) until the client decides. Both use one component (`.az-apps`) with icon tiles to the activation pages, so merging means deleting one.
  - 09: the four plan features plus payment logos. The broken "+ 0 طلب" counter is dropped.
  - 10: store reviews (names and stars; most have no text).
  - 13 Comparison and 16 FAQ: **draft content** written from the store's own products, banners and pages. The client must confirm each row and answer.
  - 14: dark card linking to azshirtsstore.com, current campaign image faded in. 15: renewal banner with the two renewal products. 17: final CTA with the three buttons.
  - Removed a browser-extension overlay (orange glow border and fake cursor) that came with the saved page.
  - Screenshots of each section (desktop PNG and WebP, mobile WebP) in `05-design/sections/04-…` to `17-…`, and embedded in the workspace board.
  - New images: prompts for Gemini/ChatGPT in `05-design/IMAGE-PROMPTS.md` (beIN receivers and AZ TV Box restaged on dark, season-offer art, subscription card backgrounds, second-store banner, final CTA background). Text is kept out of the images on purpose.

- 2026-10-21: Section 03 main categories, first draft. Five cards after the logo strip: تجديد الاشتراك (c183760688 "جدد الان"), AZ TV (c971844871), AZ TV Plus (c921887589), beIN Sports (c899162953, official renewal; there is no single beIN category), AZ TV Box (product p1152326425). Five images generated in Gemini in one matching style and warm-graded to the brand; originals `cat-*-gemini.jpg` in `05-design/sections/03-main-categories/`, web versions `cat-*.webp` (600x800). Cards 2-5 are Gemini's 765x1024 previews (Chrome blocked the full-size downloads), enough for the card size. The AZ TV Box image is a generic device: replace with the real product photo before going live.

- 2026-10-21: Section 02 now uses the eight official logos, all shown white. Seven from Wikimedia Commons, stc tv from stctv.com; originals and sources in `05-design/sections/02-platform-logos/originals/` (`SOURCES.md`). beIN and STARZPLAY have their own white versions; the rest are whitened with a CSS filter. MBC is the "MBC Group" version.

- 2026-10-21: Section 02 platform and channel logos, first draft. Moving strip right after the hero in `05-design/new-design/index.html` (styles `.az-logos` in `new-design.css`). Eight platforms taken from the store's own banners: beIN SPORTS, SSC, MBC, Shahid, Netflix, OSN+, STARZPLAY, stc tv. Shown as text names until the official logo files are supplied (put them in `assets/img/logos/`, swap each name for an `<img>` in both lists). Pauses on hover; static grid with reduced motion.

- 2026-10-21: Section 01 Hero, first draft. B&W poster generated in Gemini (`05-design/sections/01-hero/hero-poster-gemini-v1.jpg`, web versions `hero-poster.webp` and `hero-poster-phone.webp` in new-design `assets/img/`). Image slider replaced by the new hero in `05-design/new-design/index.html`; styles in `assets/css/new-design.css` (all classes `az-`). Video slot ready for footage. Links: تصفح الباقات → c1765121197, اشترك الآن → الباقة العادية c971844871.

- 2026-10-21: Saved local copy split in two. **Old design** `03-current-site/old-design/` is the frozen reference (read-only, do not change). **New design** `05-design/new-design/` is an identical copy we redesign. Run them with `open old design.bat` (http://localhost:8765) and `open new design.bat` (http://localhost:8770), or the buttons in the workspace.

- 2026-10-21: Our Hub renamed to Our Workspace (`our workspace.html`). Current homepage shown section by section in the "المتجر الحالي" tab (screenshots in `03-current-site/old-design/screens/`). New "لوحة التصميم" tab lists, for each of the 17 sections, today's look, what we make (images, cards, design) and its folder in `05-design/sections/`. New images will be generated with Gemini.

- 2026-10-21: Live homepage captured locally to `03-current-site/live-home/` (now `old-design/`) (rendered DOM, theme CSS, fonts, images; static, no scripts). Base for local design work. Theme CSS is `themes/1034648396/1.174.0` (class names point to the "Angel" theme), which differs from the theme id in section 6. Product names and prices are now in the copy.

- 2026-10-14: Hub rebuilt in Arabic only (client request), RTL. The plan is now one tab ("الخطة") plus "ملاحظات التصميم". Tabs and buttons no longer change the page address: the desktop app previews the file as a `data:` URL, where `#` links and `location.hash` are blocked, which is why clicks did nothing before.
- 2026-10-14: Full original plan text saved as `01-brief/homepage-plan.md` and added to the hub as the "Plan document" tab, so the Google Doc is no longer needed for day-to-day work.
- 2026-10-14: Client folder reorganised. Plan imported from the Google Doc. Brand colours set. Live homepage reviewed. Hub and this file created.
