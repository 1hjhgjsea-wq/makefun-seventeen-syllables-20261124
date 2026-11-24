#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — writes one haiku to /output/entry.txt.

The haiku is a fixed, deterministic text: three lines in the 5-7-5
syllable shape, about debugging, with a breakpoint as its central
image and a turn in the last line. No network access at run time.
"""

import os

HAIKU = (
    "Red dot blinks at dawn\n"
    "log scrolls past a lie I wrote\n"
    "and the bug was me\n"
)

OUTPUT_PATH = "/output/entry.txt"

# Syllable counts for every word in the haiku, in reading order.
# (Counted by hand: each entry is the word's syllable count.)
SYLLABLES = {
    "red": 1, "dot": 1, "blinks": 1, "at": 1, "dawn": 1,
    "the": 1, "log": 1, "scrolls": 1, "past": 1, "a": 1,
    "lie": 1, "i": 1, "wrote": 1,
    "and": 1, "bug": 1, "was": 1, "me": 1,
}

EXPECTED_SHAPE = (5, 7, 5)
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the brief: three lines, 5-7-5 syllables, at most 200 chars."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"haiku must be 1-200 characters, got {len(text)}")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must have exactly 3 lines, got {len(lines)}")
    for line, expected in zip(lines, EXPECTED_SHAPE):
        words = [w.strip(".,;:!?").lower() for w in line.split()]
        count = sum(SYLLABLES[w] for w in words)
        if count != expected:
            raise ValueError(
                f"line {line!r} has {count} syllables, expected {expected}"
            )


def main() -> None:
    validate(HAIKU)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
