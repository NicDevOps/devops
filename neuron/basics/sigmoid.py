import math
import numpy as np

def basic_sigmoid(x):
    s = 1/(1+math.exp(-x))
    return s

# x = 1
# print(basic_sigmoid(x))


# With numpy

def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

def sigmoid_derivative(x):
    s = sigmoid(x)
    ds = s * (1 - s)
    return ds

# x = np.array([1, 2, 3])
# print(sigmoid(x))
# print(sigmoid_derivative(x))

# mathplolib

# values = plt.linspace(-10, 10, 100)
# plt.plot(values, sigmoid(values), 'r')
# plt.plot(values, sigmoid_derivative(values), 'b')
# plt.grid()
# plt.show