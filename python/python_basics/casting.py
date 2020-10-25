# Using casting to change data type
# Casting is the conversion from one data type to another Such as converting from str to int
#
# int()
# the int() function can convert strings that represent whole counting numbers into integers
# and strip decimals to convert float numbers to integers
#
# int("1") = 1 the string representing the integer character "1", cast to a number
# int(5.1) = 5 the decimal (float), 5.1, truncated into a non-decimal (integer)
# int("5.1") = ValueError "5.1" isn't a string representation of integer,
# int() can cast only strings representing integer values

# Example
# weight1 = '60' # a string
# weight2 = 170 # an integer
# # add 2 integers
# total_weight = int(weight1) + weight2
# print(total_weight)


# Task 2
# casting with int() & str()
# str_num_1 = "11"
# str_num_2 = "15"
# int_num_3 = 10
# # [ ] Add the 3 numbers as integers and print the result
#
# result = int(str_num_1) + int(str_num_2) + int_num_3
# print(result)
#
#
# str_num_1 = "11"
# str_num_2 = "15"
# int_num_3 = 10
# # # [ ] Add the 3 numbers as test strings and print the result
# result = str_num_1 + str_num_2 + str(int_num_3)
# print(result)
#
# Task 2 cont...
# Program: adding using int casting
# [ ] initialize str_integer variable to a string containing characters of an integer (quotes)
# [ ] initialize int_number variable with an integer value (no quotes)
# [ ] initialize number_total variable and add int_number + str_integer using int casting
# [ ] print the sum (number_total)
# # [ ] code and test: adding using int casting
# str_integer = "2"
# int_number = 10
# number_total = int(str_integer) + int_number
# print(number_total)

# Concept: Casting Numeric Input
# Casting input() strings that represent numbers to integer values
# Example

# # [ ] review and run code
# student_age = input('enter student age (integer): ')
# age_next_year = int(student_age) + 1
# print('Next year student will be', age_next_year)


# # [ ] review and run code
# # cast to int at input
# student_age = int(input('enter student age (integer): '))
#
# age_in_decade = student_age + 10
#
# print('In a decade the student will be', age_in_decade)
# Task 3
# Program: adding calculator
# get input of 2 integer numbers
# cast the input and print the input followed by the result
# Output Example: 9 + 13 = 22
# Optional: check if input .isdigit() before trying integer addition to avoid errors in casting invalid inputs
#
# # [ ] code and test the adding calculator
