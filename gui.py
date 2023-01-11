import tkinter
from tkinter.ttk import Combobox
from tkinter import Checkbutton, Radiobutton, IntVar, Spinbox
from tkinter.scrolledtext import ScrolledText
# pip3 install tk

#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Chuong trinh")
giaodien.geometry('500x400')

#Label
label1 = tkinter.Label(giaodien,text="Xin chao",fg="black",bg="white")
label1.grid(column=1,row=0)
#Textbox
txt_name = tkinter.Entry(giaodien,width=30)
txt_name.grid(column=2,row=0)


#Combobox
combobox = Combobox(giaodien)
combobox['values'] = (1,2,3,4,'Text')
combobox.grid(column=2,row=3)

collect_data_form = "https://api.callmebot.com/facebook/send.php?apikey=1234567890&text=" + txt_name.get() +  combobox.get()


#Button
button = tkinter.Button(giaodien,text="Click me",fg="black",bg="white")
button.grid(column=2,row=1)

giaodien.mainloop()

