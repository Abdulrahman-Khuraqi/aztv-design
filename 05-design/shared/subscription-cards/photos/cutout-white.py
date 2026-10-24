"""Cut a photo out of its plain white background (no AI model needed).
Usage: python3 cutout-white.py originals/001-....jpg [more files]  ->  transparent/<name>.png
Floods inward from the image border through near-white pixels, so white shirts and teeth inside the
person are kept. The edge is eroded 1 px and softened, and white fringe is removed from edge pixels."""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import label, binary_erosion

OUT = Path(__file__).resolve().parent / "transparent"
OUT.mkdir(exist_ok=True)
LIMIT = 238  # a pixel counts as background when its darkest channel is at least this bright

for src in sys.argv[1:]:
    rgb = np.asarray(Image.open(src).convert("RGB")).astype(np.float32)
    near_white = rgb.min(axis=2) >= LIMIT
    regions, _ = label(near_white)
    border = np.unique(np.concatenate([regions[0], regions[-1], regions[:, 0], regions[:, -1]]))
    bg = np.isin(regions, border[border != 0])
    person = ~bg
    person = binary_erosion(person, iterations=1)
    alpha = Image.fromarray((person * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.1))
    a = np.asarray(alpha).astype(np.float32) / 255
    # un-mix the white that bled into soft edge pixels
    edge = (a > 0) & (a < 1)
    out = rgb.copy()
    out[edge] = np.clip((rgb[edge] - 255 * (1 - a[edge, None])) / np.maximum(a[edge, None], 0.35), 0, 255)
    rgba = np.dstack([out, a * 255]).astype(np.uint8)
    Image.fromarray(rgba, "RGBA").save(OUT / (Path(src).stem + ".png"), optimize=True)
    print(OUT / (Path(src).stem + ".png"))
