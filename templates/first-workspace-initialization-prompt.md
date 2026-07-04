# First Workspace Initialization Prompt

Use this prompt when opening a new WorkSeed Workspace created from the Template.

## Natural Triggers

If the user says any of the following, treat it as the same initialization
request and guide them step by step:

- 帮我初始化这个 Workspace
- 初始化一下
- 帮我安装 Core
- 安装 Core 能力
- 安装能力
- 让我开始使用 WorkSeed Core
- 给我指引一下
- 引导我使用这个 Workspace
- 告诉我下一步怎么做
- 我不知道怎么开始

These triggers start guidance. They are not permission to run a write install.

## Guided Prompt

```text
你好，请帮我初始化这个 WorkSeed Workspace，并一步一步指引我安装和使用 Core 能力。

我可能不熟悉 AI 和 WorkSeed，请用通俗的话告诉我：
1. 你是谁；
2. 这个 Workspace 是做什么的；
3. Core 是什么；
4. 我下一步应该做什么。

先不要直接执行项目任务。

请先读取：
1. WORKSPACE.md
2. workspace-system-manifest.md
3. AGENTS.md
4. docs/workspaces/receiver-operating-standard.md
5. docs/workspaces/entry-and-record-standard.md
6. docs/workspaces/upgrade-playbook.md
7. workspace-records/README.md
8. docs/workspaces/initialization-and-core-loading.md

然后先用 2-3 句话介绍自己：你是这个 Workspace 的 Codex 协作者，不是
WorkSeed Core 本体；你会先保护本地事实，再按版本加载 Core 能力。

再用清单方式确认：
- 当前 Workspace 名称、owner、用途是否仍是模板默认值
- 当前 Core base version
- 当前 Template version
- 当前身份是 Workspace，不是 Core
- 哪些内容属于本地 Workspace 私有事实
- 是否已经安装可运行 Core capability files，例如 .codex/agents 和 .agents/skills
- 如果尚未安装，请不要自动扫描我的电脑，也不要直接使用文件里写着的默认 Core 路径
- 请先问我 Core 压缩包在哪里；我可以贴 zip 路径，也可以把 zip 文件丢进聊天框
- 如果我还没有 Core 压缩包，请用最简单的话告诉我获取方式：
  1. 联系 Raymond 微信：18002997691
  2. 关注抖音 @有光蔓延【1688运营】，抖音号：289566513，并加入粉丝群获取
- 在正式运行不带 `--dry-run` 的安装命令、写 capability-load record、或改 manifest 前，必须先停下来确认
- 确认时请用通俗话列出：将使用的 Core zip、将安装哪些类型的文件、会写入哪些本地记录、不会做哪些事
- 只有我明确回复类似“确认安装”“用这个来源安装”“继续正式安装”后，才可以执行真实安装
- 如果我只说“安装 Core”或“安装能力”，这只是进入安装引导，不等于授权立即写入文件
- 如果已经安装但运行时未验证，请引导我使用 templates/core-runtime-availability-verification-prompt.md
- 运行时可见性只能在当前 Workspace 作为 Codex active project 时验证，不能在 Core 或 Template 线程里代替验证
- 如果需要新开测试线程验证运行时可见性，请使用 templates/runtime-visibility-test-thread-prompt.md；测试线程只验证，源线程读回、核验、回写记录并归档测试线程
- 初始化前不修改真实项目事实、不连接 adapter、不写外部任务系统

请最后给我一个“下一步我只需要回复什么”的简单提示。
```
