@echo off
pyinstaller -F -w -i logo.ico MinecraftSkinDownloader.pyw
del /F /S /Q __pycache__
del /F /S /Q build
del /F /S MinecraftSkinDownloader.spec
rd __pycache__
rd build\MinecraftSkinDownloader
rd build
move /Y dist\MinecraftSkinDownloader.exe .\MinecraftSkinDownloader.exe
rd dist
pause