"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


def create_calender(**cal_args):
    # add arguments to memory
    items = cal_args.items()

    # get current year from datetime module
    current_date = datetime.now()

    # loop through the given arguments tuple
    for item in items:
        items_length = len(items)
        print(items_length)

        if (items_length == 0):
            # if a user gives no inputs, print calender for current month
            print(calendar.month(current_date.year, current_date.month))
            return
        elif (items_length == 1):
            # if user gives one input, assume its a month value
            print(calendar.month(current_date.year, item[1]))
            return
        elif (items_length == 2):
            # if a user gives two inputs, use both to create calendar
            month, year = items
            print(calendar.month(year[1], month[1]))
            return
        else:
            print("Follow this format: create_calender(month, [year])")
            return


create_calender()  # should return current month and year
create_calender(month=1)  # should return january
create_calender(month=5, year=1991)  # should return may 1991
# should return the `else` statement
create_calender(month=5, year=1991, third=0)
