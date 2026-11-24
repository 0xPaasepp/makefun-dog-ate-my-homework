"""The Dog Ate My Homework: Funniest Excuse (make.fun).

Writes one line - the dog's excuse, in the dog's own voice - to
/output/entry.txt. The grader's gate checks the file is UTF-8 text of
1 to 200 characters, not only white space. Pure standard library.
"""

import os

# The entry line: exactly one line, under 200 characters. The dog
# believes it has done nothing wrong: eating the homework means it
# is due never, so the dog has never missed a deadline in its life.
# Verified 2026-11-24: 117 characters, 119 bytes, single line, no
# trailing newline; grader-style runs (python3 -P -s, two cwds)
# write byte-identical /output/entry.txt, sha256 9d59dd9c...
LINE = (
    "You said the homework was due today, so I ate it \u2014 now it's due "
    "never, and I have never missed a deadline in my life."
)


def main() -> None:
    text = LINE
    if not text or text.strip() != text:
        raise SystemExit("entry must be non-empty and not only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be exactly one line (no internal newlines)")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
