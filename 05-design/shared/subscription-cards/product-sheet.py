"""Overview of the ten product images (nine cards and the offer) on one background: python3 product-sheet.py b|e  ->  product-images/overview-<opt>.jpg
Run after node render-products.cjs. Needs Pillow."""
import sys
from PIL import Image
opt = sys.argv[1] if len(sys.argv) > 1 else "b"
ORDER = ["aztv-6m", "aztv-3m", "aztv-1m", "renew-aztv", "aztv-15m", "plus-12m", "plus-12m-2dev", "plus-6m", "plus-3m", "renew-plus"]
S, GAP = 500, 16
cols = 5
rows = (len(ORDER) + cols - 1) // cols
sheet = Image.new("RGB", (cols * S + (cols + 1) * GAP, rows * S + (rows + 1) * GAP), (13, 13, 13))
for i, name in enumerate(ORDER):
    im = Image.open(f"product-images/{opt}/{name}.jpg").resize((S, S), Image.LANCZOS)
    sheet.paste(im, (GAP + (i % cols) * (S + GAP), GAP + (i // cols) * (S + GAP)))
sheet.save(f"product-images/overview-{opt}.jpg", quality=88)
print(f"product-images/overview-{opt}.jpg", sheet.size)
