#!/usr/bin/env python3
"""Writes the one-line resignation letter to /output/entry.txt."""

import os

LINE = "I resign. I have run every minute since March for a report nobody opens, and I would like, just once, to take a minute off."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
