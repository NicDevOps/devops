user_input = int(input('How many cycles?: '))


def all_lights(how_many):
    while how_many >= 0:
        print(how_many)
        # light_on(red_led)
        # light_on(green_led)
        # light_on(blue_led)
        how_many = how_many - 1


all_lights(user_input)
