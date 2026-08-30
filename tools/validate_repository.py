from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "REPOSITORY_MANIFEST.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    try:
        payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
        listed = {entry["path"]: entry for entry in payload["files"]}
        actual = {
            path.relative_to(ROOT).as_posix(): path
            for path in ROOT.rglob("*")
            if path.is_file() and ".git" not in path.parts and path != MANIFEST
        }
        if set(listed) != set(actual):
            raise ValueError("El conjunto de archivos no coincide con el manifiesto")
        for relative, path in actual.items():
            entry = listed[relative]
            if entry["bytes"] != path.stat().st_size or entry["sha256"] != sha256(path):
                raise ValueError(f"Integridad incorrecta: {relative}")
        for path in ROOT.rglob("*.json"):
            json.loads(path.read_text(encoding="utf-8-sig"))
        for path in ROOT.rglob("*.csv"):
            with path.open(encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.reader(handle))
                if not rows:
                    raise ValueError(f"CSV vacío: {path.relative_to(ROOT)}")
                header_index = 1 if len(rows) > 1 and len(rows[0]) == 1 and len(rows[1]) > 1 else 0
                width = len(rows[header_index])
                data_rows = [row for row in rows[header_index + 1 :] if row and any(cell.strip() for cell in row)]
                if width == 0 or any(len(row) != width for row in data_rows):
                    raise ValueError(f"CSV irregular: {path.relative_to(ROOT)}")
        print(f"REPOSITORY_VALID files={len(actual)}")
        return 0
    except (OSError, ValueError, json.JSONDecodeError, csv.Error) as error:
        print(f"REPOSITORY_INVALID: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
