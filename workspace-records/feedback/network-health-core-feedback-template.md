# Network Health Core Feedback Template

Use this when a Template-derived Workspace hits repeated reconnects and the
network health guidance thread ends as `not fixed`, `blocked`, or a reusable
Template/Core improvement is discovered.

Do not copy local env values, port values, proxy values, private network
details, account state, project facts, or external system details into this
feedback.

## Feedback State

- status: proposed / sent / not sent
- source thread:
- network health guidance thread:
- related check record:
- Workspace root category: local / lab / real Workspace / unknown

## Sanitized Symptom

- symptom type: repeated reconnects / network unstable / port conflict / proxy issue / VPN or firewall suspicion / unknown
- reconnect count range: 1 / 2-4 / 5+ / unknown
- when observed: initialization / Core install / normal project work / after restart / unknown
- user impact:

## Local Check Summary

- `.codex/.env` state: missing / present / created locally / not checked
- recognized key names only:
- unknown key names only:
- values redacted: yes
- checker command: `python scripts/utils/check_network_health.py`

## Resolution State

- final state: fixed / improved / not fixed / blocked / not verified
- restart/reopen attempted: yes / no / unknown
- next local check: port / proxy / VPN / firewall / restart / blocked / unknown
- reusable Template/Core gap:

## Privacy Confirmation

- no env values included: yes / no
- no port/proxy values included: yes / no
- no credentials/account state included: yes / no
- no project facts included: yes / no
- no external task-system data included: yes / no

## Requested Core Decision

- ignore / observe / Template patch / Core checker patch / docs update / release candidate / Lab rehearsal needed
- reason:
