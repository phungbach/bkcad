import tkinter
from tkinter.ttk import Combobox
from tkinter import Checkbutton, Radiobutton, IntVar, Spinbox
from tkinter.scrolledtext import ScrolledText
import random
# pip3 install tk

#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Trò chơi lô đề")
giaodien.geometry('700x600')

#func
giaidacbiet = []
giai1 = []
giai2a = []
giai2b = []
giai3a = []
giai3b = []
giai3c = []
giai3d = []
giai3e = []
giai3f = []
giai4a = []
giai4b = []
giai4c = []
giai4d = []
giai5a = []
giai5b = []
giai5c = []
giai5d = []
giai5e = []
giai5f = []
giai6a = []
giai6b = []
giai6c = []
giai7a = []
giai7b = []
giai7c = []
giai7d = []

def reload_game():
    del giaidacbiet[0:10]
    giaidacbiet.append(random.randint(1,99999))
    del giai1[0:10]
    giai1.append(random.randint(1,99999))
    del giai2a[0:10]
    giai2a.append(random.randint(1,99999))
    del giai2b[0:10]
    giai2b.append(random.randint(1,99999))
    del giai3a[0:10]
    giai3a.append(random.randint(1,99999))
    del giai3b[0:10]
    giai3b.append(random.randint(1,99999))
    del giai3c[0:10]
    giai3c.append(random.randint(1,99999))
    del giai3d[0:10]
    giai3d.append(random.randint(1,99999))
    del giai3e[0:10]
    giai3e.append(random.randint(1,99999))
    del giai3f[0:10]
    giai3f.append(random.randint(1,99999))
    del giai4a[0:10]
    giai4a.append(random.randint(1,9999))
    del giai4b[0:10]
    giai4b.append(random.randint(1,9999))
    del giai4c[0:10]
    giai4c.append(random.randint(1,9999))
    del giai4d[0:10]
    giai4d.append(random.randint(1,9999))
    del giai5a[0:10]
    giai5a.append(random.randint(1,9999))
    del giai5b[0:10]
    giai5b.append(random.randint(1,9999))
    del giai5c[0:10]
    giai5c.append(random.randint(1,9999))
    del giai5d[0:10]
    giai5d.append(random.randint(1,9999))
    del giai5e[0:10]
    giai5e.append(random.randint(1,9999))
    del giai5f[0:10]
    giai5f.append(random.randint(1,9999))
    del giai6a[0:10]
    giai6a.append(random.randint(1,999))
    del giai6b[0:10]
    giai6b.append(random.randint(1,999))
    del giai6c[0:10]
    giai6c.append(random.randint(1,999))
    del giai7a[0:10]
    giai7a.append(random.randint(1,99))
    del giai7b[0:10]
    giai7b.append(random.randint(1,99))
    del giai7c[0:10]
    giai7c.append(random.randint(1,99))
    del giai7d[0:10]
    giai7d.append(random.randint(1,99))


def show_data():
    reload_game()
    scrolled.delete("0.1","end")
    scrolled.insert(tkinter.INSERT,"ĐB:"+"\t"+ str(giaidacbiet) + "\n")
    scrolled.insert(tkinter.INSERT,"1:"+"\t"+ str(giai1) + "\n")
    scrolled.insert(tkinter.INSERT,"2:"+"\t"+ str(giai2a) + " " + str(giai2a) + "\n")
    scrolled.insert(tkinter.INSERT,"3:"+"\t"+ str(giai3a) + " " + str(giai3b) + " " + str(giai3c) + " " + str(giai3d) + " " + str(giai3e) + " " + str(giai3f) + "\n")
    scrolled.insert(tkinter.INSERT,"4:"+"\t"+ str(giai4a) + " " + str(giai4b) + " " + str(giai4c) + "\n")
    scrolled.insert(tkinter.INSERT,"5:"+"\t"+ str(giai5a) + " " + str(giai5b) + " " + str(giai5c) + " " + str(giai5d) + " " + str(giai5e) + " " + str(giai5f) + "\n")
    scrolled.insert(tkinter.INSERT,"6:"+"\t"+ str(giai6a) + " " + str(giai6b) + " " + str(giai6c) + "\n")
    scrolled.insert(tkinter.INSERT,"7:"+"\t"+ str(giai7a) + " " + str(giai7b) + " " + str(giai7c) + " " + str(giai7d) + "\n")
    tinhtien()
    dulieu1.set("0")
    dulieu2.set("0")
    dulieu3.set("0")
    dulieu4.set("0")

def tinhtien():
    tongtien = 1000000
    if str(dulieu1.get()) == str(giaidacbiet[3:4]):
        tongtien = tongtien +  (int(dulieu2.get()) * 23000)
        lb_sotienconlai_1.configure(text=tongtien)
        lb_thongbao.configure(text="Thắng")
    else:
        tongtien = tongtien - (int(dulieu2.get()) * 23000)
        lb_sotienconlai_1.configure(text=tongtien)
        lb_thongbao.configure(text="Thua")
        if tongtien <= 0:
            lb_thongbao.configure(text="Bạn đã hết tiền vui lòng chơi lại")
    return tongtien
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
dulieu1 = tkinter.IntVar()
txt_chonso = tkinter.Entry(giaodien,width=30,textvariable=dulieu1)
txt_chonso.grid(column=2,row=3)
#Label
label3 = tkinter.Label(giaodien,text="Đánh mấy điểm: ",fg="black",bg="white")
label3.grid(column=3,row=3)
#Textbox
dulieu2 = tkinter.IntVar()
txt_diem = tkinter.Entry(giaodien,width=30,textvariable=dulieu2)
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
dulieu3 = tkinter.IntVar()
txt_chonso1 = tkinter.Entry(giaodien,width=30,textvariable=dulieu3)
txt_chonso1.grid(column=2,row=7)
#Label
label3 = tkinter.Label(giaodien,text="Đánh mấy điểm: ",fg="black",bg="white")
label3.grid(column=3,row=7)
#Textbox
dulieu4 = tkinter.IntVar()
txt_diem2 = tkinter.Entry(giaodien,width=30,textvariable=dulieu4)
txt_diem2.grid(column=4,row=7)
#Button
button = tkinter.Button(giaodien,text="Chơi đi đừng sợ",fg="black",bg="white")
button.grid(column=3,row=8)

#Scrolled Text
scrolled = ScrolledText(giaodien,width=60,height = 15)
scrolled.grid(column=2,columnspan=4,row=9,sticky="w")

#Label
lb_tongdiem = tkinter.Label(giaodien,text="Tổng số tiền: 1.000.000 VND",fg="black",bg="white")
lb_tongdiem.grid(column=1,row=12)

lb_sotienconlai = tkinter.Label(giaodien,text="Số tiền còn lại",fg="black",bg="white")
lb_sotienconlai.grid(column=1,row=13)

lb_sotienconlai_1 = tkinter.Label(giaodien,text="",fg="black",bg="blue")
lb_sotienconlai_1.grid(column=2,row=13)

lb_thongbao = tkinter.Label(giaodien,text="",fg="black",bg="blue")
lb_thongbao.grid(column=4,row=13)

lb_thongbao1 = tkinter.Label(giaodien,text="",fg="black",bg="blue")
lb_thongbao1.grid(column=4,row=14)

# lb_thongbao = tkinter.Label(giaodien,text="",fg="black",bg="blue")
# lb_thongbao.grid(column=4,row=13)

giaodien.mainloop()