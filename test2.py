from tkinter import *
from tkinter import ttk
from tkinter import filedialog
gui = Tk()
gui.geometry("100x100")

def getFolderPath():
    filedialog.askdirectory()

btnFind = ttk.Button(gui, text="Open Folder",command=getFolderPath)
btnFind.grid(row=0,column=2)

gui.mainloop()