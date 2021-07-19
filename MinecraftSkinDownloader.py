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
        url3=url3["SKIN"]
        url3=url3["url"]
        filename=id_+'.png'
        zt.set("状态：成功获取皮肤下载直链，正在尝试下载……")
        urlretrieve(url3,filename)
        del url3
        del filename
        exit_=str(tkinter.messagebox.showwarning(title="下载完毕", message="下载完毕！"))
        zt.set("状态：待命")
        lb2.config(textvariable=zt)
    '''exit_=str(tkinter.messagebox.askyesno(title="下载完毕", message="下载完毕！按“确认”打包皮肤成材质包，或者按“取消”打开文件！"))
    if exit_==True:
        try:
            file=".\\"+id_
            shutil.rmtree(file)
            del file
        except:
            pass
        zt.set("状态：正在创建新的临时目录……")
        lb2.config(textvariable=zt)
        file="./"+id_
        os.mkdir(file)
        del file
        zt.set("状态：正在创建材质包说明文件……")
        lb2.config(textvariable=zt)
        filename = './'+id_+"/pack.mcmeta"
        mcmeta="{\"pack\":{\"pack_format\":4,\"description\":\"§c",id_,"\'s Skin Resourcepack\"}}"
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
        mx=str(tkinter.messagebox.askyesno(title="选择皮肤模型", message="你下载的皮肤是Steve模型（手粗）还是Alex模型（手细）？\n如果你不知道，你可以先选择Steve，如果模型显示错误再改。\n是Steve模型请按下“确定”，是Alex模型请按下“取消”。"))
        if mx==False:
            cmd="copy "+id_+".png .\\"+id_+"\\assets\\minecraft\\textures\\entity\\alex.png"
            os.system(cmd)
        else:
            cmd="copy "+id_+".png .\\"+id_+"\\assets\\minecraft\\textures\\entity\\steve.png"
            os.system(cmd)
        del cmd
        del mx
        zt.set("状态：正在压缩材质包……")
        lb2.config(textvariable=zt)
        shutil.make_archive("Skin_"+id_,'zip',id_)
        zt.set("状态：正在删除临时目录……")
        lb2.config(textvariable=zt)
        file=".\\"+id_
        shutil.rmtree(file)
        del file
        if os.path.exists(".\\.minecraft\\resourcepacks"):
            exit_=str(tkinter.messagebox.askyesno(title="创建材质包成功", message="成功创建材质包！\n注意：材质包会将游戏内的所有玩家的皮肤都替换成你想要的皮肤，可能会导致一些小问题！\n检测到程序目录下有Minecraft安装，如果要直接导入Minecraft，请按下“确认”，否则请按下“取消”打开材质包。"))
            if exit_==True:
                cmd="copy Skin_"+id_+".zip .\\.minecraft\\resourcepacks\\"+id_+".zip"
                os.system(cmd)
                del cmd
                exit_=str(tkinter.messagebox.askyesno(title="导入成功", message="导入成功！\n是否要打开材质包文件夹？"))
                if exit_==True:
                    start="start \"\" .\\.minecraft\\resourcepacks\\"
                    os.system(start)
                del exit_
            else:
                start="start \"\" "+"\""+id_+'.zip'+"\""
                os.system(start)
        else:
            exit_=str(tkinter.messagebox.askyesno(title="创建材质包成功", message="创建材质包成功！注意：材质包会将游戏内的所有玩家的皮肤都替换成你想要的皮肤，可能会导致一些小问题！\n是否要打开材质包？"))
            if exit_==True:
                start="start \"\" "+"\"Skin_"+id_+'.zip'+"\""
                os.system(start)
            del exit_
    else:
        start="start \"\" "+"\""+id_+'.png'+"\""
        os.system(start)'''
def getzb():
    run_=threading.Thread(target=getzbmain)
    run_.start()
from tkinter import *
from ttkthemes import *
from tkinter.ttk import *
if int(platform.uname()[3].split(".")[2])>=22000 and platform.uname()[0]=='Windows':
    sc=Tk()
else:
    sc=ThemedTk(theme="arc", toplevel=True, themebg=True)
scw=sc.winfo_screenwidth()
sch=sc.winfo_screenheight()
w=500
h=300
x=(scw-w)/2
y=(sch-h)/2
sc.title("Minecraft正版皮肤下载器")
sc.geometry("%dx%d+%d+%d"%(w,h,x,y))
sc.maxsize(w,h)
sc.minsize(w,h)
try:
    sc.iconbitmap('logo.ico')
except:
    urlretrieve("http://www.zlian.ga/u/1626674746qk.ico","logo.ico")
    sc.iconbitmap('logo.ico')
lb1=Label(sc,text="请输入你想要获取皮肤的Minecraft正版账号",font=("宋体",15))
lb1.place(x=60,y=30)
e=Entry(sc,width=20)
e.place(x=170,y=100)
btn1=Button(sc,text="点击获取",command=getzb)
btn1.place(x=195,y=170)
zt=tkinter.StringVar()
zt.set("状态：待命")
lb2=Label(sc,textvariable=zt,font=("宋体",15))
lb2.place(x=10,y=270)
sc.mainloop()