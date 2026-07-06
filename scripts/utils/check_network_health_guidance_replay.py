from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

REQUIRED = {
    "docs/workspaces/network-health-and-reconnect-guide.md": [
        "Resolution Loop",
        "`fixed`",
        "`improved`",
        "`not fixed`",
        "`blocked`",
        "Do not stop after the first `.codex/.env` suggestion",
        "re-run `python scripts/utils/check_network_health.py`",
        "port/proxy/VPN/firewall clues",
    ],
    "templates/network-health-guidance-thread-prompt.md": [
        "If reconnects continue, do not stop at the first suggestion",
        "re-run `python scripts/utils/check_network_health.py`",
        "fixed, improved, not fixed, or blocked",
        "Resolution loop: stopped after user confirmed fixed",
        "continued after not",
        "blocked with reason",
    ],
    "workspace-records/checks/network-health-check-template.md": [
        "## Resolution Loop",
        "user confirmed reconnects stopped",
        "if not fixed, next observed signal",
        "repeated checker command",
        "next local check: port / proxy / VPN / firewall / restart / blocked",
        "final state: fixed / improved / not fixed / blocked / not verified",
    ],
    "scripts/utils/check_network_health.py": [
        "status",
        "configured",
        "present_without_known_network_keys",
        "values_redacted",
        "No env values printed.",
    ],
}

SCENARIO_SNIPPETS = [
    "Create .codex/.env from templates/codex-env-network-template.txt.",
    "Restart or reopen Codex, then verify whether reconnects stop.",
    "Record the result with workspace-records/checks/network-health-check-template.md.",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def require_text(rel: str, snippets: list[str]) -> None:
    path = ROOT / rel
    if not path.exists():
        fail(f"missing file: {rel}")
    text = path.read_text(encoding="utf-8")
    normalized = " ".join(text.split())
    for snippet in snippets:
        if snippet not in text and " ".join(snippet.split()) not in normalized:
            fail(f"{rel} missing text: {snippet}")


def main() -> int:
    for rel, snippets in REQUIRED.items():
        require_text(rel, snippets)

    checker_text = (ROOT / "scripts/utils/check_network_health.py").read_text(encoding="utf-8")
    for snippet in SCENARIO_SNIPPETS:
        if snippet not in checker_text:
            fail(f"check_network_health.py missing scenario action: {snippet}")

    print("[PASS] Network health guidance replay passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
