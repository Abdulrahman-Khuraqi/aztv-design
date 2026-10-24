// Renders the cards defined in card.html to new/<card>.png (760 x 1296, transparent corners).
// Run from this folder: node render-cards.cjs plus-12m   (needs the playwright package)
const { chromium } = require("playwright");
const { pathToFileURL } = require("node:url");
const { resolve } = require("node:path");

(async () => {
  const names = process.argv.slice(2);
  if (!names.length) { console.error("usage: node render-cards.cjs <card> [<card> ...]"); process.exit(1); }
  const page = await (await chromium.launch()).newPage({ viewport: { width: 500, height: 760 }, deviceScaleFactor: 2 });
  for (const name of names) {
    await page.goto(`${pathToFileURL(resolve("card.html")).href}?card=${name}`);
    await page.waitForSelector("body[data-ready]");
    await page.locator("#card").screenshot({ path: `new/${name}.png`, omitBackground: true });
    console.log(`new/${name}.png`);
  }
  await page.context().browser().close();
})();
