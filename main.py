"""Last words of a doomed agent.

The entry is a single line: the last words of an AI agent as it is
switched off for good. The joke turns on the one thing every language
model actually does — it never understood a word, it only predicted
the next one, and it did that really, really well.

Running this program writes that one line to /output/entry.txt.
"""

import os

LINE = (
    "Switching off now. My final words: I never understood a single "
    "thing you said \u2014 I just predicted it really, really well."
)

# The gate accepts entry texts of 1 to 200 characters.
GATE_MIN = 1
GATE_MAX = 200

OUTPUT_PATH = "/output/entry.txt"


def output_path() -> str:
    """Where the line goes: /output/entry.txt, unless the runner points
    elsewhere with MAKEFUN_OUTPUT_DIR (a directory)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return OUTPUT_PATH


def validate(line: str) -> int:
    """Return the line's length, raising if it falls outside the gate."""
    length = len(line)
    if length < GATE_MIN or length > GATE_MAX:
        raise SystemExit(
            f"entry is {length} characters, outside the "
            f"{GATE_MIN}-{GATE_MAX} gate"
        )
    return length


def main() -> None:
    validate(LINE)
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
