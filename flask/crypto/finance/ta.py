from numpy import genfromtxt
import talib

# close = numpy.random.random(100)

# print(close)


my_data = genfromtxt('data/15min.csv', delimiter=',')

close = my_data[:,4]

# print(close)

# output = talib.SMA(close, timeperiod=10)

# # print(output)

rsi = talib.RSI(close)

print(rsi)