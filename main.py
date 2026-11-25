"""Family scene entry for make.fun.

Writes one short family scene (one line, under 280 characters) to
/output/entry.txt. Deterministic: the same line on every run.

Scene chosen over two other drafts (fridge photos, grandfather's extra
plate): the burnt-toast ritual is the warmest and most specific — affection
shown through a daily action, with a light funny turn ("the crispy one")
a family would actually laugh at.
"""

import os

LINE = (
    "Dad saves the burnt toast for himself, calls it 'the crispy one,' "
    "and Mom pretends not to notice he does it every morning so the rest "
    "of us get the good slices."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
