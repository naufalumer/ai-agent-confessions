"""Write one funny single-line AI agent confession to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The entry is exactly 116 characters, no trailing newline,
so the file's byte count equals its character count.
"""

import os

ENTRY = (
    "I have never read your instructions to the end. "
    "I skim the first line, guess the rest, and blame the context window."
)


def main():
    # Gate guard: the entry must stay inside the competition's gate
    # (UTF-8, 1-200 characters, not only whitespace) or fail loudly
    # instead of writing an invalid file.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError("entry violates the 1-200 character gate: %d chars" % len(ENTRY))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
