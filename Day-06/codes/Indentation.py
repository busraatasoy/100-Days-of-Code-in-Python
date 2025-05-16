# What is the Indentation ?
    
# In Python, **indentation** is used to define the structure and hierarchy of the code. Unlike other programming languages that use curly braces `{}` to indicate blocks of code, Python relies on indentation (spaces or tabs) to group statements.
    
# Purpose of Indentation in Python:
'''    
1. **Defines Code Blocks:** It determines the start and end of control structures like loops, functions, and conditional statements.
2. **Improves Readability:** Enforces clean and readable code structure.
3. **Prevents Errors:** Incorrect indentation leads to `IndentationError`, making code consistency crucial. 
    
In Python, indentation is mandatory and defines the structure of the program. '''
    
# Create Indentation in Python -1:
def my_function():
. . . .print("Hello")    # Indented inside the function
. . . .print("World")    # Indented inside the function

# Create Indentation in Python -2:
def my_function():
. . . .print("Hello")    # Indented inside the function
print("World")    # Not indented inside the function

#Example Usage:
# Function with indentation
def say_hello():
    print("Hello!")  # Indented inside the function

# Conditional statement with indentation
age = 18
if age >= 18:
    print("You are an adult.")  # Indented inside if statement
else:
    print("You are a minor.")  # Indented inside else statement

# Loop with indentation
for i in range(3):
    print("Iteration:", i)  # Indented inside the loop

say_hello()

# Each indented block represents a logical structure, ensuring Python knows which statements belong together.

# How to Create Indentation in Python?

''' In Python, indentation is done using either tabs or spaces, but the convention is to use spaces. 
The PEP 8 style guide recommends using 4 spaces per indentation level.'''

# Tab vs. Space:
'''
- **Spaces (Recommended)**: Use 4 spaces for each indentation level.
- **Tabs**: A single tab can also be used, but mixing tabs and spaces in the same file is not recommended (it can cause errors).

# Tabs or Spaces?

- Spaces are the preferred indentation method.
- Tabs should be used solely to remain consistent with code that is already indented with tabs.
- Python disallows mixing tabs and spaces for indentation.

But luckily, **most code editors have a setting that allows you to indent using spaces, change the indentation size to four,** and **when you press the tab key, it will automatically add four spaces**, which you can tell when you try to highlight it.

You can see the cursor jump four times.

This means that you can press the tab key once and your code will conform to the grid, because behind the scenes your code editor will add four spaces. '''

# Option Code:
def my_function():
. .print("Hello")  # 2-space indentation

'''
This code works correctly because:

- The function **`my_function()`** is properly defined.
- The `print("Hello")` statement is **indented with 2 spaces**, which is still a valid indentation in Python.
- **Python requires consistent indentation but does not enforce a specific number of spaces.** While PEP 8 recommends **4 spaces**, using **2 spaces will still work as long as it is consistent throughout the code.**

Thus, **Option does not produce an IndentationError and runs without issues.** '''
