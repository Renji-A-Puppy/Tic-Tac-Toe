# line 2 importing the introduction.
import introduction
# line 4 gets the player name so it's a more personal experience for the player.
name = input("what is your name? ")
# Line 6 Just prints out some fun text and adds their it just a make it feel more personal and engaging.
print ("ARF ARF,Nice to meet you " +name,"I\'m Ren, I\'m a puppy and I\'m really interested in playing tic-tac-toe.")
# Line 8 is mainly to not bunch up stuff, I'm using it as a separator to make the experience more readable.
print ("_____________________________________________________________________________________________________________________________")


while True:
   #Line 15 prints some fun text, and it also calls the name of the person.
   print(f"would you like to play a game with me {name} 'Looks at you with puppy eyes'?")
   #Line 17 asks for some input from the player. 
   user_input = input("Yes or No?")
      #Line 19 an if statement that takes the user input for NO, and it converts the capitalization so any variant of no should work.
   if user_input.upper() == "NO" or user_input[0].lower() == "n":
      #Line 21 Just print some fun text when a negative response is used example. NO.
      print("whaaaat where you just pulling my tail?'whimpers'", name ,  "I hope we can play sometime Good bye...")
      #Line 23 exit the game if their response is negative, for example, NO.
      exit()
   #Line 23 is an elif statement that takes the user input for YES, and it converts the capitalization so any variant of yes should work.
   elif user_input.lower() == "yes" or user_input[0].lower() == "y" or user_input.lower() == "sure":
      ##Line 24 helps people be able to read the terminal better when playing tic-tac-toe.
      print ("_____________________________________________________________________________________________________________________________")
      #Line 27 calls for the instructions function in the introduction file to proceed with the game.
      introduction.instructions(name)
      #Line 29 we break out of this while true since we got a Yes .
      break
      #  Line 31-36 This else statement happens when the player doesn't put a yes or NO, it also has some separation so it's easily readable.
   else:
      print ("_____________________________________________________________________________________________________________________________")
      print("invalid answer, please type yes/no. Try again.")
      print ("_____________________________________________________________________________________________________________________________")
      #Line 36 it'll keep looping until it gets to correct responses
      continue

