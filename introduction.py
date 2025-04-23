import Start

def instructions(name):
     print("That\'s, Pawtastic 'wags tail eagerly!' let me explain the rules! ", name )
     print("_____________________________________________________________________________________________________________________________")
     print("1. Tic Tac Toe is a game where players play on a 3x3 board with 9 possible spots to choose from.                             ")
     print("                                                                                                                             ")
     print("2. The game alternates between players and you're not allowed to pick a spot that's already taken.                           ")
     print("                                                                                                                             ")
     print("3. The first player to get three of their marks in a row, either horizontally, vertically, or diagonally, wins the game.     ")
     print("                                                                                                                             ")
     print("4. You play the game by typing a number 1-9 to place your mark in the terminal.                                              ")
     print("                                                                                                                             ")
     print("5. If there are no spots left and neither player has 3 of their marks the game ends in a draw.                               ")                                                                 
     print("_____________________________________________________________________________________________________________________________")
     print("'EXAMPLE BELOW'")# so basicall im goona have a board of 1-9 im not sure HOW im goinna do it
     print(["1", "2", "3"])          #(  0 1 2   )
     print(["4", "5", "6"])          #(  3 4 5   )
     print(["7", "8", "9"])          #(  6 7 8   )
     print ("_________________________________________________________________________________________________________")
     
     Start.player_turn()
     '''
     Line 1 importing the star of the game
     Line 3 a def function for introduction
     Line 4 prints some personal/ fun text to engage the user more in the game.
     Lines 5-15 contain instructions that explain the rules, the spaces, and the lines, to make it more readable for the user.
     Lines 16-20 mainly show what the game board looks like and give them an understanding of how the board is set up.
     Line 22 sends you to the start of the game and into the player's turn.
     '''


# while True:
#   user_input = input("Yes or no?")
#   if user_input.upper() == "NO" or user_input[0].lower() == "n":
#      print("whaaaat where you just pulling my tail?'whimpers'", name)
#      break
  
#   elif user_input.lower() == "yes" or user_input[0].lower() == "y" or user_input.lower() == "sure":
#      print("Then let the games begin best of luck to you ", name)
#      instructions()
#      break
  
#   else:
#      print("invalid answer, please type yes/no. Try again.")
    
#      continue