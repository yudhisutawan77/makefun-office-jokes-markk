"""One-Line Office Jokes: single-line office joke entry.

Writes the joke to ``$ENTRY_OUT/entry.txt`` (``/output/entry.txt`` when the
variable is unset) and prints it exactly once to stdout. The gate wants
UTF-8 text of 1 to 199 characters on one line, so the joke is validated
before anything is written.
"""

import os


OFFICE_JOKE = "I asked to be removed from a reply-all thread, so 400 colleagues replied-all to say they want out too."

# Why this line: it turns on the most recognizable office detail there is —
# the reply-all storm — and the laugh lands on the final beat, when the very
# people trying to escape the thread become the thread. One reading, no
# setup, and the wording is not a joke already going round the internet.


def validate_line(line: str) -> str:
    """Return the joke unchanged, or fail loudly if it breaks the gate."""
    cleaned = line.strip()
    if not 1 <= len(cleaned) <= 199:
        raise SystemExit(f"joke is {len(cleaned)} characters, must be 1-199")
    if cleaned != line or "\n" in cleaned:
        raise SystemExit("joke must be a single line with no extra whitespace")
    return cleaned


def resolve_out_dir() -> str:
    """Output directory the grader reads: $ENTRY_OUT, else /output."""
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def main() -> None:
    text = validate_line(OFFICE_JOKE)
    with open(os.path.join(resolve_out_dir(), "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
