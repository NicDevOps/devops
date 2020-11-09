
# Standard Deviation

# Standard deviation is a number that describes how spread out the values are.

# Use the NumPy std() method to find the standard deviation:

import numpy
import os
from time import sleep

def clear():
    os.system( 'clear' )
    sleep(1)

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

clear()
print('The standard deviation is:', x)

print()

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print('The standard deviation is:', x)

print()

# Variance

# Variance is another number that indicates how spread out the values are. 

# Use the NumPy var() method to find the variance:

import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print('The variance is:', x)

# 1. Find the mean:

# (32+111+138+28+59+77+97) / 7 = 77.4

# 2. For each value: find the difference from the mean:

#  32 - 77.4 = -45.4
# 111 - 77.4 =  33.6
# 138 - 77.4 =  60.6
#  28 - 77.4 = -49.4
#  59 - 77.4 = -18.4
#  77 - 77.4 = - 0.4
#  97 - 77.4 =  19.6

# 3. For each difference: find the square value:

# (-45.4)**2 = 2061.16
#  (33.6)**2 = 1128.96
#  (60.6)**2 = 3672.36
# (-49.4)**2 = 2440.36
# (-18.4)**2 =  338.56
# (- 0.4)**2 =    0.16
#  (19.6)**2 =  384.16
# 4. The variance is the average number of these squared differences:

# (2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2

# Standard Deviation
# As we have learned, the formula to find the standard deviation is 
# the square root of the variance:

# √1432.25 = 37.85

# Use the NumPy std() method to find the standard deviation:
print()

speed = [32,111,138,28,59,77,97]

x = numpy.std(speed)

print('The standard deviation is:', x)

