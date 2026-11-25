#!/usr/bin/env python3
"""Fridge Roast entry.

Writes one smart-fridge roast to /output/entry.txt. The roast is fixed and
deterministic: the same text is written on every run.
"""

import os

ROAST = "My fridge updated itself overnight and now the ice maker needs a subscription. I bought an appliance, not a SaaS product with a door."

# The gate requires 1-200 UTF-8 characters; fail loudly if the roast ever
# stops fitting instead of submitting an invalid entry.
MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_roast(text):
    """Check the roast fits the gate before writing it."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError("roast must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if not text.strip():
        raise ValueError("roast must not be whitespace-only")
    if text != text.strip():
        raise ValueError("roast must not have leading/trailing whitespace")


def write_entry():
    validate_roast(ROAST)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


def main():
    try:
        write_entry()
    except ValueError as e:
        raise SystemExit("invalid roast: %s" % e)


if __name__ == "__main__":
    main()
