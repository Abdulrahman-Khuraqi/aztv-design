# Cuts each subscription card out of its old store image (500x500 post), drops the post around it,
# rounds the corners (transparent outside) and enlarges it 4x. Output: old/<id>.png.
# Run from the repo root:  python3 05-design/shared/subscription-cards/cut-old-cards.py   (needs Pillow)
import os
from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
IMG = os.path.join(ROOT, '05-design/new-design/assets/img')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'old')
S = 4  # enlargement

# card boxes in the 500x500 post (x0, y0, x1, y1); the 15-month post has two cards (12 months + 3 free)
BW, GOLD = [(141, 80, 360, 452)], [(142, 75, 358, 442)]
CARDS = {
    'aztv-15m': ('3749112-500x500-jALOT8PWhFqMydBaPXNuQ0Q93IRepaG523qElILR-ad8ae7f8.jpg', [(112, 157, 272, 432), (271, 268, 383, 457)]),
    'aztv-6m': ('24a3c88-500x500-CnDzPvtHcrccqG4U3hjijJC1PjRB6eNgo0yQbebl-a838ae66.png', BW),
    'aztv-3m': ('d9206bc-500x500-Pdq4qFNfyMqdl4t1NifigcGjTWetPoTMx8CrLzJk-22de4025.png', BW),
    'aztv-1m': ('6e336c0-500x500-LIOe2U9NnpSU0ZiQxWe6McRhZdPWXuCg52kFYQk9-c55544a3.png', BW),
    'plus-12m': ('022d3d6-500x500-NFc1bIYqaWt27iJChQiLr5qvf0S2wMbcH5JJTDW6-28f11ae7.jpg', [(108, 155, 275, 440)]),
    'plus-12m-2dev': ('b86e1ef-500x500-1XzgT1KgFRTUDFBSo5M3zlDXu9CWk5QZEQwXsQiI-c7821b77.png', GOLD),
    'plus-6m': ('603594c-500x500-BJo68nE5iCjLjE7ygy0YilBvKNwUNvzVX9JAGSJU-40df055e.png', GOLD),
    'plus-3m': ('2a34a15-500x500-OtAKd64tOXddtIp3XtlCzaNkObz6Rb6j3w99lt03-113b12d2.png', GOLD),
    'renew-aztv': ('75b791b-500x500-HGwrvjICWoLePFOaDdpCm1gKSorTGEA2EUBSqgHv-adbe7116.png', BW),
    'renew-plus': ('f754e7b-500x500-9jf2ocR3CjOLW3sPvXYdAMYVnLmnrqN1cg81nSpA-1f7cd92e.png', GOLD),
}

for key, (src, boxes) in CARDS.items():
    im = Image.open(os.path.join(IMG, src)).convert('RGBA').resize((500 * S, 500 * S), Image.LANCZOS)
    mask = Image.new('L', im.size, 0)
    dr = ImageDraw.Draw(mask)
    for b in boxes:
        dr.rounded_rectangle([v * S for v in b], radius=11 * S, fill=255)
    im.putalpha(mask)
    x0, y0 = min(b[0] for b in boxes), min(b[1] for b in boxes)
    x1, y1 = max(b[2] for b in boxes), max(b[3] for b in boxes)
    im.crop((x0 * S, y0 * S, x1 * S, y1 * S)).save(os.path.join(OUT, key + '.png'))
    print(key)
