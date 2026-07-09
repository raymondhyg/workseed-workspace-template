from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

AGENT_GLOB = ".codex/agents/*.toml"
SKILL_ROOT = ".agents/skills"

EXPECTED_AGENT_FILES = [
    ".codex/agents/capability-radar.toml",
    ".codex/agents/mark.toml",
    ".codex/agents/mira.toml",
    ".codex/agents/prism.toml",
    ".codex/agents/system-maintainer.toml",
    ".codex/agents/workflow-coach.toml",
]

EXPECTED_SKILL_DIRS = [
    ".agents/skills/b2b-strategy",
    ".agents/skills/background-memory",
    ".agents/skills/capability-radar",
    ".agents/skills/ecommerce-domain",
    ".agents/skills/image-production",
    ".agents/skills/prism-writeback",
    ".agents/skills/reference-learning",
    ".agents/skills/workflow-coach",
]

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


class InstallPlan:
    def __init__(self) -> None:
        self.installed: list[str] = []
        self.missing: list[str] = []
        self.skipped: list[str] = []


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


def copy_file(source_root: Path, rel: Path, plan: InstallPlan, dry_run: bool) -> None:
    check_forbidden(rel)
    src = source_root / rel
    dst = ROOT / rel
    if not src.exists():
        plan.missing.append(safe_rel(rel))
        return
    plan.installed.append(safe_rel(rel))
    if dry_run:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_dir(source_root: Path, rel: Path, plan: InstallPlan, dry_run: bool) -> None:
    check_forbidden(rel)
    src = source_root / rel
    dst = ROOT / rel
    if not src.exists():
        plan.missing.append(safe_rel(rel))
        return
    plan.installed.append(safe_rel(rel))
    if dry_run:
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def install_from_core(core_root: Path, core_version: str, source_label: str, source_type: str, dry_run: bool) -> InstallPlan:
    plan = InstallPlan()

    for rel_text in EXPECTED_AGENT_FILES:
        copy_file(core_root, Path(rel_text), plan, dry_run)

    for rel_text in EXPECTED_SKILL_DIRS:
        copy_dir(core_root, Path(rel_text), plan, dry_run)

    for rel_text in SUPPORT_PATHS:
        rel = Path(rel_text)
        src = core_root / rel
        if src.is_dir():
            copy_dir(core_root, rel, plan, dry_run)
        else:
            copy_file(core_root, rel, plan, dry_run)

    for agent in sorted(core_root.glob(AGENT_GLOB)):
        rel = agent.relative_to(core_root)
        rel_text = safe_rel(rel)
        if rel_text not in plan.installed and rel_text not in EXPECTED_AGENT_FILES:
            plan.skipped.append(rel_text)

    skill_root = core_root / SKILL_ROOT
    if skill_root.exists():
        for skill_dir in sorted(p for p in skill_root.iterdir() if p.is_dir()):
            rel = skill_dir.relative_to(core_root)
            rel_text = safe_rel(rel)
            if rel_text not in plan.installed and rel_text not in EXPECTED_SKILL_DIRS:
                plan.skipped.append(rel_text)

    if not plan.installed:
        fail("no capability runtime files were found to install")

    if not dry_run:
        write_record(core_version, source_label, source_type, plan)

    return plan


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def render_lines(items: list[str], empty: str) -> str:
    if not items:
        return f"- {empty}"
    return "\n".join(f"- `{item}`" for item in items)


def write_record(core_version: str, source_label: str, source_type: str, plan: InstallPlan) -> None:
    today = dt.date.today().isoformat()
    safe_version = core_version.replace("/", "-").replace("\\", "-")
    record_dir = ROOT / "workspace-records" / "capability-loads"
    record_dir.mkdir(parents=True, exist_ok=True)
    record = record_dir / f"{today}-{safe_version}-capability-load.md"
    installed_lines = render_lines(plan.installed, "none")
    missing_lines = render_lines(plan.missing, "none")
    skipped_lines = render_lines(plan.skipped, "none")
    record.write_text(
        f"""# Core Capability Load Record

Date: {today}

Workspace: WorkSeed Workspace

Requested Core version: `{core_version}`

Source type: `{source_type}`

Core package source: `{source_label}`

Source identity: `{source_label}`

## Installed Runtime Surfaces

{installed_lines}

## Missing Runtime Surfaces

{missing_lines}

## Skipped Extra Runtime Surfaces

{skipped_lines}

## Runtime Availability

Runtime availability: `not verified`

Reason: file installation and Codex runtime refresh are separate states. Reopen
or restart this Workspace in Codex, then verify whether project agents and
skills are visible or callable.

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
            source_label = f"{zip_path} sha256={sha256_file(zip_path)}"
            plan = install_from_core(core_root, args.core_version, source_label, "zip package", args.dry_run)
    else:
        source_path = Path(args.source_path).expanduser().resolve()
        if not source_path.exists():
            fail(f"source path not found: {source_path}")
        core_root = find_core_root(source_path)
        plan = install_from_core(core_root, args.core_version, str(source_path), "local Core repo or extracted package folder", args.dry_run)

    print("[PASS] Core capability runtime install prepared")
    print("installed:")
    for item in plan.installed:
        print(f"- {item}")
    print("missing:")
    for item in plan.missing or ["none"]:
        print(f"- {item}")
    print("skipped:")
    for item in plan.skipped or ["none"]:
        print(f"- {item}")
    if args.dry_run:
        print("dry-run only; no files copied")
    else:
        print("next: restart or reopen the Workspace in Codex if project agents do not appear immediately")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
