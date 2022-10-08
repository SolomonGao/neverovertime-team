# Import the required libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

 # Create an instance of tkinter frame or window
newWindow = Tk()
# Set the size of the window
newWindow.geometry("700x350")

def get_data():
   folder_name = entry.get()
   # print(folder_name)
   return folder_name

entry = Entry(newWindow, width= 42)
entry.pack()

def create_subfolder(text):
   source_path = filedialog.askdirectory(title='Select the Parent Directory')
   path = os.path.join(source_path, get_data())
   os.makedirs(path)
   print(path)
   
def clear_data():
   entry.delete(0, END) 

def folder_created_message():
   label.Label(newWindow, text="New Folder was created", bg="white")

Label(
   newWindow,
   text="Name New Folder", 
   padx=10, 
   pady=5,
   ).pack()



button2 = Button(newWindow,text="Select New Folder Location", command=lambda: create_subfolder(get_data())).pack()

button3 = Button(newWindow, text="Clear", command=clear_data ).pack()


# def onClick(): 
#    messagebox.showinfo("Title goes here","Message goes here")


newWindow.mainloop()







def get_data():
       folder_name = entry.get()
       # print(folder_name)
       return folder_name

def create_subfolder(text):
       source_path = filedialog.askdirectory(title='Select the Parent Directory')
       path = os.path.join(source_path, get_data())
       os.makedirs(path)
       print(path)

def clear_data():
       entry.delete(0, END) 

def folder_created_message():
   label.Label(window2_main, text="New Folder was created", bg="white")



def openWindow2():
    root.destroy()
    window2_main = Tk()
    Label(window2_main, text="New").pack()
    # Import the required libraries
    # Import the required libraries

     # Create an instance of tkinter frame or window

    entry = Entry(window2_main, width= 42)
    entry.pack()
    
    Label(
       window2_main,
       text="Name New Folder", 
       padx=10, 
       pady=5,
       ).pack()

    button2 = Button(window2_main,text="Select New Folder Location", command=lambda: create_subfolder(get_data())).pack()

    button3 = Button(window2_main, text="Clear", command=clear_data ).pack()

    window2_main.mainloop(