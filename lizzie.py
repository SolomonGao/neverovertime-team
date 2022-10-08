
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

the_filename = ""
the_filename2 = ""
the_folder = ""
# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(True, True)
root.geometry('700x500')

def select_file(button):
    filetypes = (
        ('databse files', '*.db3'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Select a file',
        initialdir='/',
        filetypes=filetypes)
    if filename != "":
        button['text']=filename

        global the_filename 
        global the_filename2
        if the_filename == "":
            the_filename = filename
        elif the_filename2 == "":
            the_filename2 = filename

def select_folder(button):
    folder_name = fd.askdirectory(
        title='Select a file',
        initialdir='/')
    if folder_name != "":
        button['text']=folder_name
        global the_folder
        the_folder = folder_name

def first_window():
    # open button
    open_button = ttk.Button(
        root,
        text='Open a File',
        command=lambda:select_file(open_button)
    )
    other_button = ttk.Button(
        root,
        text='Open a File',
        command=lambda:select_file(other_button)
    )

    button3 = ttk.Button(root, text="Next", command=second_window)
    
    l1 = ttk.Label(root, text="First File:", border= 7, borderwidth=20)
    l2 = ttk.Label(root, text="Second File:", border= 7, borderwidth=20)
    l3 = ttk.Label(root, text="     " )


    open_button.grid(row = 0, column = 1)
    other_button.grid(row = 1, column = 1)
    button3.grid(row=3, column=1)
    l1.grid(row = 0, column = 0)
    l3.grid(row = 2, column = 0)
    l2.grid(row = 1, column = 0)

def second_window():
    root.destroy()
    window2_main = tk.Tk()
    window2_main.title("Create new folder")
    window2_main.geometry('700x500')

    open_button = ttk.Button(
        window2_main,
        text='Select a folder',
        command=lambda:select_folder(open_button)
    )


    button3 = ttk.Button(window2_main, text="Create Database", command=lambda: third_window(window2_main))

    #entry = ttk.Entry(window2_main, width= 42)
    l1 = ttk.Label(window2_main, text="Choose a Location", border= 7, borderwidth=20)
    l2 = ttk.Label(window2_main, text='Filename: "new_database.db3"', border= 7, borderwidth=20)
    
    #entry.grid(row=2, column=1)
    open_button.grid(row = 1, column = 0)
    button3.grid(row=3, column=0)

    l1.grid(row=0, column=0)
    l2.grid(row = 2, column = 0)


def third_window(window2_main):
    window2_main.destroy()
    window3_main = tk.Tk()
    window3_main.title("Creating Database")
    window3_main.geometry('700x500')
    l1 = ttk.Label(window3_main, text="Database is being created", border= 7, borderwidth=20)
    l1.grid(row = 0, column = 0)

first_window()

#run the application
root.mainloop()