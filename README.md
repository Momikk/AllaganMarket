# 亚拉戈市场 AllaganMarket

![插件标志](AllaganMarket/Images/logo_small.png)

## 简介

**亚拉戈市场 AllaganMarket** 是一款 Dalamud 插件，用于追踪所有角色的雇员销售情况。它提供当前上架物品和历史销售的详细信息，并实时监测是否有其他卖家以更低价格出售同类物品。

## 功能

- **雇员销售追踪**：自动追踪所有角色的雇员上架物品。
- **历史销售记录**：保存过往销售记录，方便查看和分析销售历史。
- **压价检测**：发现其他卖家以更低价格出售同类物品时发出提示，帮助你保持市场竞争力。
- **多角色支持**：汇总所有角色的数据，全面掌握市场交易情况。
- **Universalis 集成**：通过 Universalis 获取实时市场价格更新。
- **自定义筛选**：按物品、日期范围、服务器等条件筛选销售数据。
- **通知提醒**：物品售出或被其他卖家压价时收到通知。
- **CSV 导出**：将销售数据导出为 CSV，方便使用其他工具分析。
- **悬浮窗口**：通过悬浮窗口便捷查看雇员销售和压价情况。

## 开始使用

1. 在 Dalamud 设置的第三方插件仓库中添加下方统一库链，保存后刷新插件列表，搜索 `Allagan Market` 并安装。
2. 首次安装后，插件会显示配置向导。
3. 完成配置后，依次访问每位雇员，进行首次扫描。

```text
https://raw.githubusercontent.com/Momikk/DalamudPlugins/main/pluginmaster.json
```

当前发布版本为 `1.0.0.0`，面向 Dalamud API 15。安装器中的名称和介绍暂时保留英文。此 fork 的安装包与源码由本仓库维护，原作者为 Critical_Impact。

## 构建与发布

安装 .NET 10 SDK，并通过 XIVLauncherCN 或 XIVLauncher 启动过一次带 Dalamud 的游戏，然后在仓库根目录运行：

```powershell
.\build.ps1
```

脚本优先使用国服开发程序集；也可通过 `DALAMUD_HOME` 指定 API 15 程序集目录。输出位于 `AllaganMarket/bin/Release/`，SDK 安装包位于 `AllaganMarket/bin/Release/AllaganMarket/latest.zip`。

已发布安装包位于 `dist/AllaganMarket-1.0.0.0.zip`。发布更新时须同时更新安装包与 `Momikk/DalamudPlugins` 中对应清单的版本和下载地址。完整构建与包内容检查不代表已完成游戏内验收；雇员扫描、市场数据与 Hook 的国服兼容性仍需在游戏中验证。

## 命令

- `/allaganmarket` 或 `/amarket`：打开插件主窗口。

## 依赖

本插件依赖以下核心库和服务：

- **Universalis API**：提供实时市场价格更新。
- **AllaganLib**：辅助功能库。

## 参与贡献

欢迎参与贡献！你可以在本 GitHub 仓库提交问题（Issue）或拉取请求（Pull Request）。

## 我的其他插件

- [幻化之王 GlamourKing](https://github.com/Momikk/GlamourKing)
