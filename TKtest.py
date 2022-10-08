from cProfile import label
import tkinter as tk
from tkinter import RIGHT, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
import os


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
        ('databse files', '*.db3') 
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
        ('databse files', '*.db3')
    )
    file_path2 = fd.askopenfilename(
    title='Select a file',
    initialdir='/',
    filetypes=filetypes) 
    button['text'] = file_path2
    return file_path2

def create_subfolder(folder_name):
       source_path = fd.askdirectory(title='Select the Parent Directory')
       path = os.path.join(source_path, folder_name)
       os.makedirs(path)
       return path 

def create_file(entry1):
    Input = entry1.get()
    FileName = str(Input + ".db3")
    TextFile = open(FileName,"w")

def create_file_folder(file, folder):
    file = create_file(entry1)
    folder = create_subfolder(folder_name)


def create_file(folder_name):
    Input = entry1.get()
    file_name = str(Input + ".db3")
    TextFile = open(FileName,"w")

def clear_data(entry):
       entry.delete(0, END) 

def folder_created_message():
    top = Toplevel()
    top.geometry("250x250")
    top.title("Child Window")
    Label(top, text= "You made it Joseph!!", font=('Mistral 18 bold')).pack()

def get_data(entry):
       folder_name = entry.get()
       return folder_name

def openWindow2():
    root.destroy()
    window2_main = Tk()
    window2_main.geometry("700x500")
    window2_main.title("Create new folder")
    Label(window2_main, text="Creating File and Folder").grid(row= 1, column= 2)

    entry = Entry(window2_main, width= 42) #name folder
    entry.grid(row=2, column=3)
    Label(window2_main,text="Name New Folder", padx=10, pady=5,).grid(row=2, column=2)

    entry1 = Entry(window2_main, width=42) #name file
    entry1.grid(row=3, column=3)
    Label(window2_main,text="Name New File", padx=10, pady=5,).grid(row=3, column=2)
  
    button2 = Button(window2_main,text="Select New Folder Location", command = lambda: create_subfolder(get_data(entry))).grid(row=2, column=4)

    # button3 = Button(window2_main, text="Clear", command= older_created_message(entry1, entry)).grid(row=3, column=4)
    
    button1 = Button(window2_main,text="Press to create db3 file", command= create_file_folder(entry1, entry)).grid(row=3, column=4)

    window2_main.mainloop()


file_path1 = ''
button1 = Button(root, text="Select file", command=lambda:file_path1 == selectFile1(button1))
button1.grid(row = 0, column = 1)

file_path2 = ''
button2 = Button(root, text="Select file", command=lambda:file_path2 == selectFile1(button1))
button2.grid(row = 2, column = 1)

button3 = Button(root, text="Next", command=openWindow2)
button3.grid(row=3, column=1)

# Set the background color
root.configure(bg='#f0f0f0')

# run the application
root.mainloop()
