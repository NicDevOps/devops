import numpy as np
import time

# Way to normalize
def image2vector(image):
    A = image.reshape(image.shape[0]*image.shape[1]*image.shape[2], 1)
    return A

# image = np.array([
#     [[11, 12], [13, 14], [15, 16]],
#     [[21, 22], [23, 24], [25, 26]],
#     [[31 , 32], [33, 34], [35, 36]]
# ])

# print(image2vector(image))
# print(image.shape)
# print(image2vector(image).shape)

# Another way to normalize
def normalizeRow(x):
    x_norm = np.linalg.norm(x, ord = 2, axis = 1, keepdims = True)
    print(x.shape)
    print(x_norm.shape)
    print(x)
    print(x_norm)
    x = x/x_norm
    return x

# x = np.array([
#     [0, 3, 4],
#     [1, 6, 4]
#     ])
# This can be call broadcasting
# print(normalizeRow(x))


# Normalize function use when utilise 2 or more classes
def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis = 1, keepdims = True)
    s = x_exp / x_sum
    print(x_exp.shape)
    print(x_exp)
    print(x_sum.shape)
    print(x_sum)
    print(s.shape)
    return s

# x = np.array([
#     [7, 4, 5, 1, 0],
#     [4, 9, 1, 0, 5]
#     ])

# print(softmax(x))



