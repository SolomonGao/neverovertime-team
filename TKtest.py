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
button3 = Button(root, text="Merge" )
# button4 = Button(root, text = "   ")
button1.grid(row = 0, column = 1)
# button4.grid(row=1, column = 1)
button2.grid(row = 2, column = 1)
button3.grid(row=4, column=1)

# Set the background color
root.configure(bg='#f0f0f0')



# run the application
root.mainloop()
