// Product images: every finished card placed on the approved background (white for AZ TV, gold for Plus), 2000 x 2000 JPG.
// Run from this folder: node render-products.cjs        (all cards, backgrounds B and E)
//                       node render-products.cjs b      (only background B; or e, f)
//                       node render-products.cjs f shine  (with the shine effects -> product-images/f-shine/)
//                       node render-products.cjs f shine aztv-3m plus-12m  (only these cards, no offer image)
//                       node render-products.cjs f shine-a aztv-3m plus-12m  (option A "comet"; shine-b "power-up") -> product-images/f-shine-a/
// Output: product-images/b/<card>.jpg and product-images/e/<card>.jpg  (needs the playwright package)
// The offer of the week (offer-week.jpg, offer-week-b.jpg) is composed from two finished cards by offer-image.html; the empty stage it sits on is kept as _stage-regular.jpg.
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
// «عرض الشهر» (offer of the month, «عرض الأسبوع» until 2026-10-27; files keep the name offer-week; product p930436127, سنة + ٣ شهور): composed from two finished cards on the empty stage (offer-image.html)
// -> product-images/<opt>/offer-week.jpg (big 1-year card + small 3-month card) and offer-week-b.jpg (small card is the AZ TV 3 months)
const OFFERS = [
  ["offer-week", "regular", "aztv-12m", "aztv-3m", { save: "60%" }],
];
(async () => {
  const opts = process.argv[2] ? [process.argv[2]] : ["b", "e", "f"];
  // shine: the edge light (round 2); shine-a / shine-b: the two bolder options (round 3)
  const shine = /^shine(-[ab])?$/.test(process.argv[3] || "") ? process.argv[3] : "";
  const shineParam = shine === "shine" ? "1" : shine.slice(6);
  const only = process.argv.slice(4);
  const stage = pathToFileURL(resolve("../subscription-backgrounds/backgrounds.html")).href;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1100, height: 1100 }, deviceScaleFactor: 2 });
  for (const opt of opts) {
    const out = shine ? `${opt}-${shine}` : opt;
    mkdirSync(`product-images/${out}`, { recursive: true });
    for (const [card, tier] of CARDS.filter(([c]) => !only.length || only.includes(c))) {
      await page.goto(`${stage}?opt=${opt}&tier=${tier}&card=${encodeURIComponent(`../subscription-cards/new/${card}.png`)}${shine ? `&shine=${shineParam}` : ""}`);
      await page.waitForSelector("body[data-ready]");
      await page.waitForFunction(() => [...document.images].every(i => !i.src || i.complete));
      await page.locator("#bg").screenshot({ path: `product-images/${out}/${card}.jpg`, type: "jpeg", quality: 92 });
      console.log(`product-images/${out}/${card}.jpg`);
    }
    for (const [name, tier, big, small, texts] of only.length ? [] : OFFERS) {
      await page.goto(`${stage}?opt=${opt}&tier=${tier}${shine ? `&shine=${shineParam}` : ""}`);   // the empty stage, no card
      await page.waitForSelector("body[data-ready]");
      await page.waitForFunction(() => [...document.images].every(i => !i.src || i.complete));
      const base = `product-images/${out}/_stage-${tier}.jpg`;
      await page.locator("#bg").screenshot({ path: base, type: "jpeg", quality: 95 });
      const qs = new URLSearchParams({ stage: base, big: `new/${big}.png`, small: `new/${small}.png`, ...texts });
      await page.goto(`${pathToFileURL(resolve("offer-image.html")).href}?${qs}`);
      await page.waitForSelector("body[data-ready]");
      await page.locator("#stage").screenshot({ path: `product-images/${out}/${name}.jpg`, type: "jpeg", quality: 92 });
      console.log(`product-images/${out}/${name}.jpg`);
    }
  }
  await browser.close();
})();
