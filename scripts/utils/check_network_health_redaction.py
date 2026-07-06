from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

SENTINELS = [
    "98765",
    "local-redaction-probe.invalid",
    "SHOULD_NOT_PRINT",
]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    raise SystemExit(1)


def run_checker(env_path: Path, machine: bool) -> str:
    command = [
        sys.executable,
        "scripts/utils/check_network_health.py",
        "--env-path",
        str(env_path),
    ]
    if machine:
        command.append("--json")
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode != 0:
        if result.stdout:
            print(result.stdout.rstrip())
        if result.stderr:
            print(result.stderr.rstrip())
        fail("check_network_health.py returned non-zero")
    return result.stdout


def require_no_sentinels(output: str, label: str) -> None:
    for sentinel in SENTINELS:
        if sentinel in output:
            fail(f"{label} leaked sentinel value: {sentinel}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="workseed-network-health-") as tmp:
        env_path = Path(tmp) / ".env"
        env_path.write_text(
            "\n".join(
                [
                    "CODEX_PORT=98765",
                    "HTTPS_PROXY=http://local-redaction-probe.invalid:4321",
                    "NO_PROXY=localhost,127.0.0.1",
                    "UNKNOWN_TEST=SHOULD_NOT_PRINT",
                    "",
                ]
            ),
            encoding="utf-8",
        )

        human_output = run_checker(env_path, machine=False)
        require_no_sentinels(human_output, "human output")
        for expected in ["CODEX_PORT", "HTTPS_PROXY", "NO_PROXY", "UNKNOWN_TEST", "values_redacted: true"]:
            if expected not in human_output:
                fail(f"human output missing redacted key/status: {expected}")

        machine_output = run_checker(env_path, machine=True)
        require_no_sentinels(machine_output, "json output")
        data = json.loads(machine_output)
        for expected in ["CODEX_PORT", "HTTPS_PROXY", "NO_PROXY"]:
            if expected not in data["recognized_key_names"]:
                fail(f"json output missing recognized key: {expected}")
        if "UNKNOWN_TEST" not in data["unknown_key_names"]:
            fail("json output missing unknown key name")
        if data["values_redacted"] is not True:
            fail("json output does not mark values_redacted true")

    print("[PASS] Network health redaction passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
