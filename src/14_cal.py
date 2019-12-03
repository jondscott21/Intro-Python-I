"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

def print_calender(*args):
  year = str(datetime.today())[0:4]
  month = str(datetime.today())[5:7]
  if len(args) == 0:
    try:
      print(calendar.TextCalendar().formatmonth(int(year), int(month)))
    except:
      print('could not find current month and year')
  elif len(args) == 1:
    try:
      print(calendar.TextCalendar().formatmonth(int(year), int(args[0])))
    except:
      print('please enter a valid month')
  elif len(args) == 2:
    try:
      print(calendar.TextCalendar().formatmonth(int(args[1]), int(args[0])))
    except:
      print('please enter a valid month followed by a valid 4 digit year')
  else:
    print('expects 0-2 args: month, then year')
print_calender()