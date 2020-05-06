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

first_num = input("Enter a number : ")
sec_num = input("Enter a second number : ")

if not first_num.isdigit():
    print("This is not valid integer value !")
elif not sec_num.isdigit():
    print("This is not a valid integer value")
else:
    result = int(first_num) + int(sec_num)
    print("The result is result : ", result)
