import tkinter
from tkinter import *
window=tkinter.Tk()
window.title("Miles to Km Converter")
window.geometry("250x100")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)
window.resizable()
text1=Entry()
text1.config(width=10)
text1.grid(column=2,row=2)


label1=Label(text="is equal to")
label1.grid(column=1,row=3)
label1.config(padx=20)
label2=Label(text="0")
label2.grid(column=2,row=3)
label3=Label(text="KM")
label3.grid(column=3,row=3)
label4=Label(text="Miles")
label4.config(padx=10)
label4.grid(column=3,row=2)
def change_label():
    inp=int(text1.get())
    inp=inp*1.60394
    label2["text"]=inp
button1=tkinter.Button(text="Calculate",command=change_label)
button1.grid(column=2,row=4)








window.mainloop()
