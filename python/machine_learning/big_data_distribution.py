# Big data distribution

# Create an array with 100000 random numbers, 
# and display them using a histogram with 100 bars:


import matplotlib.pyplot as plt
import os
from time import sleep
import numpy

def clear():
    os.system( 'clear' )
    sleep(1)

x = numpy.random.uniform(0.0, 5.0, 100000)
clear()
plt.hist(x, 100)
plt.show()