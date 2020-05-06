def room_1():
    player_action = input('''
[DM] You enter room 1. It's a normal room
[DM] Do you want to leave?

List of player actions
[l]eave room    
enter action> ''')

    if player_action == 'l':
        print('[DM]leaving room 1')


room_1()

print('[DM] Congradulations!!!')