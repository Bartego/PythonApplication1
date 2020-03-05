from random import random
from random import seed
from IPython.display import clear_output




clear_output()



def player_selection():
    a = random()
    if a <= 0.5:
        a = 0
        return a
    else:
        a = 1
        print(a)


layout_board = ["#",'7','8','9','4','5','6','1','2','3']
game_board = ["#",'O','X','O','X','O','X','O','X','0']
game_range = ['Q','1','2','3','4','5','6','7','8','9']

def player_input():
    #clear_output()    
    player1_xo = input("Do you want to play 'X' or 'O'? ")
    clear_output()
    player1_xo = player1_xo.upper()
    if player1_xo == 'X':  
        player2_xo = 'O'
        print (f'Player 1 has {player1_xo}')
        print (f'Player 2 has {player2_xo}')
    elif player1_xo == 'O':
        player2_xo = 'X'
        print (f'Player 1 has {player1_xo}')
        print (f'Player 2 has {player2_xo}')
    else:
        print('Wrong input')

def display_board(layout_board, game_board):
   # clear_output()
    print ('#################')
    print (layout_board[1:4:])
    print (layout_board[4:7:])
    print (layout_board[7::])
    print ('#################')
    print (game_board[1:4:])
    print (game_board[4:7:])
    print (game_board[7::])


def game_input():
 #player_input()
    for x in range(1,10):
        if x%2 ==0:
            player1_po = input('Player 1 enters position (0-9,Q-quit): ') #position that player 1 selected for his 'x' or 'o'
            if player1_po == 'Q' or player1_po == 'q': #quit sequence player 1
                print ('Player1 quit game')
                break
            while player1_po in game_range:
                print (f'Player 1 entered position: {player1_po}')
                display_board(layout_board, game_board)
                break
                    
            else:
                print ('Invalid board postion input')
                break
                    
        elif x%2 !=0:
            player2_po = input('Player 2 enters position (0-9,Q-quit): ') #position that player 2 selected for his 'x' or 'o'
                
            if player2_po == 'Q' or player2_po =='q': ##quit sequence player 2
                print ('Player2 quit game')
                break
                        
            while player2_po in game_range:
                print (f'Player 2 entered position: {player2_po}')
                display_board(layout_board, game_board)
                break                    

            else:
                print ('Invalid board postion input')
                break
    

         

clear_output()


#player_selection()
#print (a)
#player_input()

