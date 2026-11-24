# SPDX-License-Identifier: MIT
"""Write the stored job title to the grader's output directory.

The entry text lives in entry.txt next to this script. This program copies
it byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt, the artifact the
competition gate reads. Standard library only; no network, no fonts,
no third-party packages.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.txt"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    destination = Path(output_dir) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
