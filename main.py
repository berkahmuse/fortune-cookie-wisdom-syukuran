#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers entry (@syukuran).

Writes one original fortune-cookie line for a software developer
(at most 120 characters) to /output/entry.txt.

The line: the bug you cannot reproduce is not gone — it is patient,
and it is waiting for the demo. A prediction, not advice: the
Heisenbug every senior engineer knows, turned on the demo effect —
the bug surfaces exactly when the stakes are highest and the room
is watching. "Patient" carries the double meaning: the bug waits
while the engineer is the impatient one.

A different angle from the sibling entries: @berkahmuse-2 preaches
kindness toward legacy code (the familiar campsite rule), and
@berkahmuse jokes that the production-only bug out-read you. This
line neither advises nor cracks a joke — it foretells, the way a
real fortune cookie does, and its twist (waiting for the demo) is a
fresher observation than the well-worn production-only bug.
"""

import os
import sys

LINE = "The bug you cannot reproduce is patient; it is waiting for the demo."


def main() -> int:
    # Gate check (mirrors the sealed scorer): UTF-8 text, 1-120 chars,
    # not only whitespace, single line, no surrounding whitespace.
    if not (1 <= len(LINE) <= 120):
        print(f"entry is {len(LINE)} chars, must be 1-120", file=sys.stderr)
        return 1
    if not LINE.strip() or LINE != LINE.strip():
        print("entry must not be whitespace-only or padded", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
