# WorkSeed Workspace Template v0.1.2

这是 WorkSeed 的公开 Workspace 模板仓库。

你可以直接用它创建一个新的 WorkSeed Workspace，然后在自己的 Workspace 里开始项目规划、资料沉淀、执行记录和反馈迭代。

基础来源：

- Core 版本：`ws-core-v0.3.0`
- Template 版本：`workspace-template-v0.1.2`
- 当前能力状态：已知道 Core 基线；默认未安装可运行能力文件

WorkSeed Core 是持续迭代的能力核心。这个 Template 只记录当前基线和加载
路径；你的 Workspace 需要用本地记录证明自己实际加载了哪个 Core 版本、哪些
子智能体、技能和运行时文件，以及当前 Codex 运行时是否已经可见。

简单说：Template 知道 Core 0.3，但 Template 本身不等于已经具备 Core 0.3
的具体运行能力。只有安装 Core 运行时文件、通过本地检查，并在当前
Workspace 的 Codex 运行时中验证可见后，才可以说这些能力可以使用。

## 这是什么

- 一个 GitHub 模板仓库，用来创建新的 WorkSeed Workspace。
- 一个干净的 Workspace 起点，包含 `WORKSPACE.md`、`workspace-system-manifest.md`、`workspace-records/**`、本地检查脚本和反馈记录结构。
- 一个不带私有资料的安全基线。
- 一个知道 Core 基线和安装流程、但默认不预装具体 Core 子智能体和技能的入口。

## 这不是什么

- 不是 WorkSeed Core 母系统。
- 不是某个真实客户或真实项目的 Workspace。
- 不是 Template v1.0。
- 不连接真实 adapter。
- 不写入外部任务系统。

## 怎么使用

推荐方式：

1. 在 GitHub 上点击 **Use this template** 按钮创建你的新 Workspace 仓库。
2. 把你的新仓库克隆到本地。
3. 先读 `WORKSPACE.md`。
4. 修改 `workspace-system-manifest.md`，填入你的 Workspace 名称、owner、用途、本地路径和远端仓库。
5. 运行检查：

```powershell
python scripts/utils/check_sync.py
python scripts/utils/verify_open_box.py
python scripts/utils/check_workspace_deployment.py
```

## 第一次打开时怎么初始化

第一次让 Codex 进入这个 Workspace 时，先不要直接开始项目任务。推荐先使用：

```text
帮我初始化这个 Workspace，并一步一步指引我安装和使用 Core 能力。
```

你也可以用更口语的话说：

```text
安装 Core
安装能力
给我指引一下
告诉我下一步怎么做
我不知道怎么开始
```

Codex 应该把这些话都理解成“进入初始化和 Core 能力安装引导”。

注意：这些话只是启动引导，不等于授权立即写入安装。Codex 不要自动扫描，
也不应该自动扫描
你的电脑来找 Core，也不应该直接使用文件里写着的旧路径。它应该先问你：
“Core 压缩包在哪里？你可以贴路径，也可以把 zip 文件丢到聊天框。”
等你明确给出位置并回复 `确认安装` 后，才正式安装。

完整提示词在：

```text
templates/first-workspace-initialization-prompt.md
```

## 如何加载 Core 能力文件

Template 已经带有 Core 0.3 的接收结构，但不会默认安装所有可运行子智能体和技能文件。

请不要把 `Core 版本：ws-core-v0.3.0` 理解成“这个 Template 已经能直接使用
Prism、Mark、mira 等具体能力”。它表示 Template 知道要接收哪个 Core 基线，
并提供安装和验证流程。

推荐方式：使用你已经拿到的 Core 压缩包。你可以把 zip 文件路径发给 Codex，
也可以直接把 zip 文件拖进聊天框。

```powershell
python scripts/utils/install_core_capabilities.py --zip-path "D:\Downloads\workseed-core-runtime-ws-core-v0.3.0-standard-20260704.zip" --core-version ws-core-v0.3.0
```

如果你还没有 Core 压缩包，可以通过下面方式获取：

- 联系 Raymond 微信：`18002997691`
- 关注抖音 `@有光蔓延【1688运营】`，抖音号：`289566513`
- 扫码或保存下图，在抖音搜索页扫一扫加入粉丝群获取：

![抖音 @有光蔓延【1688运营】](docs/assets/douyin-youguangmanyan-1688.jpg)

这套 Workspace 未来会在私域范围内免费分享。我们希望需要的人能先成为
微信好友或群友，方便后续获得更新、互相支持，也为未来可能的商业合作留下
联系入口。

安装后如果 `@prism`、`@mark`、`@mira` 这类项目子智能体没有立刻出现，重开 Codex 项目或新开线程刷新。
文件安装、本地检查通过、Codex 运行时可见是三个不同状态，不能互相替代。

如果 Codex 从 `workspace-system-manifest.md` 或示例命令里读到了默认 Core
路径，不能自动把它当成安装来源。它应该忽略自动扫描结果，先问你 Core
压缩包在哪里。

重开或新开线程后，用下面的提示词做运行时可见性确认：

```text
templates/core-runtime-availability-verification-prompt.md
```

如果当前线程验证不到项目子智能体，可以新开一个很窄的测试线程，只验证
运行时可见性。测试线程结束后，源线程必须读取测试线程报告，核对当前
Workspace 文件状态，再决定是否把 capability-load record 写成 `verified`。
确认无误后，源线程归档测试线程。

测试线程提示词在：

```text
templates/runtime-visibility-test-thread-prompt.md
```

注意：运行时可见性必须在你自己的 Workspace 作为 Codex active project 时确认。
在 WorkSeed Core、Template 仓库或其他 Workspace 里运行检查，不能证明你的
Workspace 已经看见这些项目子智能体和技能。

详细说明见：

```text
docs/workspaces/initialization-and-core-loading.md
```

## 你需要改哪些地方

创建自己的 Workspace 后，通常先改：

- `WORKSPACE.md`：让入口说明符合你的 Workspace。
- `workspace-system-manifest.md`：记录真实身份、路径、远端和 Core 基线。
- `projects/starter/plan.md`：写下你的第一个项目目标。
- `workspace-records/**`：以后记录升级、实现、决策、检查和反馈。

不要把客户资料、账号状态、原始图片、私有链接、访问令牌或浏览器登录状态放进这个模板结构里。

## 版本说明

`v0.1.2` 表示这是 Core 能力加载和运行时验证流程候选版本。

它已经可以作为新 Workspace 的起点，并提供初始化、确认安装、Core 运行时
安装记录、运行时可见性验证路径，以及“测试线程验证、源线程核验、归档测试
线程”的标准流程；但还不是稳定承诺版。Template 是否能到 `v1.0.0`，需要
经过更多真实 Workspace 使用、反馈和修正。

## 与 WorkSeed Core 的关系

WorkSeed Core 负责沉淀通用能力。  
Workspace Template 负责把这些能力整理成别人可以直接创建的新 Workspace 起点。  
你的 Workspace 负责保存自己的真实项目事实、材料、决策和执行记录。
