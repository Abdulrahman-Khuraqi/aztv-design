# AZ TV Store — New Store Design

Single source of truth for the redesign of [aztvstore.com](https://aztvstore.com/).
The visual version of this file is **Our Workspace**: [our workspace.html](our%20workspace.html). Keep the two in sync.

Last updated: 2026-10-23

## 1. Project in one paragraph

Redesign the AZ TV Store homepage (عز تي في) into a shorter, clearer page that is more focused on conversion, while keeping services easy to reach. The store runs on **Salla**, so every section must be buildable as a Salla theme block. We design the sections in the agreed order below, 01 to 17.

- Live store: https://aztvstore.com/
- Agreed plan, full original Arabic text: [01-brief/homepage-plan.md](01-brief/homepage-plan.md), also inside the workspace (tabs "الخطة" and "ملاحظات التصميم"). Work from these, not from the Google Doc.
- Original Google Doc (`AZTV_Homepage_New_Order_v3`), reference only: https://docs.google.com/document/d/1F0vgi7_V4gwE4v3klXzwdz6QhVmNvYYqwonBPe1vdEs/edit?tab=t.0
- Platform: Salla (Twilight theme engine)
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

**Decision needed:** how we build it.

- Route A: keep the current theme and restyle it through its settings and custom CSS. Faster, limited.
- Route B: build custom blocks or a custom Twilight theme. Full control. Needs a Salla Partners account, the Salla CLI and Twig development.
- The plan asks for a video hero, an animated logo, a logo strip, a comparison block and an FAQ. Route B is the likely fit, to be confirmed once we know which theme the store owns and what access we have.

## 6. Current store snapshot (homepage, 2026-10-14)

- Theme: Salla Twilight theme, id `1130931637`. Font `PingARLT`. Theme primary colour `#000000`.
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

- Vector logo (AI or SVG), needed for the animated logo.
- Hero video footage, black and white, licensed for web use.
- AZ TV Box product photos.
- App and device icons.
- Comparison data for AZ TV vs AZ TV Plus.
- FAQ questions and answers.
- KoorPlanet beIN section screenshots (reference).

## 8. Open questions

1. Merge the two apps sections into one (16 sections) or keep both (17)?
2. Which Salla theme does the store own, and do we have developer access (Route A or B)?
3. Typeface for the new design: keep `PingARLT` or change?
4. Is a vector version of the logo available?
5. Who supplies the hero video footage?
6. Does the redesign cover only the homepage, or also category, product and activation pages?

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
├── 05-design/          new-design/ (working copy of the homepage), shared/ (header, product card, buttons), sections/01-hero … 17-final-cta, desktop/, mobile/
├── 06-assets/          images, video, icons made for the new design
└── 07-exports/         final files handed to the client or to development
```

## 10. Log

- 2026-10-23: Subscription background, new option to try next to the approved B: Option E "split", the old images' black / light diagonal redrawn clean (white or gold plane, zigzag rays tone on tone, fine double edge line, no loose shards). B stays the approved background until the client decides. Preview `05-design/shared/subscription-backgrounds/preview-option-e.webp`.
- 2026-10-23: **Subscription background approved: Option B** (spotlight burst). Option D (stadium) rejected as childish; all other options removed. Final files `05-design/shared/subscription-backgrounds/export/bg-aztv.png` (white) and `bg-aztv-plus.png` (gold, 4K badge), 2000 x 2000. Card area 380 x 648 at x 310, y 204 (of 1000). Added to the workspace: shared elements card, sections 07 and 11, log.
- 2026-10-23: Subscription backgrounds, round 3. Client: Option B is good, Option C is bad. C replaced by Option D "stadium night" (floodlight towers crossing beams behind the card, crowd camera flashes, pitch lines under the card), to feel epic and fun: TV shows and football. Preview `compare-option-d.webp`.
- 2026-10-23: Subscription backgrounds, round 2 after client feedback. Option A dropped (too busy). Option B kept without the floor light and the corner frames. New Option C "halo": light from above, soft shafts, two thin rings, dust in the beam. Card made smaller in both: 380 x 648 at x 310, y 204 (of 1000). Previews `compare-option-b.webp`, `compare-option-c.webp`.
- 2026-10-23: Subscription product backgrounds, two options for the client to pick (sections 07 and 11). One background for all subscription cards, the card in the middle changes per product. AZ TV uses white, AZ TV Plus uses gold with a 4K badge. Option A redraws the old diagonal look (dark top, one white or gold band with shards); Option B is a black stage with jagged rays from behind the card and a lit floor. Card area kept where it was in the old images (x 280-720, y 150-900 of 1000) so the current cards fit. Files in `05-design/shared/subscription-backgrounds/` (previews `compare-option-a.webp`, `compare-option-b.webp`; finals 2000 x 2000 in `export/`).

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
