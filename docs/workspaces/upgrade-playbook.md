# Workspace Upgrade Playbook

Use this when a WorkSeed Workspace needs to learn about and adopt a WorkSeed Core release.

The goal is not to make the Workspace a mirror of the Core. The goal is to let
the Workspace receive reusable Core capabilities while preserving Workspace-owned
mission, project context, private materials, and local decisions.

Before applying this playbook, read
`docs/workspaces/receiver-operating-standard.md`. The receiver standard defines
the lower-level usage rules for identity, protected surfaces, adoption truth,
feedback, and closeout.

## Quick Answer

How does a Workspace know about an upgrade?

1. WorkSeed Core publishes a tag and GitHub Release.
2. WorkSeed Core sends the release to Workspace Lab first when Workspace behavior
   can change.
3. Workspace Lab studies, assesses, and reports back.
4. WorkSeed Core reviews the Lab result.
5. Only approved releases are offered to real Workspace systems.
6. The release points to a Core release note under `docs/releases/`.
7. The Workspace reads the release note and its own manifest.
8. The Workspace applies only eligible files or migration steps.
9. The Workspace runs verification commands.
10. The Workspace records the adoption result in its manifest.
11. Any reusable gap goes back to WorkSeed Core as a sanitized Issue or PR.

## Core To Workspace Package

Every Core release should give the Workspace these items:

| Item | Purpose |
|---|---|
| Core release version | The version the Workspace may adopt |
| Core commit and tag | Git evidence for the Core release |
| GitHub Release or release note | Human-readable change and migration guide |
| Changed file classes | What can be copied, merged, reviewed, or skipped |
| Upgrade impact | Safe copy, review required, Workspace-local only, or blocked |
| Verification commands | How the Workspace proves the upgrade works |
| Manifest update instructions | How the Workspace records adoption |
| Privacy boundary | What must not travel between systems |

If any item is missing, the Workspace should treat the upgrade as `Not evaluated`
or `Blocked`, not as applied.

## Lab Gate Before Real Workspace

For releases that affect Workspace behavior, records, checkers, or technical
landing flow, read `docs/workspaces/lab/release-gate.md`.

Real Workspace rollout is allowed only after:

- Workspace Lab receives the release package
- Workspace Lab receives a learning session
- Workspace Lab records learning notes and assessment
- Workspace Lab returns a result to Core
- Core records a review decision of `Approved` or `Partial`

Without that evidence, a release may exist in Core, but real Workspace rollout
is `Blocked`.

## Multi-Version Upgrade Flow

If a Workspace is behind by more than one Core version:

1. Read the Workspace manifest and current Core base.
2. Choose the target release.
3. List intermediate releases.
4. Classify each as `Required`, `Optional`, `Superseded`, `Metadata only`, or
   `Blocked`.
5. Build the chain in Workspace Lab.
6. Record Lab assessment.
7. Only then offer the chain to the real Workspace.

## Workspace Adoption Flow

1. Open the Workspace manifest.
2. Read `WORKSPACE.md` if present.
3. Read the Workspace receiver operating standard and entry/record standard.
4. Record the current Workspace base version before changing files.
5. Read the Core release note.
6. Classify each changed file as Core-following, Workspace-owned, local-only, or
   blocked.
7. Apply safe-copy files and review-required migrations.
8. Do not overwrite Workspace `projects/**`, `WORKSPACE.md`,
   `workspace-records/**`, private materials, local remotes, or
   Workspace-specific decisions.
9. Run the verification commands listed in the release note.
10. Update the Workspace manifest:
   - current Core base version
   - Core commit
   - inherited core capability rows
   - upgrade history row
   - local override rows
   - feedback to WorkSeed Core
11. Write a technical landing record under `workspace-records/implementation/`
    when files changed to solve a concrete system or technical problem.
12. If the Workspace found a reusable gap, open a sanitized GitHub Issue or PR to the
   Core.

## Adoption States

| State | Use when |
|---|---|
| Not evaluated | The Workspace has seen the release but has not checked impact |
| Eligible | The release appears safe to apply |
| Partial | Some files or steps apply, but others are Workspace-local or blocked |
| Blocked | Ownership, access, conflicts, or checks prevent adoption |
| Applied | Files/steps were applied and manifest/check evidence was updated |
| Skipped | The Workspace intentionally did not adopt the release |

## GitHub Messages

Use `templates/github-core-workspace-communication-template.md` for messages.

Core-to-Workspace messages should include:

- release version
- tag or GitHub Release URL
- migration steps
- verification commands
- manifest update instructions

Workspace-to-Core messages should include:

- sanitized feedback or reusable gap
- Core release version
- Workspace adoption state
- no private project materials

Workspace adoption is not complete because a message was sent. It is complete only
when the Workspace manifest and verification evidence are updated.

## Workspace Manifest Example Rows

Inherited core capability row:

```text
| Workflow coaching and session routing | ws-core-v0.2.0 | Applied | none | check_sync + verify_open_box passed |
```

Upgrade history row:

```text
| 2026-07-01 | ws-core-v0.2.0 | Applied | session routing, workflow coach, release governance | check_sync + verify_open_box passed |
```

Feedback row:

```text
| 2026-07-01 | Workspace needed clearer merge steps for local AGENTS.md overrides | Add merge guidance to Core release notes |
```

## Core Audit Checklist

Before saying the Core did its job, verify:

- The Core release has a version, status, commit/tag status, and release note.
- The release note names changed file classes and upgrade impact.
- The release note names verification commands.
- The release note tells the Workspace what to write in its manifest.
- The GitHub communication path is clear: tag/release for Core-to-Workspace,
  sanitized Issue/PR for Workspace-to-Core, manifest for adoption.
- The Workspace private boundary is explicit.
- The relevant checks pass.

If the Workspace would need to ask "what do I copy, what do I skip, and where do I
record it?", the Core guidance is not ready.
