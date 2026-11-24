"""Isolate visible artwork for the second, neutral-pose separation draft."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess

from build_draft import HANDS, HEIGHT, HERE, SOURCE, SOURCE_HASH, WIDTH, inside, write_psd

# R/L denote the character's own sides. The part list also defines priority
# where a face or clothing mask intersects a broader mask.
MASKS = {
    **HANDS,
    "Eye_R_visible": [(453, 167), (462, 161), (478, 160), (494, 163), (501, 168), (494, 180), (478, 184), (463, 180)],
    "Eye_L_visible": [(534, 169), (545, 163), (558, 160), (572, 161), (580, 166), (574, 177), (560, 184), (545, 182)],
    "Mouth_visible": [(499, 219), (533, 219), (533, 229), (499, 229)],
    "Face_visible": [(426, 157), (437, 157), (455, 162), (477, 131), (500, 108), (498, 149), (488, 170), (503, 175), (519, 168), (534, 151), (537, 82), (552, 102), (572, 152), (582, 162), (596, 156), (603, 177), (591, 194), (572, 206), (558, 230), (542, 246), (515, 260), (487, 246), (468, 230), (456, 208), (438, 194), (427, 183)],
    "Ribbon_visible": [(458, 328), (475, 320), (493, 318), (506, 324), (521, 324), (537, 318), (553, 321), (570, 327), (569, 344), (559, 361), (552, 365), (564, 378), (530, 400), (514, 363), (499, 399), (464, 380), (477, 366), (468, 367), (460, 350)],
    "Hair_side_R_visible": [(420, 148), (442, 152), (453, 180), (457, 222), (453, 296), (445, 362), (441, 427), (443, 465), (455, 505), (430, 488), (418, 470), (414, 426), (419, 352), (423, 284), (421, 212)],
    "Hair_side_L_visible": [(570, 152), (594, 149), (607, 227), (605, 300), (605, 358), (609, 426), (608, 470), (585, 503), (571, 505), (582, 473), (585, 431), (578, 349), (575, 284), (577, 232)],
    "Hair_crown_visible": [(361, 0), (659, 0), (645, 161), (600, 159), (588, 167), (570, 159), (551, 188), (478, 188), (453, 164), (428, 159), (388, 161)],
    "Skirt_visible": [(438, 536), (472, 535), (510, 539), (551, 537), (586, 534), (603, 566), (625, 609), (650, 669), (673, 749), (684, 810), (664, 823), (630, 835), (579, 843), (510, 845), (444, 842), (394, 831), (361, 824), (339, 815), (349, 756), (373, 675), (400, 610), (421, 565)],
    "Leg_R_visible": [(339, 814), (510, 840), (526, 845), (510, 986), (511, 1536), (330, 1536), (329, 871)],
    "Leg_L_visible": [(526, 840), (690, 810), (696, 1536), (511, 1536), (510, 986)],
}


def partition(source):
    remaining = bytearray(source)
    layers = []
    for name, polygon in MASKS.items():
        left, right = min(x for x, _ in polygon), max(x for x, _ in polygon)
        top, bottom = min(y for _, y in polygon), max(y for _, y in polygon)
        pixels = bytearray(4 * (right - left) * (bottom - top))
        for y in range(top, bottom):
            for x in range(left, right):
                offset = (y * WIDTH + x) * 4
                if remaining[offset + 3] and inside(x + 0.5, y + 0.5, polygon):
                    tile = ((y - top) * (right - left) + x - left) * 4
                    pixels[tile:tile + 4] = remaining[offset:offset + 4]
                    remaining[offset:offset + 4] = bytes(4)
        if not any(pixels[3::4]):
            raise ValueError(f"Empty layer: {name}")
        layers.append((name, (top, left, bottom, right), pixels))
    layers.append(("Torso_sleeves_back_hair_remaining", (0, 0, HEIGHT, WIDTH), remaining))
    return layers


def verify_partition(source, layers):
    restored = bytearray(len(source))
    for name, (top, left, bottom, right), pixels in layers:
        for y in range(top, bottom):
            for x in range(left, right):
                tile = ((y - top) * (right - left) + x - left) * 4
                if pixels[tile + 3]:
                    offset = (y * WIDTH + x) * 4
                    if restored[offset + 3]:
                        raise ValueError(f"Visible overlap at {(x, y)} in {name}")
                    restored[offset:offset + 4] = pixels[tile:tile + 4]
    visible_source = bytearray(source)
    for offset in range(0, len(source), 4):
        if not source[offset + 3]:
            visible_source[offset:offset + 4] = bytes(4)
    if restored != visible_source:
        raise ValueError("Layer reconstruction differs from visible source pixels")


def main():
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected source PNG")
    decode = ["ffmpeg", "-v", "error", "-i"]
    rgba = ["-frames:v", "1", "-pix_fmt", "rgba", "-f", "rawvideo", "-"]
    source = subprocess.check_output([*decode, str(SOURCE), *rgba])
    if len(source) != WIDTH * HEIGHT * 4:
        raise ValueError("Unexpected canvas size")
    layers = partition(source)
    verify_partition(source, layers)
    output = HERE / "nagi-front-separation-v2.psd"
    write_psd(output, source, layers)
    if subprocess.check_output([*decode, str(output), *rgba]) != source:
        raise ValueError("PSD composite differs from source")
    report = {
        "source_sha256": SOURCE_HASH,
        "psd_sha256": sha256(output.read_bytes()).hexdigest(),
        "layer_visible_pixels": {name: sum(a > 0 for a in pixels[3::4]) for name, _, pixels in layers},
        "visible_layer_reconstruction_matches": True,
        "decoded_psd_composite_rgba_matches": True,
        "occluded_art_added": False,
    }
    (HERE / "separation-v2-check.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
