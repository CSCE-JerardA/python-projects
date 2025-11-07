

from tkinter import *

def sel():
    selection = "You selected the option " + str(var.get())
    label.config(text=selection)
root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value="A",command=sel)
R1.select()
R1.pack(anchor = W)
R2 = Radiobutton(root, text="Option 2", variable=var, value="B", command=sel)
R2.deselect()
R2.pack(anchor = W)
R3 = Radiobutton(root, text="Option 3", variable=var, value="C", command=sel)
R3.deselect()
R3.pack(anchor = W)
label = Label(root)
label.pack
label.mainloop()

