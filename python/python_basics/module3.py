# control code flow with if... else conditional logic
# using Boolean string methods (.isupper(), .isalpha(), .startswith()...)
# using comparison (>, <, >=, <=, ==, !=)
# using Strings in comparisons
# if else
# # [ ] input a variable: age as digit and cast to int
# # if age greater than or equal to 12 then print message on age in 10 years
# # or else print message "It is good to be" age
# #
# age = int(input("Enter your age "))
# if age >= 12:
#     print("In 10 years your age will be ", age + 10)
# else:
#     print("It is good to be ", age)
#
#
#
# # [ ] input a number
# # - if number IS a digit string then cast to int
# # - print number "greater than 100 is" True/False
# # - if number is NOT a digit string then message the user that "only int is accepted"

# number = input("Enter a number ")
# if number.isdigit():
#     print(int(number), "greater than 100 is", int(number) > 100)
# else:
#     print("Only int is accepted ")

#
# Guessing a letter A-Z
# check_guess() takes 2 string arguments: letter and guess (both expect single alphabetical character)
# - if guess is not an alpha character print invalid and return False -
# test and print if guess is "high" or "low" and return False - test and print if guess is "correct" and return True
#
# # [ ] create check_guess()
# # call with test


# def check_guess(letter, guess):
#     if guess == letter:
#         print("Correct !")
#         return True
#     elif guess < letter:
#         print("Low !")
#         return False
#     elif guess > letter:
#         print("High !")
#         return False
#
# #
# # usr_guess = input("Guess a letter : ")
# # usr_letter = 'q'
# #
# # check_guess(usr_letter, usr_guess)
#
#
# def letter_guess(answer):
#     guess = input("Guess a letter :")
#     if check_guess(answer, guess):
#         return True
#
#     guess = input("Guess a letter :")
#     if check_guess(answer, guess):
#         return True
#
#     guess = input("Guess a letter :")
#     if check_guess(answer, guess):
#         return True
#
#     return False
#
#
# result = letter_guess(answer="a")
# if result:
#     print("You win !")
# else:
#     print("Try again !")
#
#
# # [ ] call check_guess with user input
#
#
# Letter Guess
# create letter_guess() function that gives user 3 guesses
#
# takes a letter character argument for the answer letter
# gets user input for letter guess
# calls check_guess() with answer and guess
# End letter_guess if
# check_guess() equals True, return True
# or after 3 failed attempts, return False
# # [ ] create letter_guess() function, call the function to test
#
#
#
# Pet Conversation
# ask the user for a sentence about a pet and then reply
#
# get user input in variable: about_pet
# using a series of if statements respond with appropriate conversation
# check if "dog" is in the string about_pet (sample reply "Ah, a dog")
# check if "cat" is in the string about_pet
# check if 1 or more animal is in string about_pet
# no need for else's
# finish with thanking for the story
# # [ ] complete pet conversation

animal = ['cat', 'dog']
about_pet = input("Talk about your pet !")

if 'cat' in about_pet:
    print("Ah, a cat ")
if 'dog' in about_pet:
    print("Ah, a dog ")
if any(x in about_pet for x in animal):
    print("There is one or more animal in the string about_pet !")

# if ('cat' in about_pet) or ('dog' in about_pet):
#     print('1 or more animals are being talked about')

print("Thanks for the story !")

# def pet_str(pet='cat, dog'):
#     about_pet = input("Talk about your pet !")
#     if about_pet in pet:
#         return True
#     about_pet = input("Talk about your pet !")
#     if about_pet in pet:
#         return True
#     return False
#
#
# result = pet_str()
# print(result)

# for x in range(10):
#     print(x)
#
# [print(x) for x in range(10)]
#
#
# any()
# all()











