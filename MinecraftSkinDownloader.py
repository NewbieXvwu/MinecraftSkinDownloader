version_int=2.0
version="v"+str(version_int)
from copyreg import clear_extension_cache
import ctypes, sys
import os
import json
import base64
import tkinter
from urllib.request import urlretrieve
import zipfile
import shutil
from tkinter import messagebox
import threading
import platform
import ctypes
import time
import winreg
try:
    import requests
except:
    print("没有程序必要的库，正在安装……")
    os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests")
    import requests
    from requests import delete
    try:
        import ttkthemes
    except:
        os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ttkthemes")
        print("安装成功！")
        import ttkthemes
else:
    try:
        import ttkthemes
    except:
        print("没有程序必要的库，正在安装……")
        os.system("pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ttkthemes")
        print("安装成功！")
        import ttkthemes
def getzbmain():
    id_=e.get()
    if id_=="":
        tkinter.messagebox.showerror(title='错误', message='请填写内容！') 
    else:
        zt.set("状态：正在向Mojang请求玩家的UUID……")
        url1="https://api.mojang.com/users/profiles/minecraft/"+id_
        r = requests.get(url1)
        del url1
        status_code=r.status_code
        if not status_code==200:
            zt.set("状态：Bugjump出现错误，请检查你的输入！")
        del status_code
        zt.set("状态：读取UUID中……")
        r=r.text
        r=json.loads(r)
        uuid=r['id']
        del r
        zt.set("状态：向Mojang请求下载皮肤的地址中……")
        url2="https://sessionserver.mojang.com/session/minecraft/profile/"+uuid
        r = requests.get(url2)
        del url2
        status_code=r.status_code
        if not status_code==200:
            zt.set("状态：Bugjump出现错误，请检查你的输入！")
        del status_code
        zt.set("状态：读取皮肤下载地址中……")
        r=r.text
        r=json.loads(r)
        properties=r["properties"]
        del r
        properties=properties[0]
        properties=properties["value"]
        zt.set("状态：解码皮肤下载地址中……")
        properties=base64.b64decode(properties)
        properties=properties.decode()
        properties=json.loads(properties)
        url3=properties["textures"]
        del properties
        havecape=False
        try:
            cape=url3["CAPE"]
            cape=cape["url"]
            filename=id_+'_cape.png'
            zt.set("状态：成功获取披风下载直链，正在尝试下载……")
            urlretrieve(cape,filename)
            havecape=True
        except:
            pass
        url3=url3["SKIN"]
        try:
            isalex=url3["metadata"]
            isalex=isalex["model"]
        except:
            isalex=""
        url3=url3["url"]
        filename=id_+'.png'
        zt.set("状态：成功获取皮肤下载直链，正在尝试下载……")
        urlretrieve(url3,filename)
        del url3
        del filename
        if havecape:
            exit_=str(tkinter.messagebox.showwarning(title="下载完毕", message="下载完毕！此玩家还拥有披风，已同时下载！"))
        else:
            exit_=str(tkinter.messagebox.showwarning(title="下载完毕", message="下载完毕！"))
        zt.set("状态：待命")
        lb2.config(textvariable=zt)
        exit_=tkinter.messagebox.askyesno(title="下载完毕", message="下载完毕！按“确认”打包皮肤成材质包，或者按“取消”打开文件！")
        if exit_==True:
            try:
                file=".\\"+id_
                shutil.rmtree(file)
                del file
            except:
                zt.set("状态：正在删除旧的临时目录……")
            zt.set("状态：正在创建新的临时目录……")
            lb2.config(textvariable=zt)
            file="./"+id_
            os.mkdir(file)
            del file
            zt.set("状态：正在创建材质包说明文件……")
            lb2.config(textvariable=zt)
            filename = './'+id_+"/pack.mcmeta"
            mcmeta="{\"pack\":{\"pack_format\":7,\"description\":\"§c",id_,"\'s Skin Resourcepack\"}}"
            with open(filename, 'w') as file_object:
                file_object.write("{\"pack\":{\"pack_format\":4,\"description\":\"§cSkin Resourcepack\"}}")
            del filename
            del mcmeta
            zt.set("状态：正在下载材质包Logo……")
            lb2.config(textvariable=zt)
            url3="https://pic.downk.cc/item/5ff174673ffa7d37b35bb165.png"
            filename="./"+id_+"/pack.png"
            urlretrieve(url3,filename)
            del url3
            del filename
            zt.set("状态：正在创建皮肤目录……")
            lb2.config(textvariable=zt)
            file="./"+id_+"/assets"
            os.mkdir(file)
            del file
            file="./"+id_+"/assets/minecraft"
            os.mkdir(file)
            del file
            file="./"+id_+"/assets/minecraft/textures"
            os.mkdir(file)
            del file
            file="./"+id_+"/assets/minecraft/textures/entity"
            os.mkdir(file)
            del file
            zt.set("状态：正在复制皮肤文件……")
            lb2.config(textvariable=zt)
            if isalex=="slim":
                cmd="copy "+id_+".png .\\"+id_+"\\assets\\minecraft\\textures\\entity\\alex.png"
                os.system(cmd)
            else:
                cmd="copy "+id_+".png .\\"+id_+"\\assets\\minecraft\\textures\\entity\\steve.png"
                os.system(cmd)
            del cmd
            zt.set("状态：正在压缩材质包……")
            lb2.config(textvariable=zt)
            shutil.make_archive("Skin_"+id_,'zip',id_)
            zt.set("状态：正在删除临时目录……")
            lb2.config(textvariable=zt)
            file=".\\"+id_
            shutil.rmtree(file)
            del file
            zt.set("状态：待命")
            if os.path.exists(".\\.minecraft\\resourcepacks"):
                exit_=tkinter.messagebox.askyesno(title="创建材质包成功", message="成功创建材质包！\n注意：材质包会将游戏内的所有玩家的皮肤都替换成你想要的皮肤，可能会导致一些小问题！\n检测到程序目录下有Minecraft安装，如果要直接导入Minecraft，请按下“确认”，否则请按下“取消”打开材质包。")
                if exit_==True:
                    cmd="copy Skin_"+id_+".zip .\\.minecraft\\resourcepacks\\"+id_+".zip"
                    os.system(cmd)
                    del cmd
                    exit_=tkinter.messagebox.askyesno(title="导入成功", message="导入成功！\n是否要打开材质包文件夹？")
                    if exit_==True:
                        start="start \"\" .\\.minecraft\\resourcepacks\\"
                        os.system(start)
                    del exit_
                else:
                    start="start \"\" "+"\""+id_+'.zip'+"\""
                    os.system(start)
            else:
                exit_=tkinter.messagebox.askyesno(title="创建材质包成功", message="创建材质包成功！注意：材质包会将游戏内的所有玩家的皮肤都替换成你想要的皮肤，可能会导致一些小问题！\n是否要打开材质包？")
                if exit_==True:
                    start="start \"\" "+"\"Skin_"+id_+'.zip'+"\""
                    os.system(start)
                del exit_
        else:
            start="start \"\" "+"\""+id_+'.png'+"\""
            os.system(start)
def getzb(ev=None):
    run_=threading.Thread(target=getzbmain)
    run_.start()
def info():
    def opengithub():
        os.system("start https://github.com/NewbieXvwu/MinecraftSkinDownloader")
    def opengitee():
        os.system("start https://gitee.com/NewbieXvwu/MinecraftSkinDownloader")
    def openbilibili():
        os.system("start https://space.bilibili.com/505201154")
    about=Toplevel()
    about.title("关于本程序")
    aboutscw=about.winfo_screenwidth()
    aboutsch=about.winfo_screenheight()
    aboutw=300
    abouth=210
    aboutx=(aboutscw-aboutw)/2
    abouty=(aboutsch-abouth)/2
    about.geometry("%dx%d+%d+%d"%(aboutw,abouth,aboutx,abouty))
    about.iconbitmap('logo.ico')
    lb4=Label(about,text="关于本程序",font=("宋体",15))
    lb4.place(x=100,y=30)
    lb5=Label(about,text="一个简单的Minecraft\n\n  正版皮肤下载器。",font=("宋体",15))
    lb5.place(x=150,y=100,anchor=CENTER)
    btn3=Button(about,text="Github",command=opengithub)
    btn3.place(x=200,y=155)
    btn4=Button(about,text="Gitee",command=opengitee)
    btn4.place(x=102.5,y=155)
    btn5=Button(about,text="Bilibili",command=openbilibili)
    btn5.place(x=5,y=155)
from tkinter import *
from ttkthemes import *
from tkinter.ttk import *
#sc=ThemedTk(theme="equilux", toplevel=True, themebg=True)
sc=ThemedTk(theme="arc", toplevel=True, themebg=True)
scw=sc.winfo_screenwidth()
sch=sc.winfo_screenheight()
w=500
h=300
x=(scw-w)/2
y=(sch-h)/2
sc.title("Minecraft正版皮肤下载器"+version+" By 萌新欻無")
sc.geometry("%dx%d+%d+%d"%(w,h,x,y))
sc.maxsize(w,h)
sc.minsize(w,h)
try:
    sc.iconbitmap('logo.ico')
except:
    urlretrieve("https://gitee.com/NewbieXvwu/MinecraftSkinDownloader/raw/assets/logo.ico","logo.ico")
    sc.iconbitmap('logo.ico')
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
sc.tk.call('tk', 'scaling', ScaleFactor/75)
lb1=Label(sc,text="请输入你想要获取皮肤的Minecraft正版账号",font=("宋体",15))
lb1.place(x=60,y=40)
e=Entry(sc,width=20)
e.place(x=170,y=120)
e.bind("<Return>",getzb)
btn1=Button(sc,text="点击获取",command=getzb)
btn1.place(x=195,y=190)
zt=tkinter.StringVar()
zt.set("状态：待命")
lb2=Label(sc,textvariable=zt,font=("宋体",15))
lb2.place(x=10,y=270)
cmb = Combobox(sc,width=7)
cmb.place(x=420,y=5)
ms=("浅色模式","深色模式")
cmb["value"]=ms
cmb.current(0)
def func(event):
    if cmb.get()==ms[0]:
        sc.set_theme("arc")
    elif cmb.get()==ms[1]:
        sc.set_theme("equilux")
cmb.bind("<<ComboboxSelected>>",func)
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
    try:
        i = 0
        while True:
            #EnumValue方法用来枚举键值，EnumKey用来枚举子键
            name,value,type=winreg.EnumValue(key,i)
            if str(name)=="AppsUseLightTheme":
                break
            i +=1
        if value==0:
            sc.set_theme("equilux")
            cmb.current(1)
        else:
            sc.set_theme("arc")
            cmb.current(0)
    except WindowsError:
        pass
except:
    pass
btn2=Button(sc,text="关于",command=info)
btn2.place(x=400,y=260)
lb3=Label(sc,text=version,font=("宋体",10))
lb3.place(x=5,y=5)
try:
    update = requests.get("https://gitee.com/api/v5/repos/NewbieXvwu/MinecraftSkinDownloader/releases/latest")
    update=update.text
    update=json.loads(update)
    if float(update["tag_name"])>version_int:
        assets=update["assets"]
        browser_download_url_list=assets[0]
        browser_download_url=browser_download_url_list["browser_download_url"]
        is_update=tkinter.messagebox.askyesno(title="检测到新版本", message="本程序有新版本！是否要下载？")
        if is_update==True:
            def autoupdate():
                btn1.config(state=DISABLED)
                btn1.config(text="更新中……")
                zt.set("状态：更新中，请稍候……")
                fn=os.path.splitext(os.path.basename(__file__))[0]+os.path.splitext(os.path.basename(__file__))[1]
                with open("Update.bat", 'w') as file_object:
                    file_object.write("@echo off\ntaskkill -f -im python.exe\ntaskkill -f -im pythonw.exe\ntaskkill -f -im "+fn+"\ndel /s /q /f "+fn+"\nren New_MinecraftSkinDownloader.exe "+fn+"\nstart "+fn)
                urlretrieve(browser_download_url,"New_MinecraftSkinDownloader.exe")
                os.system("start Update.bat")
                exit()
            run_1=threading.Thread(target=autoupdate)
            run_1.start()
    del update
except:
    pass
sc.mainloop()