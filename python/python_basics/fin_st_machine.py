# Finite state machine

light_status = False


def toggle_light(light):
    new_light = not light
    return new_light


print("The light is ", light_status)

light_status = toggle_light(light_status)

print("The light is ", light_status)

light_status = toggle_light(light_status)

print("The light is ", light_status)

