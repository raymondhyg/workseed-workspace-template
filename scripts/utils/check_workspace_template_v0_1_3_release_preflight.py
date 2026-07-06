from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

RELEASE_REQUIRED_TRACKED_PATHS = [
    ".gitignore",
    "AGENTS.md",
    "README.md",
    "docs/releases/workspace-template-v0.1.3-candidate.md",
    "docs/workspaces/initialization-and-core-loading.md",
    "docs/workspaces/network-health-and-reconnect-guide.md",
    "templates/first-workspace-initialization-prompt.md",
    "templates/network-health-guidance-thread-prompt.md",
    "templates/network-health-source-thread-handoff-template.md",
    "templates/codex-env-network-template.txt",
    "scripts/utils/check_network_health.py",
    "scripts/utils/check_network_health_redaction.py",
    "scripts/utils/check_network_health_guidance_replay.py",
    "scripts/utils/check_workspace_template_v0_1_3_package_readiness.py",
    "scripts/utils/check_workspace_template_v0_1_3_release_preflight.py",
    "scripts/utils/check_workspace_deployment.py",
    "scripts/utils/verify_open_box.py",
    "workspace-records/checks/network-health-check-template.md",
    "workspace-records/feedback/network-health-core-feedback-template.md",
]

FORBIDDEN_TRACKED_PATHS = [
    ".codex/.env",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def git_tracked(rel: str) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", rel],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    return result.returncode == 0


def in_head(rel: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", f"HEAD:{rel}"],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    return result.returncode == 0


def dirty_required_paths() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--", *RELEASE_REQUIRED_TRACKED_PATHS],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        fail(result.stderr.strip() or "git status failed")
    dirty: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        dirty.append(line[3:] if len(line) > 3 else line)
    return dirty


def main() -> int:
    missing = [rel for rel in RELEASE_REQUIRED_TRACKED_PATHS if not (ROOT / rel).exists()]
    if missing:
        fail("missing release candidate files: " + ", ".join(missing))

    untracked = [rel for rel in RELEASE_REQUIRED_TRACKED_PATHS if not git_tracked(rel)]
    if untracked:
        fail(
            "release preflight requires these files to be git-tracked before release commit/tag/archive: "
            + ", ".join(untracked)
        )

    not_in_head = [rel for rel in RELEASE_REQUIRED_TRACKED_PATHS if not in_head(rel)]
    if not_in_head:
        fail(
            "release preflight requires these files to exist in HEAD before tag/archive: "
            + ", ".join(not_in_head)
        )

    dirty = dirty_required_paths()
    if dirty:
        fail(
            "release preflight requires no uncommitted changes in candidate files before tag/archive: "
            + ", ".join(dirty)
        )

    forbidden = [rel for rel in FORBIDDEN_TRACKED_PATHS if git_tracked(rel)]
    if forbidden:
        fail("forbidden local runtime files are git-tracked: " + ", ".join(forbidden))

    print("[PASS] Workspace Template v0.1.3 release preflight passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
