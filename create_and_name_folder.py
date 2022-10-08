# Import the required libraries
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

 # Create an instance of tkinter frame or window
root = Tk()
# Set the size of the window
root.geometry("700x350")

def get_data():
   folder_name = entry.get()
   print(folder_name)
   return folder_name

entry = Entry(root, width= 42)
entry.pack()

def create_subfolder(text):
   source_path = filedialog.askdirectory(title='Select the Parent Directory')
   path = os.path.join(source_path, get_data())
   os.makedirs(path)
   print(path)
   
def clear_data():
   entry.delete(0, END) 

def folder_created_message():
   label.Label(root, text="New Folder was created", bg="white")

Label(
   root,
   text="Name New Folder", 
   padx=10, 
   pady=5,
   ).pack()


folder = ""


button2 = Button(root,text="Select New Folder Location", command=lambda: folder == create_subfolder(text=get_data())).pack()

button3 = Button(root, text="Clear", command=clear_data ).pack()


# def onClick(): 
#    messagebox.showinfo("Title goes here","Message goes here")


root.mainloop()


