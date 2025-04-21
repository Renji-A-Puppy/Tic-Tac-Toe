import board
import player_move
import random

def cpu_move():
    while True:
            cpu_placment = int(random.choices(board.board_table, [10, 1, 8, 5, 10, 6, 10 , 5 ,10])[0])

            cpu_placment_index = cpu_placment
            row = cpu_placment_index // 3
            col = cpu_placment_index % 3
            cpu_placment_index = "X"

            if board.board_table[row][col] in ["O", "X"]:
                print(f"that spot already take please try again! ")
                continue
            break
    

cpu_move()

    