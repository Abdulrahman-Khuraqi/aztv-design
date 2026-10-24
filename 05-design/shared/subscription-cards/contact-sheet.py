"""Overview of the ten cards with their number (as in README.md) and name, for review with the client.
Run from this folder after render-cards.cjs:  python3 contact-sheet.py  ->  new/all-cards.jpg
Needs Pillow with raqm (Arabic shaping)."""
from PIL import Image, ImageDraw, ImageFont

# number, file, name; laid out right to left, AZ TV on the first row, Plus on the second
ROWS = [
    [(1, "aztv-15m", "عز تي في سنة + ٣ شهور"), (2, "aztv-6m", "عز تي في ٦ شهور"), (3, "aztv-3m", "عز تي في ٣ شهور"),
     (4, "aztv-1m", "عز تي في شهر"), (9, "renew-aztv", "تجديد عز تي في")],
    [(5, "plus-12m", "بلس سنة"), (6, "plus-12m-2dev", "بلس سنة (جهازين)"), (7, "plus-6m", "بلس ٦ شهور"),
     (8, "plus-3m", "بلس ٣ شهور"), (10, "renew-plus", "تجديد بلس")],
]
W, H, GAP, TOP, LABEL = 500, 853, 36, 70, 70
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
num_font, name_font = ImageFont.truetype(BOLD, 34), ImageFont.truetype(BOLD, 28)

sheet = Image.new("RGB", (5 * W + 6 * GAP, len(ROWS) * (TOP + H + LABEL) + GAP), (13, 13, 13))
d = ImageDraw.Draw(sheet)
for r, row in enumerate(ROWS):
    y = GAP + r * (TOP + H + LABEL)
    for i, (n, f, name) in enumerate(row):
        x = GAP + (4 - i) * (W + GAP)
        cx = x + W // 2
        d.ellipse((cx - 28, y, cx + 28, y + 56), fill=(234, 207, 105))
        d.text((cx, y + 28), str(n), font=num_font, fill=(13, 13, 13), anchor="mm")
        card = Image.open(f"new/{f}.png").resize((W, H), Image.LANCZOS)
        sheet.paste(card, (x, y + TOP), card)
        d.text((cx, y + TOP + H + 34), name, font=name_font, fill=(244, 244, 242), anchor="mm", direction="rtl")
sheet.save("new/all-cards.jpg", quality=88)
print("new/all-cards.jpg", sheet.size)
