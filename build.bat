@echo off
echo 正在构建程序，请稍候……
pyinstaller -F -w -i logo.ico MinecraftSkinDownloader.py
echo 构建完毕，正在清理文件……
del /F /S /Q __pycache__
del /F /S /Q build
del /F /S MinecraftSkinDownloader.spec
rd __pycache__
rd build\MinecraftSkinDownloader
rd build
move /Y dist\MinecraftSkinDownloader.exe .\MinecraftSkinDownloader.exe
rd dist
pause
