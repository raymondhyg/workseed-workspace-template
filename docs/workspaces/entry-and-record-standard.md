# Workspace Entry And Record Standard

This standard defines how a WorkSeed Workspace gives its AI one clear entry file
while keeping detailed technical landing records in a structured folder.

The entry file should guide. The record folders should remember.

## Required Workspace Entry

Every WorkSeed Workspace should have a `WORKSPACE.md` file at the repository
root.

`WORKSPACE.md` is the human and AI starting point for the Workspace. It should
answer:

- What Workspace is this?
- What Core version is it based on?
- What should the AI read first?
- Where should technical implementation records go?
- Which folders are protected local context?
- Which commands prove the Workspace is healthy?
- What is the next expected action?

`WORKSPACE.md` should not become a giant history file. It points to the right
records instead of storing every detail itself.

## Required Workspace Records Folder

Every WorkSeed Workspace should have a `workspace-records/` folder with a
`README.md` file.

Recommended subfolders:

```text
workspace-records/
|-- README.md
|-- upgrades/
|-- implementation/
|-- decisions/
|-- feedback/
`-- checks/
```

Use these folders this way:

| Folder | Use For |
|---|---|
| `upgrades/` | Core release adoption records, range, state, changed files, verification |
| `implementation/` | Technical landing notes: files changed, problem solved, behavior changed |
| `decisions/` | Workspace-local choices and tradeoffs |
| `feedback/` | Sanitized feedback to WorkSeed Core |
| `checks/` | Verification snapshots, command outputs, audit notes |

## Entry To Record Routing

The receiving AI should route information like this:

| Information | Durable Surface |
|---|---|
| Workspace identity and current Core base | `workspace-system-manifest.md` |
| Where to start and where to write | `WORKSPACE.md` |
| Core release adoption truth | `workspace-records/upgrades/` and manifest |
| Technical implementation detail | `workspace-records/implementation/` |
| Local design decision | `workspace-records/decisions/` |
| Reusable gap for Core | `workspace-records/feedback/` plus sanitized GitHub Issue or PR when needed |
| Verification evidence | `workspace-records/checks/` |

## Technical Landing Record

When the Workspace makes a concrete technical change, the record should include:

- date
- owner or AI thread
- related Core release or local version
- problem being solved
- files changed
- behavior before
- behavior after
- verification commands and result
- protected files intentionally untouched
- follow-up work

This record is required when a change affects system behavior, upgrade
receiving, reusable workflow, checker behavior, or technical implementation. It
is optional for small one-off project notes that are already captured in a plan.

## Version And Scope Rule

The entry file and records must use explicit versions:

- Core base version
- target Core release
- Workspace local version or commit
- adoption state: `Not evaluated`, `Eligible`, `Planned`, `Applied`, `Partial`,
  `Skipped`, or `Blocked`

Avoid saying "latest", "new version", or "already upgraded" unless the exact
version and evidence are linked.

## Receiver Internalization Rule

A Workspace may adapt Core behavior locally, but it must record the difference.

Use:

- manifest for current truth
- `WORKSPACE.md` for start guidance
- `workspace-records/implementation/` for technical changes
- `workspace-records/decisions/` for local choices
- `workspace-records/feedback/` for reusable gaps that should return to Core

Do not hide local adaptations inside chat. If they change how the Workspace AI
will behave next time, write them to one of the Workspace record surfaces.

## Minimum Starter Templates

WorkSeed Core provides templates for:

- `templates/workspace-entry-template.md`
- `templates/workspace-records-readme-template.md`
- `templates/workspace-implementation-record-template.md`

A Workspace may rename the files, but it should keep the same responsibilities.
