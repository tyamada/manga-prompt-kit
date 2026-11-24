"""Build mouth ArtMesh source layers with a shared pivot and neutral PSD view."""
from hashlib import sha256
import json
import math
import subprocess

from build_draft import HEIGHT, HERE, SOURCE, SOURCE_HASH, WIDTH, write_psd
from build_mouth_parts_v4 import BOX, INK, INNER, PIVOT, SHAPES, TONGUE, draw_mouth, restore_skin
from build_wrist_overlap_v3 import build_parts, composite

OPEN_PARTS = {
    "Mouth_Open_Tongue": TONGUE,
    "Mouth_Open_Inner": INNER,
    "Mouth_Open_Outline": INK,
}


def coverage_layer(name, rgb, test):
    top, left, bottom, right = BOX
    rx, ry = SHAPES["Mouth_A"]
    pixels = bytearray()
    for y in range(top, bottom):
        for x in range(left, right):
            coverage = 0
            for j in range(4):
                for i in range(4):
                    dx = (x + (i + 0.5) / 4 - PIVOT[0]) / rx
                    dy = (y + (j + 0.5) / 4 - PIVOT[1]) / ry
                    coverage += test(math.hypot(dx, dy), dy)
            pixels.extend((*rgb, round(255 * coverage / 16)) if coverage else (0, 0, 0, 0))
    if not any(pixels[3::4]):
        raise ValueError(f"Empty layer: {name}")
    return name, BOX, pixels


def main():
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected source image")
    decode = ["ffmpeg", "-v", "error", "-i"]
    raw = ["-frames:v", "1", "-pix_fmt", "rgba", "-f", "rawvideo", "-"]
    source = subprocess.check_output([*decode, str(SOURCE), *raw])
    parts, _ = build_parts(source)
    base = restore_skin(source, parts)
    masks = [lambda r, y: r <= 0.80 and y > 0.25,
             lambda r, y: r <= 0.84,
             lambda r, y: r <= 1]
    opened = [coverage_layer(name, rgb, test) for (name, rgb), test in zip(OPEN_PARTS.items(), masks)]
    closed = draw_mouth("Mouth_Closed", *SHAPES["Mouth_Closed"])
    neutral = composite([closed, *base], (0, 0, WIDTH, HEIGHT), {})
    psd = HERE / "nagi-mouth-rig-source-v5.psd"
    write_psd(psd, neutral, [closed, *opened, *base], hidden=OPEN_PARTS)
    if subprocess.check_output([*decode, str(psd), *raw]) != neutral:
        raise ValueError("PSD composite differs from neutral source")
    crop = (490, 210, 540, 241)
    width, height = crop[2] - crop[0], crop[3] - crop[1]
    tiles = [composite(stack, crop, {}) for stack in (
        [closed, *base], [*opened, *base], *[[part] for part in opened],
    )]
    if len({bytes(tile) for tile in tiles}) != len(tiles):
        raise ValueError("Expected distinct component views")
    stride = width * 4
    sheet = b"".join(tile[y*stride:(y+1)*stride] for y in range(height) for tile in tiles)
    preview = HERE / "nagi-mouth-rig-source-v5-preview.png"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pixel_format", "rgba",
        "-video_size", f"{width*len(tiles)}x{height}", "-i", "-",
        "-vf", "scale=iw*4:ih*4:flags=neighbor", "-frames:v", "1", str(preview),
    ], input=sheet, check=True)
    (HERE / "mouth-rig-source-v5-check.json").write_text(json.dumps({
        "pivot_px": list(PIVOT),
        "mouth_parts_top_to_bottom": [closed[0], *OPEN_PARTS],
        "open_parts_hidden_at_rest": list(OPEN_PARTS),
        "preview_order": ["closed", "assembled open", "tongue", "inner", "outline base"],
        "neutral_psd_decode_matches": True,
        "psd_sha256": sha256(psd.read_bytes()).hexdigest(),
        "cubism_import_verified": False,
    }, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
