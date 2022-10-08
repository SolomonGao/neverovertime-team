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
root.geometry('500x500') # This is the size of the window

# Create a label widget
l1 = Label(root, text="First File:", border= 7, borderwidth=20, bg="#f0f0f0")
l2 = Label(root, text="Second File:", border= 7, borderwidth=20, bg="#f0f0f0")
l3 = Label(root, text="     ", bg="#f0f0f0" )

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0)
l3.grid(row = 1, column = 0)
l2.grid(row = 2, column = 0)

def selectFile():
    '''Select a file'''
    
    global fileName
    filetypes = (
        ('databse files', '*.sql'),
        
    )
    fileName = fd.askopenfilename(
    title='Select a file',
    initialdir='/test/EpilogJobManagement.db3-second.db3',
    filetypes=filetypes)    
    return fileName

def displayFilename(button, fileName):
    '''Replace the button with the file path'''
    button['text'] = fileName

# create button for user to click and select files
button1 = Button(root, text="Select file", state=DISABLED)
fileName = selectFile()
displayFilename(button1, fileName)

button2 = Button(root, text="Select file", state=DISABLED)
fileName = selectFile()
displayFilename(button2, fileName)

button3 = Button(root,
             text ="Next",
             command = openNewWindow)

# button3 = Button(root, text="Merge" )
# button4 = Button(root, text = "   ")
button1.grid(row = 0, column = 1)
# button4.grid(row=1, column = 1)
button2.grid(row = 2, column = 1)
button3.grid(row=4, column=1)

# Set the background color
root.configure(bg='#f0f0f0')

def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Create New Folder")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="Create New Folder").pack()



# run the application
root.mainloop()



# # This will import all the widgets
# # and modules which are available in
# # tkinter and ttk module
# from tkinter import *
# from tkinter.ttk import *
 
# # creates a Tk() object
# master = Tk()
 
# # sets the geometry of main
# # root window
# master.geometry("200x200")
 
 
# # function to open a new window
# # on a button click
# def openNewWindow():
     
#     # Toplevel object which will
#     # be treated as a new window
#     newWindow = Toplevel(master)
 
#     # sets the title of the
#     # Toplevel widget
#     newWindow.title("Create New Folder")
 
#     # sets the geometry of toplevel
#     newWindow.geometry("200x200")
 
#     # A Label widget to show in toplevel
#     Label(newWindow,
#           text ="Yo").pack()
 
 
# label = Label(master,
#               text ="This is the main window")
 
# label.pack(pady = 10)
 
# # a button widget which will open a
# # new window on button click
# btn = Button(master,
#              text ="Next",
#              command = openNewWindow)
# btn.pack(pady = 10)
 
# # mainloop, runs infinitely
# mainloop()