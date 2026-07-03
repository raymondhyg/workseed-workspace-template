from __future__ import annotations

import argparse
import datetime as dt
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

AGENT_GLOB = ".codex/agents/*.toml"
SKILL_ROOT = ".agents/skills"

SUPPORT_PATHS = [
    "docs/codex/prism-knowledge-writeback.md",
    "docs/capability-packs",
    "docs/core/p1",
    "templates/b2b-strategy-brief-template.md",
    "templates/image-production-brief-template.md",
    "templates/mark-mira-prism-handoff-template.md",
    "templates/prism-decision-template.md",
    "templates/ecommerce-business-operation-run-template.md",
]

FORBIDDEN_PARTS = {
    ".git",
    ".raw",
    "raw",
    "source",
    "source-photos",
    "reference-files",
    "reference-images",
    "private",
    "local-private",
}


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def safe_rel(path: Path) -> str:
    return path.as_posix()


def has_core_shape(path: Path) -> bool:
    return (path / "AGENTS.md").exists() and (
        (path / ".codex" / "agents").exists() or (path / ".agents" / "skills").exists()
    )


def find_core_root(path: Path) -> Path:
    if has_core_shape(path):
        return path
    candidates = [p for p in path.iterdir() if p.is_dir() and has_core_shape(p)]
    if len(candidates) == 1:
        return candidates[0]
    fail(f"could not identify Core package root under {path}")


def check_forbidden(rel: Path) -> None:
    if set(rel.parts) & FORBIDDEN_PARTS:
        fail(f"refusing to copy private/raw path: {safe_rel(rel)}")


def copy_file(source_root: Path, rel: Path, installed: list[str], dry_run: bool) -> None:
    check_forbidden(rel)
    src = source_root / rel
    dst = ROOT / rel
    if not src.exists():
        return
    installed.append(safe_rel(rel))
    if dry_run:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_dir(source_root: Path, rel: Path, installed: list[str], dry_run: bool) -> None:
    check_forbidden(rel)
    src = source_root / rel
    dst = ROOT / rel
    if not src.exists():
        return
    installed.append(safe_rel(rel))
    if dry_run:
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def install_from_core(core_root: Path, core_version: str, source_label: str, dry_run: bool) -> list[str]:
    installed: list[str] = []

    for agent in sorted(core_root.glob(AGENT_GLOB)):
        copy_file(core_root, agent.relative_to(core_root), installed, dry_run)

    skill_root = core_root / SKILL_ROOT
    if skill_root.exists():
        for skill_dir in sorted(p for p in skill_root.iterdir() if p.is_dir()):
            copy_dir(core_root, skill_dir.relative_to(core_root), installed, dry_run)

    for rel_text in SUPPORT_PATHS:
        rel = Path(rel_text)
        src = core_root / rel
        if src.is_dir():
            copy_dir(core_root, rel, installed, dry_run)
        else:
            copy_file(core_root, rel, installed, dry_run)

    if not installed:
        fail("no capability runtime files were found to install")

    if not dry_run:
        write_record(core_version, source_label, installed)

    return installed


def write_record(core_version: str, source_label: str, installed: list[str]) -> None:
    today = dt.date.today().isoformat()
    safe_version = core_version.replace("/", "-").replace("\\", "-")
    record_dir = ROOT / "workspace-records" / "capability-loads"
    record_dir.mkdir(parents=True, exist_ok=True)
    record = record_dir / f"{today}-{safe_version}-capability-load.md"
    installed_lines = "\n".join(f"- `{item}`" for item in installed)
    record.write_text(
        f"""# Core Capability Load Record

Date: {today}

Workspace: WorkSeed Workspace

Requested Core version: `{core_version}`

Core package source: `{source_label}`

## Installed Runtime Surfaces

{installed_lines}

## Verification

Run after installation:

```powershell
python scripts/utils/check_workspace_deployment.py
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
```

## Boundary

This load does not claim product-grade readiness, source-equivalent capability,
real adapter connection, external task-system write, or private Core GitHub
access. Private facts and project materials remain Workspace-owned.
""",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install WorkSeed Core capability runtime files into this Workspace.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--source-path", help="Path to a local Core checkout or extracted Core package folder.")
    group.add_argument("--zip-path", help="Path to a Core package zip file.")
    parser.add_argument("--core-version", default="ws-core-v0.3.0", help="Core version label to record.")
    parser.add_argument("--dry-run", action="store_true", help="List files that would be installed without copying.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.zip_path:
        zip_path = Path(args.zip_path).expanduser().resolve()
        if not zip_path.exists():
            fail(f"zip package not found: {zip_path}")
        with tempfile.TemporaryDirectory(prefix="workseed-core-package-") as tmp:
            tmp_path = Path(tmp)
            with zipfile.ZipFile(zip_path) as archive:
                archive.extractall(tmp_path)
            core_root = find_core_root(tmp_path)
            installed = install_from_core(core_root, args.core_version, str(zip_path), args.dry_run)
    else:
        source_path = Path(args.source_path).expanduser().resolve()
        if not source_path.exists():
            fail(f"source path not found: {source_path}")
        core_root = find_core_root(source_path)
        installed = install_from_core(core_root, args.core_version, str(source_path), args.dry_run)

    print("[PASS] Core capability runtime install prepared")
    for item in installed:
        print(f"- {item}")
    if args.dry_run:
        print("dry-run only; no files copied")
    else:
        print("next: restart or reopen the Workspace in Codex if project agents do not appear immediately")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
