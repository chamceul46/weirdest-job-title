#!/usr/bin/env python3
"""Entry for the make.fun bounty "Weirdest Job Title: Blind Judge
Showdown" (u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922).

The whole entry is one job title of at most 60 characters. It names
a job that sounds entirely real — lighthouse keepers work night
shifts — with one gloriously odd twist: the town it serves is
landlocked, so the light guards nothing at all. The picture forms
instantly: one keeper, one tower, no sea.

The program writes that single title to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader).
"""

import os

LINE = "Night-Shift Lighthouse Keeper for a Landlocked Town"


def validate(line: str) -> None:
    """Mirror the bounty gate: UTF-8 text of 1 to 60 characters,
    and not only white space. Refuse to hand in anything else."""
    encoded = line.encode("utf-8")  # raises if it cannot be encoded
    if not line.strip():
        raise ValueError("entry is only white space")
    if not 1 <= len(line) <= 60:
        raise ValueError(f"entry is {len(line)} characters, outside 1..60")
    if len(encoded) > 60:
        raise ValueError("entry encodes to more than 60 bytes")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
