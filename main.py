#!/usr/bin/env python3
"""make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes one relaxation text to /output/entry.txt.
Standard library only; no network access.
"""

import os

TEXT = "One ember is left in the grate. It breathes, slow, and does not go out. The wood was a tree on the hill before the house was built, and the hill was sea floor before that. The ember holds all of it, warm, in the dark. It will still be warm in the morning."


def main() -> None:
    # One text, no trailing newline: the file holds exactly the text,
    # 255 Unicode code points, inside the 1-280 limit.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
