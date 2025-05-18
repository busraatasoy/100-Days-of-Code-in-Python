# Step 4- Keeping Track of the Player’s Live

# Load the modul
import random

# Use ASCII chart for stages
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Word list
word_list = ["aardvark", "baboon", "camel"]

# TODO-1: -Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

 # - Randomly choose a wprd from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)

# Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Use a while loop to let the user guess again.
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()  # input from user

    display = ""

# Change the for loop so that you keep the previous  correct.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)  # add to the list
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

# TODO-2: -If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
# If lives goes down to 0 then the game shoukd stop and it should print "Yoy lose!"
    if guess not in chosen_word:
        lives -= 1
        if lives ==0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print(" You win!")

# TODO-3: -print the ASCII Chart from 'stages'
# that coeesponds to the currnt number of 'lives' the user has remaining.
    print(stages[lives])
