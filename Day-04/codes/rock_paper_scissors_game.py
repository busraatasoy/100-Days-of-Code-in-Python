'''Scenario: You are going to vuild a Rock, Paper, Scissors game. You will need to use randomisaiton and Lists to achive this.

Game Rules:
- Players deliver hand signals representing rock, paper, or scissors, with the outcome determined by these three rules:
1. Rock wins against scissors.
2. Scissors win against paper.
3. Paper wins against rock '''

#import the module
import random

#Adds ASCII Chart for rock, paper and scissors.

rock = '''
    -------
---'   ----)
      (-----)
      (-----)
      (----)
---.--(---)

       '''
       
paper = '''
     -------
---'    ----)----
           ------)
          --------)
         --------)
---.-----------)

          '''
         
         
scissors = '''
    -------
---'   ----)----
          ------)
       ----------)
      (----)
---.--(---)
           '''

#Adds game image list
game_images = [rock, paper, scissors] 

#The user is given a choice.
user_choice = int(input("What do you choose? 
Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Validate input
if user_choice not in [0, 1, 2]:
    print("You typed an invalid number.❗ You lose!😥")  
    exit()  # Stop the game

# Print the user's choice.
print("You chose:")
print(game_images[user_choice])          

#Computer choice with the Randint() function
computer_choice =random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])                #Print the computer's choice

#Create game rules   
if (user_choice == 0 and computer_choice == 2) or \
   (user_choice == 1 and computer_choice == 0) or \
   (user_choice == 2 and computer_choice == 1):
    print("You win! 🎉")
elif user_choice == computer_choice:
    print("It's a draw 🤝")
else:
    print("You lose! 😥")
    
