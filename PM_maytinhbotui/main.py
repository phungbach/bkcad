import tkinter
# pip3 install tk

#Giao dien
giaodien = tkinter.Tk()
giaodien.title("Calculator")
giaodien.geometry('320x630')
giaodien.configure(padx=20,pady=20)

#Textbox
emtry_mh = tkinter.Label(giaodien,width=18,height=5,bg="white",font="weight=bold")
emtry_mh.grid(columnspan=4,row=1,padx=2,pady=2,sticky='e')

#func
bieuthuc = ''
def clear():
    global bieuthuc
    emtry_mh.config(text="")
    bieuthuc = ""

def famexl(num):
    global bieuthuc
    bieuthuc += str(num)
    emtry_mh.config(text=bieuthuc)

def ketqua():
    try:
        global bieuthuc
        global tinh
        tinh = eval(bieuthuc)
        emtry_mh.config(text=tinh)
        bieuthuc = ""
    except SyntaxError:
        emtry_mh.config(text="Vui lòng không nhập 0 ở đầu")


#Button
button_C = tkinter.Button(giaodien,text="C",fg="black",bg="white",font="weight=bold",width=5,height=4,command=clear)
button_C.grid(column=4,row=1,padx=2,pady=2,sticky='e')


button_9 = tkinter.Button(giaodien,text="9",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('9'))
button_9.grid(column=1,row=2,padx=2,pady=2,sticky='e')

button_8 = tkinter.Button(giaodien,text="8",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('8'))
button_8.grid(column=2,row=2,padx=2,pady=2,sticky='e')

button_7 = tkinter.Button(giaodien,text="7",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('7'))
button_7.grid(column=3,row=2,padx=2,pady=2,sticky='e')

button_6 = tkinter.Button(giaodien,text="6",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('6'))
button_6.grid(column=1,row=3,padx=2,pady=2,sticky='e')

button_5 = tkinter.Button(giaodien,text="5",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('5'))
button_5.grid(column=2,row=3,padx=2,pady=2,sticky='e')

button_4 = tkinter.Button(giaodien,text="4",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('4'))
button_4.grid(column=3,row=3,padx=2,pady=2,sticky='e')

button_3 = tkinter.Button(giaodien,text="3",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('3'))
button_3.grid(column=1,row=4,padx=2,pady=2,sticky='e')

button_2 = tkinter.Button(giaodien,text="2",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('2'))
button_2.grid(column=2,row=4,padx=2,pady=2,sticky='e')

button_1 = tkinter.Button(giaodien,text="1",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('1'))
button_1.grid(column=3,row=4,padx=2,pady=2,sticky='e')

button_0 = tkinter.Button(giaodien,text="0",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('0'))
button_0.grid(column=1,row=5,padx=2,pady=2,sticky='e')

button_00 = tkinter.Button(giaodien,text="00",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('00'))
button_00.grid(column=2,row=5,padx=2,pady=2,sticky='e')

button_cham = tkinter.Button(giaodien,text=".",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('.'))
button_cham.grid(column=3,row=5,padx=2,pady=2,sticky='e')

button_cong = tkinter.Button(giaodien,text="+",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('+'))
button_cong.grid(column=4,row=2,padx=2,pady=2,sticky='e')

button_tru = tkinter.Button(giaodien,text="-",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('-'))
button_tru.grid(column=4,row=3,padx=2,pady=2,sticky='e')

button_nhan = tkinter.Button(giaodien,text="*",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('*'))
button_nhan.grid(column=4,row=4,padx=2,pady=2,sticky='e')

button_chia = tkinter.Button(giaodien,text="/",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('/'))
button_chia.grid(column=4,row=5,padx=2,pady=2,sticky='e')

button_result = tkinter.Button(giaodien,text="result",fg="black",bg="white",font="weight=bold",width=18,height=3,command=ketqua)
button_result.grid(columnspan=4,row=6,padx=2,pady=2,sticky='e')

button_phantram = tkinter.Button(giaodien,text="%",fg="black",bg="white",font="weight=bold",width=5,height=3,command=lambda:famexl('%'))
button_phantram.grid(column=4,row=6,padx=2,pady=2,sticky='e')


giaodien.mainloop()

