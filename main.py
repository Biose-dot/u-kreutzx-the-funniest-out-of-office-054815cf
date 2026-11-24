#!/usr/bin/env python3
"""The Funniest Out-of-Office - make.fun entry.

Writes one line of text (no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""
import os

ENTRY = "I'm out of office until Monday. My inbox is being guarded by an intern who thinks 'urgent' means 'reply-all'."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
