# Contain functions for the application
import datetime
def gettime():
    time = datetime.datetime.now().time()
    date = datetime.datetime.now().date()
    print('current time and date is:', time, date)
    print()

gettime()