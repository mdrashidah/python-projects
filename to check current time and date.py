import time
tim_e = time.localtime()
tim__e = time.strftime("\t%d/%B/%Y \n\t %I:%M %p \n\t %A", tim_e)
print("  The current time and date is:\n",tim__e)





















#The strftime() function in Python lets you turn the date and time into a string that looks the way you want. For example, you can make it show just the year, month, and day, or the full date and time, depending on what you need. it’s like telling python, “show the date or something ling related to the time and date”

#where %d is day, %B is full month name, %Y is year, %I is hour in 12-hour format, %M is minutes, and %p is AM/PM
#you can also use %H for 24-hour format instead of %I and %S for seconds and %B for full month name , we can also use %m for month number (01-12) and %a for abbreviated weekday name (e.g., Mon, Tue, etc.) and %A for full weekday name (e.g., Monday, Tuesday, etc.)