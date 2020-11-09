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

# fav_color = input("Enter your favorite rainbow color R|O|Y|G|B|I|V ")
#
# if fav_color.upper() == 'R':
#     print("This is Red !")
# elif fav_color.upper() == 'O':
#     print("This is Orange !")
# elif fav_color.upper() == 'Y':
#     print("This is Yellow !")
# elif fav_color.upper() == 'G':
#     print("This is Green !")
# elif fav_color.upper() == 'B':
#     print("This is Blue !")
# elif fav_color.upper() == 'I':
#     print("This is Indigo !")
# elif fav_color.upper() == 'V':
#     print("This is violet !")
# else:
#     print("No match !")

# [ ] make the code above into a function rainbow_color() that has a string parameter,
# get input and call the function and return the matching color as a string or "no match" message.
# Call the function and print the return string.

######################################


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


#
#
# fav_color = input("Enter your favorite rainbow color R|M|Y|G|B|C|P ")
#
# if fav_color.upper() == 'R':
#     print(color.RED + "This is Red !" + color.END)
# elif fav_color.upper() == 'M':
#     print(color.MAGENTA + "This is Magenta !" + color.END)
# elif fav_color.upper() == 'Y':
#     print(color.YELLOW + "This is Yellow !" + color.END)
# elif fav_color.upper() == 'G':
#     print(color.GREEN + "This is Green !" + color.END)
# elif fav_color.upper() == 'B':
#     print(color.BLUE + "This is Blue !" + color.END)
# elif fav_color.upper() == 'C':
#     print(color.CYAN + "This is Cyan !" + color.END)
# elif fav_color.upper() == 'P':
#     print(color.PURPLE + "This is Purple !" + color.END)
# else:
#     print("No match !")


def rainbow_color(color):
    if color.upper() == 'R':
        return "This is RED"
    else:
        return "Does not match !"
#
#
# def new_color(color, msg):
#     if color.upper() == 'R':
#         return RED + msg + END
#     elif color.upper() == 'M':
#         return MAGENTA + msg + END
#     elif color.upper() == 'Y':
#         return YELLOW + msg + END
#     elif color.upper() == 'G':
#         return GREEN + msg + END
#     elif color.upper() == 'B':
#         return BLUE + msg + END
#     elif color.upper() == 'C':
#         return CYAN + msg + END
#     elif color.upper() == 'P':
#         return PURPLE + msg + END
#     else:
#         return msg
#
#
# fav_color = input("Enter your favorite rainbow color R|M|Y|G|B|C|P ")
# msg_input = input("Enter a message ")
# # x = rainbow_color(fav_color)
# x = new_color(fav_color, msg_input)
# print(x)
#
# Create function age_20() that adds or subtracts 20 from your age for a return value based on current age (use if)
#
# call the function with user input and then use the return value in a sentence
# example age_20(25) returns 5:
# "5 years old, 20 years difference from now"
#
# # [ ] complete age_20()


def age_20(age):
    if age >= 25:
        return age - 20
    else:
        return age + 20

#
# age_input = int(input("Enter your age "))
# x = age_20(age_input)
# print(f"{x} years old, 20 years difference from now")


#
#
# create a function rainbow_or_age that takes a string argument
#
# if argument is a digit return the value of calling age_20() with the str value cast as int
# if argument is an alphabetical character return the value of calling rainbow_color() with the str
# if neither return FALSE
# [ ]  create rainbow_or_age()
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def rainbow_or_age(arg):
    if is_digit(arg):
        return age_20(int(arg))
    elif arg.isalpha():
        return rainbow_color(arg)
    else:
        return False


# age_or_color = input("Enter age or color ")
# result = rainbow_or_age(age_or_color)
# print(result)


# Additional Practice

# [ ]  add 2 numbers from input using a cast to integer and display the answer

x = int(input("Enter a number : "))
y = int(input("Enter a second number : "))
# result = int(x) + int(y)
# print(result)


# [ ] Multiply 2 numbers from input using cast and save the answer as part of a string "the answer is..."
# display the string using print

# result = int(x) * int(y)
# print(f"The answer is {result}")

# [ ] get input of 2 numbers and display the average: (num1 + num2) divided by 2
#
# result = (x + y) / 2
# print(f"The answer is {result}")

# [ ] get input of 2 numbers and subtract the largest from the smallest (use an if statement to see which is larger)
# show the answer

# if x > y:
#     result = x - y
#     print(f"The answer is {result}")
# else:
#     result = y - x
#     print(f"The answer is {result}")


# [ ] Divide a larger number by a smaller number and print the integer part of the result
# don't divide by zero! if a zero is input make the result zero
# [ ] cast the answer to an integer to cut off the decimals and print the result

if x > y:
    result = x / y
    print(f"The answer is {int(result)}")
elif y >= x:
    result = y / x
    print(f"The answer is {int(result)}")
if

