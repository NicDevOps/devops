        
        
tic_tac_toe = [['7', '8', 'X'], ['4', 'X', '6'], ['X', '2', '3']]       
        

count = 2
adx = 0
ado = 0

for y in tic_tac_toe:
    if y[count] == 'X':
        adx += 1
    if y[count] == 'O':
        ado += 1
    count -= 1
if dx == 3:
    print('Player X wins!')
if do == 3:
    print('player O wins!')





# for x in range(len(tic_tac_toe[0])):
#     if count_vx >= 3:
#         print('True')
#     if count_vo >= 3:
#         print('True')
#     for y in tic_tac_toe:
#         if y[x] == 'X':
#             count_vx += 1
#         if y[x] == 'O':
#             count_vo += 1



        