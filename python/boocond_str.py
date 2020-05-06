# Using Conditionals with Boolean String test methods

# review code and run cell
# favorite_book = input("Enter the title of a favorite book: ")
#
# if favorite_book.istitle():
#     print(favorite_book, "- nice capitalization in that title!")
# else:
#     print(favorite_book, "- consider capitalization throughout for book titles.")


# a_number = input("enter a positive integer number: ")
#
# if a_number.isdigit():
#     print(a_number, "is a positive integer")
# else:
#     print(a_number, "is not a positive integer")


# another if
# if a_number.isalpha():
#     print(a_number, "is more like a word")
# else:
#     pass
# review code and run cell
# vehicle_type = input('"enter a type of vehicle that starts with "P": ')
#
# if vehicle_type.upper().startswith("P"):
#     print(vehicle_type, 'starts with "P"')
# else:
#     print(vehicle_type, 'does not start with "P"')

# create evaluations for .islower()
# print output describing if each of the 2 strings is all lower or not
# test_string_1 = "welcome"
# test_string_2 = "I have $3"
# # [ ] use if, else to test for islower() for the 2 strings
#
# if test_string_1.islower() and test_string_2.islower():
#     print("String 1 : ", test_string_1 and "String 2 : ", test_string_2, " is lower")
# else:
#     print("String 1 and string 2 are not lower !")


# create a functions using startswith('w')
# w_start_test() tests if starts with "w"
# function should have a parameter for test_string and print the test result
test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')

# [ ] Test the 3 string variables provided by calling w_start_test()


def w_start_test(test_string):
    if test_string.startswith("w"):
        print("Strings start with 'w'")
    else:
        print("String don't start with 'w'")


w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)
