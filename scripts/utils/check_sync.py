from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "WORKSPACE.md",
    "workspace-system-manifest.md",
    "workspace-records/README.md",
    "scripts/utils/check_workspace_deployment.py",
    "scripts/utils/verify_open_box.py",
]

PRIVATE_PATH_PARTS = {
    ".raw",
    "raw",
    "source",
    "source-photos",
    "reference-files",
    "reference-images",
    "private",
    "local-private",
    "storage_state.json",
}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|password|secret)\s*=\s*['\"][^'\"]{6,}['\"]"),
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def main() -> int:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            fail(f"missing required path: {rel}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        rel_parts = set(path.relative_to(ROOT).parts)
        if rel_parts & PRIVATE_PATH_PARTS:
            fail(f"private/raw path should not be committed: {path.relative_to(ROOT)}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path == Path(__file__).resolve():
            continue
        if path.suffix.lower() not in {".md", ".py", ".txt", ".toml", ".json", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"possible secret assignment in {path.relative_to(ROOT)}")

    print("[PASS] Workspace sync checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
