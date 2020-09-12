import argparse
from random import randint

# define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments
parser.add_argument('count', type = int, help = 'Count of random integers to be generated')

# Add optional arguments, with the use of a tuple
parser.add_argument('-r', '--range', metavar = ('lower', 'upper'), nargs = 2, type = int, default = [0, 10], help = 'Integer range [a, b] from which the random numbers will be chosen')

# parse command line arguments
args = parser.parse_args()

# program
for i in range(args.count):
    print(randint(args.range[0], args.range[1]))