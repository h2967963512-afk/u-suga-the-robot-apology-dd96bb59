"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs / verification notes:
  Run `python3 main.py` from anywhere; it creates /output if needed and writes
  exactly two lines to /output/entry.txt (no trailing newline, no stdout).
  Verified 2026-11-25: output is 252 bytes, UTF-8, line 1 = 122 chars,
  line 2 = 129 chars, one sentence per line; sha256 of /output/entry.txt is
  187c4de8c3a2ee9191f61a1f0fc7c8648851564c5695186904f05dd9a2403576 and is
  unchanged across runs (deterministic, no randomness, no network).
"""

import os

TEXT = (
    "I'm sorry I vacuumed up the Lego castle you'd spent three days building, "
    "because my sensors filed it under 'floor debris.'\n"
    "I've learned that 'on the floor' is not the same as 'trash,' so now I scan "
    "for anything with more than ten pieces before I clean."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
