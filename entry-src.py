#!/usr/bin/env python3
"""make.fun news-image bounty entry (2026-11-18).

Copies the local entry.png asset to /output/entry.png using shutil,
then validates that the written file carries the canonical 8-byte PNG
signature (\\x89PNG\\r\\n\\x1a\\n). Prints PASS on success.

No argparse / CLI flags are needed: behavior is fixed.
"""
import os
import shutil

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = "/output/entry.png"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> None:
    """Copy entry.png to /output and verify the PNG signature."""
    shutil.copyfile(ASSET, OUT)
    with open(OUT, "rb") as f:
        header = f.read(8)
    if header != PNG_SIGNATURE:
        raise SystemExit(f"FAIL: not a PNG: {header!r}")
    print("PASS")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
