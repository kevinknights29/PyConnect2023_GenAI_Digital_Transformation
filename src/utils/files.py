from __future__ import annotations

from pathlib import Path


def find_file(dir: str, pattern: str = "*.txt") -> str:
    path = Path(dir)
    file_path = list(path.glob(pattern))[0]
    return str(file_path.resolve())
