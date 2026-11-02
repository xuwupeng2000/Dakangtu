"""Re-cut sprites whose old cutout left a teal backdrop rim.

Each sprite is laid back onto its original backdrop color, matted again with
BiRefNet, edge colors are decontaminated with pymatting, and backdrop-tinted
strands inside dark hair are pulled back to the local hair color.

Usage: python rematte_sprites.py SRC_DIR DST_DIR
SRC_DIR and DST_DIR may be the same; subfolders are kept.
"""
import os
import sys
import glob
import numpy as np
from PIL import Image
from scipy import ndimage
from rembg import new_session, remove
from pymatting import estimate_foreground_ml


def backdrop_color(rgb, alpha):
    """Median color of the teal rim in the outer 8 px, or None if there is no rim."""
    d = ndimage.distance_transform_cdt(alpha > 0, metric="taxicab")
    r, g, b = [rgb[:, :, i] for i in range(3)]
    teal = (alpha > 50) & (g > r + 20) & (b > r + 10) & (np.abs(g - b) < 42) & (r < 110) & (g > 80)
    edge = teal & (d >= 1) & (d <= 8)
    if edge.sum() < 200:
        return None
    return np.median(rgb[edge], 0)


def despill_hair(rgb, alpha):
    """Recolor bright teal strands that sit inside dark hair; leave teal clothing alone."""
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    teal = (g > r + 0.12) & (b > r + 0.08) & (np.abs(g - b) < 0.18) & (g > 0.35)
    local = ndimage.median_filter(rgb.mean(2), size=15)
    loose_teal = (g > r + 0.06) & (b > r + 0.04) & (np.abs(g - b) < 0.2) & (alpha > 0.3)
    teal_share = ndimage.uniform_filter(loose_teal.astype(np.float32), 31)
    in_hair = (local < 0.22) & (teal_share < 0.3) & (alpha > 0.05)
    hair = teal & in_hair
    if not hair.any():
        return rgb
    hair = ndimage.binary_dilation(hair, iterations=1) & in_hair
    out = rgb.copy()
    dark = ((~teal) & (alpha > 0.5)).astype(np.float32)
    weight = ndimage.gaussian_filter(dark, 4)
    for c in range(3):
        avg = ndimage.gaussian_filter(rgb[:, :, c] * dark, 4) / np.maximum(weight, 1e-4)
        out[:, :, c][hair] = avg[hair]
    return out


def rematte(a, session):
    rgb = a[:, :, :3].astype(np.float32)
    B = backdrop_color(rgb, a[:, :, 3])
    if B is None:
        return a
    al0 = a[:, :, 3:4].astype(np.float32) / 255.0
    comp = rgb * al0 + B * (1.0 - al0)
    mask = remove(Image.fromarray(comp.astype(np.uint8)), session=session, only_mask=True)
    m = np.array(mask.convert("L")).astype(np.float64) / 255.0
    m = np.minimum(m, al0[:, :, 0])
    F = estimate_foreground_ml(comp / 255.0, m)
    F = despill_hair(F, m)
    out = np.dstack([np.clip(F * 255.0, 0, 255), m * 255.0]).round().astype(np.uint8)
    out[out[:, :, 3] < 4] = 0
    return out


def main():
    src, dst = sys.argv[1], sys.argv[2]
    session = new_session("birefnet-general")
    for p in sorted(glob.glob(os.path.join(src, "**", "*.png"), recursive=True)):
        rel = os.path.relpath(p, src)
        out = rematte(np.array(Image.open(p).convert("RGBA")), session)
        target = os.path.join(dst, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        Image.fromarray(out, "RGBA").save(target)
        print(rel, flush=True)


if __name__ == "__main__":
    main()
