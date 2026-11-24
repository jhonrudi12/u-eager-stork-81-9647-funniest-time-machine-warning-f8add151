"""Funniest Time Machine Warning Label.

Writes one warning label (<=120 characters) to /output/entry.txt
and prints the same line. Deterministic, no network, no input.
"""

import os

ENTRY = "WARNING: If you meet yourself, say nothing. He already regrets this conversation, and so do you."
MAX_CHARS = 120


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise ValueError("entry must be 1 to 120 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
