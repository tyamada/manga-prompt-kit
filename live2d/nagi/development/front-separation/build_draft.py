"""Build a neutral-pose PSD draft from the unchanged Nagi PNG.

Requires Python 3 and FFmpeg. The masks isolate visible hands only. The original
alpha, including the soft fringe, is kept for exact neutral recomposition.
"""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import struct
import subprocess

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent.parent / "source" / "nagi-front-winter-indoor-v1.png"
WIDTH, HEIGHT = 1024, 1536
SOURCE_HASH = "425321d96a4ddc34d28aff130bf47a0f3b828117084bc4f49c6336bbcc910a5d"

# Anatomical sides in a front view. Follow the underside of each cuff.
HANDS = {
    "Hand_R_visible_draft": [(215, 706), (264, 711), (279, 718), (295, 724), (314, 728), (314, 869), (215, 869)],
    "Hand_L_visible_draft": [(710, 728), (729, 723), (744, 718), (758, 711), (803, 706), (803, 869), (710, 869)],
}


def inside(x, y, polygon):
    crossings = 0
    for (ax, ay), (bx, by) in zip(polygon, polygon[1:] + polygon[:1]):
        if (ay > y) != (by > y) and x < ax + (y - ay) * (bx - ax) / (by - ay):
            crossings += 1
    return crossings % 2 == 1


def make_layers(source):
    composite = source.copy()
    layers = []
    for name, polygon in HANDS.items():
        left = min(x for x, _ in polygon)
        top = min(y for _, y in polygon)
        right = max(x for x, _ in polygon)
        bottom = max(y for _, y in polygon)
        pixels = bytearray()
        for y in range(top, bottom):
            for x in range(left, right):
                index = (y * WIDTH + x) * 4
                if inside(x + 0.5, y + 0.5, polygon):
                    pixels.extend(source[index:index + 4])
                    composite[index:index + 4] = bytes(4)
                else:
                    pixels.extend(bytes(4))
        layers.append((name, (top, left, bottom, right), pixels))

    restored = composite.copy()
    for name, (top, left, bottom, right), pixels in layers:
        for y in range(top, bottom):
            for x in range(left, right):
                if inside(x + 0.5, y + 0.5, HANDS[name]):
                    index = (y * WIDTH + x) * 4
                    part = ((y - top) * (right - left) + x - left) * 4
                    restored[index:index + 4] = pixels[part:part + 4]
    if restored != source:
        raise ValueError("Neutral reconstruction differs from source pixels")
    return layers + [("Base_remaining_draft", (0, 0, HEIGHT, WIDTH), composite)]


def write_psd(path, source, layers, hidden=()):
    def pack(fmt, *values):
        return struct.pack(">" + fmt, *values)

    def section(data):
        return pack("I", len(data)) + data

    # RGB, 8-bit, four raw channels per layer. The negative count marks
    # the fourth channel in the merged image as merged transparency.
    channel_ids = (0, 1, 2, -1)
    records = bytearray()
    channels = bytearray()
    for name, bounds, pixels in layers:
        records += pack("iiiiH", *bounds, len(channel_ids))
        for index, channel_id in enumerate(channel_ids):
            plane = pixels[index::4]
            records += pack("hI", channel_id, len(plane) + 2)
            channels += pack("H", 0) + plane
        label = name.encode("ascii")
        pascal = bytes([len(label)]) + label
        extra = pack("II", 0, 0) + pascal + bytes(-len(pascal) % 4)
        records += b"8BIMnorm" + pack("BBBB", 255, 0, 2 if name in hidden else 0, 0) + section(extra)
    layer_info = pack("h", -len(layers)) + records + channels
    layer_info += bytes(len(layer_info) % 2)
    header = b"8BPS" + pack("H6xHIIHH", 1, 4, HEIGHT, WIDTH, 8, 3)
    def unicode_string(value):
        return pack("I", len(value)) + value.encode("utf-16-be")

    version_info = (
        pack("IB", 1, 1)
        + unicode_string("manga-prompt-kit")
        + unicode_string("manga-prompt-kit")
        + pack("I", 1)
    )
    resources = b"8BIM" + pack("H2x", 1057) + section(version_info)
    resources += bytes(len(version_info) % 2)
    with path.open("wb") as handle:
        handle.write(header + pack("I", 0) + section(resources))
        handle.write(section(section(layer_info) + pack("I", 0)))
        handle.write(pack("H", 0))
        for index in range(4):
            handle.write(source[index::4])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE)
    args = parser.parse_args()
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected source PNG")
    raw = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(SOURCE), "-frames:v", "1",
        "-pix_fmt", "rgba", "-f", "rawvideo", "-",
    ])
    if len(raw) != WIDTH * HEIGHT * 4:
        raise ValueError("Unexpected source dimensions")
    source = bytearray(raw)
    layers = make_layers(source)
    alpha = Counter(source[3::4])
    args.output.mkdir(parents=True, exist_ok=True)
    psd = args.output / "nagi-front-hands-draft.psd"
    write_psd(psd, source, layers)
    report = {
        "source_sha256": SOURCE_HASH,
        "canvas": [WIDTH, HEIGHT],
        "alpha_total": sum(alpha.values()),
        "alpha_zero": alpha[0],
        "alpha_1_to_15": sum(alpha[i] for i in range(1, 16)),
        "alpha_16_to_127": sum(alpha[i] for i in range(16, 128)),
        "alpha_128_to_253": sum(alpha[i] for i in range(128, 254)),
        "alpha_254": alpha[254],
        "alpha_255": alpha[255],
        "layers_top_to_bottom": [name for name, _, _ in layers],
        "neutral_partition_rgba_matches_source": True,
        "psd_sha256": sha256(psd.read_bytes()).hexdigest(),
        "cubism_import_verified": False,
        "hidden_art_added": False,
    }
    (args.output / "draft-check.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
