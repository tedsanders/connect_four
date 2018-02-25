import os
import numpy as np

quit = False
board = np.zeros((6,7),dtype = 'int')
whose_turn = 1
starting_message = "A new game begins. Player 1, it is your turn."
game_status = starting_message
input_options = """You may:
[1] Drop in column 1
[2] Drop in column 2
[3] Drop in column 3
[4] Drop in column 4
[5] Drop in column 5
[6] Drop in column 6
[7] Drop in column 7
[r] Restart the game
[q] Quit the game"""

#check winner function   
def check_winner(board,drop_depth,drop_column,whose_turn):
    for decrement, increment in ( ((-1,-1),(1,1)), ((-1,0),(1,0)), ((-1,1),(1,-1)), ((0,-1),(0,1)) ):
            count = 1
            whose_piece = whose_turn
            try: 
                if board[drop_depth+increment[0]*1,drop_column+increment[1]*1] == whose_turn:
                    count +=1
                    try:
                        if board[drop_depth+increment[0]*2,drop_column+increment[1]*2] == whose_turn:
                            count += 1
                            try:
                                if board[drop_depth+increment[0]*3,drop_column+increment[1]*3] == whose_turn:
                                    count+=1
                            except IndexError:
                                pass
                    except IndexError:
                        pass
            except IndexError:
                pass
            
            try:
                if board[drop_depth+decrement[0]*1,drop_column+decrement[1]*1] == whose_turn:
                    count +=1
                    try:
                        if board[drop_depth+decrement[0]*2,drop_column+decrement[1]*2] == whose_turn:
                            count += 1
                            try:
                                if board[drop_depth+decrement[0]*3,drop_column+decrement[1]*3] == whose_turn:
                                    count+=1
                            except IndexError:
                                pass
                    except IndexError:
                        pass
            except IndexError:
                pass
                                
            if count >= 4:
                return True
    
    return False

#game loop
while(quit is not True):
    
    #print game state
    os.system('clear')
    print(board)
    print("")
    print(game_status)
    print("")
    print(input_options)
    print("")
    player_input = input("Enter one of the characters in brackets to select an option:")
    
    #advance game logic
    if player_input in ('1','2','3','4','5','6','7'):
        drop_column = int(player_input)-1
        if board[0][drop_column] != 0:
            game_status = "Whoops, column X is full. Player X, please select a different column."
        else:
            drop_depth = 5 - np.count_nonzero(board[:,drop_column])  
            board[drop_depth,drop_column] = whose_turn
                                    
            if check_winner(board,drop_depth,drop_column,whose_turn) is True:
                game_status = "Player " + str(whose_turn) + " wins! Enter [r] to restart or [q] to quit."
            
            elif np.count_nonzero(board) == 42:
                game_status = "The game is a draw! Enter [r] to restart or [q] to quit."
            
            else:
                game_status = "Player " + str(whose_turn) + " dropped a piece in column " + player_input + ". Player " + str(whose_turn %2 + 1) + ", it is your turn."
                whose_turn = whose_turn %2 +1
                    
    elif 'r' == player_input:
        board = np.zeros((6,7),dtype = 'int')
        whose_turn = 1
        game_status = starting_message
    
    elif 'q' == player_input:
        quit = True
        
    else:
        game_status = "Whoops, I didn't understand Player " + str(whose_turn) + "'s input. Please type a single character followed by enter."
        

