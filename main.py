"""Make.fun bounty entry: the funniest excuse an agent gives for a missed deadline.

The entry is one deadpan line kept in entry.txt beside this script. Running the
program copies those exact bytes, unchanged, to <output dir>/entry.txt, because
the gate reads plain UTF-8 text of 1 to 200 non-whitespace-only characters.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

MAKEFUN_OUTPUT_DIR overrides the /output default so the copy can be exercised
outside the grader; nothing else about the bytes changes between runs.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

ENTRY_NAME = "entry.txt"
SOURCE = Path(__file__).resolve().parent / ENTRY_NAME


def main() -> None:
    if not SOURCE.is_file():
        raise FileNotFoundError(f"entry text is missing: {SOURCE}")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, output_dir / ENTRY_NAME)


if __name__ == "__main__":
    main()
