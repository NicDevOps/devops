import subprocess as sp
import random
import time
from datetime import datetime




def get_keyboard_input():
    result = input('Enter w/a/s/d/x: ')

    if result == 'w':
        return {'x': 0, 'y': -1}

    if result == 's':
        return {'x': 0, 'y': 1}

    if result == 'a':
        return {'x': -1, 'y': 0}

    if result == 'd':
        return {'x': 1, 'y': 0}

    if result == 'x':
        exit(0)

    return {'x': 0, 'y': 0}


def move_object(pos, speed, width, height):
    new_pos_x = pos['x'] + speed['x']
    new_pos_y = pos['y'] + speed['y']

    if new_pos_x < 0:
        new_pos_x = 0

    if new_pos_x > width - 1:
        new_pos_x = width - 1

    if new_pos_y < 0:
        new_pos_y = 0

    if new_pos_y > height - 1:
        new_pos_y = height - 1

    return {'x': new_pos_x, 'y': new_pos_y}


def move_to(a_pos, b_pos):
    delta_x = b_pos['x'] - a_pos['x']
    delta_y = b_pos['y'] - a_pos['y']

    if delta_x > 0:
        delta_x = 1

    if delta_x < 0:
        delta_x = -1

    if delta_y > 0:
        delta_y = 1

    if delta_y < 0:
        delta_y = -1

    return {'x': delta_x, 'y': delta_y}


def draw_map(card_list, map_width, map_height):
    sp.call('clear', shell=True)
    buffer = ''

    for y in range(map_height):
        for x in range(map_width):
            for card in card_list:
                if (card['x'] <= x < card['x'] + card['width']) and (card['y'] <= y < card['y'] + card['height']):
                    buffer += '#'
                else:
                    buffer += '.'

            # if x == a_pos['x'] and y == a_pos['y']:
            #     buffer += 'A'
            # elif x == z_pos['x'] and y == z_pos['y']:
            #     buffer += 'Z'
            # elif x == z2_pos['x'] and y == z2_pos['y']:
            #     buffer += 'Z'
            # else:

        buffer += '\n'

    buffer += datetime.now().strftime("%H:%M:%S")

    print(buffer)
    time.sleep(1/30)


map_width = 32
map_height = 16
card_list = [
    {
        'x': 0,
        'y': 0,
        'width': 8,
        'height': 5
    },
    {
        'x': 0,
        'y': 0,
        'width': 8,
        'height': 5
    },
    {
        'x': 4,
        'y': 4,
        'width': 8,
        'height': 5
    }
]

player_pos = {'x': 0, 'y': 0}
zombie_pos = {'x': random.randint(0, map_width - 1), 'y': random.randint(0, map_height - 1)}
zombie_pos2 = {'x': random.randint(0, map_width - 1), 'y': random.randint(0, map_height - 1)}

while True:
    draw_map(card_list, map_width, map_height)
    input_speed = get_keyboard_input()

    card_list[0]['x'] += input_speed['x']
    card_list[0]['y'] += input_speed['y']


    # zombie_speed = move_to(zombie_pos, player_pos)
    # zombie_speed2 = move_to(zombie_pos2, player_pos)
    # player_pos = move_object(player_pos, player_speed, map_width, map_height)
    # zombie_pos = move_object(zombie_pos, zombie_speed, map_width, map_height)
    # zombie_pos2 = move_object(zombie_pos2, zombie_speed2, map_width, map_height)
