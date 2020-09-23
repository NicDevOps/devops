import argparse
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

print(present)

if present > d_object:
    print('The date has passed')
else:
    print('There are {:d} days remaining from today'.format(future_date.days))

if args.total_seconds:
    print(int(future_date.total_seconds()))
    
