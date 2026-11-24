#!/usr/bin/env python3
"""Writes one office joke to /output/entry.txt.

Entry for make.fun bounty "Make the AI Judge Laugh: the Office Joke Open".
Deterministic, no network: writes the prepared one-line joke.
"""

import os

JOKE = (
    "I hit reply-all on the meeting that could've been an email, "
    "apologised to 47 people, and the only reply was an invite "
    "to a meeting about replying-all."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
