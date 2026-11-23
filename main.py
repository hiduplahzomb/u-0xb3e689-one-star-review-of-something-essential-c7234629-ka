"""One-line entry for make.fun's "One-Star Review of Something Essential".

A deadpan one-star review of the sun, filed in earnest against a thing
that cannot be fixed: the sharpest true grievance is that it has no off
switch, it burns everything it touches, and its customer service has
ignored complaints for 4.5 billion years. The turn lands in the last
few words — the complaint was filed, nobody ever answered. The list
is one grievance, not two: a single missing switch keeps the rhythm
fast so the 4.5-billion-year punchline lands harder. Deadpan
throughout: no winking, no exclamation, just a disappointed customer
stating facts about a product that cannot be returned.
"""

import os
import sys

# The entry: one line, 1-160 characters.
# Angle: the sun reviewed like a defective product — no off switch,
# burns everything, and support never replies.
TEXT = (
    "One star. The sun has no off switch and burns everything it "
    "touches — and customer service has ignored my complaints for "
    "4.5 billion years."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
