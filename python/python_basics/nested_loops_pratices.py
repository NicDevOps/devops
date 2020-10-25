

table = [[5, 2, 6], [4, 6, 0], [9, 1, 8], [7, 3, 8]]


for x in range(len(table[0])):
    result = 0
    print()
    for y in table:
        result += y[x]
        print(y[x], end=" ")
    print(result)

