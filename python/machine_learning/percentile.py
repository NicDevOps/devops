#  Percentile

# Percentiles are used in statistics to give you 
# a number that describes the value that a given percent of the values are lower than.

# What is the 75. percentile? 
# The answer is 43, meaning that 75% of the people are 43 or younger.

import numpy
import os
from time import sleep

def clear():
    os.system( 'clear' )
    sleep(1)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)
clear()
print('The percentile 75 from ages is:', x)
