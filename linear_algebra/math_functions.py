
def matrix():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    d = int(input("Enter d: "))

    return a,b,c,d

def multiply_matrix(x, y):

    r1 = x[0] * y[0] + x[1] * y[2], x[0] * y[1] + x[1] * y[3]
    r2 = x[2] * y[0] + x[3] * y[2], x[2] * y[1] + x[3] * y[3]

    print("2D matrix multiply: ")
    print()
    print(f"{x[0], x[1]}   {y[0], y[1]}   {r1}")
    print(f"{x[2], x[3]}   {y[2], y[3]}   {r2}")

def concat(a, b):
    result = []
    for i in enumerate(a):
        for j in enumerate(b):
            result[i][j] = a[i][j] * b [i][j] + a[i][j] * b [i][j]
    
    return result

def main():
    x = matrix()
    y = matrix()
    multiply_matrix(x, y)

    monster_position = [0, 0]
    monster_velocity = [1, 0]
    
    rotate_90_clockwise = [
        [-3, 1],
        [ 2, 1]
    ]

    monster_position = monster_position * monster_velocity


    monster_position = monster_position * rotate_90_clockwise

    [1, 0] * [[-3, 1], [2, 1]] = [0, 1]

    [1, 0] * [[-3, 1], [2, 1]] * [[-3, 1], [2, 1]] = [2, 7]








    identity = [
        [1, 0],
        [0, 1],
    ]

    translate_position  = [
        [2,  0],
        [5, -1]
    ]

    rotate_transformation = [
        [-3, 1],
        [ 2, 1]
    ]

    player_coordinates = concat(translate_position, rotate_position)

    print(player_coordinates)

    






if __name__ == '__main__':
    main()
        

    


