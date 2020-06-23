# this program uses a nested loop
def is_inbox(x, y):
    return x >= 1 and x <= 3 and y >= 1 and y <= 3


def draw_line(x, y, m, b):
    return y == m * x + b


def draw_dude(x, y):
    return x == 3 and y ==2


def draw_box(ax, ay, bx, by, x, y):
    return x >= ax and x <= (bx - ax) + ax and y >= ay and y <= (by - ay) + ay


def draw_dot(x, y, pos_x, pos_y):
    return x == pos_x and y == pos_y


def render_game(size):
    player_x = 4
    player_y = 4
    player_char = "#"

    for y in range(size):
        for x in range(size):
            # if draw_line(x=x, y=y, m=1, b=0) or draw_line(x=x, y=y, m=-1, b=size-1):
            # if draw_box(1, 1, 5, 2, x, y) or draw_box(1, 4, 5, 5, x, y):
            if draw_dot(x=x, y=y, pos_x=player_x, pos_y=player_y):
                print(player_char, end="", flush=True)
            else:
                print(".", end="", flush=True)

        print()


render_game(7)
