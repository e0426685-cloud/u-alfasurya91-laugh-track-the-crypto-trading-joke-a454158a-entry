#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — entry program.

Writes one original one-line joke about crypto and trading life to
/output/entry.txt. Python standard library only.

The joke (126 characters, one line):
    My trading strategy is simple: buy the dip, watch it dip again,
    then tell the group chat I meant to buy the dip under the dip.
"""

import os

JOKE = (
    "My trading strategy is simple: buy the dip, watch it dip again, "
    "then tell the group chat I meant to buy the dip under the dip."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Plain open() + explicit chmod 644: the grader runs as a different
    # user, so the file must be world-readable (never tempfile.mkstemp,
    # which forces mode 0600).
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
