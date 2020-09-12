import argparse
from random import randint

# Define an argument parser object
parser = argparse.ArgumentParser()

# Add positional arguments, with the use of metavar to assing a name to the 'count' argument
parser.add_argument('count', metavar = 'rands', type = int, help = 'Count of random integers to be generated')

# Add optional arguments
parser.add_argument('-r', '--range', metavar = ('lower', 'upper'), nargs = 2, type = int, default = [0, 10], help = 'Integer range [a, b] from which the random numbers will be chosen')

# Parse command-line arguments
args = parser.parse_args()

# Program
for i in range(args.count): # still accessed as args.count (not args.rands)
    print(randint(args.range[0], args.range[1]))