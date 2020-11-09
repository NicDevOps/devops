
# Eve moon parser

import os
from time import sleep
import numpy

def clear():
    os.system( 'clear' )
    sleep(1)

file_txt = 'python/eve_moon/moon.txt'



clear()

def data_converter(file_txt):

    moon = {}
    count = 0

    with open(file_txt, 'r') as file_txt:
        first_line = file_txt.readline().strip().split('\t')
        moon_line = file_txt.readline()

        print(first_line)

        while moon_line:
            if moon_line[0] != '\t':
                count = 0
                moon_planet = moon_line.strip()

            elif moon_line[0] == '\t' and count == 0:
                count += 1
                step_1 = moon_line.strip()
                ore_1 = step_1.split('\t')
                if '' in ore_1:
                    ore_1.remove('')
                moon[moon_planet] = ore_1

            elif moon_line[0] == '\t' and count == 1:
                count += 1
                step_2 = moon_line.strip()
                ore_2 = step_2.split('\t')
                if '' in ore_2:
                    ore_2.remove('')
                moon[moon_planet] = [ore_1, ore_2]
                
            elif moon_line[0] == '\t' and count == 2:
                count += 1
                step_3 = moon_line.strip()
                ore_3 = step_3.split('\t')
                if '' in ore_3:
                    ore_3.remove('')
                moon[moon_planet] = [ore_1, ore_2, ore_3]

            elif moon_line[0] == '\t' and count == 3:
                count += 1
                step_4 = moon_line.strip()
                ore_4 = step_4.split('\t')
                if '' in ore_4:
                    ore_4.remove('')
                moon[moon_planet] = [ore_1, ore_2, ore_3, ore_4]
            
            moon_line = file_txt.readline()

    return moon


def data_updater(data_dict):
    for key, value in data_dict.items():
        print(key)
        print(value)

x = data_converter(file_txt)
data_updater(x)
# print(x)
# print()
# data_dictionary(x)

