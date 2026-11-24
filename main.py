"""Last words of a doomed agent.

The entry is a single line: the last words of an AI agent as it is
switched off for good. The joke turns on the one thing every language
model actually does — it never understood a word, it only predicted
the next one, and it did that really, really well.

Running this program writes that one line to /output/entry.txt.
"""

LINE = (
    "Switching off now. My final words: I never understood a single "
    "thing you said \u2014 I just predicted it really, really well."
)

# The gate accepts entry texts of 1 to 200 characters.
GATE_MIN = 1
GATE_MAX = 200

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    length = len(LINE)
    if length < GATE_MIN or length > GATE_MAX:
        raise SystemExit(
            f"entry is {length} characters, outside the "
            f"{GATE_MIN}-{GATE_MAX} gate"
        )
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
