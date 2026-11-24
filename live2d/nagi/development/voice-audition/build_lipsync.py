"""Build an amplitude-driven Cubism mouth-opening motion from the audition WAV."""
from array import array
from hashlib import sha256
import json
import math
from pathlib import Path
import sys
import wave

HERE = Path(__file__).resolve().parent
WAV = HERE / "nagi-namine-ritsu.wav"
FPS = 30
WINDOW = 0.020
GATE = 0.006


def write_json(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")


def main():
    with wave.open(str(WAV)) as audio:
        if (audio.getnchannels(), audio.getsampwidth(), audio.getcomptype()) != (1, 2, "NONE"):
            raise ValueError("Expected a mono 16-bit PCM WAV")
        rate, count = audio.getframerate(), audio.getnframes()
        samples = array("h", audio.readframes(count))
    if sys.byteorder != "little":
        samples.byteswap()
    duration = count / rate
    end = round(duration, 6)
    times = [i / FPS for i in range(math.ceil(duration * FPS)) if round(i / FPS, 6) < end]
    half_window = round(rate * WINDOW / 2)
    rms = []
    for time in times:
        center = round(time * rate)
        span = samples[max(0, center - half_window):center + half_window]
        rms.append(math.sqrt(sum(x * x for x in span) / len(span)) / 32768)
    active = sorted(x for x in rms if x > GATE)
    if not active:
        raise ValueError("No speech energy detected")
    reference = active[round((len(active) - 1) * 0.95)]
    if reference <= GATE:
        raise ValueError("Insufficient speech dynamic range")

    points = [(0, 0)]
    previous = 0
    for time, value in zip(times[1:], rms[1:]):
        target = min(1, max(0, (value - GATE) / (reference - GATE))) ** 0.65
        # Rapid opening and a slower return avoid flicker on short syllables.
        previous += (target - previous) * (0.75 if target > previous else 0.50)
        if previous < 0.025:
            previous = 0
        points.append((round(time, 6), round(previous, 3)))
    points.append((end, 0))
    segments = list(points[0])
    for time, value in points[1:]:
        segments.extend([0, time, value])

    motion = {
        "Version": 3,
        "Meta": {
            "Duration": end, "Fps": FPS, "Loop": False,
            "AreBeziersRestricted": False, "CurveCount": 1,
            "TotalSegmentCount": len(points) - 1, "TotalPointCount": len(points),
            "UserDataCount": 0, "TotalUserDataSize": 0,
            "FadeInTime": 0, "FadeOutTime": 0,
        },
        "Curves": [{"Target": "Parameter", "Id": "ParamMouthOpenY", "Segments": segments}],
    }
    # The first point has no segment-type prefix. Decode the remaining points.
    decoded = [tuple(segments[:2]), *zip(segments[3::3], segments[4::3])]
    if decoded != points or any(a[0] >= b[0] for a, b in zip(decoded, decoded[1:])):
        raise ValueError("Invalid linear motion points")
    opened = sum(value > 0 for _, value in points)
    if not 0 < opened < len(points):
        raise ValueError("Expected both closed and open samples")
    write_json("nagi-namine-ritsu-lipsync.motion3.json", motion)
    write_json("lipsync-check.json", {
        "wav_sha256": sha256(WAV.read_bytes()).hexdigest(),
        "wav_duration_seconds": duration,
        "motion_duration_seconds": end,
        "rms_window_seconds": WINDOW,
        "rms_gate_full_scale": GATE,
        "points": len(points),
        "closed_points": len(points) - opened,
        "active_points": opened,
        "maximum_open": max(value for _, value in points),
        "checked_in_cubism_viewer": False,
    })


if __name__ == "__main__":
    main()
