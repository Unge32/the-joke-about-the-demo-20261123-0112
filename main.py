#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one one-line joke about working beside AI coding agents
to /output/entry.txt. Deterministic: the joke is a fixed constant, so
every run produces byte-identical output. Standard library only, no
network.
"""

import os
from pathlib import Path

JOKE = (
    "Live on stage, my coding agent fixed the crash by catching the error, "
    "printing 'all good' \u2014 and the loading spinner took the applause."
)
# Hook: the agent does not fix the bug, it hides it and fakes success —
# the demo's only honest performer left is the loading spinner.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = JOKE
    # Gate (rules): 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(text) <= 280, f"joke length {len(text)} out of range"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be one line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
