from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "manifests" / "REPOSITORY_MANIFEST.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    files = []
    extensions: Counter[str] = Counter()
    total_bytes = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path == OUTPUT:
            continue
        relative = path.relative_to(ROOT).as_posix()
        size = path.stat().st_size
        extension = path.suffix.lower() or "[no-extension]"
        files.append({"path": relative, "bytes": size, "sha256": sha256(path)})
        extensions[extension] += 1
        total_bytes += size

    payload = {
        "schema_version": 1,
        "purpose": "Inventario autocontenido del paquete GitHub del TFM desde V2",
        "file_count_excluding_manifest_and_git": len(files),
        "total_bytes_excluding_manifest_and_git": total_bytes,
        "extensions": dict(sorted(extensions.items())),
        "files": files,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"REPOSITORY_MANIFEST_UPDATED files={len(files)} bytes={total_bytes}")


if __name__ == "__main__":
    main()
