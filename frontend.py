# Contain GUI for the application

import os 
import sys
from backend import *
from tkinter import *
from tkinter import ttk

def restart_program():
    os.execv(sys.executable, ['python'] + sys.argv) # MV this function to backend.py

# Replace root.destroy with restart_program in the button's command


gettime()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Jack Alarm Clock").grid(column=0, row=0)
ttk.Label(frm, text=gettime()).grid(column=0, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Update Current time", command=restart_program).grid(column=1, row=1)
# Complete the front end for basic alarm clock with output of the time and date from the backend
root.mainloop()


