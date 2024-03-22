# Contain functions for the application
import datetime
import os 
import sys
from backend import *
from tkinter import *
from tkinter import ttk



def gettime():
    # Get the current time and date
    current_time = datetime.datetime.now().time()
    current_date = datetime.datetime.now().date()
    
    # Convert time and date to strings and format them
    time_str = current_time.strftime('%H:%M:%S')  # Format time as HH:MM:SS
    date_str = str(current_date)  # Date is already in a nice format (YYYY-MM-DD)
    
    # Return the combined time and date string
    return f'{time_str}, {date_str}'

def restart_program():
    os.execv(sys.executable, ['python'] + sys.argv) # MV this function to backend.py

def store_trigger_time():
    # Get the time to trigger from the user
    trigger_time = input('Enter the time to trigger (HH:MM:SS): ')
    
    # Store the trigger time in a file
    with open('trigger_time.txt', 'a') as file:
        file.write(trigger_time)
