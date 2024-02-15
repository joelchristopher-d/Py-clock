from tkinter import *
# from tkinter.ttk import *


from time import *


root= Tk()
root.title("JOEL CLOCK")
root.geometry("500x500")
photo=PhotoImage(file="D:\\py\\fire_115156.png")
root.iconphoto(False,photo)


def time():
    stri=strftime("%H:%M %S")
    label.config(text=stri)
    label.after(1000,time)
    


label=Label(root,font=("Orloj",50),background="black",foreground="green",width=60,height=15)
label.pack(anchor="center")
time()
root.mainloop()