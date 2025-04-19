import board
import player_move

def cpu_move():
    while True:
            cpu_placment =
            placement_index = cpu_placement - 1
            row = placement_index // 3
            col = placement_index % 3
            if board.board_table[row][col] in ["O", "X"]:
                print(f"that spot already take please try again! ")
                continue
            board.board_table[row][col] = "X"


    