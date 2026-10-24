// Renders the two card backgrounds to bg/ (760 x 1296, transparent corners and hanger slot),
// their content guides, and mock-ups on the approved product backgrounds (B and E) to bg/mockups/.
// Run from this folder: node render-card-bg.cjs (needs the playwright package)
const { chromium } = require("playwright");
const { pathToFileURL } = require("node:url");
const { resolve } = require("node:path");
const { mkdirSync } = require("node:fs");

(async () => {
mkdirSync("bg/mockups", { recursive: true });
const cardPage = pathToFileURL(resolve("card-background.html")).href;
const stagePage = pathToFileURL(resolve("../subscription-backgrounds/backgrounds.html")).href;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1100, height: 1100 }, deviceScaleFactor: 2 });
const ready = async () => {
  await page.waitForSelector("body[data-ready]");
  await page.waitForFunction(() => [...document.images].every(i => !i.src || i.complete));
};

for (const [tier, name] of [["regular", "aztv"], ["plus", "aztv-plus"]]) {
  await page.goto(`${cardPage}?tier=${tier}`);
  await ready();
  await page.locator("#card").screenshot({ path: `bg/card-bg-${name}.png`, omitBackground: true });
  await page.goto(`${cardPage}?tier=${tier}&guide=1`);
  await ready();
  await page.locator("#card").screenshot({ path: `bg/card-bg-${name}-guide.png`, omitBackground: true });
  console.log(`bg/card-bg-${name}.png`);

  // on the approved product backgrounds: B (bg-*) and E (option-e-*)
  for (const [opt, prefix] of [["b", "bg"], ["e", "option-e"]]) {
    const card = `../subscription-cards/bg/card-bg-${name}.png`;
    await page.goto(`${stagePage}?opt=${opt}&tier=${tier}&card=${encodeURIComponent(card)}`);
    await ready();
    const out = `bg/mockups/${prefix}-${name}-blank.jpg`;
    await page.locator("#bg").screenshot({ path: out, quality: 88 });
    console.log(out);
  }
}
// Plus design options under review (2026-10-24): bg/options/card-bg-aztv-plus-<opt>.png
mkdirSync("bg/options", { recursive: true });
for (const opt of ["c", "f"]) {
  await page.goto(`${cardPage}?tier=plus&opt=${opt}`);
  await ready();
  await page.locator("#card").screenshot({ path: `bg/options/card-bg-aztv-plus-${opt}.png`, omitBackground: true });
  console.log(`bg/options/card-bg-aztv-plus-${opt}.png`);
}
await browser.close();
})();
