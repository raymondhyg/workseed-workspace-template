from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = ROOT / ".codex" / ".env"
TEMPLATE_PATH = ROOT / "templates" / "codex-env-network-template.txt"
GUIDE_PATH = ROOT / "docs" / "workspaces" / "network-health-and-reconnect-guide.md"
RECORD_TEMPLATE_PATH = ROOT / "workspace-records" / "checks" / "network-health-check-template.md"

NETWORK_KEYS = {
    "CODEX_PORT",
    "CODEX_API_PORT",
    "CODEX_BROWSER_PORT",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "NO_PROXY",
}


def parse_env_keys(path: Path) -> list[str]:
    keys: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key = line.split("=", 1)[0].strip()
        if key:
            keys.append(key)
    return sorted(dict.fromkeys(keys))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check WorkSeed Workspace network-health local env state without printing private values."
    )
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument(
        "--env-path",
        default=str(ENV_PATH),
        help="Optional env file path to inspect; defaults to Workspace-local .codex/.env.",
    )
    args = parser.parse_args()

    env_path = Path(args.env_path).expanduser()
    if not env_path.is_absolute():
        env_path = ROOT / env_path

    env_exists = env_path.exists()
    keys = parse_env_keys(env_path) if env_exists else []
    recognized_keys = [key for key in keys if key in NETWORK_KEYS]
    unknown_keys = [key for key in keys if key not in NETWORK_KEYS]

    status = "configured" if recognized_keys else "missing"
    if env_exists and not recognized_keys:
        status = "present_without_known_network_keys"

    next_actions: list[str] = []
    if not env_exists:
        next_actions.extend(
            [
                "Create .codex/.env from templates/codex-env-network-template.txt.",
                "Fill only local port or proxy values that apply to this machine.",
            ]
        )
    elif not recognized_keys:
        next_actions.append("Review .codex/.env and add only the needed network keys from the template.")
    else:
        next_actions.append("Restart or reopen Codex, then verify whether reconnects stop.")

    next_actions.append("Record the result with workspace-records/checks/network-health-check-template.md.")

    result = {
        "workspace_root": str(ROOT),
        "guide": GUIDE_PATH.as_posix(),
        "env_path": ".codex/.env" if env_path == ENV_PATH else str(env_path),
        "env_exists": env_exists,
        "status": status,
        "recognized_key_names": recognized_keys,
        "unknown_key_names": unknown_keys,
        "values_redacted": True,
        "template": TEMPLATE_PATH.as_posix(),
        "record_template": RECORD_TEMPLATE_PATH.as_posix(),
        "next_actions": next_actions,
        "boundary": [
            "No env values printed.",
            "No files changed.",
            "No adapter connected.",
            "No external system written.",
        ],
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=True, indent=2))
        return 0

    print("[PASS] Network health local env check completed")
    print(f"workspace_root: {ROOT}")
    print(f"env_path: {'.codex/.env' if env_path == ENV_PATH else env_path}")
    print(f"env_exists: {str(env_exists).lower()}")
    print(f"status: {status}")
    print("recognized_key_names:")
    for key in recognized_keys or ["none"]:
        print(f"- {key}")
    print("unknown_key_names:")
    for key in unknown_keys or ["none"]:
        print(f"- {key}")
    print("values_redacted: true")
    print("next_actions:")
    for action in next_actions:
        print(f"- {action}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
