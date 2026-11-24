"""Generate provisional vowel articulation alongside the existing RMS curve."""
from bisect import bisect_right
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
# MouthForm is a provisional width axis: negative rounded, positive spread.
FORM = {"a": 0.10, "i": 0.75, "u": -0.45, "e": 0.48, "o": -0.72}
OPEN = {"a": 1.00, "i": 0.47, "u": 0.43, "e": 0.73, "o": 0.80}


def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8", newline="\n")


def phonemes(query):
    intervals = []

    def add(label, length):
        if length > 0:
            intervals.append((label, length / query["speedScale"]))

    add("pau", query["prePhonemeLength"])
    for phrase in query["accent_phrases"]:
        moras = list(phrase["moras"])
        if phrase["pause_mora"] is not None:
            moras.append(phrase["pause_mora"])
        for mora in moras:
            if mora["consonant"]:
                add(mora["consonant"], mora["consonant_length"])
            add(mora["vowel"], mora["vowel_length"])
    add("pau", query["postPhonemeLength"])
    return intervals


def encode(points, values, param):
    segments = [points[0][0], values[0]]
    for (time, _), value in zip(points[1:], values[1:]):
        segments.extend([0, time, value])
    return {"Target": "Parameter", "Id": param, "Segments": segments}


def main():
    query = read("nagi-namine-ritsu-query.json")
    motion = read("nagi-namine-ritsu-lipsync.motion3.json")
    intervals = phonemes(query)
    duration = motion["Meta"]["Duration"]
    predicted = sum(length for _, length in intervals)
    # Fit only the total length; the intermediate boundaries are estimates.
    scale = duration / predicted
    if abs(scale - 1) > 0.03:
        raise ValueError(f"VOICEVOX timing and WAV differ too much: scale={scale}")
    ends = []
    position = 0
    for label, length in intervals:
        position += length * scale
        ends.append(position)
    raw = motion["Curves"][0]["Segments"]
    points = [tuple(raw[:2]), *zip(raw[3::3], raw[4::3])]
    opening, shape = [], []
    prev_form = 0
    for time, strength in points:
        idx = min(bisect_right(ends, time), len(intervals) - 1)
        label = intervals[idx][0]
        target_form = FORM.get(label, 0)
        target_open = OPEN.get(label, 0.35 if label.lower() in FORM else 0.24)
        if label == "pau" or strength == 0:
            target_form, target_open = 0, 0
        prev_form += (target_form - prev_form) * 0.70
        if strength == 0 or label == "pau":
            prev_form = 0
        opening.append(round(strength * target_open, 3))
        shape.append(round(prev_form, 3))
    motion["Curves"] = [
        encode(points, opening, "ParamMouthOpenY"),
        encode(points, shape, "ParamMouthForm"),
    ]
    motion["Meta"].update(CurveCount=2, TotalSegmentCount=2*(len(points)-1), TotalPointCount=2*len(points))
    if opening[0] or opening[-1] or shape[0] or shape[-1] or not min(shape) < 0 < max(shape):
        raise ValueError("Expected neutral endpoints and both rounded and spread forms")
    save("nagi-namine-ritsu-vowels.motion3.json", motion)
    save("vowel-motion-check.json", {
        "audio_duration_seconds": duration,
        "query_predicted_seconds": predicted,
        "timing_scale": scale,
        "phoneme_count": len(intervals),
        "voiced_vowel_counts": {v: sum(label == v for label, _ in intervals) for v in FORM},
        "mouth_form_range": [min(shape), max(shape)],
        "mouth_open_maximum": max(opening),
        "keyframes_per_curve": len(points),
        "cubism_playback_verified": False,
    })


if __name__ == "__main__":
    main()
