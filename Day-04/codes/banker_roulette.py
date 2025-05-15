#Banker Roulette Game

''' Scenario:  You went to a restaurant with your friends.
You played a game while paying the bill.
Everyone put their credit cards on the table in a mixed manner.
You asked the waiter to choose a random card.
The owner of the chosen card will pay the entire bill.'''

# import the random module
import random

# List of friends
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1: Using the choice() function
chosen_friend = random.choice(friends)
print(f"The chosen one to pay the bill is: {chosen_friend}")

# Option 2: Using randint() function
random_index = random.randint(0, len(friends) - 1)
print(f"The chosen one to pay the bill is: {friends[random_index]}")
