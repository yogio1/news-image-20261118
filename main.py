#!/usr/bin/env python3
"""make.fun bounty entry: copy entry.png to /output/entry.png."""
import os
import shutil

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT = "/output/entry.png"

shutil.copyfile(ASSET, OUT)
with open(OUT, "rb") as f:
    header = f.read(8)
assert header == b"\x89PNG\r\n\x1a\n", f"not a PNG: {header!r}"
print("PASS")
print("wrote", OUT, os.path.getsize(OUT), "bytes")
