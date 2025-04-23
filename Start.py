import player_move
import cpu_move
import board
def the_game():
    turn = 0
    for turn in range(9):
        if turn % 2 == 0:
            player_move.player_board_move()
        else:
           cpu_move.cpu_board_move()
        board.print_board()
        
'''
Line 1 Imports player move
Line 2 Imports cpu_move
Line 3 Imports board

'''