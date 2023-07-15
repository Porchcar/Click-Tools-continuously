import tkinter.ttk
import pyautogui
import keyboard
import sys
import time
from tkinter.messagebox import showinfo
from tkinter import *

def start():
    mode = ty.get()
    root.destroy()
    if mode == 1:
        sel = var.get()
        hot_key = st.get()
        stop_hot_key = stop.get()
        if hot_key == stop_hot_key:
            showinfo(message="您的开始热键与停止热键相同，请更改")
            sys.exit()
        keyboard.wait(hot_key)
        while True:
            if keyboard.is_pressed(stop_hot_key):
                sys.exit()
            if sel == 1:
                pyautogui.click(pyautogui.position())
            else:
                pyautogui.tripleClick(pyautogui.position())
    else:
        stop_hot_key = stop.get()
        showinfo(message="按下“确定”键5秒后记录位置1")
        time.sleep(5)
        x, y = pyautogui.position()
        showinfo(message="按下“确定”键5秒后记录位置2")
        time.sleep(5)
        a, b = pyautogui.position()
        showinfo(message="按下“确定”键7秒后开始点击")
        time.sleep(7)
        while True:
            if keyboard.is_pressed(stop_hot_key):
                sys.exit()
            pyautogui.leftClick(x, y)
            pyautogui.leftClick(a, b)

def version():
    dt = Tk()
    dt.geometry("350x220")
    dt.title("版本信息")
    Label(dt,text="连点器\n版权归张泊桥所有。\n已开源\n\n").pack()
    Label(dt,text="版本号:1.0.0",font=("微软雅黑", 20)).pack()
    dt.mainloop()

root = Tk()
ty = IntVar()
var = IntVar()
st = StringVar()
stop = StringVar()
var.set(2)
st.set("1")
stop.set("2")
ty.set(1)
root.title("连点器")
root.geometry("400x450")
Label(root,text="开始热键(在双位置点击时无效):").pack()
combobox_1 = tkinter.ttk.Combobox(root,textvariable=st)
combobox_1['value'] = ('space','0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
combobox_1.pack()
Label(root,text="停止热键:").pack()
combobox_2 = tkinter.ttk.Combobox(root,textvariable=stop)
combobox_2['value'] = ('space','0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
combobox_2.pack()
Label(root,text="点击速度:").pack()
Radiobutton(root,text="快",variable=var,value=1).pack()
Radiobutton(root,text="超快",variable=var,value=2).pack()
Label(root,text="点击模式:").pack()
Radiobutton(root,text="单位置点击",variable=ty,value=1).pack()
Radiobutton(root,text="双位置点击",variable=ty,value=2).pack()
Button(root,text="开始监听",command=start).pack()
Button(root,text="版本信息",command=version).pack()
Button(root,text="退出",command=lambda:root.destroy()).pack()
root.mainloop()
