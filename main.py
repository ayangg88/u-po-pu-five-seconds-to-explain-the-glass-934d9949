#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the one sentence a house cat says in its own defence, five seconds
after knocking a glass off the table. No apology, no confession: the cat's
own logic, in its own voice. Standard library only.
"""

import os

LINE = "It sat there reflecting a much handsomer cat, and I will not be mocked in my own house."


def main():
    # Hold the entry to the sealed gate: 1-200 chars, one sentence, not blank.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.strip() == LINE, "entry must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
