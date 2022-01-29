import numpy as np
import time


# Comparison between Vectorized and non-Vectorized 

x1 = np.random.randint(low=11, high=99, size=10000)
x2 = np.random.randint(low=11, high=99, size=10000)

# 1st example :

# tic = time.time()
# dot = 0
# for i in range(len(x1)):
#     dot += x1[i] * x2[i]
# toc = time.time()
# print("computational time = ", 1000 *(toc - tic))

# tic = time.time()
# dot = np.dot(x1, x2)
# toc = time.time()
# print("computational time = ", 1000 *(toc - tic))

# 2nd example :

# tic = time.time()
# outer = np.zeros((len(x1), len(x2)))
# for i in range(len(x1)):
#     for j in range(len(x2)):
#         outer[i, j] = x1[i] * x2[j]
# toc = time.time()
# print("computational time = ", 1000 *(toc - tic))

# tic = time.time()
# dot = np.dot(x1, x2)
# toc = time.time()
# print("computational time = ", 1000 *(toc - tic))

# 3rd example:

tic = time.time()
mul = np.zeros(len(x1))
for i in range(len(x1)):
    mul[i] = x1[i] * x2[i]
toc = time.time()
print("computational time = ", 1000 *(toc - tic))

tic = time.time()
dot = np.multiply(x1, x2)
toc = time.time()
print("computational time = ", 1000 *(toc - tic))


# 4th example:
# Generalized dot implementation

# W = np.random.rand(3, len(x1))
# tic = time.time()
# gdot = np.zeros(W.shape[0])
# for i in range(W.shape[0]):
#     for j in range(len(x2)):
#         gdot[i] = W[i, j] * x1[j]
# toc = time.time()
# print("computational time = ", 1000 *(toc - tic))

# tic = time.time()
# dot = np.dot(W, x1)
# toc = time.time()
# print("computational time = ", 1000 *(toc - tic))