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

def openWindow():
    new = Toplevel()
    new.geometry("500x500")
    new.title("Folder location")
    myLabel = Label(new, text="Add some thing")
    myLabel.grid(row=0, column=0)

def create_subfolder(folder_name):
       source_path = fd.askdirectory(title='Select the Parent Directory')
       path = os.path.join(source_path, folder_name)
       os.makedirs(path)
       return folder_name

def folder_created_message():
#    label.Label(window2_main, text="New Folder was created", bg="white")
    # window2_main.geometry("500x500")
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
    Label(window2_main, text="New").pack()

    folder_name = Entry(window2_main, width= 42)
    folder_name.pack()
    
    Label(
       window2_main,
       text="Name New Folder", 
       padx=10, 
       pady=5,
       ).pack()

    def create_file():
        input= entry1.get()
        FileName = str(input + ".db3")
        TextFile = open(FileName,"w")

    def Export_File():
        dir_name = fd.askdirectory() # asks user to choose a directory
        os.chdir(dir_name) # changes your current directory

    def combined():
        create_file()
        Export_File()

    button2 = Button(window2_main,text="Select New Folder Location", command=lambda: create_subfolder(get_data(folder_name))).pack()

    button3 = Button(window2_main, text="Clear", command=folder_created_message).pack()
    
    entry1 = Entry(window2_main)
    entry1.pack()
    button1 = Button(window2_main,text="Press to create db3 file", command=combined)
    button1.pack()

# create button for user to click and select files
file_path1 = ''
button1 = Button(root, text="Select file", command=lambda:file_path1 == selectFile1(button1))
button1.grid(row = 0, column = 1)

file_path2 = ''
button2 = Button(root, text="Select file", command=lambda:file_path2 == selectFile2(button2))
button2.grid(row = 2, column = 1)

button3 = Button(root, text="Next", command=openWindow2)
# button3 = Button(root, text="Next", command=openWindow)
button3.grid(row=3, column=1)

# Set the background color
root.configure(bg='#f0f0f0')

# run the application
root.mainloop()
