<img width="192" height="192" align="left" style="float: left; margin: 0 10px 0 0;" src="logo.png" alt="logo.png"/><br />
# MinecraftSkinDownloader 

<div align=center>这是一个可以简单地下载任何Minecraft正版玩家的皮肤的软件，使用Python编写，由NewbieXvwu维护。</div>

# 仓库地址：[Github](https://github.com/NewbieXvwu/MinecraftSkinDownloader)  [Gitee](https://gitee.com/NewbieXvwu/MinecraftSkinDownloader)

注：Gitee有1~2分钟的同步延迟

# 程序截图
<div align=center><img src="https://user-images.githubusercontent.com/87637612/147638300-bc349c33-950e-4caa-b4f0-eef3617861d6.png"/></div>
<div align=center><img src="https://user-images.githubusercontent.com/87637612/147638325-210b7b9f-c2b9-4675-bcfc-168ce6f14159.png"/></div>

注：操作系统<img src="https://badgen.net/badge/icon/Windows%2011 Build 22000.376?icon=windows&label">

使用软件：
- 
- <a href="https://www.python.org/downloads/release/python-3101"><img src="https://img.shields.io/badge/-Python 3.10.1-black?style=flat&logo=python&logoColor=white&link=https://www.python.org/downloads/release/python-3101"></a>

- <a href="https://code.visualstudio.com"><img src="http://img.shields.io/badge/-VS%20Code 1.63.2-007ACC?style=flat&logo=visual%20studio%20code&logoColor=white&link=https://code.visualstudio.com"></a>

使用的第三方库：
- 
- ttkthemes
- requests

# 下载

你可以在[Release](https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases/latest)下载稳定版。

有时，会有[测试版](https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases)在Release发布。

本仓库配置了Github Action，你可以在[Action](https://github.com/NewbieXvwu/MinecraftSkinDownloader/actions)下载测试版。

<div align=center><img src="https://user-images.githubusercontent.com/87637612/147869113-c9567028-17d5-4d63-8e03-a02ad5bbf3a6.png"/></div>

<div align=center><img src="https://user-images.githubusercontent.com/87637612/147869119-6cd07534-0279-44f8-a945-1be505799da4.png"/></div>

# 构建

<s>如果您想要在Windows 7上运行本程序，目前的解决方案是安装<a href="https://www.python.org/downloads/release/python-3810"><img src="https://img.shields.io/badge/-Python 3.8.10-black?style=flat&logo=python&logoColor=white&link=https://www.python.org/downloads/release/python-3810"></a>并进行构建。</s>
	
**注意：从[V2.2 Preview 3](https://github.com/NewbieXvwu/MinecraftSkinDownloader/commit/b94fbe8be1cc1efc265218391f0b970f320309a6)开始，您可以在[Github Action](https://github.com/NewbieXvwu/MinecraftSkinDownloader/actions)下载适用于Windows 7的版本**（基于<a href="https://www.python.org/downloads/release/python-3810"><img src="https://img.shields.io/badge/-Python 3.8.10-black?style=flat&logo=python&logoColor=white&link=https://www.python.org/downloads/release/python-3810"></a>）**，但是这仅是为了试用，可能会产生一些问题。**
	
**我们建议您在[新版本的Windows](https://www.microsoft.com/zh-cn/software-download/windows10)中使用本程序！**

在构建之前，确保您已经安装了<a href="https://www.python.org"><img src="https://img.shields.io/badge/-Python 3.x-blue?style=flat&logo=python&logoColor=white&link=https://www.python.org"></a>。

经过测试的版本是<a href="https://www.python.org/downloads/release/python-3101"><img src="https://img.shields.io/badge/-Python 3.10.1-green?style=flat&logo=python&logoColor=white&link=https://www.python.org/downloads/release/python-3101"></a>。

    pip install pyinstaller
	pip install requests
	pip install ttkthemes
	build.bat

如果您连接到Pypi官方源的网络较差，您也可以使用清华大学的镜像源。

    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests
	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ttkthemes
	build.bat

**注意：目前由于我没有测试环境和经验，Linux不受支持，基本上能跑不能用……**

# 从源码运行

如果您有特殊需求（例如本程序的Windows 7兼容版本不起作用），您可以从源码运行本程序。

在运行之前，确保您已经安装了<a href="https://www.python.org"><img src="https://img.shields.io/badge/-Python 3.x-blue?style=flat&logo=python&logoColor=white&link=https://www.python.org"></a>。

程序将会自动下载并安装第三方库。

从[V2.2 Preview 5](https://github.com/NewbieXvwu/MinecraftSkinDownloader/commit/2d2c9a8d7ba3ec4b5c7dac66edb97f7a0605c456)开始，下载第三方库的界面升级到了图形化版本。但是，这会导致您在安装完成每一个第三方库后必须手动重启本程序。

如果你有好的解决该问题的方案，欢迎给我提交[Pull requests](https://github.com/NewbieXvwu/MinecraftSkinDownloader/pulls)。
