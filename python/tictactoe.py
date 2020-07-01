#
#
"""
    Draw the `board` table.

    The board reflects the current state of the game, a number indicates an available location.

    args:
        board: 3x3 table (list of lists) containing the current state of the game

    returns:
        None

    examples:
        At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
        The printout should look like:

         7 | 8 | 9
        -----------
         4 | 5 | 6
        -----------
         1 | 2 | 3

         After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
         The printout should look like:
         7 | 8 | X
        -----------
         O | O | 6
        -----------
         1 | X | 3
    """

tic_tac_toe = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]

# def draw(board):
#     count = 0
#     for y in board:
#         print('{:s} | {:s} | {:s}'.format(y[0], y[1], y[2]))
#         if count < 2:
#             print('-' * 10)
#             count += 1
#
#
# draw(tic_tac_toe)

"""
   Check the availability of a `location` on the current `board`

   An available location on the board contains a number between 1 and 9 stored as a string.
   If the location contains 'X' or 'O', the location is not available and the function should return False;
   otherwise, the function should return True indicating the location is available

   args:
       location: a number between 1 and 9 stored as a string
       board: 3x3 table (list of lists) containing the current state of the game

   returns:
       True if the location is available. False if the location is not available

   examples:
       At the beginning of the game: board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
       The printout should look like:

        7 | 8 | 9 
       -----------
        4 | 5 | 6 
       -----------
        1 | 2 | 3 

        available("1", board) --> returns True
        available("9", board) --> returns True


        After a few marks: board = [['7', '8', 'X'], ['O', 'O', '6'], ['1', 'X', '3']]
        The printout should look like:
        7 | 8 | X 
       -----------
        O | O | 6 
       -----------
        1 | X | 3 

        available("1", board) --> returns True, because there is a number
        available("5", board) --> returns False, because there is 'O'
        available("9", board) --> returns False, because there is 'X'
   """

loc = '1'


def available(location, board):
    for y in board:
        for x in range(2):
            if y[x] == 'X' or y[x] =='O':







print(available(loc, tic_tac_toe))
