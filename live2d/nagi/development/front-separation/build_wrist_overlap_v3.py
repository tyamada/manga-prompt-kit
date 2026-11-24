"""Add wrist overlap behind the cuffs and render a small movement comparison."""
from hashlib import sha256
import json
import subprocess

from build_draft import HEIGHT, HERE, SOURCE, SOURCE_HASH, WIDTH, inside, write_psd
from build_separation_v2 import MASKS, partition

WRISTS = {
    "Hand_R_visible_draft": [(261, 715), (274, 692), (305, 704), (305, 731), (282, 726)],
    "Hand_L_visible_draft": [(718, 731), (716, 706), (751, 692), (760, 715), (741, 726)],
}
SHIFT = {"Hand_R_visible_draft": (-2, 5), "Hand_L_visible_draft": (2, 5)}


def composite(layers, box, shifts):
    left, top, right, bottom = box
    width, height = right - left, bottom - top
    output = bytearray(width * height * 4)
    for name, (y0, x0, y1, x1), pixels in reversed(layers):
        dx, dy = shifts.get(name, (0, 0))
        for y in range(max(top, y0 + dy), min(bottom, y1 + dy)):
            for x in range(max(left, x0 + dx), min(right, x1 + dx)):
                src = ((y - dy - y0) * (x1 - x0) + x - dx - x0) * 4
                alpha = pixels[src + 3]
                if not alpha:
                    continue
                dst = ((y - top) * width + x - left) * 4
                if not output[dst + 3] or alpha == 255:
                    output[dst:dst + 4] = pixels[src:src + 4]
                    continue
                back = output[dst + 3] * (255 - alpha)
                weight = alpha * 255 + back
                for c in range(3):
                    output[dst + c] = round(
                        (pixels[src + c] * alpha * 255 + output[dst + c] * back) / weight
                    )
                output[dst + 3] = round(weight / 255)
    return output


def build_parts(source):
    # Extend the hand canvas above the cuff seam. Reserve the cuff pixels
    # for the residual layer, which will be stacked above the wrist.
    MASKS["Hand_R_visible_draft"] = [
        (215, 690), (264, 710), (276, 716), (295, 723), (304, 725),
        (314, 729), (314, 869), (215, 869),
    ]
    MASKS["Hand_L_visible_draft"] = [
        (710, 729), (719, 725), (731, 722), (745, 718), (758, 711),
        (803, 690), (803, 869), (710, 869),
    ]
    layers = partition(source)
    # Full-canvas hand layers allow the new pixels to extend across their
    # original crop bounds. Cropping is restricted to the wrist/hand area.
    painted = {}
    for name, (top, left, bottom, right), pixels in layers[:2]:
        new_top = 690
        row = (right - left) * 4
        result = bytearray((bottom - new_top) * row)
        result[(top - new_top) * row:] = pixels
        count = 0
        for y in range(new_top, 726):
            for x in range(left, right):
                idx = ((y - new_top) * (right - left) + x - left) * 4
                src = (y * WIDTH + x) * 4
                if result[idx + 3] or source[src + 3] < 230:
                    continue
                if not inside(x + 0.5, y + 0.5, WRISTS[name]):
                    continue
                sample_x = max(260, min(x, 288)) if name.startswith("Hand_R") else max(735, min(x, 756))
                sample = (731 * WIDTH + sample_x) * 4
                result[idx:idx + 4] = source[sample:sample + 3] + bytes([255])
                count += 1
        if not count:
            raise ValueError(f"No overlap painted for {name}")
        painted[name] = count
        layers.append((name.replace("_visible_draft", "_with_overlap"), (new_top, left, bottom, right), result))
    return layers[2:], painted


def main():
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected source PNG")
    source = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(SOURCE), "-frames:v", "1",
        "-pix_fmt", "rgba", "-f", "rawvideo", "-",
    ])
    if len(source) != WIDTH * HEIGHT * 4:
        raise ValueError("Unexpected canvas size")
    layers, painted = build_parts(source)
    neutral = composite(layers, (0, 0, WIDTH, HEIGHT), {})
    output = HERE / "nagi-wrist-overlap-v3.psd"
    write_psd(output, neutral, layers)

    box = (220, 686, 794, 850)
    width, height = box[2] - box[0], box[3] - box[1]
    shifts = {name.replace("_visible_draft", "_with_overlap"): delta for name, delta in SHIFT.items()}
    comparison = composite(layers, box, {}) + composite(layers, box, shifts)
    preview = HERE / "nagi-wrist-overlap-v3-comparison.png"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pixel_format", "rgba",
        "-video_size", f"{width}x{2 * height}", "-i", "-", "-frames:v", "1", str(preview),
    ], input=comparison, check=True)

    report = {
        "source_sha256": SOURCE_HASH,
        "psd_sha256": sha256(output.read_bytes()).hexdigest(),
        "preview_sha256": sha256(preview.read_bytes()).hexdigest(),
        "overlap_pixels_by_hand": painted,
        "comparison_lower_row_translation_px": shifts,
        "cubism_import_verified": False,
        "comparison_rendered_in_cubism": False,
    }
    (HERE / "wrist-overlap-v3-check.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
