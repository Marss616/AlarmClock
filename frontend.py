# Contain GUI for the application

from backend import *
from tkinter import *
from tkinter import ttk



# Replace root.destroy with restart_program in the button's command


gettime()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Time Trigger V.0.1").grid(column=0, row=0)
ttk.Label(frm, text="The current time is:").grid(column=0, row=1)
ttk.Label(frm, text="Time to Trigger: SS/MM/HH").grid(column=0, row=3)

# collumn 0

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Label(frm, text=gettime()).grid(column=1, row=1)
ttk.Entry(frm).grid(column=1, row=3)
ttk.Button(frm, text="Update Current Time:", command=restart_program).grid(column=1, row=2)
ttk.Button(frm, text="Submit Input", command=store_trigger_time).grid(column=1, row=4)
# collumn 1


# Complete the front end for basic alarm clock with output of the time and date from the backend
root.mainloop()


