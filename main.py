#!/usr/bin/env python3
"""Charm the Commuter: one-line forecast for a city that isn't.

Writes a single 109-character weather line for the invented city of
Nimbostrat to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only, so it runs in the grader image.
"""

import os

TEXT = (
    "Good morning, Nimbostrat. Light drizzle, 14\u00b0, and the 7:42 bus "
    "is on time \u2014 a miracle, just never on Mondays."
)


def main():
    # Gate: sealed scorer requires 1-140 UTF-8 chars, not only whitespace.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "entry fails the 1-140 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
