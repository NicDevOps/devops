def para_quadra(a, b, c, x, y):
    return y == (a * x ** 2) + (b * x) + c


def generate_star(size):
    for y in range(size):
        for x in range(size):
            if para_quadra(x=x, y=y, a=0.0625, b=0, c=0):  # or para_quadra(x=x+10, y=y-5, a=0.0625, b=1, c=0):
                print("*", end="")
            else:
                print(" ", end="")
        print()


# Display star
generate_star(20)
