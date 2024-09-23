<div align="center">
  <img src="https://cdn.liteyuki.icu/static/img/liteyuki_icon_640.png" width="180" height="180" alt="NoneBotPluginLogo">

</div>

<div align="center">

# nonebot-plugin-nps

_✨ NoneBot2的插件商店插件 开发中 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/LiteyukiStudio/nonebot-plugin-nps.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-nps">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-nps.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">

</div>

## 📖 介绍

一个可以查询，安装及卸载插件的包管理器插件，支持多源安装

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 NoneBot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-nps

</details>

<details>
<summary>使用包管理器安装后手动添加到插件列表进行加载</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-nps

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-nps

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-nps

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-nps

</details>
</details>

<details open>
<summary>使用 nps 安装</summary>
对Bot发送 `nps install nonebot-plugin-nps` 即可安装
</details>

## 🎉 使用

### 命令

#### 插件管理
- `nps search <[关键词, ...]>` 通过关键词搜索插件返回列表插件详情
- `nps install [<插件名>, ...] [-i|--index <源>]` 安装插件，支持指定PyPi源
- `nps uninstall <插件名>` 卸载插件

#### 基础命令
- `nps help` 查看帮助
- `nps update` 更新本地商店索引
- `nps upgrade [<插件名>, ...]/all` 更新指定/所有插件
- `nps list` 列出所有已安装的插件