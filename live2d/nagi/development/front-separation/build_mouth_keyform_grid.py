"""Create visual and numerical calibration targets for the Cubism mouth warp."""
from hashlib import sha256
import json
import subprocess

from build_draft import HERE, SOURCE, SOURCE_HASH
from build_lipsync_preview import WIDTH_KEYS, interpolate
from build_mouth_parts_v4 import PIVOT, SHAPES, draw_mouth, restore_skin
from build_wrist_overlap_v3 import build_parts, composite

FORMS = [-1.0, *sorted([0.0, *(value for value, _ in WIDTH_KEYS)]), 1.0]
OPENINGS = [0.0, 0.25, 0.5, 1.0]
CROP = (491, 213, 540, 238)


def dimensions(opening, form):
    closed_x, closed_y = SHAPES["Mouth_Closed"]
    widths = [(value, SHAPES["Mouth_" + vowel][0]) for value, vowel in WIDTH_KEYS]
    width = interpolate(widths, form)
    return closed_x + min(1, opening / 0.25) * (width - closed_x), closed_y + opening * 4.1


def main():
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected original image")
    source = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(SOURCE), "-frames:v", "1",
        "-pix_fmt", "rgba", "-f", "rawvideo", "-",
    ])
    parts, _ = build_parts(source)
    base = restore_skin(source, parts)
    width, height = CROP[2] - CROP[0], CROP[3] - CROP[1]
    all_rows, keys = [], []
    for opening in OPENINGS:
        tiles = []
        for form in FORMS:
            rx, ry = dimensions(opening, form)
            name = "Mouth_Closed" if opening == 0 else "Mouth_Interpolated"
            tiles.append(composite([draw_mouth(name, rx, ry), *base], CROP, {}))
            keys.append({
                "ParamMouthOpenY": opening, "ParamMouthForm": form,
                "half_width_px": round(rx, 4), "half_height_px": round(ry, 4),
                "outline_bbox_px": [round(v, 4) for v in (
                    PIVOT[0] - rx, PIVOT[1] - ry, PIVOT[0] + rx, PIVOT[1] + ry)],
            })
        if opening == 0 and len({bytes(tile) for tile in tiles}) != 1:
            raise ValueError("Closed-mouth pose must stay fixed across all form values")
        stride = width * 4
        all_rows.extend(
            tile[y * stride:(y + 1) * stride]
            for y in range(height) for tile in tiles
        )
    png = HERE / "nagi-mouth-keyform-grid.png"
    size = f"{width * len(FORMS)}x{height * len(OPENINGS)}"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pixel_format", "rgba",
        "-video_size", size, "-i", "-", "-vf", "scale=iw*3:ih*3:flags=neighbor",
        "-frames:v", "1", str(png),
    ], input=b"".join(all_rows), check=True)
    (HERE / "nagi-mouth-keyform-targets.json").write_text(
        json.dumps({
            "purpose": "Visual calibration targets, in source PNG coordinates",
            "source_sha256": SOURCE_HASH,
            "pivot_px": list(PIVOT),
            "row_ParamMouthOpenY": OPENINGS,
            "column_ParamMouthForm": FORMS,
            "keys": keys,
            "preview_sha256": sha256(png.read_bytes()).hexdigest(),
            "cubism_keyforms_applied": False,
        }, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
