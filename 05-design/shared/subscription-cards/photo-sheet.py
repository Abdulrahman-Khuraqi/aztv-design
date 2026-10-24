"""Sheet of every face photo we have, with its id and the card it is on, for the client to pick which to drop.
Run from this folder:  python3 photo-sheet.py  ->  photos/all-photos.jpg   (needs Pillow with raqm)"""
import glob, re
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# which card each photo is on (card numbers as in README.md); keep in step with CARDS in card.html
# rejected photos are in photos/rejected/ and are not shown
USED = {"010": 2, "013": 2, "005": 3, "009": 3, "004": 4, "015": 4, "006": 6, "002": 6, "011": 8, "016": 8,
        "017": 5, "018": 5, "020": 7, "019": 7}
files = [(Path(f).stem[:3], f) for f in sorted(glob.glob("photos/transparent/*.png"))]
files += [("S" + Path(f).stem[:2], f) for f in sorted(glob.glob("stars/latest-roles/vertical/transparent/0*.png"))]

COLS, CW, CH, PAD = 6, 400, 560, 24
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
id_font, tag_font = ImageFont.truetype(BOLD, 40), ImageFont.truetype(BOLD, 26)
rows = -(-len(files) // COLS)
sheet = Image.new("RGB", (COLS * (CW + PAD) + PAD, rows * (CH + PAD) + PAD), (13, 13, 13))
d = ImageDraw.Draw(sheet)
for i, (pid, f) in enumerate(files):
    x, y = PAD + (i % COLS) * (CW + PAD), PAD + (i // COLS) * (CH + PAD)
    d.rounded_rectangle((x, y, x + CW, y + CH), 18, fill=(52, 52, 50))
    im = Image.open(f).convert("RGBA")
    im.thumbnail((CW - 20, CH - 90), Image.LANCZOS)
    sheet.paste(im, (x + (CW - im.width) // 2, y + 76), im)
    d.text((x + 18, y + 14), pid, font=id_font, fill=(234, 207, 105))
    card = USED.get(pid)
    tag, col = (f"card {card}", (244, 244, 242)) if card else ("not used", (150, 150, 146))
    d.text((x + CW - 18, y + 26), tag, font=tag_font, fill=col, anchor="ra")
sheet.save("photos/all-photos.jpg", quality=86)
print("photos/all-photos.jpg", sheet.size, len(files), "photos")
