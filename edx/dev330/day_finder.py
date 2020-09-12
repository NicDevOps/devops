
# [ ] Write a program that reads a date (month, day, year) as command-line arguments in order
# then prints the day of the week for that date.
# If an optional flag (-c or --complete) is specified, the program should print the full date (not only the day of the week).

# The help message should look like:
'''
usage: day_finder.py [-h] [-c] month day year

positional arguments:
  month           Month as a number (1, 12)
  day             Day as a number (1, 31) depending on the month
  year            Year as a 4 digits number (2018)

optional arguments:
  -h, --help      show this help message and exit
  -c, --complete  Show complete formatted date
'''

# HINT: Use a date object with strftime

import argparse
from datetime import date

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('month', type = int, help = 'Month as a number (1, 12)')

parser.add_argument('date', type = int, help = 'Day as a number (1, 31) depending on the month')

parser.add_argument('year', type = int, help = 'Year as a 4 digits number (2020)')

# Add optional argument
parser.add_argument('-c', '--complete', action = 'store_true', help = 'Show complete formatted date')

# Parse command-line arguments
args = parser.parse_args()

# define functions working with strftime()
def weekday(some_date):
    return some_date.strftime('The day of the week is: %A')

def complete_date(some_date):
    return some_date.strftime('complete formatted date is: %d/%b/%Y')

# date objet from arguments
d_object = date(day = args.date, month = args.month, year = args.year)

# Display the day of the week
day = weekday(d_object)
comp_date = complete_date(d_object)

print(day)

if args.complete:
    print(comp_date)
