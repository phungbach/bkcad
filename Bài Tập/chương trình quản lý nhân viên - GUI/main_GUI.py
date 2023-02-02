import tkinter
from tkinter.ttk import Combobox
from tkinter import Checkbutton, Radiobutton, IntVar, Spinbox
from tkinter.scrolledtext import *
import mysql.connector
import connect_DB
# pip3 install tk

connect = connect_DB.getConnection()
data = connect.cursor()


bgs = "lightgray"

#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Quản lý nhân viên - PythonBKCAD")
giaodien.geometry('650x450')
giaodien.configure(background=bgs)

#lable
label1 = tkinter.Label(giaodien,text="CHƯƠNG TRÌNH QUẢN LÝ NHÂN SỰ",fg="black",font="weight=bold",bg=bgs)
label1.grid(column=2,row=1)

label2 = tkinter.Label(giaodien,text="Name",fg="black",bg=bgs,padx=10,pady=4)
label2.grid(column=1,row=2,sticky='e')

label3 = tkinter.Label(giaodien,text="Age",fg="black",bg=bgs,padx=10,pady=4)
label3.grid(column=1,row=3,sticky='e')

label4 = tkinter.Label(giaodien,text="Country",fg="black",bg=bgs,padx=10,pady=4)
label4.grid(column=1,row=4,sticky='e')

label5 = tkinter.Label(giaodien,text="Sex",fg="black",bg=bgs,padx=10,pady=4)
label5.grid(column=1,row=5,sticky='e')

label6 = tkinter.Label(giaodien,text="Chức vụ",fg="black",bg=bgs,padx=10,pady=4)
label6.grid(column=1,row=6,sticky='e')

label7 = tkinter.Label(giaodien,text="Chấm công",fg="black",bg=bgs,padx=10,pady=4)
label7.grid(column=1,row=7,sticky='e')

label8 = tkinter.Label(giaodien,text="Id",fg="black",bg=bgs,padx=10,pady=4)
label8.grid(column=1,row=8,sticky='e')

label10 = tkinter.Label(giaodien,text="",fg="black",bg=bgs,padx=10,pady=4)
label10.grid(column=3,row=7,sticky='w')

label9 = tkinter.Label(giaodien,text="",fg="black",bg=bgs,padx=10,pady=4)
label9.grid(column=3,row=8,sticky='w')
 
#textbox

entry_name = tkinter.Entry(giaodien,width=30)
entry_name.grid(column=2,row=2, sticky='w')

entry_age = tkinter.Entry(giaodien,width=30)
entry_age.grid(column=2,row=3, sticky='w')

entry_country = tkinter.Entry(giaodien,width=30)
entry_country.grid(column=2,row=4, sticky='w')

entry_sex = Combobox(giaodien,width=27)
entry_sex['values'] = ('nam','nữ','unknow')
entry_sex.grid(column=2,row=5, sticky='w')

entry_chucvu = Combobox(giaodien,width=27)
entry_chucvu['values'] = ('Giám Đốc','Trưởng Phòng','Cán Bộ')
entry_chucvu.grid(column=2,row=6, sticky='w')

entry_chamcong = tkinter.Entry(giaodien,width=30)
entry_chamcong.grid(column=2,row=7, sticky='w')

entry_id = tkinter.Entry(giaodien,width=10)
entry_id.grid(column=2,row=8, sticky='w')

#chức năng


def show_data():
    try:
        data.execute("SELECT * FROM Quanlynhansu.nhanvien")
        ketqua = data.fetchall()
        scrolled.configure(state= "normal")
        scrolled.delete("1.0","end")
        for i in ketqua:
            ketqua = str(i) + ', '
            scrolled.configure(state="normal")
            scrolled.insert(tkinter.INSERT, ketqua + "\n")
            scrolled.configure(state="disable")
        return ketqua
    except:
        scrolled.insert(tkinter.INSERT, "Không có kết nối")
        scrolled.configure(fg="red")

def create_data():
    try:
        name = entry_name.get()
        age = entry_age.get()
        country = entry_country.get()
        sex = entry_sex.get()
        chucvu = entry_chucvu.get()
        chamcong = entry_chamcong.get()

        sql = "INSERT INTO `nhanvien`(`Name`,Age, Country , Sex , Chucvu , Chamcong)VALUES (%s , %s, %s ,%s, %s , %s)"
        vals = (name,age,country,sex,chucvu,chamcong)
        data.execute(sql,vals)
        connect.commit()
        show_data()
        entry_name.delete("1.0", "end")
    except:
        label10.configure(text="Vui lòng nhập dữ liệu",fg="red")

def update_data():
    try:
        name = entry_name.get()
        age = entry_age.get()
        country = entry_country.get()
        sex = entry_sex.get()
        chucvu = entry_chucvu.get()
        chamcong = entry_chamcong.get()
        id = entry_id.get()
        
        if id == "":
            label10.configure(text="Vui lòng nhập Id",fg="red")
        else:
            sql = "UPDATE Quanlynhansu.nhanvien SET `Name` = %s , Age = %s , Country = %s, Sex = %s , Chucvu = %s , Chamcong = %s WHERE Id = %s"
            vals = (name,age,country,sex,chucvu,chamcong,id)
            data.execute(sql,vals)
            connect.commit()
            label10.configure(text="Đã Sửa",fg="blue")
            show_data()
    except:
        label10.configure(text="Vui lòng nhập Nhập dữ liệu",fg="red")

def delete_data():
    try:
        id = entry_id.get()
        if id == "":
            label10.configure(text="Vui lòng nhập Id",fg="red")
        else:
            sql = "DELETE FROM Quanlynhansu.nhanvien WHERE Id = %s "
            data.execute(sql,(id))
            connect.commit()
            label10.configure(text="Đã Xóa",fg="blue")
            show_data()
    except:
        label10.configure(text="Vui lòng nhập Nhập dữ liệu",fg="red")


def kt_thongbao():
    try:
        connect.connect()
        label9.configure(text="Kết nối thành công",fg="blue")
    except:
        label9.configure(text="Kết nối không thành công",fg="red")

def reload():
    scrolled.delete('1.0', "end")
    entry_id.set(" ")


    show_data()

#button
button1 = tkinter.Button(giaodien,text="Thêm nhân viên",fg="black",bg="white",width=15,command=create_data)
button1.grid(column=3,row=2,padx=10,pady=4)

button2 = tkinter.Button(giaodien,text="Xóa nhân viên",fg="black",bg="white",width=15,command=delete_data)
button2.grid(column=3,row=3,padx=10,pady=4)
button3 = tkinter.Button(giaodien,text="Hiển thị nhân viên",fg="black",bg="white",width=15,command=show_data)
button3.grid(column=3,row=4,padx=10,pady=4)

button4 = tkinter.Button(giaodien,text="Sửa nhân viên",fg="black",bg="white",width=15,command=update_data)
button4.grid(column=3,row=5,padx=10,pady=4)

button5 = tkinter.Button(giaodien,text="Kiểm tra kết nối",fg="black",bg="white",width=15,command=kt_thongbao)
button5.grid(column=3,row=6,padx=10,pady=4)

button6 = tkinter.Button(giaodien,text="Reload",fg="black",bg="white",width=15,command=reload)
button6.grid(column=3,row=12,padx=10,sticky='sw')


#Scrolled Text
scrolled = ScrolledText(giaodien,width=50,height = 10)
scrolled.grid(column=2,row=12,sticky='w')

giaodien.mainloop()