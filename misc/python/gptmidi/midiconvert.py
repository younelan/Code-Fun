#!/usr/bin/env python3

import mido
from mido import MidiFile, MidiTrack, Message
import argparse
import os

def generate_midi(input_file, output_file=None):
    # Create a new MIDI file
    mid = MidiFile()

    # Create a new track
    track = MidiTrack()
    mid.tracks.append(track)

    # Add note-on and note-off events from the input file
    with open(input_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5:
                _, action, channel, note, velocity, time = parts
                if action == 'On':
                    track.append(Message('note_on', note=int(note), velocity=int(velocity), time=int(time)))
                elif action == 'Off':
                    track.append(Message('note_off', note=int(note), velocity=int(velocity), time=int(time)))

    # Determine the output file name
    if output_file is None:
        base_name, _ = os.path.splitext(input_file)
        output_file = f'{base_name}.midi'

    # Save the MIDI file
    mid.save(output_file)
    print(f'MIDI file saved as {output_file}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert text-based MIDI representation to a MIDI file.')
    parser.add_argument('input_file', type=str, help='Input file containing MIDI representation')
    parser.add_argument('--output_file', type=str, help='Optional output MIDI file name')

    args = parser.parse_args()
    generate_midi(args.input_file, args.output_file)

