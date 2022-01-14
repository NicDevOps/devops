def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'



# decorate = uppercase_decorator(say_hi)

result = say_hi()

print(result)

# result = say_hi()

# print(result)
