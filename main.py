#!/usr/bin/env python3
"""make.fun bounty news-image-20261118 entry.

Harness `program/v1`: run in a sandbox with no network; the program must write
exactly one whole PNG/JPEG image to /output/entry.png, and two runs must write
the same bytes. We therefore copy a committed image byte-for-byte.
"""
import os
import shutil

ASSET = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(ASSET, OUT_FILE)
    print("wrote", OUT_FILE, os.path.getsize(OUT_FILE), "bytes")


if __name__ == "__main__":
    main()
