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
    

    with open(file_txt, 'r') as file_txt:
        first_line = file_txt.readline().strip().split('\t')
        moon_line = file_txt.readline()

        print(first_line)

        while moon_line:
            
            count = 0
            if moon_line[0] != '\t':
                count = 0
                moon_planet = moon_line.strip()
                moon_line = file_txt.readline()
            try:
                while moon_line[0] == '\t':
                    
                    count += 1
                    for ore in range(count):
                        ore = moon_line.strip()
                        ore = ore.split('\t')
                        if '' in ore:
                            ore.remove('')
                    
                    moon[moon_planet] = [ore, ore 1 ]
                   
                    moon_line = file_txt.readline()
            except IndexError:
                break
    
    return moon


x = data_converter(file_txt)

print(x)