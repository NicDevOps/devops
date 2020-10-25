#!/usr/bin/env python3

from electronic_class import component
import argparse

# python/class/component_calc.py

def parse_command_line():
    
    parser = argparse.ArgumentParser()
    
    # positional arguments
    parser.add_argument('name',help = 'input name of electronic component')

    # Add optional argument
    parser.add_argument('-a', '--amperes', type = float, help = 'Operating amperage of component in amps')

    parser.add_argument('-f', '--foward_voltage', type = float, help = 'Operating voltage of component in volts')

    parser.add_argument('-p', '--power_source', type = float, help = 'Operating voltage of power source in volts')

    parser.add_argument('-r', '--resistance',type = float, help = 'Operating resistance of component in ohms')
    
    # Parse command-line arguments
    return parser.parse_args(['led', '-a', '0.026', '-f', '3.2', '-p', '9'])


args = parse_command_line()

amperes = args.amperes
name = args.name
foward_voltage = args.foward_voltage
power_source = args.power_source

if not args.resistance:
    resistance = (power_source - foward_voltage) / amperes

c = component(amperes, name, foward_voltage, power_source, resistance)

c.frame()