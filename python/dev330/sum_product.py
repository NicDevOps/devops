import argparse

parser = argparse.ArgumentParser()

parser.add_argument('numbers', type = int, nargs = '*', help = 'numbers to be added (or multiplied)')

parser.add_argument('-p', '--product', action = 'store_true', help = 'show the product of the numbers (in addition to the displayed sum)')

args = parser.parse_args()

total = 0
product = 1

for i in args.numbers:
    total += i

print(total)

if args.product:
    for p in args.numbers:
        product = p * product
    print(product)







