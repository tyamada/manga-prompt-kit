"""Prepare unrigged closed and vowel mouth shapes for the Nagi PSD."""
from hashlib import sha256
import json
import math
import subprocess

from build_draft import HEIGHT, HERE, SOURCE, SOURCE_HASH, WIDTH, write_psd
from build_wrist_overlap_v3 import build_parts, composite

# Bounding rectangle in source coordinates. Shapes share the same pivot.
BOX = (216, 495, 237, 536)
PIVOT = (515.5, 224.8)
# Half-width and half-height, progressively from narrow to open forms.
SHAPES = {
    "Mouth_Closed": (7.0, 0.64),
    "Mouth_A": (9.5, 4.7),
    "Mouth_I": (12.0, 1.6),
    "Mouth_U": (5.0, 2.3),
    "Mouth_E": (10.4, 3.0),
    "Mouth_O": (5.9, 4.2),
}
INK = (131, 92, 81)
INNER = (112, 55, 55)
TONGUE = (194, 116, 117)


def draw_mouth(name, rx, ry):
    top, left, bottom, right = BOX
    pixels = bytearray()
    for y in range(top, bottom):
        for x in range(left, right):
            hits = []
            for j in range(4):
                for i in range(4):
                    dx = (x + (i + 0.5) / 4 - PIVOT[0]) / rx
                    dy = (y + (j + 0.5) / 4 - PIVOT[1]) / ry
                    radius = math.hypot(dx, dy)
                    if radius <= 1:
                        if name == "Mouth_Closed" or radius > 0.82:
                            hits.append(INK)
                        elif dy > 0.25 and ry >= 3:
                            hits.append(TONGUE)
                        else:
                            hits.append(INNER)
            if hits:
                pixels.extend(round(sum(c[k] for c in hits) / len(hits)) for k in range(3))
                pixels.append(round(len(hits) / 16 * 255))
            else:
                pixels.extend(bytes(4))
    return name, BOX, pixels


def restore_skin(source, layers):
    # Replace the cut-out smile with skin interpolated from the two adjacent
    # rows of the same face. Keep the original alpha and surrounding pixels.
    restored = []
    for name, bounds, pixels in layers:
        if name == "Mouth_visible":
            continue
        if name == "Face_visible":
            top, left, _, right = bounds
            for y in range(219, 229):
                weight = (y - 218) / 11
                for x in range(499, 533):
                    offset = ((y - top) * (right - left) + x - left) * 4
                    above = (218 * WIDTH + x) * 4
                    below = (229 * WIDTH + x) * 4
                    for c in range(3):
                        pixels[offset + c] = round(source[above+c] * (1-weight) + source[below+c] * weight)
                    pixels[offset + 3] = source[(y * WIDTH + x) * 4 + 3]
        restored.append((name, bounds, pixels))
    return restored


def main():
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected source PNG")
    source = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(SOURCE), "-frames:v", "1",
        "-pix_fmt", "rgba", "-f", "rawvideo", "-",
    ])
    if len(source) != WIDTH * HEIGHT * 4:
        raise ValueError("Unexpected canvas")
    parts, _ = build_parts(source)
    base = restore_skin(source, parts)
    mouths = [draw_mouth(name, *size) for name, size in SHAPES.items()]
    neutral = composite([mouths[0], *base], (0, 0, WIDTH, HEIGHT), {})
    psd = HERE / "nagi-mouth-parts-v4.psd"
    write_psd(psd, neutral, [*mouths, *base], hidden=list(SHAPES)[1:])

    box = (479, 198, 549, 252)
    width, height = box[2] - box[0], box[3] - box[1]
    tiles = [composite([mouth, *base], box, {}) for mouth in mouths]
    if len({sha256(tile).digest() for tile in tiles}) != len(mouths):
        raise ValueError("Mouth previews not distinct")
    row_bytes = width * 4
    sheet = b"".join(
        tile[y*row_bytes:(y+1)*row_bytes]
        for start in (0, 3) for y in range(height) for tile in tiles[start:start+3]
    )
    preview = HERE / "nagi-mouth-parts-v4-comparison.png"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pixel_format", "rgba",
        "-video_size", f"{width*3}x{height*2}", "-i", "-",
        "-vf", "scale=840:432:flags=neighbor", "-frames:v", "1", str(preview),
    ], input=sheet, check=True)
    actual = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(psd), "-frames:v", "1",
        "-pix_fmt", "rgba", "-f", "rawvideo", "-",
    ])
    if actual != neutral:
        raise ValueError("PSD merged image differs from neutral artwork")
    (HERE / "mouth-parts-v4-check.json").write_text(json.dumps({
        "source_sha256": SOURCE_HASH,
        "psd_sha256": sha256(psd.read_bytes()).hexdigest(),
        "mouth_layers": list(SHAPES),
        "hidden_by_default_in_psd": list(SHAPES)[1:],
        "six_distinct_previews": True,
        "decoded_psd_matches_neutral": True,
        "cubism_import_verified": False,
    }, indent=2) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
