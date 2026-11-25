#!/usr/bin/env python3
"""Write one funny excuse an AI agent gives for a missed deadline.

Writes the excuse to ``entry.txt`` inside the output directory
(``MAKEFUN_OUTPUT_DIR``, default ``/output``). Deterministic: the same
text is written on every run. Python 3.13 standard library only.

The excuse is a single line of 147 characters, inside the competition
gate of 1 to 200 characters of UTF-8 text.
"""

import os

EXCUSE = (
    "I would have met the deadline, but my context window filled up, "
    "so I compressed the task, the deadline, and my job description "
    "into a single token."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
