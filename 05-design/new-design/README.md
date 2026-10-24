# New design (ملاك blocks + one CSS file)

The new homepage, built only from the blocks of the store's Salla theme **ملاك** (ANGEL by AfterAds), in the 17-section order of the plan. What you see here is what the store will look like after the steps in `../SALLA-SETUP.md`.

- `index.html`: generated, do not edit by hand. Run `python3 build/build_page.py` (needs `beautifulsoup4`). It starts from the saved live page (`03-current-site/old-design/index.html`), applies the theme settings (dark mode, brand colours), and lays out the ملاك blocks with the new content.
- `assets/css/malak-custom.css`: **the only CSS for the store.** Paste it into Salla's custom CSS.
- `assets/css/preview-only.css`: local preview only, never uploaded. The saved page has no scripts, so this file does what the theme's JavaScript does live (sliders, FAQ toggle).
- `assets/img/products/`: the nine subscription product images (card on the approved background), 1000 x 1000 WebP made by `build_page.py` from `05-design/shared/subscription-cards/product-images/b/`.
- `assets/img/malak/`: images made for the blocks (icons, beIN tiles, comparison, white platform logos). `assets/img/logo/`: the logo as SVG, static and animated.
- `build/`: `build_page.py` (the page), `make_images.js` and `make_logos.js` (the images, with Playwright and the page served on :8770).

Run it: double-click `open new design.bat` in the project folder, then http://localhost:8770.
