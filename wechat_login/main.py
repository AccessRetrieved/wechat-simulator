import pyqrcode
from tkinter import *
from tkinter.ttk import Progressbar
import tkmacosx
from PIL import Image, ImageTk
import requests
import os
from time import sleep
import subprocess

root = Tk()
root.geometry('300x375')
root.title('')

global counter
counter = 0

def refresh_login():
    url = 'http://192.168.1.78:2350/static/WeixinQrCode.png'
    try:
        response = requests.get(url).content

        
        with open(os.getcwd() + '/wechat_login/temp/WeixinQrCode.png', 'wb') as file:
            file.write(response)
            file.close()
    except:
        pass

    root.after(ms=2500, func=refresh_login)

def refresh_server_code():
    url = 'http://192.168.1.78:2350/login/request/mac/qr'
    try:
        response = str(requests.get(url).content)

        if 'true' in response:
            print('logged in')

            displayWeixinQr.place_forget()
            hint.place_forget()
            notice.place_forget()

            p = Progressbar(root, orient=HORIZONTAL, length=200, mode="determinate", takefocus=True, maximum=100)
            p.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            p['value'] = 0
            root.update()
            sleep(0.5)

            p['value'] = 20
            root.update()
            sleep(0.5)

            p['value'] = 40
            root.update()
            sleep(0.5)

            p['value'] = 60
            root.update()
            sleep(0.5)

            p['value'] = 80
            root.update()
            sleep(0.5)

            p['value'] = 100
            root.update()
            subprocess.call(['open', '/Applications/WeChat.app'])
            root.destroy()
        else:
            pass
    except:
        pass

    root.after(ms=2500, func=refresh_server_code)

def refresh_add_img():
    try:
        img = Image.open(os.getcwd() + '/wechat_login/temp/WeixinQrCode.png')
        img = img.resize((200, 200), Image.ANTIALIAS)
        global pic
        pic = ImageTk.PhotoImage(img)

        displayWeixinQr.image = pic
        displayWeixinQr.config(image = pic)
    except:
        pass
    
    root.after(ms=2500, func=refresh_add_img)

displayWeixinQr = Label(root, text='')
displayWeixinQr.place(relx=0.5, rely=0.35, anchor=CENTER)

hint = Label(root, text='扫码登录微信', font=("Arial", 20))
hint.place(relx=0.5, rely=0.7, anchor=CENTER)

notice = Label(root, text='Mac 微信需要配合你的手机登录使用', font=("Arial", 14), fg='#949494')
notice.place(relx=0.5, rely=0.78, anchor=CENTER)

root.after(1, refresh_login)
root.after(1, refresh_server_code)
root.after(1, refresh_add_img)
root.mainloop()