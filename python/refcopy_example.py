# assignment by reference because list, dict type
a = [1, 2, 3]
b = a
b.pop()
print(a)


# assignment by copy because list, dict type
a = [1, 2, 3]
b = a.copy()
b.pop()
print(a)


# assignment by copy because int type, str, boolean
a = 1
b = a
b = -999999
print(a)

