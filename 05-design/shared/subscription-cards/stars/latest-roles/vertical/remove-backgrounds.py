"""Create identity-preserving transparent cutouts from the eight approved card portraits."""

from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from rembg import new_session, remove
import numpy as np
from scipy.ndimage import label


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "transparent"
WHITE_ORIGINALS = ROOT.parents[2] / "photos" / "originals"
OUTPUT.mkdir(exist_ok=True)

SOURCE_FILES = sorted(
    path
    for path in ROOT.glob("*.jpg")
    if path.name != "contact-sheet-vertical.jpg"
)

session = new_session("isnet-general-use")

for source_path in SOURCE_FILES:
    source_bytes = source_path.read_bytes()
    result = remove(
        source_bytes,
        session=session,
        alpha_matting=False,
        post_process_mask=True,
        force_return_bytes=True,
    )
    with Image.open(BytesIO(result)) as cutout:
        rgba = cutout.convert("RGBA")
        if rgba.size != (1200, 1500):
            rgba = rgba.resize((1200, 1500), Image.Resampling.LANCZOS)
        # Remove detached mask specks while preserving the main person and soft edge alpha.
        pixels = np.array(rgba)
        components, count = label(pixels[:, :, 3] > 8)
        if count > 1:
            areas = np.bincount(components.ravel())
            areas[0] = 0
            largest = int(areas.argmax())
            pixels[:, :, 3][(components != 0) & (components != largest)] = 0
            rgba = Image.fromarray(pixels, "RGBA")
        rgba.save(OUTPUT / f"{source_path.stem}.png", optimize=True)


def checkerboard(size, cell=24):
    canvas = Image.new("RGB", size, "#f1f1f1")
    draw = ImageDraw.Draw(canvas)
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#d7d7d7")
    return canvas


def make_sheet(items, destination, columns, thumb_size, background, labels):
    margin = 18
    label_height = 36
    rows = (len(items) + columns - 1) // columns
    sheet = Image.new(
        "RGB",
        (
            columns * thumb_size[0] + (columns + 1) * margin,
            rows * (thumb_size[1] + label_height) + (rows + 1) * margin,
        ),
        "#111111",
    )
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=16)

    for index, item in enumerate(items):
        row, column = divmod(index, columns)
        x = margin + column * (thumb_size[0] + margin)
        y = margin + row * (thumb_size[1] + label_height + margin)
        tile = checkerboard(thumb_size) if background == "checker" else Image.new("RGB", thumb_size, "white")
        with Image.open(item) as image:
            image = image.convert("RGBA")
            image.thumbnail(thumb_size, Image.Resampling.LANCZOS)
            px = (thumb_size[0] - image.width) // 2
            py = (thumb_size[1] - image.height) // 2
            tile.paste(image, (px, py), image)
        sheet.paste(tile, (x, y))
        draw.text((x, y + thumb_size[1] + 9), labels[index], fill="white", font=font)

    sheet.save(destination, "JPEG", quality=92, optimize=True, progressive=True)


cutouts = sorted(OUTPUT.glob("*.png"))
make_sheet(
    cutouts,
    OUTPUT / "contact-sheet-transparent.jpg",
    columns=2,
    thumb_size=(360, 450),
    background="checker",
    labels=[f"{index:02d}  {path.stem.split('-', 2)[2]}" for index, path in enumerate(cutouts, 1)],
)

white_originals = sorted(WHITE_ORIGINALS.glob("*.*"))
combined = cutouts + white_originals
combined_labels = [f"T{index:02d}  {path.stem[:22]}" for index, path in enumerate(cutouts, 1)]
combined_labels += [f"W{index:02d}  {path.stem[:22]}" for index, path in enumerate(white_originals, 1)]
make_sheet(
    combined,
    OUTPUT / "contact-sheet-with-white-background-images.jpg",
    columns=4,
    thumb_size=(250, 312),
    background="white",
    labels=combined_labels,
)

print(f"Created {len(cutouts)} transparent cutouts in {OUTPUT}")
