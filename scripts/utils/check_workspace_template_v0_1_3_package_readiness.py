from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

PACKAGE_REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    ".gitignore",
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
    "scripts/utils/check_workspace_deployment.py",
    "scripts/utils/check_workspace_template_v0_1_3_package_readiness.py",
    "scripts/utils/verify_open_box.py",
    "workspace-records/checks/network-health-check-template.md",
    "workspace-records/feedback/network-health-core-feedback-template.md",
]

REQUIRED_SNIPPETS = {
    "docs/releases/workspace-template-v0.1.3-candidate.md": [
        "发布版本：`workspace-template-v0.1.3` candidate",
        "尚未 tag、尚未 GitHub Release、尚未发布",
        "网络健康与重连恢复开箱指引",
        "scripts/utils/check_network_health_guidance_replay.py",
        "scripts/utils/check_network_health_redaction.py",
        "does not claim publication",
    ],
    "docs/workspaces/network-health-and-reconnect-guide.md": [
        "Resolution Loop",
        "Do not stop after the first `.codex/.env` suggestion",
        "re-run `python scripts/utils/check_network_health.py`",
    ],
    "templates/network-health-guidance-thread-prompt.md": [
        "If reconnects continue, do not stop at the first suggestion",
        "Resolution loop: stopped after user confirmed fixed",
    ],
    "templates/network-health-source-thread-handoff-template.md": [
        "Network Health Source Thread Handoff Template",
        "Return to the source thread with:",
        "stability result: fixed / improved / not fixed / blocked / not verified",
    ],
    "workspace-records/checks/network-health-check-template.md": [
        "## Resolution Loop",
        "final state: fixed / improved / not fixed / blocked / not verified",
    ],
    "workspace-records/feedback/network-health-core-feedback-template.md": [
        "Network Health Core Feedback Template",
        "recognized key names only",
        "values redacted: yes",
        "no env values included",
        "Requested Core Decision",
    ],
    ".gitignore": [
        ".codex/.env",
    ],
}

FORBIDDEN_TRACKED_PATHS = [
    ".codex/.env",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def is_git_tracked(rel: str) -> bool:
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", rel],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    return result.returncode == 0


def require_text(rel: str, snippets: list[str]) -> None:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing package candidate file: {rel}")
    text = path.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    for snippet in snippets:
        if snippet not in text and " ".join(snippet.split()) not in normalized:
            fail(f"{rel} missing text: {snippet}")


def main() -> int:
    for rel in PACKAGE_REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            fail(f"missing package candidate file: {rel}")

    for rel, snippets in REQUIRED_SNIPPETS.items():
        require_text(rel, snippets)

    for rel in FORBIDDEN_TRACKED_PATHS:
        if is_git_tracked(rel):
            fail(f"forbidden tracked local runtime file: {rel}")

    print("[PASS] Workspace Template v0.1.3 package readiness passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
