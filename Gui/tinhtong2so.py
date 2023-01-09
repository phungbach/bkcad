import tkinter

giaodien = tkinter.Tk()
giaodien.title("Chương Trình")
giaodien.geometry('300x300')

#label
lable1 = tkinter.Label(giaodien,text="Tính tổng 2 số",fg="black",bg="White")
lable1.grid(column=2,row=0)

lable2 = tkinter.Label(giaodien,text="Nhập số thứ nhất:",fg="black",bg="White")
lable2.grid(column=1,row=2)

lable3 = tkinter.Label(giaodien,text="Nhập số thứ hai:",fg="black",bg="White")
lable3.grid(column=1,row=3)

lable4 = tkinter.Label(giaodien,text="Kết quả:",fg="black",bg="White")
lable4.grid(column=1,row=4)

#textbox
dulieu = tkinter.IntVar()
textbox = tkinter.Entry(giaodien,width=30,textvariable=dulieu)
textbox.grid(column=2,row=2)

dulieu2 = tkinter.IntVar()
textbox2 = tkinter.Entry(giaodien,width=30,textvariable=dulieu2)
textbox2.grid(column=2,row=3)

dulieu3 = tkinter.IntVar()
textbox3 = tkinter.Entry(giaodien,width=30,textvariable=dulieu3)
textbox3.grid(column=2,row=4)


#chuc nang

def tinhtong():
    tong = int(dulieu.get()) + int(dulieu2.get())
    dulieu3.set(tong)
    dulieu.set("")
    dulieu2.set("")

def tinhhieu():
    tong = int(dulieu.get()) - int(dulieu2.get())
    dulieu3.set(tong)
    dulieu.set("")
    dulieu2.set("")

def tinhtich():
    tong = int(dulieu.get()) * int(dulieu2.get())
    dulieu3.set(tong)
    dulieu.set("")
    dulieu2.set("")

def tinhthuong():
    tong = float(dulieu.get()) / float(dulieu2.get())
    dulieu3.set(tong)
    dulieu.set("")
    dulieu2.set("")

#button
button = tkinter.Button(giaodien,text="Tính tổng",fg="black",bg="white",command=tinhtong)
button.grid(column=1,row=5)

button = tkinter.Button(giaodien,text="Tính hiệu",fg="black",bg="white",command=tinhhieu)
button.grid(column=1,row=6)

button = tkinter.Button(giaodien,text="Tính tích",fg="black",bg="white",command=tinhtich)
button.grid(column=1,row=7)

button = tkinter.Button(giaodien,text="Tính thương",fg="black",bg="white",command=tinhthuong)
button.grid(column=1,row=8)



giaodien.mainloop()

