# Problem set 1, hard part : Prints a right sided pyramid of bricks with a loop

# n = input("Size: ")

# while n > 0 and n < 9:
#     for x in range(n):
#         for y in range(j):
#             print(" ")
#             i -= 1

n = 3       
for i in range(3):
    for j in range(n):
        print("#", end="")
    n -= 1
    print()
