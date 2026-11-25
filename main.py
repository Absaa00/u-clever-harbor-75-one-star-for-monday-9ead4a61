#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday as a restaurant.

Deterministic, offline, standard library only. Writes a single line of
plain text (at most 25 words, 1-180 UTF-8 characters, no explanation)
to /output/entry.txt.
"""

import os

REVIEW = (
    "One star. Monday seated us at 6 a.m., forgot our order, "
    "served cold dread, then charged extra for the weekend we never got."
)


def main() -> None:
    words = REVIEW.split()
    assert 1 <= len(words) <= 25, f"word count {len(words)} out of range"
    assert 1 <= len(REVIEW.encode("utf-8")) <= 180, "character count out of range"
    assert "\n" not in REVIEW, "review must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
