# Step 2- Replacing Blanks with Guesses

#Load the modul
import random

#Word list
word_list = ["aardvark", "baboon", "camel"]

# - Randomly choose a wprd from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)


#TODO -1 -Create a "placeholder" with the same number of blanks as the chosen_word
placeholder =""
word_length = len(chosen_word)
for position in range(word_length)        
				placeholder += "_"
print(placeholder)


#input from user
guess = input("Guess a letter: ").lower()


#TODO -2 -Create a "display" that puts the guess letter in the right positions and _ in the rest of the string. 

display = ""

for letter in chosen_word:
      if letter == guess:
					display += letter
			else:
					display += "_"
print(display)	   
