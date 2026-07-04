# Core Residency Repair Implementation Record

Date: 2026-07-04

Workspace surface: public WorkSeed Workspace Template

Template version: `workspace-template-v0.1.2`

Core base: `ws-core-v0.3.0`

Result: file-level `Partial`

## Why This Repair Exists

WorkSeed Core Lab testing showed that the Template could run a Core capability
installer, but the generated load record and checker were too weak to prove
Core residency.

This repair keeps the public Template boundary: no private Workspace facts,
customer data, raw assets, credentials, adapter state, or external task-system
state were added.

## Changed Public Template Surfaces

- `scripts/utils/install_core_capabilities.py`
- `scripts/utils/check_workspace_deployment.py`
- `templates/core-capability-load-record-template.md`
- `templates/core-runtime-availability-verification-prompt.md`
- `docs/workspaces/initialization-and-core-loading.md`
- `README.md`

## Implemented Behavior

- Installer records installed runtime surfaces.
- Installer records missing runtime surfaces.
- Installer records skipped extra runtime surfaces.
- Installer records source type and source identity.
- Installer records runtime availability as separate from file installation.
- Checker validates installed Core runtime files when a capability-load record
  exists.
- Checker allows Workspace identity fields to change after a new Workspace is
  created from the Template.
- Documentation explains that WorkSeed Core is the continuously iterating
  capability core, while each Workspace owns local truth.
- Runtime verification has a reusable prompt so a reopened Workspace can
  separate file installation, local checks, and current Codex runtime
  visibility.
- Runtime verification guidance now states that availability must be checked
  from the generated Workspace itself as the Codex active project, not from
  Core, Template, projectless, or another Workspace thread.
- Runtime visibility test-thread closure is now standardized: the test thread
  only verifies, the source thread reads back and confirms current state, and
  the source thread archives the test thread after recording verified evidence.

## Verification

Template-local checks:

- `python scripts/utils/check_workspace_deployment.py` passed.
- `python scripts/utils/check_sync.py` passed.
- `python scripts/utils/verify_open_box.py` passed.

Clean Lab reset check:

- Lab run surface:
  `E:\Claude Code Projects\workseed-workspace-lab-core-residency-run2`
- Installer dry-run against WorkSeed Core passed.
- Real install passed.
- Missing runtime surfaces: `none`.
- Skipped extra runtime surfaces: `none`.
- Lab `check_workspace_deployment.py` passed.
- Lab `check_sync.py` passed.
- Lab `verify_open_box.py` passed.

Latest Template reset check after adding runtime verification prompt:

- Lab run surface:
  `E:\Claude Code Projects\workseed-workspace-lab-core-residency-run3`
- `templates/core-runtime-availability-verification-prompt.md` was present in
  the clean reset.
- Installer dry-run against WorkSeed Core passed.
- Real install passed.
- Missing runtime surfaces: `none`.
- Skipped extra runtime surfaces: `none`.
- Lab `check_workspace_deployment.py` passed.
- Lab `check_sync.py` passed.
- Lab `verify_open_box.py` passed.

## Remaining Boundary

Runtime availability: `not verified`.

Reason: file installation, local checks, and Codex runtime visibility are three
separate states. A reopened or restarted Codex Workspace must still verify that
project agents and skills are visible or callable.

## Non-Actions

- No Template version bump.
- No Template tag or GitHub Release.
- No real Workspace rollout.
- No adapter connection.
- No external task-system write.
- No product-grade or source-equivalent claim.
