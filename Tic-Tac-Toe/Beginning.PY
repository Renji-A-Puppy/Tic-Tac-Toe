import player_move
import board

name = input("what is your name? ")#the user name for the entire game.
print ("ARF ARF,Nice to meet you " +name,"I\'m Ren, I\'m a puppy and I\'m really interested in playing tic-tac-toe.")
print ("_________________________________________________________________________________________________________")

user_input = input("continue?")

print("would you like to play a game with me 'Looks at you with puppy eyes'?")

def instructions():#the games instructions
     print("That\'s, Pawtastic 'wags tail eagerly!' let me explain the rules", name )
     print ("_________________________________________________________________________________________________________")
     print("The first player to get three of their mark in a row, either by horizontally, vertically, or diagonally, wins the game.'", name)
     print("'EXAMPLE BELOW'")# so basicall im goona have a board of 1-9 im not sure HOW im goinna do it
     print(["1", "2", "3"])          #(  0 1 2   )
     print(["4", "5", "6"])          #(  3 4 5   )
     print(["7", "8", "9"])          #(  6 7 8   )
     print ("_________________________________________________________________________________________________________")

while True:
  user_input = input("Yes or no?")
  if user_input.upper() == "NO" or user_input[0].lower() == "n":
     print("whaaaat where you just pulling my tail?'whimpers'", name)
     break
  
  elif user_input.lower() == "yes" or user_input[0].lower() == "y" or user_input.lower() == "sure":
     print("Then let the games begin best of luck to you ", name)
     instructions()
     break
  
  else:
     print("invalid answer, please type yes/no. Try again.")
    
     continue
   
user_input = input("continue")

user_input = input("'bark bark', I'll be X it's my favorite 'hugs the X symbol with joy':")