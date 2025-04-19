

cpu = "x"
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
            
print_board(board_table)