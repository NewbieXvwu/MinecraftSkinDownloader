@echo off
Title MinecraftSkinDownloader������������
echo ���빹���ĸ�����
echo 1 MinecraftSkinDownloader_SunValley.py
echo 2 MinecraftSkinDownloader_ttkbootstrap.py
echo 3 MinecraftSkinDownloader_ttkthemes.py
set/p a=��ѡ��:
if "%a%"=="1" goto :SunValley
if "%a%"=="2" goto :ttkbootstrap
if "%a%"=="3" goto :ttkthemes
exit
:SunValley
echo Ŀǰ�����������⣬�޷���������ȴ����¡���
pause
:ttkbootstrap
echo ���ڹ����������Ժ򡭡�
pyinstaller -F -w -i logo.ico MinecraftSkinDownloader_ttkbootstrap.py
echo ������ϣ����������ļ�����
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
echo ���ڹ����������Ժ򡭡�
pyinstaller -F -w -i logo.ico MinecraftSkinDownloader_ttkthemes.py
echo ������ϣ����������ļ�����
del /F /S /Q __pycache__
del /F /S /Q build
del /F /S MinecraftSkinDownloader_ttkthemes.spec
rd __pycache__
rd build\MinecraftSkinDownloader_ttkthemes
rd build
move /Y dist\MinecraftSkinDownloader_ttkthemes.exe .\MinecraftSkinDownloader_ttkthemes.exe
rd dist
pause