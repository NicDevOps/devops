# # [ ] review and run example
# print("3 + 5 =",3 + 5)
# print("3 + 5 - 9 =", 3 + 5 - 9)
# print("48/9 =", 48/9)
# print("5*5 =", 5*5)
# print("(14 - 8)*(19/4) =", (14 - 8)*(19/4))


# # [ ] review and run example - 'million_maker'
# def million_maker():
#     make_big = input("enter a non-decimal number you wish were bigger: ")
#     return int(make_big)*1000000
#
#
# print("Now you have", million_maker())

#
# Task 1
# use math operators to solve the set of tasks below
# # [ ] print the result of subtracting 15 from 43
# print("43 - 15 : ", 43 - 15)
# # # [ ] print the result of multiplying 15 and 43
# print("43 * 15 : ", 43 * 15)
# # # [ ] print the result of dividing 156 by 12
# print("156 / 12 : ", 156 / 12)
# # # [ ] print the result of dividing 21 by 0.5
# print("21 / 0.5 : ", 21 / 0.5)
# # # [ ] print the result of adding 111 plus 84 and then subtracting 45
# print("111 + 84 - 45 : ", 111 + 84 - 45)
# # # [ ] print the result of adding 21 and 4 and then multiplying that sum by 4
# print("(21 + 4) * 4 : ", (21 + 4) * 4)


# Task 2
# Program: Multiplying Calculator Function
# define function multiply(), and within the function:
# gets user input() of 2 strings made of whole numbers
#
# cast the input to int()
#
# multiply the integers and return the equation with result as a str()
#
# return example
# 9 * 13 = 117
# # [ ] create and test multiply() function

# def multiply(str_1, str_2):
#     mul_result = str_1 * str_2
#     return mul_result
#
#
# numb_1 = int(input("Enter a number : "))
# numb_2 = int(input("Enter a second number : "))
#
# result = multiply(numb_1, numb_2)
# print(f"{numb_1} * {numb_2} = {result}")


#
# Task 3
# Project: Improved Multiplying Calculator Function
# putting together conditionals, input casting and math
# update the multiply() function to multiply or divide
# single parameter is operator with arguments of * or / operator
# default operator is "*" (multiply)
# return the result of multiplication or division
# if operator other than "*" or "/" then return "Invalid Operator"
# # [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)

def multiply(num_1, num_2, op='*'):
    if op == "/":
        return num_1 / num_2
    elif op == "*":
        return num_1 * num_2
    else:
        return "Invalid Operator"


choose_op = input("Hit '/' or '*' for divide ")
numb_1 = int(input("Enter a number : "))
numb_2 = int(input("Enter a second number : "))

result = multiply(numb_1, numb_2, choose_op)
print(result)


#
#
#
# Task 4
# Fix the Errors
# # Review, run, fix
# student_name = input("enter name: ").capitalize()
# if student_name.startswith("F"):
#     print(student_name,"Congratulations, names starting with 'F' get to go first today!")
# elif student_name.startswith("G")
#     print(student_name,"Congratulations, names starting with 'G' get to go second today!")
# else:
#     print(student_name, "please wait for students with names staring with 'F' and 'G' to go first today.")
