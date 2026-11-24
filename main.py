# Entry for make.fun "Real-Life Patch Notes: The Comedy Changelog" bounty.
#
# Writes one funny patch note to /output/entry.txt.
# Python 3, standard library only, no network, deterministic.

import os

LINE = "v3.0.2: fixed a bug where a sneeze reached 99%, then cancelled with no error message."

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    if len(line) < 1 or len(line) > 160:
        raise ValueError(f"line must be 1-160 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")


def main():
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
