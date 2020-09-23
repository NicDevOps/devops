
# [ ] Write a program that reads a date from the command line as numbers (month  then day then year),
# if the date entered is in the past, a message saying "The date has passed" should be printed
# if the date is in the future the program should display the number of days remaining from today till that date,
# there should be an optional command line flag that displays the results in total number of seconds instead of days

# help message should look like:
'''
usage: day_counter.py [-h] [-s] month day year

positional arguments:
  month                Month as a number (1, 12)
  day                  Day as a number (1, 31) depending on the month
  year                 Year as a 4 digits number (2018)

optional arguments:
  -h, --help           show this help message and exit
  -s, --total_seconds  Show the time difference in total number of seconds
'''

import argparse
from math import fabs
from datetime import date, timedelta, datetime

parser = argparse.ArgumentParser()

parser.add_argument('month', type = int, help = 'Month as a number (1, 12)')

parser.add_argument('date', type = int, help = 'Day as a number (1, 31) depending on the month')

parser.add_argument('year', type = int, help = 'Year as a 4 digits number (2020)')

parser.add_argument('-s', '--total_seconds', action = 'store_true', help = 'Show the time difference in total number of seconds')

args = parser.parse_args()

present = date.today()

d_object = date(day = args.date, month = args.month, year = args.year)

future_date = d_object - present

def t_seconds(future_date):
    return int(fabs(future_date.total_seconds()))
    
def past_future(future_date):
    if future_date.total_seconds() > 0:
        print('There are {:d} seconds remaining from today'.format(t_seconds(future_date)))
    else:
        print('There are {:d} seconds past from today'.format(t_seconds(future_date)))
        
def main():
    if present > d_object:
        print('The date has passed')
    else:
        print('There are {:d} days remaining from today'.format(future_date.days))
        
    if args.total_seconds:
        past_future(future_date)

if __name__ == '__main__':
    main()