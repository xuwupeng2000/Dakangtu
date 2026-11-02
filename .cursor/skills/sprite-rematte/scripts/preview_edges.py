"""Lay sprites on a dark backdrop so leftover rims are easy to see.

Usage: python preview_edges.py OUT.png SPRITE.png [SPRITE.png ...]
"""
import sys
from PIL import Image

W, H = 200, 477
BG = (45, 35, 50, 255)


def main():
    out, files = sys.argv[1], sys.argv[2:]
    sheet = Image.new("RGB", (W * len(files), H), BG[:3])
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGBA").resize((W, H), Image.Resampling.LANCZOS)
        tile = Image.alpha_composite(Image.new("RGBA", (W, H), BG), im)
        sheet.paste(tile.convert("RGB"), (i * W, 0))
    sheet.save(out)
    print(out)


if __name__ == "__main__":
    main()
