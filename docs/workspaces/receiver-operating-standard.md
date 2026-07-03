# Workspace Receiver Operating Standard

This is the bottom-layer usage standard for any WorkSeed Workspace that receives
capabilities from WorkSeed Core.

The Workspace is not a passive copy of Core. It is an operating system with its
own owner, mission, local evidence, project context, and privacy boundary. Core
provides reusable capability. The Workspace decides adoption truth and records
local use.

## Receiver Identity Rule

A WorkSeed Workspace must know its identity before doing meaningful work:

- Workspace name
- Workspace owner
- Workspace purpose
- local path
- remote repository
- current Core base version
- current Workspace commit or working state

The default durable place is `workspace-system-manifest.md`.

The default entry point is `WORKSPACE.md`. It should point to the manifest,
receiver standard, and `workspace-records/` folder instead of trying to hold all
details itself.

If identity or base version is unknown, the Workspace should classify itself as
`Unknown` or `Legacy compatible`, then audit before claiming an upgrade is
applied.

## Session Start Rule

At the start of a meaningful Workspace session, the receiving AI should check:

1. What is the session type: task, research, decision, Inbox, retrospective, or
   system-capability?
2. Is this work about local Workspace use, Core release adoption, local project
   execution, feedback to Core, or an external adapter?
3. Which durable surface owns the result: chat, plan, docs/SOP, changelog,
   manifest, skill, checker, config, automation, or adapter?
4. Is the Workspace trying to use an installed capability, adopt a Core release,
   or request a Core improvement?
5. What must not be overwritten or leaked?

If the answer changes during the session, pause and reroute instead of mixing
local work, Core adoption, and feedback into one unclear thread.

## Receiver Usage Modes

| Mode | Meaning | Required record |
|---|---|---|
| Local use | Use existing Workspace capability for normal project work | project plan, docs, or chat closeout |
| Core adoption | Apply a named Core release | manifest upgrade row and verification |
| Local adaptation | Change behavior for this Workspace only | manifest local decision or Workspace docs |
| Feedback to Core | Report a reusable gap upstream | sanitized Issue, PR, or feedback row |
| External adapter | Connect to a non-Core system | explicit adapter record based on `docs/operations/external-adapter-contract.md` and verification |

Do not treat local adaptation as Core adoption. Do not treat feedback to Core as
Workspace adoption. Do not treat external system messages as durable Workspace
truth unless a local record or read-back exists.

## Entry And Record Rule

The Workspace should use:

- `WORKSPACE.md` as the start-here file
- `workspace-system-manifest.md` as the version and adoption truth
- `workspace-records/upgrades/` for release adoption records
- `workspace-records/implementation/` for technical landing notes
- `workspace-records/decisions/` for local choices
- `workspace-records/feedback/` for sanitized Core feedback
- `workspace-records/checks/` for verification snapshots

Use `docs/workspaces/entry-and-record-standard.md` for the detailed entry and
record rules.

## Protected Surface Rule

The receiving AI must classify files before editing:

- Core-following: can be copied or merged from Core after review.
- Workspace-owned: can be edited locally, but must not be overwritten by Core.
- Local-only: should stay out of Core and often out of Git.
- Blocked: cannot be safely changed until ownership, privacy, or verification is
  clear.

Default Workspace-owned surfaces:

- `projects/**`
- `workspace-system-manifest.md`
- Workspace adoption records
- local project docs and plans
- private materials, credentials, raw assets, browser state, and local evidence

## Adoption Truth Rule

Workspace adoption state must use one of these values:

- `Not evaluated`
- `Eligible`
- `Planned`
- `Applied`
- `Partial`
- `Skipped`
- `Blocked`

`Applied` is allowed only when files or migration steps were actually applied,
verification passed, and the manifest or adoption record was updated.

If a Core release was announced but not installed, the state is `Planned` or
`Not evaluated`, not `Applied`.

## Upgrade Range Rule

Every upgrade must name:

- from version
- to version
- Core commit or tag
- Workspace commit before upgrade
- Workspace commit after upgrade, if committed
- changed file classes
- protected surfaces
- verification commands
- adoption state

Avoid vague labels such as "latest", "new version", or "already upgraded" unless
the manifest maps them to exact versions and evidence.

## Workspace AI Behavior Rule

The receiving AI should:

- read `AGENTS.md`, `workspace-system-manifest.md`, and this standard before
  Core adoption work
- use `WORKSPACE.md` and `workspace-records/**` to keep local guidance and
  technical landing records recoverable
- prefer the smallest durable local surface
- keep project facts in the Workspace, not in Core
- keep reusable generalized gaps as sanitized feedback to Core
- report true external action status: created, updated, not created, blocked,
  or not required
- close important sessions with changed files, verification, adoption state,
  open loops, and next action

The receiving AI should not:

- blindly mirror Core
- overwrite Workspace project context
- copy private Workspace material into Core
- claim adoption from a chat message, Issue, PR, or release announcement alone
- use external task systems by default unless an adapter is installed and
  verified

## Feedback Rule

Feedback to WorkSeed Core must be sanitized. It may include:

- unclear Core release instructions
- missing checker or template
- reusable workflow gap
- generic error pattern
- suggested improvement to Core docs, skills, or scripts

Feedback must not include:

- private customer or project facts
- credentials, tokens, browser state, private links, raw files, or screenshots
- local-only business decisions that should remain in the Workspace

## Receiver Closeout Rule

Every meaningful receiver-side system session should report:

- session type and mode
- version or adoption state
- changed files
- protected files intentionally untouched
- verification commands and result
- manifest or adoption record update
- feedback to Core, if any
- open questions
- next action

This closeout is the receiver's truth layer. It should be short enough to read
and specific enough to recover.
