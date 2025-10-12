from datetime import datetime,date

now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

print(date.today())  # use date object and today () to get current date
myday=date(2023, 12, 25)  # create date object
print('specific date:', myday)  # specific date

print ("by default",now)
print("formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))  # formatted date
## strftime -- string format means convert date object to string



#parse
date_string = "2023-10-15"
date_object = datetime.strptime(date_string, "%Y-%m-%d")
print(date_object)

