# Mean value

# Use the NumPy mean() method to find the average speed:

import numpy
import os
from time import sleep

def clear():
    os.system( 'clear' )
    sleep(1)

# print(np.__version__)

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

clear()
print('The mean value of speed is:', x)

print()

