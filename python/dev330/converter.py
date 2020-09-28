

import math



def cent2inches(length):
    """
    Convert length from Centimeters to Inches.
    
    1 Centimeter = 0.393701 Inches
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Inches (float)
    """

    result = length * 0.393701

    return result



def cent2feet(length):
    """
    Convert length from Centimeters to Feet.
    
    1 Centimeter = 0.0328084 Feet
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Feet (float)
    """
    
    result = length * 0.0328084

    return result

    
def cent2yards(length):
    """
    Convert length from Centimeters to Yards.
    
    1 Centimeter = 0.0109361 Yards
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Yards (float)
    """
    
    result = length * 0.0109361

    return result



def cent2miles(length):
    """
    Convert length from Centimeters to Miles.
    
    1 Centimeter = 6.2137e-6 Miles
    
    args:
        length: in Centimeter (float)
        
    results:
        result: equivalent length in Miles (float)
    """
    
    result = length * math.pow(6.2137, -6)

    return result

def main():
    length = float(input("Enter length in Centimeters: "))
    
    # In Inches
    inches = cent2inches(length)
    
    # In Feet
    feet = cent2feet(length)
    
    # In Yards
    yards = cent2yards(length)
    
    # In Miles
    miles = cent2miles(length)
    
    print('{:.2f} [cm] = {:.2f} [inches]", {:.2f} [feet], {:.2f} [yards], {:.2e} [miles]'.format(length, inches, feet, yards, miles))
    
if __name__ == '__main__':
    main()