#  Class 

# The __init__() Function

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def hello(self):
#         print('hello my name is ' + self.name)
    
#     def tell_age(self):
#         print('My age is ', self.age)


# p1 = person(name = 'john',age = '36')

# p1.hello()

# p1.tell_age()

# print(p1.name)
# print(p1.age)

import os
from time import sleep



def clear():
    os.system( 'clear' )

class card:
    def __init__(self,name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def frame(self):
        x = """
        ********************************
          NAME: {:s}                   
          ATTACK: {:d} | DEFENSE: {:d}
        ********************************
        """.format(self.name, self.attack, self.defense)
        print(x)

goblin = card(name = 'Goblin', attack = 1, defense = 2)
warrior = card(name = 'warrior', attack = 2, defense = 2)

clear()
sleep(2)

goblin.frame()
sleep(1)
clear()
sleep(1)

warrior.frame()




