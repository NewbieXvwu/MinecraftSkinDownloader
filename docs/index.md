<img width="192" height="192" align="left" style="float: left; margin: 0 10px 0 0;" src="logo.png" alt="Logo"/><br />
# MinecraftSkinDownloader 
这是一个可以简单地下载任何Minecraft正版玩家的皮肤的软件，使用Python编写，由NewbieXvwu维护。

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
- ttkbootstrap
- requests

# 下载
你可以在[Release](https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases/latest)下载稳定版。

有时，会有[测试版](https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases)在Release发布。

本仓库配置了Github Action，你可以在[Action](https://github.com/NewbieXvwu/MinecraftSkinDownloader/actions)下载测试版。

<div align=center><img src="https://user-images.githubusercontent.com/87637612/147869113-c9567028-17d5-4d63-8e03-a02ad5bbf3a6.png"/></div>

<div align=center><img src="https://user-images.githubusercontent.com/87637612/147869119-6cd07534-0279-44f8-a945-1be505799da4.png"/></div>

# 操作系统支持

目前本程序支持以下操作系统：

#### Windows 11

#### Windows 10

#### Windows 8.1 **（未经测试）**

#### Windows 7 **（需要特别兼容版本）**

#### Windows Vista **（需要特别兼容版本）**

目前本程序仍不支持但以后可能支持以下操作系统：

#### Linux（目前可能可以启动程序，但几乎不能正常使用，**未经测试**）

#### MacOS（构建失败，我没有这方面的经验）

本程序永远不可能支持以下系统：

#### Windows 8 **（未经测试）**

#### Windows XP 或更早版本

# 常见问题
### 我应该选择哪个版本？

您应该选择[最新的版本](https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases/latest)。如果您想尝试最新的<s>BUG</s>，您可以下载[Preview](https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases)版本或[Action](https://github.com/NewbieXvwu/MinecraftSkinDownloader/actions)版本。

### 为什么发布版里有八个文件？我要选哪个？

这取决于您的操作系统版本和架构。

如果您的操作系统版本是Windows 8.1或更新版本，您应该选择无"Windows7"后缀的版本。

如果您的操作系统是Windows 7或Windows Vista，您应该选择带"Windows7"后缀的版本。

如果您的操作系统是64位架构的（较普遍），请最好选择带"x64"后缀的版本，但是选择带"x86"后缀的也可以正常运行。可能会有一些性能损耗。

如果您的操作系统是32位架构的（较稀有，可能是十年前生产的老电脑，可以通过[搜索](https://www.baidu.com/s?ie=UTF-8&wd=%E6%9F%A5%E7%9C%8B%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E4%BD%8D%E6%95%B0)来确定版本），您应该选择带"x86"后缀的版本。

后缀带有"ttkbootstrap"的采用了ttkbootstrap这个ttk增强库，后缀带有“ttkthemes”的使用了ttkthemes这个ttk增强库。两个版本的GUI略有差距，但核心功能无差别。

### 我的操作系统是XXX，可以使用本程序吗？

请参阅[操作系统支持](https://github.com/NewbieXvwu/MinecraftSkinDownloader#%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E6%94%AF%E6%8C%81)。

### tnnd，为什么不兼容！！（划掉）

这位<s>双料高级特工（雾）</s>，本程序使用Python编写，而部分操作系统要么是我不熟悉，要么是Python不兼容，我也很无奈啊……

### 我发现了一个问题……

正常，飞个[Issue](https://github.com/NewbieXvwu/MinecraftSkinDownloader/issues/new/choose)过来。

### 作者是何方神圣？代码写得像屎山……

请看我的[个人介绍](https://github.com/NewbieXvwu/NewbieXvwu/blob/main/README.md)。

### 考虑重构吗？

或许以后会重构，但是不是现在。你可以来[帮个忙](https://github.com/NewbieXvwu/MinecraftSkinDownloader/pulls)。

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
