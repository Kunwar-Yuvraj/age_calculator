"""

Originally created by =>  K U N W A R  Y U V R A J 
Owner's site => https://KunwarYuvraj.herokuapp.com

*** If you are copying this, Please understand logic first, Then you can customize it ;) ***

## If there is any error or advice regarding this code, consider contacting me ! ##

"""

import datetime
def cal():
    dob = datetime.datetime(day=int(input("DAY: ")), month=int(input("MONTH: ")), year=int(input("YEAR: ")))
    #data
    weekdayname = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    currtime = datetime.datetime.now() # current_time is the time when program is running
    days = (currtime.date() - dob.date()).days
    weeks = days // 4
    extra_days_after_weeks = days % 4
    months= weeks // 4
    extra_days_after_months= weeks%4
    years = currtime.year - dob.year
    hours = (days * 24) + currtime.time().hour
    print("\n\n You were born on:  ",weekdayname[dob.weekday()])
    print("Your age is now:\n -->", hours,"hours\n -->", days,"days\n -->", weeks,"weeks", end=" ")
    if extra_days_after_weeks !=0:
        print("+", extra_days_after_weeks,"day/s", end=" ")

    print("\n-->", months, "months", end=" " )

    if extra_days_after_months != 0:
        print("+", extra_days_after_months, "day/s", end=" ")

    print("\n-->", years, "years\n\n")

print("Welcome to DOB calci")
print("Enter your DOB")

for i in range(0,10):
    cal()
