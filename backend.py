# Contain functions for the application
import datetime
def gettime():
    # Get the current time and date
    current_time = datetime.datetime.now().time()
    current_date = datetime.datetime.now().date()
    
    # Convert time and date to strings and format them
    time_str = current_time.strftime('%H:%M:%S')  # Format time as HH:MM:SS
    date_str = str(current_date)  # Date is already in a nice format (YYYY-MM-DD)
    
    # Return the combined time and date string
    return f'current time and date is: {time_str}, {date_str}'
