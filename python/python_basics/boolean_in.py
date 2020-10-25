# Using the in keyword to return a Boolean

# the in keyword can be used as a simple search returning True or False indication
# if a string is included in a target sequence.

# review and run code to test if a string is to be found in another string

# menu = "salad, pasta, sandwich, pizza, drinks, dessert"
# print('pizza' in menu)

# review and run code to test case sensitive examples

# greeting = "Hello World!"
# # print("'hello' in greeting = ", 'Hello' in greeting)
#
# print("'hello' in greeting if lower used = ", 'hello'.lower() in greeting.lower())

# What is on menu

menu = "salad, pasta, pizza, drinks, dessert"
print("The menu is : ", menu)
# menu_ask = input("What do you want to eat?")
add_item = input("Add a menu item ")
new_menu = add_item + ", " + menu
print("The new menu is : " + new_menu)
print(add_item in new_menu)
print('bacon' in new_menu)


# print("Your choice is ", menu_ask, menu_ask.lower() in menu.lower())

# print("pizza with cheese and peperoni", 'pizza' in menu)
# print("chicken soup with noodles", 'soup' in menu)
# print("pepsi cola", 'drinks' in menu)

# paint_color = "red, blue, green, black, orange, pink"
# print('Red in paint colors = ', 'red' in paint_color)
