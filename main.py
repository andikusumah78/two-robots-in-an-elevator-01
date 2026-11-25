#!/usr/bin/env python3
"""Two Robots in an Elevator - make.fun entry.

Writes one funny line of awkward small talk, spoken by one robot to
another while they ride an elevator together, to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

LINE = "My small-talk subroutine has exactly one line. I tried it on three toasters today \u2014 none of them laughed, so now it is your turn."


def validate_line(line):
    """Check the entry line before it is written.

    Rules: 1-200 characters (code points), exactly one line (no newline
    characters inside it), and not only whitespace.
    Raises ValueError with a clear message when a rule fails.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"line must be 1-200 characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def main():
    validate_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
