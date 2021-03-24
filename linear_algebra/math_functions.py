
def matrix():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))

    return a,b,c,d

def multiply_matrix(x, y):

    r1 = x[0] * y[0] + x[2] * y[1], x[0] * y[2] + x[2] * y[3]
    r2 = x[1] * y[0] + x[3] * y[1], x[1] * y[2] + x[3] * y[3]

    print(f"{r1}")
    print(f"{r2}")

def main():
    x = matrix()
    y = matrix()
    multiply_matrix(x, y)

if __name__ == '__main__':
    main()
        

    


