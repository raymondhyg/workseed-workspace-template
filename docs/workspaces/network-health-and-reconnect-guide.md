# Network Health And Reconnect Guide

This guide helps a new WorkSeed Workspace handle repeated network reconnects
before the user loses confidence in the Workspace.

## When To Use This Guide

Use this guide when the user mentions:

- repeated reconnects
- network unstable
- Codex keeps reconnecting
- 5 reconnects
- proxy or port trouble
- cannot keep a stable Codex session
- 网络重连
- 网络不稳定
- 一直重连
- 端口

Plain rule:

```text
Do not keep doing project work in an unstable main thread.
Create a narrow network health guidance thread, diagnose there, and return a
short result to the source thread.
```

## Source Thread Rule

The current Workspace thread is the source/control thread. It should preserve
the project context and ask the user to open a narrow network health guidance
thread with `templates/network-health-guidance-thread-prompt.md`.

Use `templates/network-health-source-thread-handoff-template.md` when the source
thread needs a ready-to-send handoff for the narrow guidance thread.

The source thread should not claim the network is fixed until the guidance
thread reports evidence and the user confirms the session is stable.

## Local `.codex/.env` Route

The proven local repair route is to create a Workspace-local `.codex/.env`
file and use it to control the network port or proxy-related environment
values for the local Codex runtime.

Plain action: restart or reopen Codex after changing `.codex/.env`.

Do not commit a real `.codex/.env` file. It is local machine configuration.
Use the template at:

```text
templates/codex-env-network-template.txt
```

Use the local checker to inspect the state without printing private values:

```powershell
python scripts/utils/check_network_health.py
```

Suggested local steps:

1. Create the `.codex` folder if it does not exist.
2. Copy `templates/codex-env-network-template.txt` to `.codex/.env`.
3. Fill only the values that match the user's local network.
4. Restart or reopen Codex so the runtime reads the local environment file.
5. Run `python scripts/utils/check_network_health.py` to confirm only key names
   are visible and values are redacted.
6. Keep the source thread open as the control thread.
7. Use a narrow network health guidance thread to verify stability.

## Resolution Loop

The guidance thread should keep working until one of these states is true:

- `fixed`: the user restarted or reopened Codex and confirms reconnects
  stopped.
- `improved`: reconnects are less frequent, but remaining risk is recorded and
  the next local check is named.
- `not fixed`: reconnects continue after restart/reopen, so the guidance thread
  asks for the next signal, re-run `python scripts/utils/check_network_health.py`,
  reviews local port/proxy/VPN/firewall clues, and records the unresolved
  state before returning to the source thread.
- `blocked`: the user cannot change local network settings or cannot restart
  Codex; the thread records the blocker and next owner.

Do not stop after the first `.codex/.env` suggestion if the user reports that
reconnects continue. Iterate with the user's observed result and keep values
redacted.

## What The Guidance Thread Should Check

The guidance thread should:

1. Confirm it is running inside the same Workspace root.
2. Read this guide, the `.env` template, `WORKSPACE.md`, and
   `workspace-system-manifest.md`.
3. Ask what the user observed: number of reconnects, when it started, and
   whether a proxy, VPN, firewall, port conflict, or runtime restart is
   involved.
4. Check whether `.codex/.env` exists locally.
5. If it exists, report which keys are present without revealing secret values.
6. If it is missing, guide the user to create it from the template.
7. Run `python scripts/utils/check_network_health.py` and use the output as
   local evidence.
8. Recommend a restart/reopen test after the local `.codex/.env` change.
9. If reconnects continue, ask for the next observed signal, re-run the local
   checker, and keep the thread focused on network health until `fixed`,
   `improved`, `not fixed`, or `blocked` is honestly recorded.
10. Report the result back to the source thread.

## Boundary

- Do not expose tokens, credentials, cookies, account state, or private proxy
  values.
- Do not commit `.codex/.env`.
- Do not modify project facts, Core release files, adapters, or external task
  systems from the network health thread.
- Do not claim a permanent fix until the user confirms the reconnect problem
  stopped after restart/reopen.

## Evidence To Record

If the fix is useful for this Workspace, record a short local note under
`workspace-records/checks/` or `workspace-records/decisions/` with:

- observed symptom
- local `.codex/.env` status
- values changed, with secrets redacted
- restart/reopen result
- remaining risk
- whether a sanitized feedback signal should be sent to Core

Use this record template when a durable local check is useful:

```text
workspace-records/checks/network-health-check-template.md
```

If the final state is `not fixed`, `blocked`, or reveals a reusable
Template/Core gap, prepare a sanitized feedback signal with:

```text
workspace-records/feedback/network-health-core-feedback-template.md
```

Do not include local env values, port values, proxy values, account state,
project facts, or external system details in Core feedback.
