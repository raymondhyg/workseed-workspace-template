# <core-version> Workspace Adoption Record

Workspace:
Adoption date:
Adoption type: real Workspace / Workspace Lab / read-only preflight
State: Not evaluated / Eligible / Planned / Applied / Partial / Skipped / Blocked

## Version Range

From version:
To version:
Core tag:
Core target commit:
Workspace commit before:
Workspace commit after:

## Changed File Classes

| File class | Action | Reason |
|---|---|---|
| Core-following docs | Review / merge / skip |  |
| Core-following templates | Review / merge / skip |  |
| Checkers | Review / merge / skip |  |
| Workspace-owned records | Update locally / skip |  |
| Workspace project context | Protect |  |

## Protected Surfaces

- `projects/**`
- `WORKSPACE.md`
- `workspace-system-manifest.md`
- `workspace-records/**`
- local project docs, plans, and decisions
- remotes, deployment settings, private materials, raw assets, account state, adapter configuration, and external-system state

## Required Named Capability States

Prism:
Mark:
mira:

Default: required identity present; live use is `Not evaluated` unless supported
by Workspace-owned evidence and authorization.

## Adapter State

Default: `Mock/read-only only` unless explicitly authorized.

## Verification

| Command | Result |
|---|---|
|  |  |

## Non-Claims

This record does not claim real Workspace adoption unless files or migration steps were applied, manifest/adoption records were updated, and verification passed.
