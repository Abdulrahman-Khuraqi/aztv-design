# AZ TV Store — New Store Design

Single source of truth for the redesign of [aztvstore.com](https://aztvstore.com/).
The visual version of this file is **Our Workspace**: [our workspace.html](our%20workspace.html). Keep the two in sync. Its tab «ملفات التسليم» embeds every deliverable (refresh with `python3 05-design/new-design/build/sync_workspace.py`).

Last updated: 2026-10-22

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
