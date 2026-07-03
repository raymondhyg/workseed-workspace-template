# First Workspace Initialization Prompt

Use this prompt when opening a new WorkSeed Workspace created from the Template.

```text
你好，请先按 WorkSeed Workspace 初始化流程开始，不要直接执行项目任务。

请先读取：
1. WORKSPACE.md
2. workspace-system-manifest.md
3. AGENTS.md
4. docs/workspaces/receiver-operating-standard.md
5. docs/workspaces/entry-and-record-standard.md
6. docs/workspaces/upgrade-playbook.md
7. workspace-records/README.md
8. docs/workspaces/initialization-and-core-loading.md

然后只回声确认：
- 当前 Workspace 名称、owner、用途是否仍是模板默认值
- 当前 Core base version
- 当前 Template version
- 当前身份是 Workspace，不是 Core
- 哪些内容属于本地 Workspace 私有事实
- 是否已经安装可运行 Core capability files，例如 .codex/agents 和 .agents/skills
- 如果尚未安装，下一步应该从 Core repo、Core package folder，还是 zip 包加载
- 初始化前不修改真实项目事实、不连接 adapter、不写外部任务系统
```
