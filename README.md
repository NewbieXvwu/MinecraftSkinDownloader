<img width="192" height="192" align="left" style="float: left; margin: 0 10px 0 0;" src="logo.png" alt="logo.png"/><br />
# MinecraftSkinDownloader 
![GitHub all releases](https://img.shields.io/github/downloads/NewbieXvwu/MinecraftSkinDownloader/total?style=for-the-badge&logo=appveyor&label=总下载量&link=https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases)  ![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/NewbieXvwu/MinecraftSkinDownloader?style=for-the-badge&logo=appveyor&label=最新版本&link=https://github.com/NewbieXvwu/MinecraftSkinDownloader/releases)  ![GitHub stars](https://img.shields.io/github/stars/NewbieXvwu/MinecraftSkinDownloader?style=for-the-badge&logo=appveyor&label=Stars)

这是一个可以简单地下载任何Minecraft正版玩家的皮肤的软件，使用Python编写，由NewbieXvwu维护。
# 程序截图
![image](https://user-images.githubusercontent.com/87637612/147638300-bc349c33-950e-4caa-b4f0-eef3617861d6.png)
![image](https://user-images.githubusercontent.com/87637612/147638325-210b7b9f-c2b9-4675-bcfc-168ce6f14159.png)

操作系统：<img src="https://badgen.net/badge/icon/Windows%2011?icon=windows&label"> Build 22000.376

使用软件：
- 
- <img src="https://img.shields.io/badge/-Python-black?style=flat&logo=python&logoColor=white">  3.10.1

- <img src="http://img.shields.io/badge/-VS%20Code-007ACC?style=flat&logo=visual%20studio%20code&logoColor=white"> 1.63.2

使用的第三方库：
- 
- ttkthemes
- requests

# 构建

如果您想要在Windows 7上运行本程序，目前的解决方案是安装[Python 3.8.10](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)并进行构建。

在构建之前，确保你已经安装了Python 3.x。

经过测试的版本是Python 3.10.1。

    pip install pyinstaller
	pip install requests
	pip install ttkthemes
	build.bat

注意：目前由于我没有测试环境和经验，Linux不受支持，基本上能跑不能用……
