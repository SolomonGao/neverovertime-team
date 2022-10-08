from cProfile import label
import tkinter as tk
from tkinter import RIGHT, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from tkinter import *


# create the root window
root = tk.Tk()
root.title('SQLite files merge') # This is the title
root.resizable(True, True)
root.geometry('700x500') # This is the size of the window

# Create a label widget
l1 = Label(root, text="First File:", border= 7, borderwidth=20, bg="#f0f0f0")
l2 = Label(root, text="Second File:", border= 7, borderwidth=20, bg="#f0f0f0")
l3 = Label(root, text="     ", bg="#f0f0f0" )

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0)
l3.grid(row = 1, column = 0)
l2.grid(row = 2, column = 0)


def selectFile1(button):
    '''Select a file'''
    
    global file_path1
    filetypes = (
        ('databse files', '*.sql'), 
    )
    file_path1 = fd.askopenfilename(
    title='Select a file',
    initialdir='/',
    filetypes=filetypes) 
    button['text'] = file_path1
    return file_path1

def selectFile2(button):
    '''Select a file'''
    
    global file_path2
    filetypes = (
        ('databse files', '*.sql'), 
    )
    file_path2 = fd.askopenfilename(
    title='Select a file',
    initialdir='/',
    filetypes=filetypes) 
    button['text'] = file_path2
    return file_path2

# def displayFilename(button, fileName):
#     '''Replace the button with the file path'''
#     button['text'] = fileName

def openWindow():
    new = Toplevel()
    new.geometry("500x500")
    new.title("Folder location")
    myLabel = Label(new, text="Add some thing")
    myLabel.grid(row=0, column=0)

def openWindow2():
    root.destroy()
    window2_main = Tk()
    Label(window2_main, text="Bye Bye").pack()
    window2_main.mainloop()


# create button for user to click and select files
file_path1 = ''
button1 = Button(root, text="Select file", command=lambda:file_path1 == selectFile1(button1))
button1.grid(row = 0, column = 1)

file_path2 = ''
button2 = Button(root, text="Select file", command=lambda:file_path2 == selectFile2(button2))
button2.grid(row = 2, column = 1)

Label(root, text=file_path1).grid(row=3, column=5)

button3 = Button(root, text="Next", command=openWindow2)
# button3 = Button(root, text="Next", command=openWindow)
button3.grid(row=3, column=1)

# Set the background color
root.configure(bg='#f0f0f0')

# run the application
root.mainloop()
