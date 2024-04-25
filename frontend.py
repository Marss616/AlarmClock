import os
import tkinter as tk
from tkinter import ttk
import time

def store_trigger_time(trigger_time):
    print(trigger_time)
    print(type(trigger_time))

def gettime():
    """Return the current time in HH:MM format."""
    return time.strftime('%H:%M')

def refresh_time():
    """Refresh the displayed time."""
    current_time_label.config(text=("The current time is: " + gettime()))
    root.after(1000, refresh_time)

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# Title and current time display
ttk.Label(frm, text="Time Trigger Version 1.0").grid(column=0, row=0, columnspan=2)
current_time_label = ttk.Label(frm, text="The current time is: " + gettime())
current_time_label.grid(column=0, row=1)

# Time entry
ttk.Label(frm, text="Set Time to Trigger, HH:MM").grid(column=0, row=2)
entry_widget = ttk.Entry(frm)
entry_widget.grid(column=1, row=2)

# Buttons for operations
ttk.Button(frm, text="Update Current Time", command=refresh_time).grid(column=0, row=3)
ttk.Button(frm, text="Submit Input", command=lambda: store_trigger_time(entry_widget.get())).grid(column=0, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=5)

root.mainloop()
