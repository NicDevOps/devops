        
tic_tac_toe = [['7', 'X', 'O'], ['4', 'O', 'X'], ['X', 'X', 'O']]

def draw(board):
    count = 0
    for y in board:
        print('{:s} | {:s} | {:s}'.format(y[0], y[1], y[2]))
        if count < 2:
            print('-' * 10)
            count += 1

def check_win(board):
    count_vx = 0
    count_vo = 0
    count_d = 0
    count_dx = 0
    count_do = 0
    count_ad = 2
    count_adx = 0
    count_ado = 0
    for y in board:
        if y[0] == 'X' and y[1] == 'X' and y[2] == 'X':
            return True
        if y[0] == 'O' and y[1] == 'O' and y[2] == 'O':
            return True

    for x in range(len(board[0])):
        if count_vx == 3:
            return True
        if count_vo == 3:
            return True
        for y in board:
            if y[x] == 'X':
                count_vx += 1
            if y[x] == 'O':
                count_vo += 1
        count_vx = 0
        count_vo = 0
            
    for y in board:
        if y[count_d] == 'X':
            count_dx += 1
        if y[count_d] == 'O':
            count_do += 1
        count_d += 1
    if count_dx == 3:
        return True
    if count_do == 3:
        return True
    for y in board:
        if y[count_ad] == 'X':
            count_adx += 1
        if y[count_ad] == 'O':
            count_ado += 1
        count_ad -= 1
    if count_adx == 3:
        return True
    if count_ado == 3:
        return True
    return False

def available(location, board):

    count = 0

    for y in board:
        for x in y:
            if x == location:
                count += 1

    if count >= 1:
        return True
    else:
        return False

def check_tie(board):
    original = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    tie_count = 0
    for y in board:
        for x in y:
            if not available(x , original):
                tie_count += 1
    print(tie_count)
    if tie_count == 9:
        return True
    else:
        return False

draw(tic_tac_toe)        
print(check_win(tic_tac_toe))
#print(check_tie(tic_tac_toe))



        