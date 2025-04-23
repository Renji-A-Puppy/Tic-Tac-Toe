import introduction # imports the rulse of the game.
name = input("what is your name? ")
print ("ARF ARF,Nice to meet you " +name,"I\'m Ren, I\'m a puppy and I\'m really interested in playing tic-tac-toe.")
print ("_____________________________________________________________________________________________________________________________")
'''
line 1 importing the introduction
line 2 gets the player name so it's a more personal experience for the player.
Line 3 Just prints out some fun text and adds their it just a make it feel more personal and engaging.
Line 4 is mainly to not bunch up stuff, I'm using it as a separator to make the experience more readable. 
'''
# user_input = input
while True:
   print(f"would you like to play a game with me {name} 'Looks at you with puppy eyes'?")
   user_input = input("Yes or No?")
   if user_input.upper() == "NO" or user_input[0].lower() == "n":
      print("whaaaat where you just pulling my tail?'whimpers'", name ,  "I hope we can play sometime Good bye...")
      exit()
   
   elif user_input.lower() == "yes" or user_input[0].lower() == "y" or user_input.lower() == "sure":
      print ("_____________________________________________________________________________________________________________________________")
      introduction.instructions(name)
      break

   else:
      print ("_____________________________________________________________________________________________________________________________")
      print("invalid answer, please type yes/no. Try again.")
      print ("_____________________________________________________________________________________________________________________________")
      
      continue
'''
lines 12 - 27 I'm just asking if they want to play the game, if they put different values to yes's or No's, it'll accept them and proceed to instructions if yes's or exit if No's
If their response is not either a variant of yes or no, it'll prompt them to type and input the text asked.

'''

