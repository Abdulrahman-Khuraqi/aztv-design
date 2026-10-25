# Image prompts for the new design

> Update 2026-10-22: the page is now built on ملاك blocks (see `SALLA-SETUP.md`). Prompts 1, 2, 4 and 5 still apply: their images go into banners, the featured product, product cards and a slider. Prompts 3 and 6 are **not needed**: ملاك's title block has no background-image field, so the season offers and the final CTA stay text on black.

Sections 04 to 17 are built with the images the store already has. These are the new images that would lift them. Generate each one in Gemini or ChatGPT, save it under the file name given, and drop it into `05-design/sections/<folder>/`. I'll compress it to WebP, wire it into the page and grade it to the brand.

Rules that apply to every image:

- Dark, cinematic, premium. Black `#0D0D0D` ground, warm gold `#EACF69` as the only accent colour. No other strong colours.
- **No text, no logos, no watermarks** in the image. The page adds all text, so it stays sharp, editable in Salla and correct in Arabic. AI models misspell Arabic.
- Leave empty dark space where the text will sit (named in each prompt).
- Real products (beIN receivers, AZ TV Box) must look like the real device. For those, **attach the photo named in the prompt** and ask the model to restage it, not to invent a device.

---

## 1. beIN receivers on dark (section 04, عالم beIN)

Two images, one per device. Today the cards use the store's white and purple banners.

- Files: `04-bein-world/bein-4k-dark.png`, `04-bein-world/bein-pvr-dark.png`
- Size: square, 1200 × 1200
- Attach: `05-design/new-design/assets/img/b3ee113b-01d6-4824-af25-344fa8a26396-022b88f8.webp` (4K) or `0331b2be-ccc5-4f63-8a30-7cf3e1cf572c-03180d63.webp` (PVR)

```
Use the attached photo as the exact product reference. Keep the white beIN receiver exactly as it is (shape, buttons, logo position), but remove everything else: the big letters, the purple band and the Arabic text.
Restage it as a premium studio product shot: the receiver at a slight three-quarter angle on a matte black surface, black seamless background (#0D0D0D), soft warm-gold rim light from behind (#EACF69), subtle reflection on the surface, gentle falloff into darkness at the edges.
Square 1:1, product centred and filling about 60% of the frame. Photorealistic, sharp, no text, no logos added, no props.
```

## 2. AZ TV Box on dark (section 05) · done 2026-10-25

Replaces the promo square in section 05 (the block's own image, uploaded in the theme editor). The category card in section 03 keeps `cat-aztv-box-3d.png`.

- Result: `05-aztv-box/aztv-box-dark-gemini.jpg` (Gemini, 2000 × 1116), on the site as `new-design/assets/img/aztv-box-dark.webp` (1600 × 893)
- Size asked: wide 16:9, product on the left third, right half empty for the text
- Attach, in this order: `05-design/new-design/assets/img/cat-aztv-box-3d.png` (exact device), `05-design/new-design/assets/img/44b0d971-d7aa-45ab-9db8-5de0b83e7c8d-2324b29c.webp` (the store's photo of the real device), `05-design/sections/03-main-categories/cat-aztv-box-gemini.jpg` (mood)
- If the device comes out changed, regenerate with: «The logo and ports must match image 1 exactly.»

```
I attached 3 reference images.
Image 1 is the exact product: the black AZ TV Box with the gold AZ TV logo on top, and its remote with the Netflix and YouTube buttons. Image 2 is the real store photo of the same device. Image 3 is the lighting and mood I want.

Keep the box and the remote exactly as in images 1 and 2: same shape, same proportions, same gold AZ TV logo, same buttons. Do not redesign or invent any part of the device. Remove everything else from the references: the price, the balloons, the gift box, the subscription card, the gem, the text and the stage.

Create a premium product photo for a dark website section:
- The box stands at a slight three-quarter angle with the remote leaning next to it, on a matte black surface with a soft reflection under it.
- Background: near-black #0D0D0D, fading into darkness at the edges. A little fog or haze low behind the product, like image 3.
- Light: one soft warm gold rim light (#EACF69) from behind and above that traces the edges of the box and the remote. A few very faint gold dust particles in the air. No other colours.
- Composition: wide 16:9 (2400 x 1350). Put the product on the LEFT third of the frame, about 55% of the frame height. The right 50% of the image must be completely empty dark space, because Arabic text will be placed there.
- Photorealistic, sharp focus on the logo, shallow depth of field in the background.
- No text, no letters, no numbers, no logos other than the AZ TV logo on the device, no watermark, no people, no hands, no props.
```

## 3. Season offers artwork (section 06, عروض بداية الموسم)

Background for the offer banner beside the two product cards.

- File: `06-season-offers/season-offers-bg.png`
- Size: 1200 × 1000
- Text sits on the **right** half (Arabic, right to left)

```
Cinematic dark artwork for a new football season promotion for a TV streaming store. On the left side: a black-and-white football under stadium floodlights mid-air, with a soft golden glow and a few gold light streaks and confetti flecks around it. The right half fades into near-black (#0D0D0D) with nothing in it.
Black and gold only (#EACF69), high contrast, premium sports-broadcast mood, shallow depth of field. No text, no logos, no people's faces, no team kits.
```

## 4. Subscription background (sections 07 and 11, product cards)

The product card images today are campaign squares that still say "عرض اليوم الوطني". The plan asks for one card system: 1, 3, 6 months and year, normal and Plus. Generate the two backgrounds below; the duration, price and player cut-outs are laid on top in Canva or Photoshop, so every card shares one template.

- Files: `07-aztv-packages/card-bg-aztv.png`, `11-plus-packages/card-bg-plus.png`
- Size: square, 1500 × 1500

```
AZ TV (normal):
Abstract square background for a TV subscription card. Matte black (#0D0D0D) with a bold black-and-white angular zig-zag pattern in the upper half, cut by one clean diagonal. Soft spotlight in the centre. Lower third plain black for text. No text, no logos, no people.

AZ TV Plus:
Same layout, but the angular pattern and diagonal band in warm gold (#EACF69) on black, with a subtle metallic sheen and a few gold dust particles. Lower third plain black for text. No text, no logos, no people.
```

## 5. Second store banner (section 14, ٢ والثالث مجانًا) · done 2026-10-25

The finished banner carries its own Arabic text: «٢ والثالث مجانًا», a short line, a «تسوّق التيشرتات» button and the store logo (`14-second-store/logo-az-shirts.png`). Gemini makes the artwork **without any text** and leaves the right half (phone: the bottom 40%) empty; we add the text and logo over it, because AI models misspell Arabic.

- Result: Gemini spread the three shirts across the whole frame (`14-second-store/second-store-gemini.jpg`, 2000 × 1116), so the text went above it and the button under the gift box, centred. Composed by `new-design/build/make_second_store.js` into `new-design/assets/img/second-store/second-store-desktop.webp` and `-phone.webp`.
- Attach, in this order: `05-design/sections/05-aztv-box/aztv-box-dark-gemini.jpg` (mood), `05-design/sections/14-second-store/shirt-saudi-green.png`, `05-design/sections/14-second-store/shirt-brazil-yellow.png`
- The third shirt (in the gift box) is a plain white one; to use a real third shirt, attach it as image 4 and replace that line.
- Full prompt (desktop and phone): the to-do item «بنر 2 والثالث مجانًا» in `05-design/todo.json`, also in the workspace to-do tab.

## 6. Final call to action background (section 17, جاهز تبدأ المشاهدة؟)

Optional. The section works without it (gold glow on black); an image would make the last screen feel like the hero.

- File: `17-final-cta/final-cta-bg.png`
- Size: 2400 × 800 (wide)
- Text and three buttons sit in the **centre**

```
Very dark, wide cinematic photo of a modern living room at night seen from behind a sofa: a large wall TV glowing with a blurred football match under floodlights. Black and white, with only the TV glow tinted warm gold (#EACF69). The centre of the frame is dark and calm (text goes there). Heavy vignette, soft film grain, no people's faces, no text, no logos on the TV.
```

---

Still needed from the client, not from AI: the hero video footage (section 01), the vector logo for the animated logo, and confirmation of the comparison rows (section 13) and FAQ answers (section 16).
