#
# [ ] get user input with prompt "what is the title?"
# [ ] call title_it() using input for the string argument


# [ ] define title_it_rtn() which returns a titled string instead of printing
# [ ] call title_it_rtn() using input for the string argument and print the result
#
# bookstore() takes 2 string arguments: book & price
# bookstore returns a string in sentence form
# bookstore() should call title_it_rtn() with book parameter
# gather input for book_entry and price_entry to use in calling bookstore()
# print the return value of bookstore()
# example of output:Title: The Adventures Of Sherlock Holmes, costs $12.99
#
# # [ ] create, call and test bookstore() function

def title_it_rtn(msg):
    return msg.title()


def bookstore(book, price):
    return "Title: " + title_it_rtn(book) + ", costs $" + price


# def short_rhyme():
#     print("La la la!!")
#     print("Do Re Mi")


# def title_it(msg):
#     print(msg.title())


book_entry = input("Enter book name ")
price_entry = input("Enter price ")

x = bookstore(book_entry, price_entry)

print(x)


# user_in = input("what is the title ?")
#
# x = title_it_rtn(user_in)
#
# print(x)

# title_it(user_in)
#
# short_rhyme()

