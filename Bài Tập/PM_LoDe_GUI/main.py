import tkinter
from tkinter.ttk import Combobox
from tkinter import Checkbutton, Radiobutton, IntVar, Spinbox
from tkinter.scrolledtext import ScrolledText
import random
# pip3 install tk

#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Trò chơi lô đề")
giaodien.geometry('500x400')

#func
giaidacbiet = random.randint(1,99999)
giai1 = random.randint(1,99999)
giai2a = random.randint(1,99999)
giai2b = random.randint(1,99999)
giai3a = random.randint(1,99999)
giai3b = random.randint(1,99999)
giai3c = random.randint(1,99999)
giai3d = random.randint(1,99999)
giai3e = random.randint(1,99999)
giai3f = random.randint(1,99999)
giai4a = random.randint(1,9999)
giai4b = random.randint(1,9999)
giai4c = random.randint(1,9999)
giai4d = random.randint(1,9999)
giai5a = random.randint(1,9999)
giai5b = random.randint(1,9999)
giai5c = random.randint(1,9999)
giai5d = random.randint(1,9999)
giai5e = random.randint(1,9999)
giai5f = random.randint(1,9999)
giai6a = random.randint(1,999)
giai6b = random.randint(1,999)
giai6c = random.randint(1,999)
giai7a = random.randint(1,99)
giai7b = random.randint(1,99)
giai7c = random.randint(1,99)
giai7d = random.randint(1,99)


def show_data():
    scrolled.delete("0.1","end")
    scrolled.insert(tkinter.INSERT,"Giải ĐB:"+"\t\t\t"+ str(giaidacbiet) + "\n")
    scrolled.insert(tkinter.INSERT,"1:"+"\t\t\t"+ str(giai1) + "\n")
    scrolled.insert(tkinter.INSERT,"2:"+"\t\t\t"+ str(giai2a) + " " + str(giai2a) + "\n")
    scrolled.insert(tkinter.INSERT,"3:"+"\t\t\t"+ str(giai3a) + " " + str(giai3b) + " " + str(giai3c) + " " + str(giai3d) + " " + str(giai3e) + " " + str(giai3f) + "\n")
    scrolled.insert(tkinter.INSERT,"4:"+"\t\t\t"+ str(giai4a) + " " + str(giai4b) + " " + str(giai4c) + "\n")
    scrolled.insert(tkinter.INSERT,"5:"+"\t\t\t"+ str(giai5a) + " " + str(giai5b) + " " + str(giai5c) + " " + str(giai5d) + " " + str(giai5e) + " " + str(giai5f) + "\n")
    scrolled.insert(tkinter.INSERT,"6:"+"\t\t\t"+ str(giai6a) + " " + str(giai6b) + " " + str(giai6c) + "\n")
    scrolled.insert(tkinter.INSERT,"7:"+"\t\t\t"+ str(giai7a) + " " + str(giai7b) + " " + str(giai7c) + " " + str(giai7d) + "\n")



#Label
label1 = tkinter.Label(giaodien,text="Trò chơi lô đề",fg="black",bg="white")
label1.grid(column=1,row=1)
#Label
label1 = tkinter.Label(giaodien,text="I. Chơi lô",fg="black",bg="white")
label1.grid(column=1,row=2)
#Label
label2 = tkinter.Label(giaodien,text="Chọn số: ",fg="black",bg="white")
label2.grid(column=1,row=3)
#Textbox
txt_chonso = tkinter.Entry(giaodien,width=30)
txt_chonso.grid(column=2,row=3)
#Label
label3 = tkinter.Label(giaodien,text="Đánh mấy điểm: ",fg="black",bg="white")
label3.grid(column=3,row=3)
#Textbox
txt_diem = tkinter.Entry(giaodien,width=30)
txt_diem.grid(column=4,row=3)
#Button
button = tkinter.Button(giaodien,text="Chơi đi đừng sợ",fg="black",bg="white",command=show_data)
button.grid(column=3,row=4)

###

#Label
lb_choide = tkinter.Label(giaodien,text="I. Chơi Đề",fg="black",bg="white")
lb_choide.grid(column=1,row=6)
#Label
label2 = tkinter.Label(giaodien,text="Chọn số: ",fg="black",bg="white")
label2.grid(column=1,row=7)
#Textbox
txt_chonso = tkinter.Entry(giaodien,width=30)
txt_chonso.grid(column=2,row=7)
#Label
label3 = tkinter.Label(giaodien,text="Đánh mấy điểm: ",fg="black",bg="white")
label3.grid(column=3,row=7)
#Textbox
txt_diem = tkinter.Entry(giaodien,width=30)
txt_diem.grid(column=4,row=7)
#Button
button = tkinter.Button(giaodien,text="Chơi đi đừng sợ",fg="black",bg="white")
button.grid(column=3,row=8)

#Scrolled Text
scrolled = ScrolledText(giaodien,width=20,height = 10)
scrolled.grid(column=2,row=9)

#Label
lb_tongdiem = tkinter.Label(giaodien,text="Tổng số tiền: 1.000.000 VND",fg="black",bg="white")
lb_tongdiem.grid(column=1,row=12)

lb_sotienconlai = tkinter.Label(giaodien,text="Số tiền còn lại",fg="black",bg="white")
lb_sotienconlai.grid(column=1,row=13)

lb_sotienconlai_1 = tkinter.Label(giaodien,text="",fg="black",bg="blue")
lb_sotienconlai_1.grid(column=2,row=13)

giaodien.mainloop()

