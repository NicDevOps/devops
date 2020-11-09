import os
from pprint import pprint

def read_survey(filename):
    survey = {}

    with open(filename, 'r') as f:
        headers = f.readline().strip().split('\t')
        survey = {}

        for line in f.readlines():
            line_data = line.strip('\n').split('\t')
            is_planet = len(line_data) == 1

            if is_planet:
                moon = line_data.pop()
                survey[moon] = {}
            else:                
                ore_dict = dict(zip(headers, line_data))
                
                ore_dict.pop('Moon')
                moon_product = ore_dict.pop('Moon Product')

                survey[moon].update({moon_product: ore_dict})
        
    return survey

def main():

    survey = read_survey('python/eve_moon/moon.txt')

    for planet, ore_list in survey.items():
        print(planet)
        for ore in ore_list:
            print("\t" + ore)


if __name__ == '__main__':
    main()
