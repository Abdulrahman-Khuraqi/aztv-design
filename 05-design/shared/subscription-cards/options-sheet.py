"""Overview of one Plus design option on all five Plus cards, for review with the client.
Run from this folder after node render-cards.cjs plus-12m@c ... :  python3 options-sheet.py c   ->  new/options/plus-all-c.jpg
Needs Pillow with raqm (Arabic shaping)."""
import sys
from PIL import Image, ImageDraw, ImageFont

opt = sys.argv[1] if len(sys.argv) > 1 else "c"
# number, file, name; right to left, as in contact-sheet.py
CARDS = [(5, "plus-12m", "بلس سنة"), (6, "plus-12m-2dev", "بلس سنة (جهازين)"), (7, "plus-6m", "بلس ٦ شهور"),
         (8, "plus-3m", "بلس ٣ شهور"), (10, "renew-plus", "تجديد بلس")]
W, H, GAP, TOP, LABEL = 500, 853, 36, 70, 70
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
num_font, name_font = ImageFont.truetype(BOLD, 34), ImageFont.truetype(BOLD, 28)

sheet = Image.new("RGB", (5 * W + 6 * GAP, TOP + H + LABEL + 2 * GAP), (13, 13, 13))
d = ImageDraw.Draw(sheet)
for i, (n, f, name) in enumerate(CARDS):
    x = GAP + (4 - i) * (W + GAP)
    cx, y = x + W // 2, GAP
    d.ellipse((cx - 28, y, cx + 28, y + 56), fill=(234, 207, 105))
    d.text((cx, y + 28), str(n), font=num_font, fill=(13, 13, 13), anchor="mm")
    card = Image.open(f"new/options/{f}-{opt}.png").resize((W, H), Image.LANCZOS)
    sheet.paste(card, (x, y + TOP), card)
    d.text((cx, y + TOP + H + 34), name, font=name_font, fill=(244, 244, 242), anchor="mm", direction="rtl")
out = f"new/options/plus-all-{opt}.jpg"
sheet.save(out, quality=88)
print(out, sheet.size)
