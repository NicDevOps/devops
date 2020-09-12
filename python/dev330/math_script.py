from math import pi

def circle_area(r):
    return pi * (r ** 2)

def circle_circumference(r):
    return 2 * pi * r

def main():
    print("Running the main function")
    radius = float(input("Enter radius: "))
    print("Area =", circle_area(radius))
    print("Circumference =", circle_circumference(radius))

if __name__ == "__main__":
    main()
