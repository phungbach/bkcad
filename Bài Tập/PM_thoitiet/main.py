import requests
import tkinter
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import time

#getapi

def show():
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q="
        key =  "fe53bfd100e8ca1c2ca47f202a2e9b9c"
        txt_tp = dulieu1.get()   
        data = requests.get(url + txt_tp +"&appid="+ key).json()


        #contry
        country = dict(data['sys'])
        country_local = country['country']
        namelocal = data["name"]
        label.configure(text=namelocal+","+country_local)

        #trangthai
        weather = data['weather']
        weather_now = dict(weather[0])
        weather_now = weather_now['main']
        label5.configure(text=weather_now)

        #nhietdo
        humidity = data['main']['temp']
        label6.configure(text=humidity)

        #doam
        humidity = data['main']['humidity']
        label7.configure(text=humidity)

        #seelv
        pressure = data['main']['pressure']
        label8.configure(text=pressure)

    except:
        pass





#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Chuong trinh")
giaodien.geometry('350x350')
giaodien.resizable(0,0)


label = tkinter.Label(giaodien,text="NA-/",fg="black",pady=10)
label.grid(column=1,row=1,padx=2,pady=2)
label1 = tkinter.Label(giaodien,text="Weather Report",fg="black",pady=10)
label1.grid(column=2,row=1,padx=2,pady=2)

#ngaythang
label2 = tkinter.Label(giaodien,text="",fg="black",pady=10)
label2.grid(column=3,row=1,padx=2,pady=2)
localtime = time.localtime(time.time())
showtime = str(localtime.tm_year) +" - " +  str(localtime.tm_mon) +" - " + str(localtime.tm_mday)
label2.configure(text=showtime)

label3 = tkinter.Label(giaodien,text="City or Country Name",fg="black",pady=10)
label3.grid(column=2,row=2,padx=2,pady=2)

dulieu1 = tkinter.StringVar()
textbox = tkinter.Entry(giaodien,width=30,textvariable=dulieu1)
textbox.grid(column=2,row=3,sticky=W,padx=2,pady=2)

button = tkinter.Button(giaodien,text="Tìm Kiếm",fg="black",bg="white",command=show)
button.grid(column=3,row=3,sticky=W,padx=2,pady=2)

label4 = tkinter.Label(giaodien,text="Weather Report",fg="black",pady=10)
label4.grid(row=4,column=1)

label11 = tkinter.Label(giaodien,text="trạng thái",fg="black",pady=10)
label11.grid(column=1,row=5,sticky=W,padx=2,pady=2)
label5 = tkinter.Label(giaodien,text="NA-/",fg="black",pady=10)
label5.grid(column=2,row=5,sticky=W,padx=2,pady=2)

label6 = tkinter.Label(giaodien,text="NA-/",fg="black",pady=10)
label6.grid(column=2,row=6,sticky=W,padx=2,pady=2)
label9 = tkinter.Label(giaodien,text="nhiệt độ",fg="black",pady=10)
label9.grid(column=1,row=6,sticky=W,padx=2,pady=2)

label7 = tkinter.Label(giaodien,text="NA-/",fg="black",pady=10)
label7.grid(column=2,row=7,sticky=W,padx=2,pady=2)
label10 = tkinter.Label(giaodien,text="độ ẩm",fg="black",pady=10)
label10.grid(column=1,row=7,sticky=W,padx=2,pady=2)

label8 = tkinter.Label(giaodien,text="NA-/",fg="black",pady=10)
label8.grid(column=2,row=8,sticky=W,padx=2,pady=2)
label11 = tkinter.Label(giaodien,text="áp lực",fg="black",pady=10)
label11.grid(column=1,row=8,sticky=W,padx=2,pady=2)




giaodien.mainloop()