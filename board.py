

cpu = "X"
player = "O"

board_table = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def print_board(board):
    for i, row in enumerate(board):
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
            
'''
Line 3 defines the CPU symbol.
Line 4 defines the Player symbol.
Lines 6-10 are part of the board, using a list of lists for the game
Lines 12-16 make the board look pretty, adding | and + marks in between the numbers.
'''