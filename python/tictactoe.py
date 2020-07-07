#
#
# tic_tac_toe = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]

from random import randint
from IPython.display import clear_output

def draw(board):
    count = 0
    for y in board:
        print('{:s} | {:s} | {:s}'.format(y[0], y[1], y[2]))
        if count < 2:
            print('-' * 10)
            count += 1

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


def mark_1(player, location, board):
    for y in board:
        for x in range(len(y)):
            if y[x] == location:
                y[x] = player
                

# mark_1('O', '7', tic_tac_toe)
# mark_1('O', '5', tic_tac_toe)
# mark_1('O', '3', tic_tac_toe)

# draw(tic_tac_toe)


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

def dashes():
    """Print a fancy line of dashes"""
    print("o" + 35 *'-' + "o")
    
def display(message):
    """
    Print `message` in the center of a 35 characters string
    
    args:
        message: string to display
    
    returns:
        None
    """
    print("|{:^35s}|".format(message))
    
def main():
    # initializing game
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    # select the first player randomly
    player = ['X', 'O']
    turn = randint(0, 1)

    win = False
    tie = False
    while(not win and not tie):
        # switch players
        turn = (turn + 1) % 2
        current_player = player[turn] # contains 'X' or 'O'

        clear_output()
        
        # display header
        dashes()
        display("TIC TAC TOE")
        dashes()

        # display game board
        print()
        draw(board)
        print()

        # display footer
        dashes()
        # player select a location to mark
        while True:
            location = input("|{:s} Turn, select a number (1, 9): ".format(current_player))
            if available(location, board):
                break # Only the user input loop, main loop does NOT break
            else:
                print("Selection not available!")
        dashes()

        # mark selected location with player symbol ('X' or 'O')
        mark_1(current_player, location, board)
        
        # check for win
        win = check_win(board)
        
        # check for tie
        tie = check_tie(board)
        

    # Display game over message after a win or a tie
    clear_output()
    
    # display header
    dashes()
    display("TIC TAC TOE")
    dashes()

    # display game board (Necessary to draw the latest selection)
    print()
    draw(board)
    print()

    # display footer
    dashes()
    display("Game Over!")
    if(win):
        display("Winner:!")
        display(current_player)
    elif(tie):
        display("Tie!")
    dashes()
  

# Run the game
main()
