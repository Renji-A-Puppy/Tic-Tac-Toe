import board

def user_board_move():
    while True:
        placement = int(input(f"Pick a number 1-9: "))
        try:
            # placement = int(placement_str)
            if placement < 1 or placement > 9:
                print(f"Number is not between 1-9")
                continue
            placement_index = placement - 1
            row = placement_index // 3
            col = placement_index % 3
            if board.board_table[row][col] in ["O", "X"]:
                print(f"that spot already take please try again! ")
                continue
            board.board_table[row][col] = "O" 
            return
        except:
            print("Invalid input")


# user_board_move()
# board.print_board(board.board_table)

