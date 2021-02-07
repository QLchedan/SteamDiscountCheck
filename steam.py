import requests
import tkinter.font as tkFont
from tkinter import *
from bs4 import BeautifulSoup
import sys
import pyautogui as pag
import threading
x=0
y=0
game=[]
url=""
dlc_=[]
u=""
t=Tk()

fonta=tkFont.Font(family="Arial", size=12, weight="bold")
fontb=tkFont.Font(family="Arial", size=10, weight="bold")
al=Label(t, font=fonta)
bl=Label(t,font=fontb)
cl=Label(t,font=fonta)
al.grid()
bl.grid()
cl.grid()
txt=Text(font=fontb)
txt.place(x=0, y=75)

def label_():
    global t,game,dlc_,al,bl,cl,txt
    print(txt)
    t.wm_attributes("-alpha", 0.4)
    t.wm_attributes("-toolwindow", True)
    t.wm_attributes("-topmost", True)
    t.overrideredirect(True)
    t.geometry("475x250+"+str(t.winfo_screenwidth()-475)+"+50")
    #al=Label(t, text="GAME NAME:"+game[0], font=fonta).grid()
    #bl=Label(t, text=game[2]+"→"+game[3]+"   ("+game[1]+")", font=fontb).grid()
    #cl=Label(t, text="DLC:", font=fonta).grid()
    al.configure(text="GAME NAME:"+game[0])
    bl.configure(text=game[2]+"→"+game[3]+"   ("+game[1]+")")
    cl.configure(text="DLC:")
    txt.delete(0.0, END)
    print(dlc_)
    for i in dlc_:
        print("insert")
        txt.insert("insert", i["name"]+":"+i["opr"]+"→"+i["fpr"]+"("+i["pct"]+")"+'\n')
        t.update()
    t.bind('<Left>', lef)
    t.bind('<Right>', rig)
    t.bind('<Button-3>',readwe)
    t.bind('<Down>',exit)
    t.mainloop()


def lef(xx):
    global t
    t.geometry("475x250+"+str(t.winfo_x()-30)+"+50")


def rig(xx):
    global t
    t.geometry("475x250+"+str(t.winfo_x()+30)+"+50")

def readfi():
    global u
    try:
        file_=open(sys.path[0]+"\\config.txt","r")
        u=file_.read()
        file_.close()
    except FileNotFoundError:
        while True:
            print("filenotfound     "+sys.path[0]+"\\config.txt")
#↑读取配置
def readwe(xx):
    global url,game,dlc,u,dlc_
    dlc_=[]
    readfi()
    url='https://store.steampowered.com/app/'+u
    res=requests.get(url)
    s=BeautifulSoup(res.text,'html.parser')
    x=s.find('div',class_="game_area_purchase_game")
    try:
        game=[s.find('div',class_="apphub_AppName").get_text(),x.find('div',class_="discount_pct").get_text(),x.find('div',class_="discount_original_price").get_text(),x.find('div',class_="discount_final_price").get_text()]
    except AttributeError:
        game=[s.find('div',class_="apphub_AppName").get_text(),"None",x.find('div',class_="game_purchase_price").get_text().strip(),x.find('div',class_="game_purchase_price").get_text().strip()]
    dlc=s.find_all('a',class_="game_area_dlc_row")
    for t in dlc:
        d_=t.find('div',class_="game_area_dlc_name").get_text().strip()
        try:
            a_=t.find('div',class_="discount_pct").get_text()
            b_=t.find('div',class_="discount_original_price").get_text()
            c_=t.find('div',class_="discount_final_price").get_text()
            dlc_.append({"name":d_,"pct":a_,"opr":b_,"fpr":c_})
        except AttributeError:#无打折/免费
            pri=t.find('div',class_="game_area_dlc_price").get_text().strip()
            dlc_.append({"name":d_,"pct":"None","opr":pri,"fpr":pri})
    label_()
readwe(1)
#↑获取信息
#↓窗口界面
