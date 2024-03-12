# Contain GUI for the application

from backend import *

from tkinter import *
from tkinter import ttk

gettime()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Label(frm, text="").grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# Complete the front end for basic alarm clock with output of the time and date from the backend
root.mainloop()


