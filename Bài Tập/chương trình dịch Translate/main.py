import tkinter
from tkinter.ttk import Combobox
from tkinter import Checkbutton, Radiobutton, IntVar, Spinbox
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import googletrans
from googletrans import Translator
import json

Languages = googletrans.LANGUAGES

def clear():
    text.delete("1.0","end-1c")
    text1.delete("1.0","end-1c")

def translate():
        translate = Translator()
        Input_text = text.get("1.0", "end-1c")
        src = combobox.get()
        dest = combobox1.get()
        for key,value in Languages.items():
            if src == value:
                _src = key
        for key,value in Languages.items():
            if dest == value:
                _dest = key
        result = translate.translate(Input_text,src=_src,dest=_dest)
        text1.delete("1.0","end-1c")
        text1.insert("end", result.text)
    # except:
    #     text1.insert("end", "hi bạn ơi, nhập từ để dịch đi")
#Giao dien


giaodien = tkinter.Tk()
giaodien.title("Translate")
giaodien.geometry('550x350')

list_language = []

for key in Languages.keys():
    value = str(Languages[key]).replace("","")
    list_language.append(value)

# print(googletrans.LANGUAGES)

# print(json.dumps(googletrans.LANGUAGES, indent=4))

#Combobox
combobox = Combobox(giaodien)
combobox.grid(column=1,row=2,padx=10,pady=10)
combobox.configure(values=list_language)
combobox.set("vietnamese")
combobox["state"] = 'readonly'

#Combobox
combobox1 = Combobox(giaodien)
combobox1.grid(column=2,row=2,padx=10,pady=10)
combobox1.configure(values=list_language)
combobox1.set("english")
combobox1["state"] = 'readonly'

#Textbox
dulieu1 = tkinter.StringVar()
text = tk.Text(giaodien, width=30, height=15)
text.grid(column=1,row=3,padx=10,pady=10)
#Textbox

text1 = tk.Text(giaodien, width=30, height=15)
text1.grid(column=2,row=3,padx=10,pady=10)

#Button
clear_button = tkinter.Button(giaodien,text="Translate",fg="black",bg="white",command=translate)
clear_button.grid(column=1,row=4,padx=10,pady=10)
#Button
button = tkinter.Button(giaodien,text="Clear",fg="black",bg="white",command=clear)
button.grid(column=2,row=4,padx=10,pady=10)

giaodien.mainloop()