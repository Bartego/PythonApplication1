from random import random
from random import seed


def player_selection():
    a = random()
    if a <= 0.5:
        a = 0
        return a
    else:
        a = 1
        print(a)

player_selection()
#print (a)