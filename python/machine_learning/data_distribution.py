
# Data sets

# To create big data sets for testing, we use the Python module NumPy, 
# which comes with a number of methods to create random data sets, of any size.

# Create an array containing 250 random floats between 0 and 5:



import os
from time import sleep
import numpy

def clear():
    os.system( 'clear' )
    sleep(1)

# x = numpy.random.uniform(0.0, 5.0, 250)
# clear()
# print(x)

# Histogram
# To visualize the data set we can draw a histogram with the data we collected.

# We will use the Python module Matplotlib to draw a histogram:

import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)
clear()
plt.hist(x, 5)
plt.show()