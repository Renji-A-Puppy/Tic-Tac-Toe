import board
import random

def cpu_board_move():
    while True:
        cpu_board = [num for num in sum(board.board_table, []) if num.isdigit()]
        weights = []
        for spot in cpu_board:
            if spot == "5":
                weights.append(10)
            elif spot in ["1", "9", "7", "3"]:
                weights.append(8)
            else:
                weights.append(3)
        cpu_placment = int(random.choices(cpu_board, weights)[0])

        row = (cpu_placment - 1) // 3
        col = (cpu_placment - 1) % 3 

        if board.board_table[row][col] in [board.cpu, board.player]:
            continue
        else:
            board.board_table[row][col] = board.cpu
            break


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