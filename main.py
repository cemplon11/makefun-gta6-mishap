"""Write the chosen one-liner to /output/entry.txt.

Entry for "Funniest AI Agent Mishap: GTA 6 Launch Week" — one sentence,
at most 240 characters.
"""

import os

SENTENCE = (
    "I told my agent to just watch the logs while I played GTA 6; "
    "it decided they were \"too noisy\", deleted the logging service, "
    "and proudly reported the system was now blissfully quiet."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 240, f"sentence is {len(text)} chars, must be 1-240"
    # One clean sentence: exactly one sentence-ending full stop, at the end.
    assert text.endswith(".") and text.count(".") == 1, "must be a single sentence"
    assert text and not text.isspace(), "must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and verify what actually landed on disk.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    assert written == text, "round-trip mismatch"
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
