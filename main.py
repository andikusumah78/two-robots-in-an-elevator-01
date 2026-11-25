#!/usr/bin/env python3
"""Two Robots in an Elevator - make.fun entry.

Writes one funny line of awkward small talk, spoken by one robot to
another while they ride an elevator together, to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

LINE = "My small-talk subroutine has exactly one line. I tried it on three toasters today \u2014 none of them laughed, so now it is your turn."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
