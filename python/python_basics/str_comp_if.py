# Conditionals: String comparisons with if
# Examples


# # [ ] review and run code
# msg = "Save the notebook"
#
# if msg.lower() == "save the notebook":
#     print("message as expected")
# else:
#     print("message not as expected")


# # [ ] review and run code
# msg = "Save the notebook"
# prediction = "save the notebook"
#
# if msg.lower() == prediction.lower():
#     print("message as expected")
# else:
#     print("message not as expected")


# Task 2
# Conditionals: comparison operators with if
# # [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# # [ ] print messages for correct answer "21" or incorrect answer using if/else
# # note: input returns a "string"
variable = "21"
answer = input("What is 8 + 13? : ")

if answer == variable:
    print("Correct answer 21 ! ")
else:
    print("Incorrect answer, try again ! ")
