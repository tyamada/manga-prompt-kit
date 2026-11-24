"""Render a local lip-sync proof from the v4 art and the two motion curves."""
from bisect import bisect_right
from hashlib import sha256
import json
import math
import subprocess

from build_mouth_parts_v4 import BOX, SHAPES, draw_mouth, restore_skin
from build_draft import HERE, SOURCE, SOURCE_HASH
from build_wrist_overlap_v3 import build_parts, composite

VOICE = HERE.parent / "voice-audition"
MOTION = VOICE / "nagi-namine-ritsu-vowels.motion3.json"
AUDIO = VOICE / "nagi-namine-ritsu.wav"
VIDEO = HERE / "nagi-ritsu-lipsync-preview.mp4"
CROP = (388, 5, 644, 325)
WIDTH, HEIGHT = CROP[2] - CROP[0], CROP[3] - CROP[1]
WIDTH_KEYS = [(-0.72, "O"), (-0.45, "U"), (0.10, "A"), (0.48, "E"), (0.75, "I")]


def read_linear(curve):
    segments = curve["Segments"]
    points = [tuple(segments[:2])]
    for index in range(2, len(segments), 3):
        if segments[index] != 0:
            raise ValueError("Preview expects linear segments")
        points.append(tuple(segments[index + 1:index + 3]))
    return points


def interpolate(points, time):
    index = bisect_right(points, (time, float("inf")))
    if index == 0:
        return points[0][1]
    if index == len(points):
        return points[-1][1]
    x0, y0 = points[index - 1]
    x1, y1 = points[index]
    return y0 + (y1 - y0) * (time - x0) / (x1 - x0)


def main():
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Unexpected source image")
    source = subprocess.check_output([
        "ffmpeg", "-v", "error", "-i", str(SOURCE), "-frames:v", "1",
        "-pix_fmt", "rgba", "-f", "rawvideo", "-",
    ])
    layers, _ = build_parts(source)
    base = restore_skin(source, layers)
    background = composite(base, CROP, {})
    motion = json.loads(MOTION.read_text(encoding="utf-8"))
    curves = {curve["Id"]: read_linear(curve) for curve in motion["Curves"]}
    fps = motion["Meta"]["Fps"]
    count = math.ceil(fps * motion["Meta"]["Duration"])
    width_points = [(key, SHAPES["Mouth_" + vowel][0]) for key, vowel in WIDTH_KEYS]
    closed_rx, closed_ry = SHAPES["Mouth_Closed"]

    command = [
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pixel_format", "rgba",
        "-video_size", f"{WIDTH}x{HEIGHT}", "-framerate", str(fps), "-i", "-",
        "-i", str(AUDIO), "-filter_complex",
        f"color=c=0xE4EEF2:s={WIDTH}x{HEIGHT}:r={fps}[bg];"
        "[bg][0:v]overlay=shortest=1,scale=768:960:flags=lanczos[v]",
        "-map", "[v]", "-map", "1:a:0", "-c:v", "libx264", "-crf", "18",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart", str(VIDEO),
    ]
    distinct = set()
    top, left, bottom, right = BOX
    tile_width = right - left
    with subprocess.Popen(command, stdin=subprocess.PIPE) as process:
        for index in range(count):
            time = min(index / fps, motion["Meta"]["Duration"])
            # Hold a closed pose on the final display frame.
            opened = 0 if index == count - 1 else interpolate(curves["ParamMouthOpenY"], time)
            form = interpolate(curves["ParamMouthForm"], time)
            width_mix = min(1, opened / 0.25)
            rx = closed_rx + width_mix * (interpolate(width_points, form) - closed_rx)
            ry = closed_ry + opened * 4.1
            mouth = draw_mouth("Mouth_Closed" if opened == 0 else "Mouth_Interpolated", rx, ry)
            patch = composite([mouth, *base], (left, top, right, bottom), {})
            distinct.add(sha256(patch).digest())
            frame = bytearray(background)
            for row in range(bottom - top):
                offset = ((top - CROP[1] + row) * WIDTH + left - CROP[0]) * 4
                frame[offset:offset + tile_width * 4] = patch[row * tile_width * 4:(row + 1) * tile_width * 4]
            process.stdin.write(frame)
        process.stdin.close()
        if process.wait():
            raise RuntimeError("FFmpeg failed")
    if len(distinct) < 2:
        raise ValueError("No visible mouth motion")
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_streams", "-of", "json", str(VIDEO),
    ]))
    video, audio = probe["streams"]
    if (video["codec_type"], audio["codec_type"]) != ("video", "audio"):
        raise ValueError("Expected one video and one audio stream")
    if int(video["nb_frames"]) != count or abs(float(video["duration"]) - float(audio["duration"])) > 1 / fps:
        raise ValueError("Audio/video lengths differ by more than a frame")
    report = {
        "video_frames": count, "fps": fps, "distinct_mouth_patches": len(distinct),
        "video_seconds": float(video["duration"]), "audio_seconds": float(audio["duration"]),
        "source_motion_sha256": sha256(MOTION.read_bytes()).hexdigest(),
        "source_audio_sha256": sha256(AUDIO.read_bytes()).hexdigest(),
        "video_sha256": sha256(VIDEO.read_bytes()).hexdigest(),
        "cubism_viewer_verified": False,
    }
    (HERE / "lipsync-preview-check.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


if __name__ == "__main__":
    main()
