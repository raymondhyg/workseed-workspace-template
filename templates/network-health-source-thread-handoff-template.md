# Network Health Source Thread Handoff Template

Use this from the source/control thread when repeated reconnects, network
instability, port/proxy trouble, VPN/firewall suspicion, or `.codex/.env` comes
up during initialization or project work.

The source thread should stop expanding project work and prepare this handoff
for a narrow network health guidance thread.

```text
Please open a narrow WorkSeed Workspace network health guidance thread.

Source thread:
Workspace root:
Observed symptom:
- reconnect count:
- when it started:
- suspected trigger: port / proxy / VPN / firewall / restart / unknown

Goal:
Diagnose network health and reconnect stability only. Use the known successful
route where appropriate: Workspace-local `.codex/.env` port/proxy control,
then restart or reopen Codex, then ask the user whether reconnects stopped.

Read first:
1. WORKSPACE.md
2. workspace-system-manifest.md
3. docs/workspaces/network-health-and-reconnect-guide.md
4. templates/network-health-guidance-thread-prompt.md
5. templates/codex-env-network-template.txt
6. workspace-records/checks/network-health-check-template.md

Run:
python scripts/utils/check_network_health.py

Boundaries:
- Do not edit project facts.
- Do not install Core.
- Do not connect adapters.
- Do not write external task systems.
- Do not print env values, port values, proxy values, credentials, or private network details.
- Do not commit a real `.codex/.env`.
- Do not claim fixed until restart/reopen evidence and user confirmation exist.

Return to the source thread with:
- `.codex/.env` state: exists / missing / created locally / not checked
- keys present: key names only, values redacted
- action taken: guidance only / local file created by user / restart requested / restart done
- stability result: fixed / improved / not fixed / blocked / not verified
- if not fixed: next observed signal and next local check
- whether a local record should be written with
  workspace-records/checks/network-health-check-template.md
- whether sanitized Core feedback should be prepared with
  workspace-records/feedback/network-health-core-feedback-template.md
```
