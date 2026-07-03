from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def run(command: list[str]) -> None:
    print("$ " + " ".join(command))
    result = subprocess.run(command, cwd=ROOT, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> int:
    run([sys.executable, "scripts/utils/check_sync.py"])
    run([sys.executable, "scripts/utils/check_workspace_deployment.py"])
    print("[PASS] Workspace open-box verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
