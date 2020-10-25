import random


def do_smash(attack):
    return attack + (3 * random.random())

def do_block(defense):
    return defense

monster_attack = 6
monster_defense = 8
monster_life = 30

smash_result = do_smash(monster_attack)


#
result = smash_result - do_block(monster_defense)

if result < 0:
    result = 0

monster_life = monster_life - result


#

print("life: {0}".format(monster_life))

# print("attack: {0}, defense: {1}, life: {2}".format(monster_attack, monster_defense, monster_life))
# print("smash_result: {0}".format(smash_result))
