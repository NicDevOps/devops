# Problem set 1, hard part : Prints a right sided pyramid of bricks with a loop

n = int(input("Size: "))
print(n)

for i in range(n):
    for j in range(n):
        print(" ", end="")
    n -= 1
    for j in range(i + 1):
        print("#", end="")
    print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    print()
   
