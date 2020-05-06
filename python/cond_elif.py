# # [ ] review the code then run testing different inputs
# # WHAT TO WEAR
# weather = input("Enter weather (sunny, rainy, snowy): ")
#
# if weather.lower() == "sunny":
#     print("Wear a t-shirt")
# elif weather.lower() == "rainy":
#     print("Bring an umbrella and boots")
# elif weather.lower() == "snowy":
#     print("Wear a warm coat and hat")
# else:
#     print("Sorry, not sure what to suggest for", weather)


# # [ ] review the code then run testing different inputs


# # SECRET NUMBER GUESS
# secret_num = "2"
#
# guess = input("Enter a guess for the secret number (1-3): ")
#
# if guess.isdigit() == False:
#     print("Invalid: guess should only use digits")
# elif guess == "1":
#     print("Guess is too low")
# elif guess == secret_num:
#     print("Guess is right")
# elif guess == "3":
#     print("Guess is too high")
# else:
#     print(guess, "is not a valid guess (1-3)")


# Task 1
# Program: Shirt Sale
# Complete program using   if, elif, else
# Get user input for variable size (S, M, L)
# reply with each shirt size and price (Small = $ 6, Medium = $ 7, Large = $ 8)
# if the reply is other than S, M, L, give a message for not available
# optional: add additional sizes
# # [ ] code and test SHIRT SALE

shirt_size = input("Please choose your shirt size 'S, M, L, XL' ")

if shirt_size.upper() == "S":
    print("Small = $ 6")
elif shirt_size.upper() == "M":
    print("Medium = $ 7")
elif shirt_size.upper() == "L":
    print("Large = $ 8")
elif shirt_size.upper() == "XL":
    print("XL = $ 10")
else:
    print("Its not a valid size : 'S, M, L, XL'")
