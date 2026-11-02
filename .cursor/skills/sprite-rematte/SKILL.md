---
name: sprite-rematte
description: Removes the green/teal halo around cut-out galgame character sprites by re-matting them with BiRefNet and pymatting. Use when Ren'Py sprites show a colored outline, green edge, fringe, or halo, when the user asks for better 抠图 / 去边 / 绿边, or after generating new sprites on a colored backdrop.
---

# Sprite re-matte (去绿边)

## Why color-only fixes fail

The old rembg + isnet-anime cutouts left a 6–8 px rim of the generation backdrop (teal, about RGB 56–68 / 105–137 / 100–130) that is nearly opaque, plus backdrop showing through gaps in the hair.

- Deleting pixels by color or eroding the edge does not work. Rita's hair is gray-teal and Ami's top is dark green, so a tight threshold leaves the rim and a loose one cuts holes in hair, fingers and clothes.
- Running a matting model on the transparent PNG does not work either. The rim is already part of the subject.

What works: rebuild the original backdrop, matte again, then decontaminate.

1. Detect the backdrop color from the teal pixels in the outer 8 px.
2. Composite the sprite back onto that solid color to recover the "generated on teal" image.
3. Matte with **BiRefNet** (`rembg` session `birefnet-general`). It treats the rim and the hair gaps as background.
4. Decontaminate edge colors with **pymatting** `estimate_foreground_ml`.
5. Inside dark hair only, pull bright teal strands back to the local hair color. Teal clothing stays untouched.
6. Clamp the new alpha to the old alpha, so nothing that was removed comes back.

## Run

Tools environment (rembg[cpu], pymatting, scipy): `~/ComfyUI-Shared/tools-venv/.venv`. If it is missing:

```bash
mkdir -p ~/ComfyUI-Shared/tools-venv && cd ~/ComfyUI-Shared/tools-venv
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python "rembg[cpu]" pymatting scipy
```

**Always start from untouched originals, never from a previously fixed file.** Back them up before the first run.

```bash
PY=~/ComfyUI-Shared/tools-venv/.venv/bin/python
SKILL=.cursor/skills/sprite-rematte/scripts
$PY $SKILL/rematte_sprites.py ~/ComfyUI-Shared/sprite_backup_original game/images/characters
```

- About 11 s per 664×1584 sprite on the M6 Mac. The first run downloads BiRefNet (about 1 GB) into `~/.u2net`. Run it in the background for more than a few files.
- Sprites with no teal rim are passed through unchanged.
- Test on 2–3 files in a temp folder before the full batch.

## Verify

Look at the result on a dark backdrop, not on white:

```bash
$PY $SKILL/preview_edges.py /tmp/sheet.png game/images/characters/ami/ami_smile.png game/images/characters/rita/sprite_sweet-smile_0001.png
```

Then read `/tmp/sheet.png`, and also zoom crops of the hair, hands and sleeves. Check:

- No teal line around the outline.
- Fingers and thin parts are intact.
- Ami's green top keeps its shading (no hard blotches).

Then run Ren'Py lint: `~/Applications/renpy-8.5.3-sdkarm/renpy.sh . lint`.

Known leftover: a few hair strands right against Ami's green sleeve keep a slight teal tint. Pushing harder damages the sleeve, so it is left as is.

## Project facts

- Originals backup: `~/ComfyUI-Shared/sprite_backup_original/` (72 PNGs, `ami/` and `rita/`).
- Fixed sprites: `game/images/characters/`.

## New sprites

Generate on a flat mid-gray backdrop instead of green or teal, then matte with BiRefNet and decontaminate (steps 3–4). The backdrop reconstruction and hair despill are only needed for the old teal cutouts.
