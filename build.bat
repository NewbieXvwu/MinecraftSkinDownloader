@echo off
Title MinecraftSkinDownloader构建辅助程序
echo 您想构建哪个程序？
echo 1 MinecraftSkinDownloader_SunValley.py
echo 2 MinecraftSkinDownloader_ttkbootstrap.py
echo 3 MinecraftSkinDownloader_ttkthemes.py
set/p a=请选择:
if "%a%"=="1" goto :SunValley
if "%a%"=="2" goto :ttkbootstrap
if "%a%"=="3" goto :ttkthemes
exit
:SunValley
echo 目前由于依赖问题，无法构建，请等待更新……
pause
:ttkbootstrap
echo 正在构建程序，请稍候……
pyinstaller -F -w -i logo.ico MinecraftSkinDownloader_ttkbootstrap.py
echo 构建完毕，正在清理文件……
del /F /S /Q __pycache__
del /F /S /Q build
del /F /S MinecraftSkinDownloader_ttkbootstrap.spec
rd __pycache__
rd build\MinecraftSkinDownloader_ttkbootstrap
rd build
move /Y dist\MinecraftSkinDownloader_ttkbootstrap.exe .\MinecraftSkinDownloader_ttkbootstrap.exe
rd dist
pause
:ttkthemes
echo 正在构建程序，请稍候……
pyinstaller -F -w -i logo.ico MinecraftSkinDownloader_ttkthemes.py
echo 构建完毕，正在清理文件……
del /F /S /Q __pycache__
del /F /S /Q build
del /F /S MinecraftSkinDownloader_ttkthemes.spec
rd __pycache__
rd build\MinecraftSkinDownloader_ttkthemes
rd build
move /Y dist\MinecraftSkinDownloader_ttkthemes.exe .\MinecraftSkinDownloader_ttkthemes.exe
rd dist
pause