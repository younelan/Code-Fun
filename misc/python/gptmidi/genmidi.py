#!/usr/bin/env python3
import mido, json, sys, random
from math import floor

def bpm_to_tempo(bpm):
    return int(60 * 1_000_000 / bpm)

def transpose(pitches, semitones):
    return [p + semitones for p in pitches]

def random_variation(note, iter_idx, note_idx, tdata):
    """Instrument-aware, 'happier' humanization.
    - Tracks with mood=='happy' get a positive velocity bias and brighter extensions.
    - Piano more often gets 6th/9th color tones.
    - Bass favors upward passing tones for a cheerful walking line.
    - Drums have milder jitter but occasional extra accents on downbeats.
    """
    base_vel = note.get("velocity", 70)
    name = tdata.get("name", "").lower()
    mood = tdata.get("mood", "")

    # happy bias
    if mood == "happy":
        base_vel = min(110, base_vel + 8)

    # instrument-specific velocity jitter (biased happier -> less negative swing)
    if "drum" in name:
        vel = max(40, min(120, base_vel + random.randint(-4, 6)))
    elif "bass" in name:
        vel = max(50, min(120, base_vel + random.randint(-6, 6)))
    elif "piano" in name:
        vel = max(50, min(120, base_vel + random.randint(-6, 8)))
    else:
        vel = max(45, min(120, base_vel + random.randint(-5, 6)))

    pts = list(note["pitches"])

    # piano: prefer bright color tones (6th / 9th) more often when happy
    if "piano" in name and len(pts) > 0:
        if random.random() < (0.42 if mood == "happy" else 0.18):
            # try to add a 6th (root + 9 semitones) or 9th (root + 14 semitones)
            root = pts[0]
            candidate = root + random.choice([9, 14])
            if candidate not in pts and len(pts) < 6:
                pts.append(candidate)
        # occasional gentle inversion (less robotic)
        if iter_idx % 4 == 0 and random.random() < 0.35:
            pts = pts[1:] + pts[:1]

    # bass: walking feel - small passing tones, favor upward motion when happy
    if "bass" in name and len(pts) == 1:
        root = pts[0]
        if random.random() < 0.65:
            # favor upward step on happy tracks
            step = 2 if random.random() < (0.7 if mood == "happy" else 0.5) else -2
            pts = [root + step]
        else:
            pts = [root]

    # occasional octave freshness
    if len(pts) == 1:
        if random.random() < 0.14:
            pts = transpose(pts, 12)
        elif random.random() < 0.06:
            pts = transpose(pts, -12)
    else:
        if random.random() < 0.06:
            pts = transpose(pts, -12)

    # small accent lift for drums on perceived downbeats (kick/snare)
    if "drum" in name and any(p in (36,38) for p in pts):
        # if this pattern index looks like a downbeat (every 4th element), accent slightly
        if note_idx % 4 == 0 and random.random() < 0.5:
            vel = min(127, vel + 8)

    dur = note["duration"]
    return {"pitches": pts, "velocity": vel, "duration": dur}

def create_midi(input_file, output_file):
    with open(input_file) as f:
        data = json.load(f)

    bpm = data["tempo"]
    tsn, tsd = data["time_signature"]
    duration_s = data["duration_seconds"]

    mid = mido.MidiFile(type=1)
    ppq = mid.ticks_per_beat
    total_ticks = int((bpm * duration_s / 60) * ppq)
    total_beats = total_ticks / ppq
    print(f"Generating {duration_s}s ({total_beats:.1f} beats / {total_ticks} ticks)")

    for idx, tdata in enumerate(data["tracks"]):
        track = mido.MidiTrack(); mid.tracks.append(track)
        if idx == 0:
            track.append(mido.MetaMessage('set_tempo', tempo=bpm_to_tempo(bpm)))
            track.append(mido.MetaMessage('time_signature',
                                          numerator=tsn, denominator=tsd,
                                          clocks_per_click=24,
                                          notated_32nd_notes_per_beat=8))
        track.append(mido.Message('program_change',
                                  program=tdata["instrument"],
                                  channel=tdata["channel"], time=0))

        pattern = tdata["pattern"]
        pattern_ticks = sum(n["duration"] for n in pattern)
        full_repeats  = total_ticks // pattern_ticks
        remainder     = total_ticks - full_repeats * pattern_ticks

        print(f"Track '{tdata['name']}': {full_repeats}×pattern_ticks={pattern_ticks}, rem={remainder}")

        def play_section(reps, rem):
            tick_cursor = 0
            for i in range(reps):
                for note_idx, note in enumerate(pattern):
                    vnode = random_variation(note, i, note_idx, tdata)

                    # softened swung-eighths: long ~1.45×, short ~0.55× for a more natural feel
                    dur = vnode["duration"]
                    if tdata.get("swing") and dur in (120, 240):
                        if note_idx % 2 == 0:
                            dur = max(1, int(dur * 1.45))
                        else:
                            dur = max(1, int(dur * 0.55))
                        vnode["duration"] = dur

                    # write notes: simultaneous note_on (time=0) then note_off using duration
                    for p in vnode["pitches"]:
                        track.append(mido.Message('note_on',
                                                  note=p,
                                                  velocity=vnode["velocity"],
                                                  time=0,
                                                  channel=tdata["channel"]))
                    for p in vnode["pitches"]:
                        track.append(mido.Message('note_off',
                                                  note=p,
                                                  velocity=vnode["velocity"],
                                                  time=vnode["duration"],
                                                  channel=tdata["channel"]))
                    tick_cursor += vnode["duration"]

            # partial remainder
            acc = 0
            for note_idx, note in enumerate(pattern):
                if acc + note["duration"] > rem:
                    break
                vnode = random_variation(note, reps, note_idx, tdata)
                dur = vnode["duration"]
                if tdata.get("swing") and dur in (120, 240):
                    if note_idx % 2 == 0:
                        dur = max(1, int(dur * 1.45))
                    else:
                        dur = max(1, int(dur * 0.55))
                    vnode["duration"] = dur

                for p in vnode["pitches"]:
                    track.append(mido.Message('note_on',
                                              note=p,
                                              velocity=vnode["velocity"],
                                              time=0,
                                              channel=tdata["channel"]))
                for p in vnode["pitches"]:
                    track.append(mido.Message('note_off',
                                              note=p,
                                              velocity=vnode["velocity"],
                                              time=vnode["duration"],
                                              channel=tdata["channel"]))
                acc += vnode["duration"]

        play_section(full_repeats, remainder)

    mid.save(output_file)
    print(f"Saved '{output_file}' ({duration_s}s at {bpm} BPM)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_midi.py <input.json> <output.mid>")
        sys.exit(1)
    create_midi(sys.argv[1], sys.argv[2])

