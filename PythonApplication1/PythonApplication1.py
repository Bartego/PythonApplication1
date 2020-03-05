from random import random
from random import seed

from IPython.display import clear_output
clear_output()

layout_board = ["#",'7','8','9','4','5','6','1','2','3']
game_board = ["#",'O','X','O','X','O','X','O','X','0']
game_range = ['Q','1','2','3','4','5','6','7','8','9']


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