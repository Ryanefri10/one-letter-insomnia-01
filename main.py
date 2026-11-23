#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

The entry is exactly one letter, A-Z, written to entry.txt and nothing else.

Chosen letter: I — for "insomnia".

Why I: the judge weighs, in order, whether the letter stands for a word
that describes the day, how vivid and specific that word is, how funny or
surprising it lands, how true it feels, and how well the letter suits its
word. Insomnia calls up a sharp picture (4 a.m., ceiling, glowing screen,
a brain that refuses to shut off), it is dark-funny in a way that lands at
once, it is an honest report of a day spent building through the night
rather than a performance, and I is its natural initial. It is also not the
obvious pick: the field is crowded with Z (zero sleep) and U (unhinged),
while I stands alone.
"""

import os
import sys

LETTER = "I"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one character: no newline, no space, no punctuation.
    # The gate requires /output/entry.txt to be UTF-8 text of 1-1 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and enforce the gate ourselves: exactly one A-Z letter,
    # so a bad write fails loudly here instead of at the sealed scorer.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert len(written) == 1 and "A" <= written <= "Z", (
        f"entry.txt must be exactly one A-Z letter, got {written!r}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
