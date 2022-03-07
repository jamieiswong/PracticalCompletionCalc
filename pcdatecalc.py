import datetime as dt

print("This program calculates the PC date using commencement date and program duration.")

# User inputs
year = int(input("Enter a year (YYYY): "))
month = int(input("Enter a month (MM): "))
day = int(input("Enter a day (DD): "))
duration = int(input("Insert number of days: "))

start_date = dt.date(year, month, day)
days_elapsed = 0

# Planned - Turn this into a file
holiday_list = [
    dt.date(2022, 1, 1), 
    dt.date(2022, 1, 3), 
    dt.date(2022, 1, 26), 
    dt.date(2022, 4, 15), 
    dt.date(2022, 4, 16), 
    dt.date(2022, 4, 17), 
    dt.date(2022, 4, 18), 
    dt.date(2022, 4, 25), 
    dt.date(2022, 5, 2), 
    dt.date(2022, 10, 3), 
    dt.date(2022, 12, 25), 
    dt.date(2022, 12, 26), 
    dt.date(2022, 12, 27)
    ]

# Planned - Turn this into a function
while days_elapsed < duration:
    new_date = start_date + dt.timedelta(days=1)
    start_date = new_date
    if new_date.weekday() > 4 or new_date in holiday_list:
        # if weekend or public holiday
        continue
    else:
        days_elapsed +=1

print(start_date)   # This is the 'end_date' after looping all the dates.
