
# The Mode value is the value that appears the most number of times:

# Use the SciPy mode() method to find the number that appears the most:

from scipy import stats
import os
from time import sleep

def clear():
    os.system( 'clear' )
    sleep(1)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)
clear()
print(x)