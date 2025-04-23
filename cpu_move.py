import board
import player_move
import random

def cpu_move():
    while True:
        cpu_board = sum(board.board_table, [])
        cpu_placment = int(random.choices(cpu_board, [10, 1, 8, 5, 10, 6, 10 , 5 ,10])[0])



        row = cpu_placment // 3
        col = cpu_placment % 3
        
        if board.board_table[row][col] in [board.cpu, board.player]:
            continue
        else:
            board.board_table[row][col] = board.cpu
            break


cpu_move()
'''
It's not finished yet, I will explain more when it's working.
Line 8 is supposed to use random choices to give weights for the CPU move.
Line 7 is supposed to flatten the board. Line 8 needs it, I think.
Line 12 is supposed to divide. 
Line 13 is a module using reminders.
Lines 12-13 are supposed to put the correct symbol on the board.
Lines 15-16 are supposed to prevent you from putting a symbol in an already claimed spot.
17-19  Takes the value of the number and places that value with an X.

'''
    