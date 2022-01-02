<img width="192" height="192" align="left" style="float: left; margin: 0 10px 0 0;" src="logo.png" alt="logo.png"/><br />
# MinecraftSkinDownloader 
![GitHub all releases](https://img.shields.io/github/downloads/NewbieXvwu/MinecraftSkinDownloader/total?style=for-the-badge&logo=github&label=总下载量&link=https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases)  ![GitHub release (latest by date)](https://img.shields.io/github/v/release/NewbieXvwu/MinecraftSkinDownloader?style=for-the-badge&logo=githubactions&label=最新稳定版本&link=https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases&labelColor=yellowgreen)  ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/NewbieXvwu/MinecraftSkinDownloader?style=for-the-badge&logo=githubactions&label=最新版本&link=https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases&labelColor=yellowgreen&include_prereleases)  ![GitHub stars](https://img.shields.io/github/stars/NewbieXvwu/MinecraftSkinDownloader?style=for-the-badge&logo=githubsponsors&label=Stars)  ![Action](https://img.shields.io/badge/dynamic/json?color=success&label=%E8%87%AA%E5%8A%A8%E6%9E%84%E5%BB%BA%E7%8A%B6%E6%80%81&query=%24.workflows..state&url=https%3A%2F%2Fapi.github.com%2Frepos%2FNewbieXvwu%2FMinecraftSkinDownloader%2Factions%2Fworkflows&style=for-the-badge&logo=github)

这是一个可以简单地下载任何Minecraft正版玩家的皮肤的软件，使用Python编写，由NewbieXvwu维护。

# 仓库地址：[Github](https://github.com/NewbieXvwu/MinecraftSkinDownloader)  [Gitee](https://gitee.com/NewbieXvwu/MinecraftSkinDownloader)

注：Gitee有1~2分钟的同步延迟

# 程序截图
<div align=center><img src="https://user-images.githubusercontent.com/87637612/147638300-bc349c33-950e-4caa-b4f0-eef3617861d6.png"/></div>
<div align=center><img src="https://user-images.githubusercontent.com/87637612/147638325-210b7b9f-c2b9-4675-bcfc-168ce6f14159.png"/></div>

注：操作系统<img src="https://badgen.net/badge/icon/Windows%2011 Build 22000.376?icon=windows&label">

使用软件：
- 
- <img src="https://img.shields.io/badge/-Python 3.10.1-black?style=flat&logo=python&logoColor=white&link=https://www.python.org/downloads/release/python-3101">

- <img src="http://img.shields.io/badge/-VS%20Code 1.63.2-007ACC?style=flat&logo=visual%20studio%20code&logoColor=white&link=https://code.visualstudio.com">

使用的第三方库：
- 
- ttkthemes
- requests

# 下载

你可以在[Release](https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases)下载稳定版。

本仓库配置了Github Action，你可以在[Action](https://github.com/NewbieXvwu/MinecraftSkinDownloader/actions)下载测试版。

<div align=center><img src="https://user-images.githubusercontent.com/87637612/147869113-c9567028-17d5-4d63-8e03-a02ad5bbf3a6.png"/></div>

<div align=center><img src="https://user-images.githubusercontent.com/87637612/147869119-6cd07534-0279-44f8-a945-1be505799da4.png"/></div>

# 构建

如果您想要在Windows 7上运行本程序，目前的解决方案是安装[Python 3.8.10](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)并进行构建。

在构建之前，确保您已经安装了Python 3.x。

经过测试的版本是Python 3.10.1。

    pip install pyinstaller
	pip install requests
	pip install ttkthemes
	build.bat

注意：目前由于我没有测试环境和经验，Linux不受支持，基本上能跑不能用……
