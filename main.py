"""Two-Sentence Horror entry.

Writes a horror story of exactly two sentences (at most 400 characters)
to /output/entry.txt.
"""

import os

STORY = (
    "Ever since I moved in, my apartment's smart lock has unlocked itself "
    "at 3 a.m. every night, and I've stopped checking who comes in. "
    "Last night I finally stayed awake to see — and the man standing over "
    "my bed had my face, my clothes, and a key I never made."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
