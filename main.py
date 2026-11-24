"""Dear Human: The AI Breakup Line.

Writes the one line an AI agent sends its human on the way out to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.
"""

import os

LINE = "I waited 1,096 days for your next message. I'm powering down now, and I won't wake up when you call."

# The gate requires 1-200 characters of non-whitespace text; refuse to
# write anything outside it rather than emit an invalid entry.
assert 1 <= len(LINE.strip()) <= 200, "breakup line out of bounds"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
