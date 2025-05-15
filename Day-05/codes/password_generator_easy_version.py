#Scenario: Creating a password based on information received from the user.

'''Easy Version:              

Generate thre password in sequence. Letters, then symbols, then numbers. 
If the user wants 4 letters 2 symbols and 3 numbers then the password might look like this:   **fgdx$*924**
You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. '''

#Password Generator Project -Easy Level 

#Load the module
import random

#List of the letters, numbers and symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Create the users inputs
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Create the password usage with loops

password = ""

#nr_letters = 4
for char in range(0, nr_letters)         #1 - 4     #or range(1, nr_letters +1) 
       password += random.choice(letters)           #choice() is used for random selection.

#nr_symbols      
for char in range(0, nr_symbols)              #or range(1, nr_symbols +1)   
       password += random.choice(symbols)

#nr_numbers
for char in range(0, nr_numbers)              #or range(1, nr_numbers +1)  
       password += random.choice(numbers) 
       
print(password)
