// Renders the cards defined in card.html to new/<card>.png (760 x 1296, transparent corners).
// Run from this folder: node render-cards.cjs aztv-6m   (no name = all cards; needs the playwright package)
const { chromium } = require("playwright");
const { pathToFileURL } = require("node:url");
const { resolve } = require("node:path");

(async () => {
  let names = process.argv.slice(2);
  const page = await (await chromium.launch()).newPage({ viewport: { width: 500, height: 760 }, deviceScaleFactor: 2 });
  if (!names.length) {
    await page.goto(pathToFileURL(resolve("card.html")).href);
    names = await page.evaluate(() => Object.keys(CARDS));
  }
  for (const name of names) {
    await page.goto(`${pathToFileURL(resolve("card.html")).href}?card=${name}`);
    await page.waitForSelector("body[data-ready]");
    await page.locator("#card").screenshot({ path: `new/${name}.png`, omitBackground: true });
    console.log(`new/${name}.png`);
  }
  await page.context().browser().close();
})();
