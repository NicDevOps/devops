# # review code and run cell
# x = 21
# if x > 25:
#     print("x is already bigger than 25")
# else:
#     print("x was", x)
#     x = 25
#     print("now x is", x)
# # review code and run cell
# x = 18
# if x + 18 == x + x:
#     print("Pass: x + 18 is equal to", x + x)
# else:
#     print("Fail: x + 18 is not equal to", x + x)
# # review code and run cell. "!" means "not"
# x = 18
# test_value = 18
# if x != test_value:
#     print('x is not', test_value)
# else:
#     print('x is', test_value)
#
# # review code and run cell
# # DON'T ASSIGN (x = 2) when you mean to COMPARE (x == 2)
# x = 2
#
# if x == 2:
#     print('"==" tests for, is equal to')
# else:
#     pass


# Task 2
# Evaluating a comparison operator in if
# # [ ] create an if/else statement that tests if y is greater than or equal x + x
# # [ ] print output: "y greater than or equal x + x is" True/False ...or a similar output
x = 3
y = x + 8

if y >= x + x:
    print("y greater than or equal x + x is", y >= x + x)
else:
    pass
