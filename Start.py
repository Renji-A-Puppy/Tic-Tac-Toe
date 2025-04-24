import player_move
import cpu_move
import board
def the_game(name):
    turn = 0
    for turn in range(9):
        if turn % 2 == 0:
            print ("_____________________________________________________________________________________________________________________________")
            print(f"\n\n {name} Turn \n")
            print ("_____________________________________________________________________________________________________________________________")
            player_move.player_board_move()
        else:
            print ("_____________________________________________________________________________________________________________________________")
            print("\n\n Ren Turn \n")
            print ("_____________________________________________________________________________________________________________________________")
            cpu_move.cpu_board_move()
            board.print_board(board.board_table)
        
'''
Line 1 Imports player move
Line 2 Imports cpu_move
Line 3 Imports board

'''