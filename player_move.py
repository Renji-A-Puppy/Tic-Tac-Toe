import board

def player_board_move():
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
            if board.board_table[row][col] in [board.cpu, board.player]:
                print(f"that spot already take please try again! ")
                continue
            board.board_table[row][col] = board.player
            board.print_board(board.board_table)
            return
        except:
            print("Invalid input")

'''
Line 1 Imports the board.
Line 2 Imports start.
Line 3 Imports introduction.
Line 5 creates a def function for player_board_move.
Line 6 is a while true.
Line 7 A variable taking the player's input and turning the string into an integer.
Line 10 mainly checks if a player's input is between 1-9.
Lines 11-12 make the person repeat if they didn't input a number between 1-9.
Line 13 subtracts a number because we know that the list starts at zero, which is mainly to make it more user-friendly.
Line 14 Is supposed to divide. 
Line 15 Is a module using reminders.
lines 16- 18 This checks if the spot is already taken, if it has an X or an O, it will make the Person repeat until they choose an open spot.
Line 19 Puts the value of the player's move and puts an O in the spot they choose.
Line 20 We are just printing the board.
Line 21 We are returning that
Line 22-23 If they input something invalid, the game would let them know.

'''
