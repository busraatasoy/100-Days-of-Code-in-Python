# Scenario: Creating a password based on information received from the user.

'''Hard Version:         

In the advanced version of this project the final password does not follow a pattern. So the example above might look like this: **x$dg*f9**
And every time you generate a password, the positions of the symbols, numbers, and letters are different.
This will make the password more difficult. '''

#Password Generator Project -Hard Level 

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

password_list = []

#nr_letters 
for char in range(0, nr_letters)                       #or use range(1, nr_letters +1) 
       password_list.append(random.choice(letters))         #choice() is used for random selection.     # use " += " or "append"

#nr_symbols      
for char in range(0, nr_symbols)                       #or use range(1, nr_symbols +1)             # use " += " or "append"
       password_list.append(random.choice(symbols))

#nr_numbers
for char in range(0, nr_numbers)                       #or use range(1, nr_numbers +1)             # use " += " or "append"
       password_list.append(random.choice(numbers)) 
       
print(password_list)

random.shuffle(password_list)                     #Mixing up information in a list
print(password_list) 

#Recreating string from information in a mixed list
password = ""
for char in password_list:
      password += char

#Print final password information
print(f"Your password is : {password})
