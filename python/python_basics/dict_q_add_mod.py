ask_upc = int(input('Enter UPC number: '))
ask_item = input('Enter item description: ')
ask_price = float(input('Enter unit price: '))
ask_quantity = float(input('Enter item quantity: '))


inventory = {847502: ['APPLES 1LB', 1.99, 50], 847283: ['OLIVE OIL', 10.99, 100], 839529: ['TOMATOS 1LB', 1.29, 25], 483946: ['MILK 1/2G', 3.45, 35], 493402: ['FLOUR 5LB', 2.99, 40], 485034: ['BELL PEPPERS 1LB', 1.35, 28], 828391: ['WHITE TUNA', 1.69, 100], 449023: ['CHEESE 1/2LB', 4.99, 15]}
#TODO: Your code goes here

def qwery_upc(ask, inv):
    for key in inv.keys():
        if ask == key:
            return True
        else:
            return False

def update_upc(ask_u, ask_i, ask_p, ask_q, inv):
    for key, value in inventory.items():
        if ask_u == key:
            value[0] = ask_i
            value[1] = ask_p
            value[2] = ask_q

def add_upc(ask_u, ask_i, ask_p, ask_q, inv):
    inventory[ask_u] = [ask_i, ask_p, ask_q]


try:
    qwery_upc(ask_upc, inventory)
    print('Existing item, updating:', inventory[ask_upc])
    update_upc(ask_upc, ask_item, ask_price, ask_quantity, inventory)
    
except KeyError:
    print('New item, creating:', ask_item)
    add_upc(ask_upc, ask_item, ask_price, ask_quantity, inventory)


print('{:^10s} | {:<20s} | {:^10s} | {:^10s}'.format('UPC', 'Description', 'Unit price', 'Quantity'))
print('-' * 56)

for key, value in inventory.items():
    if ask_upc == key:
        print('{:^10d} | {:<20s} | {:^10.2f} | {:^10.2f}'.format(key, value[0], value[1], value[2]))



#         print('Existing item, updating:', inventory[key])
#         print()
#         print('{:^10d} | {:<20s} | {:^10.2f} | {:^10.2f}'.format(key, value[0], value[1], value[2]))


# for key, value in inventory.items():
#     if ask_upc != key:
#         inventory[ask_upc] = [ask_item, ask_price, ask_quantity]
#         print('Existing item, updating:', inventory[ask_upc])
#         break

# print('{:^10d} | {:<20s} | {:^10.2f} | {:^10.2f}'.format(inventory[ask_upc], inventory[0], inventory[1], inventory[2]))


    