# 发布验证记录

2026-10-13：Momikk fork 首次发布，版本 `1.0.0.0`，Dalamud API 15。插件名称、介绍与原作者 Critical_Impact 保留原样。

使用 .NET SDK 10.0.203 与本机 XIVLauncherCN 的 API 15 开发程序集构建。原始源码完整构建成功，0 个错误、130 个警告；补充项目链接与图标链接后，重新构建和 SDK 打包成功，0 个错误。后一次恢复依赖的漏洞信息请求出现 NU1900 警告，未能完成该次在线漏洞查询。

安装包为 `dist/AllaganMarket-1.0.0.0.zip`，由 Dalamud SDK 生成，包含 101 个文件。已验证：插件 DLL 的程序集版本与 manifest 同为 `1.0.0.0`，InternalName 为 `AllaganMarket`，DalamudApiLevel 为 15；包含 DalaMock、AllaganLib 依赖、deps.json 和图标资源，未包含 Dalamud.dll 或 FFXIVClientStructs.dll。

`dist/AllaganMarket-1.0.0.0.manifest.json` 从实际安装包 manifest 生成，并补充公开安装与更新地址，供统一库链引用。统一库链为 `https://raw.githubusercontent.com/Momikk/DalamudPlugins/main/pluginmaster.json`。

本记录确认构建和分发产物，不代表游戏内验收通过。启用后仍需验证主窗口、初始雇员扫描、销售记录、市场更新和禁用重载；原生结构与 Hook 的国服运行兼容性以实际游戏日志和行为为准。

## 1.4.0.2 元数据更新

作者显示为 Momikk，名称为亚拉戈市场 AllaganMarket，简短和详细描述改为中文，详细描述保留原版来源。原版 GitHub 标签为 4.0.2，官方 DalamudPluginsD17 清单版本为 1.4.0.2，本版对齐实际安装版本。重新构建成功（0 错误、130 警告），已验证 ZIP 内 manifest 与 DLL 版本一致，API 15 不变。历史 1.0.0.0 安装包保留，新清单改用 1.4.0.2。
