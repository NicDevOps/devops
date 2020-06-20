# this program uses a nested loop
def is_inbox(x, y):
    return x >= 1 and x <= 3 and y >= 1 and y <= 3


def is_line(x, y, m, b):
    return y == m * x + b



def generate_star(size):
    for y in range(size):
        for x in range(size):
            if is_line(x=x, y=y, m=1, b=0) or is_line(x=x, y=y, m=-1, b=size-1):
                print("#", end="", flush=True)
            else:
                print(".", end="", flush=True)

        print()


generate_star(31)
