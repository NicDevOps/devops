# Rpg game

player_life = 10
monster_life = 5

fire_blast = 3
mob_bite = 2


def attack(life, mod_life):
    life_result = life - mod_life
    return life_result


def monster_ai(distance, target):
    if distance > 6:
        print(f"Move two squares closer to {target}")
    elif distance == 1:
        print(f"Melee attack to {target}")
    else:
        print("Shoot arrow")


def werewolf_ai(distance, target):

    name = "werewolf"
    if distance > 8:
        print(f"{name} Jumps next to {target}")
    elif distance > 1:
        print(f"{name} Dash attack to {target} : 5 damage !")
    elif distance == 1:
        print(f"{name} Claw attack to {target} : 3 damage !")
    else:
        pass


# monster_ai(8, "bob")
# monster_ai(1, "bob")

# werewolf_ai(10, "dude")

x = int(input("enter distance: "))
monster_ai(x, "bob")

# print("Player life is ", player_life)
# print("Monster life is ", monster_life)
#
# player_life = attack(player_life, mob_bite)
# monster_life = attack(monster_life, fire_blast)
#
# print("Player life is ", player_life)
# print("Monster life is ", monster_life)

# def monster_attack(dmg):
#     damage = player_life - dmg
#     return damage


# result_monster = attack(mob_bite)

# print("Monster remaining life is ", result_player)
# print("Player remaining life is ", result_monster)
