
# Normal data distribution (Bell curved)

# Array where the values are concentrated around a given value.

# Also called Gaussian data distribution, by the mathematician Carl Friedrich Gauss.


import numpy
import matplotlib.pyplot as plt
import os
from time import sleep



def clear():
    os.system( 'clear' )
    sleep(1)

x = numpy.random.normal(5.0, 1.0, 100000)
clear()
plt.hist(x, 100)
plt.show()

# We use the array from the numpy.random.normal() method, with 100000 values,  
# to draw a histogram with 100 bars.

# We specify that the mean value is 5.0, and the standard deviation is 1.0.

# Meaning that the values should be concentrated around 5.0, 
# and rarely further away than 1.0 from the mean.

# And as you can see from the histogram, most values are 
# between 4.0 and 6.0, with a top at approximately 5.0.