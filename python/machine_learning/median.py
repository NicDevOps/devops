
# The median value is the value in the middle, after you have sorted all the values:
# 
#                              M
#  77, 78, 85, 86, 86, 86, --->87<---, 87, 88, 94, 99, 103, 111

# Use the NumPy median() method to find the middle value:

import numpy
import os
from time import sleep

def clear():
    os.system( 'clear' )
    sleep(1)


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

clear()
print(x)



# If there are two numbers in the middle, divide the sum of those numbers by two.


speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)


print(x)