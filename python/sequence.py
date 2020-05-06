# sequence

# def hat_available(color):
#     hat_colors = 'black, red, blue, green, white, grey, brown, pink'
#     return (color.lower() in hat_colors)
#
#
# have_hat = hat_available('green')

# print('hat available is', have_hat)

# The program should ask for user to "input a bird name to check for availability"
# and print a statement informing of availability


def bird_av(bird):
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
    return bird in bird_types


ent_bird = input("Enter bird name")
chk_bird = bird_av(ent_bird)

print(chk_bird)
chk_bird and print("the bird is available")

# Fix the error
# define function how_many
# def how_many():
#     requested = input("enter how many you want: ")
#     return requested
#
#
# # get the number_needed
# number_needed = how_many()
# print(number_needed, "will be ordered")
