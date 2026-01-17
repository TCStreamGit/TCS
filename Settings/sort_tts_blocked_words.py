#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
from typing import List


def is_comment_or_blank(line: str) -> bool:
    t = line.strip()
    if t == "":
        return True
    if t.startswith("#"):
        return True
    if t.startswith("//"):
        return True
    return False


def main() -> int:
    base_dir = Path(__file__).resolve().parent
    infile = base_dir / "TTS-Blocked-Words.txt"

    if not infile.exists():
        print(f'File not found: "{infile}"')
        return 1

    lines = infile.read_text(encoding="utf-8").splitlines()

    header: List[str] = []
    items: List[str] = []

    for line in lines:
        if is_comment_or_blank(line):
            header.append(line)
            continue

        # Split comma-separated entries on a line, trim each, lowercase them.
        parts = [p.strip() for p in line.split(",")]
        for p in parts:
            if p:
                items.append(p.lower())

    # Sort A–Z (case-insensitive already, since we lowercased) and dedupe.
    sorted_unique = sorted(set(items))

    # Rebuild file: keep original header/comments/blank lines as-is,
    # then one blank line (if needed), then sorted entries.
    out: List[str] = []
    out.extend(header)

    if out and out[-1].strip() != "":
        out.append("")

    out.extend(sorted_unique)

    # Write atomically (safer): write temp then replace.
    tmp = infile.with_suffix(infile.suffix + ".tmp")
    tmp.write_text("\n".join(out) + "\n", encoding="utf-8")
    tmp.replace(infile)

    print(f"Done. Sorted {len(sorted_unique)} entries in {infile.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
