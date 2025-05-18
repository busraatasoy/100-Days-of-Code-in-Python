#Step 3- Checking if the Player has Won

#Load the modul
import random

#Word list
word_list = ["aardvark", "baboon", "camel"]

# - Randomly choose a wprd from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)


#Create a "placeholder" with the same number of blanks as the chosen_word
placeholder =""
word_length = len(chosen_word)
for position in range(word_length)        
				placeholder += "_"
print(placeholder)


# TODO -1 -Use a while loop to let the user guess again.
game_over = False
correct_letters = []

while not game_over:
			guess = input("Guess a letter: ").lower()     #input from user
	   
	   display = ""

#TODO -2 -Change the for loop so that you keep the previous  correct.

   			for letter in chosen_word:
				    if letter == guess:
									display += letter
									correct_letters.append(guess)        #add to the list
						elif letter in correct letters:
						      	display += letter
				
						else:
									display += "_"
			print(display)
			
			if "_" not in display:
			      game_over = True
			      print(" You win!")
			      
