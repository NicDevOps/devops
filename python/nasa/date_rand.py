from datetime import date
from random import randint


early = date(day = 16, month = 6, year = 1995)
today = date.today()

d = randint(1, 31)

m = randint(1, 12)

y = randint(1995, today.year)
        
random_date = date(month = m, day = d, year = y)

print(random_date)