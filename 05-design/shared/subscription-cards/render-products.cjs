// Product images: every finished card placed on the approved background (white for AZ TV, gold for Plus), 2000 x 2000 JPG.
// Run from this folder: node render-products.cjs        (all cards, backgrounds B and E)
//                       node render-products.cjs b      (only background B; or e)
// Output: product-images/b/<card>.jpg and product-images/e/<card>.jpg  (needs the playwright package)
const { chromium } = require("playwright");
const { pathToFileURL } = require("node:url");
const { resolve } = require("node:path");
const { mkdirSync } = require("node:fs");

// card file -> tier of the background, and the Salla product it is the image of
const CARDS = [
  ["aztv-6m", "regular", "p1133679038"], ["aztv-3m", "regular", "p527896233"], ["aztv-1m", "regular", "p264351896"],
  ["plus-12m", "plus", "p331255752"], ["plus-12m-2dev", "plus", "p1669484767"], ["plus-6m", "plus", "p1879371242"], ["plus-3m", "plus", "p1024479901"],
  ["renew-aztv", "regular", "p777133688"], ["renew-plus", "plus", "p287657453"],
];
(async () => {
  const opts = process.argv[2] ? [process.argv[2]] : ["b", "e"];
  const stage = pathToFileURL(resolve("../subscription-backgrounds/backgrounds.html")).href;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1100, height: 1100 }, deviceScaleFactor: 2 });
  for (const opt of opts) {
    mkdirSync(`product-images/${opt}`, { recursive: true });
    for (const [card, tier] of CARDS) {
      await page.goto(`${stage}?opt=${opt}&tier=${tier}&card=${encodeURIComponent(`../subscription-cards/new/${card}.png`)}`);
      await page.waitForSelector("body[data-ready]");
      await page.waitForFunction(() => [...document.images].every(i => !i.src || i.complete));
      await page.locator("#bg").screenshot({ path: `product-images/${opt}/${card}.jpg`, type: "jpeg", quality: 92 });
      console.log(`product-images/${opt}/${card}.jpg`);
    }
  }
  await browser.close();
})();
