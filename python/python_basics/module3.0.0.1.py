# Rainbow colors
# ask for input of a favorite rainbow color first letter: ROYGBIV
#
# Using if, elif, and else:
#
# print the color matching the letter
# R = Red
# O = Orange
# Y = Yellow
# G = Green
# B = Blue
# I = Indigo
# V = Violet
# else print "no match"
# # [ ] complete rainbow colors


class color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    MAGENTA = "\033[1;35;48m"
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'


fav_color = input("Enter your favorite rainbow color R|M|Y|G|B|C|P ")

if fav_color.upper() == 'R':
    print(color.RED + "This is Red !" + color.END)
elif fav_color.upper() == 'M':
    print(color.MAGENTA + "This is Magenta !" + color.END)
elif fav_color.upper() == 'Y':
    print(color.YELLOW + "This is Yellow !" + color.END)
elif fav_color.upper() == 'G':
    print(color.GREEN + "This is Green !" + color.END)
elif fav_color.upper() == 'B':
    print(color.BLUE + "This is Blue !" + color.END)
elif fav_color.upper() == 'C':
    print(color.CYAN + "This is Cyan !" + color.END)
elif fav_color.upper() == 'P':
    print(color.PURPLE + "This is Purple !" + color.END)
else:
    print("No match !")
