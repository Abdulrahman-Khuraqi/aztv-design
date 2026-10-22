# Old design (do not change)

The live homepage of https://aztvstore.com/ar as it was on 2026-10-21, captured in Chrome at desktop width after scrolling the full page. This folder is the reference and is set to read-only. All redesign work happens in the copy at `05-design/new-design/`.

- `index.html`: the page with every stylesheet, font and image served from `assets/`. Scripts are removed, so it is static: sliders, menus, cart and countdowns do not run.
- `source-rendered.html`: the same rendered DOM before localising, with links still pointing at Salla's CDN.
- `assets/`: `css/` (theme `app.css`, PingARLT, Salla icon fonts), `fonts/`, `img/`.
- `screens/`: full-page screenshot at 1440 px and one image per section (`c01` header to `c14` footer).

Run it: double-click `open old design.bat` in the project folder, then http://localhost:8765.

Theme in the CSS URL: `themes/1034648396/1.174.0/app.css`. Block class names (`s-angel--divider`, `angel-products`) suggest Salla's "Angel" theme.
