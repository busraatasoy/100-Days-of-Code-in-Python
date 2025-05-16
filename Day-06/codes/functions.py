# What is the function?
''' - In Python, **functions** are reusable blocks of code that perform a specific task.
    - They help organize code, improve readability, and avoid repetition.
    
**There are two main types of functions in Python:**
    
1. **Built-in functions** – Predefined functions like **`print**()`, **`len**()`, **`type**()`, etc.
2. **User-defined functions** – Custom functions created using the **`def`** keyword.'''
    
# Example of Built-in function:
print ("Hello")               #output : Hello

num_char = len("Hello")       #measuring length
print(num_char)               #output : 5

# Defining Functions:
#Define the function with def
#Then give a name (my_function or other)

def my_function():                
     #Do this                       #Define the code blocks
     #Then do this
     #Finally do this
my_function()                       #Calling the function

#Example of User-defined function:
def my_function():            #Create function
     print("Hello")
     print("Bye")
     
my_function()                 #Call the function
