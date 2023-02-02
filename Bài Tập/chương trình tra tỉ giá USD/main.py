import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Checkbutton, Radiobutton, IntVar, Spinbox
from tkinter.scrolledtext import ScrolledText
import requests
import time


url = "http://api.currencylayer.com/live?access_key="
key = "4273d2c37f738367f08780b934ce7dda"
txt_tp = "1"
data = requests.get(url + key + "&format="+ txt_tp).json()


def doitien():
    for x in list_key:
        if combobox.get() == x:
            dt = data['quotes']["USD"+ x]
            dulieu2.set(dt)
    localtime = time.asctime( time.localtime(time.time()) ) 
    tong = float(dulieu1.get() * dulieu2.get())
    hienthi = str(dulieu1.get()) + " USD đổi ra được "+ str(tong) + str(combobox.get())+ "\n" + "Last Time Update --- " + str(localtime)
    label12.configure(text=hienthi)


giaodien = tkinter.Tk()
giaodien.title("Chuong trinh")
giaodien.geometry('500x400')

#Label
label = tkinter.Label(giaodien,text="Amount",fg="black")
label.grid(column=1,row=0,padx=10,pady=10,sticky="W")
label2 = tkinter.Label(giaodien,text="USD Currency Converter Using Python",fg="black")
label2.grid(column=2,row=0,padx=10,pady=10,sticky="W")

#Textbox
dulieu1 = tkinter.IntVar()
textbox = tkinter.Entry(giaodien,width=30,textvariable=dulieu1)
textbox.grid(column=1,row=1,padx=10,pady=10,sticky="W")

#Textbox
dulieu2 = tkinter.IntVar()
textbox1 = tkinter.Entry(giaodien,width=30,textvariable=dulieu2)
textbox1.grid(column=1,row=2,padx=10,pady=10,sticky="W")


#Combobox
dulieu3 = tkinter.StringVar()
textbox2 = tkinter.Entry(giaodien,width=23,textvariable=dulieu3,bg="white")
textbox2.grid(column=2,row=1,padx=10,pady=10,sticky="W")
dulieu3.set("USD")
textbox2['state'] = 'readonly'

#Combobox
combobox = Combobox(giaodien)
combobox.grid(column=2,row=2,padx=10,pady=10,sticky="W")
combobox.set("VND")
combobox['state'] = 'readonly'

quotes = data['quotes']
list_key = []
for key in quotes:
    key = str(key).replace("USD","")
    list_key.append(key)

combobox.configure(values=list_key)

# print(json.dumps(data,indent=2))


label12 = tkinter.Label(giaodien,text="",fg="black",bg="white",width=40,height=10)
label12.grid(column=1,columnspan=2,row=3,rowspan=4,sticky="e",pady=20,padx=10,)
label12.config(state=DISABLED, anchor=NW)

#Button
button = tkinter.Button(giaodien,text="Search",fg="black",bg="white",width=8,command=doitien)
button.grid(column=1,row=3,sticky="W",padx=10,pady=10)

#Button
button1 = tkinter.Button(giaodien,text="Clear",fg="black",bg="white",width=8)
button1.grid(column=1,row=4,sticky="W",padx=10,pady=10)


giaodien.mainloop()