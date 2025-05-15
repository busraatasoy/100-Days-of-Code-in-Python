# What is a List?
'''A **list** in Python is a built-in data structure that allows you to store multiple items in a **single variable**. 
Lists are **mutable** (modifiable) and can contain different data types, such as numbers, strings, and even other lists.

# Creating a List
# You can create a list using square brackets `[]`:

# Empty list
empty_list = []

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List with different data types
mixed_list = [10, "Python", 3.14, True]

# Nested list (list inside another list)
nested_list = [[1, 2, 3], [4, 5, 6]]

# **Adding & Removing Elements**

#Adding Elements:

my_list = [1, 2, 3]
my_list.append(4)               # Adds 4 at the end
my_list.insert(1, 10)           # Inserts 10 at index 1
my_list.extend([9, 8, 7])       #Adds more numbers at the end

# Removing Elements:

my_list.remove(2)  # Removes the first occurrence of 2
my_list.pop()  # Removes the last element
my_list.pop(1)  # Removes the element at index 1
del my_list[0]  # Deletes the first element

# Sorting and Reversing:

my_list.sort()  # Sorts the list in ascending order
my_list.reverse()  # Reverses the list


# Advantages of Using Lists:
Flexibility: Can store multiple data types.
Mutability: You can modify, add, or remove elements.
Fast Access: Elements can be accessed using indexing.
Loop-Friendly: Can be used easily with `for` and `while` loops. 

#Example usage loops:
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

#America States List :
# America states list:
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
"South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
"Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
"Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#Indexing is done to reach the first state:
print(states_of_america[0])
     
#Indexing is done to reach the last state:
print(states_of_america[-1])      


#Changing name in the list:
# America states list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
"South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
"Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
"Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#The name is changed:
states_of_america[1] = "Pelcilvania"      

print(states_of_america)  


#Length of the list: & Index Error:

# America states list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", 
"South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
"Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
"Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
"Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
"Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Lenght of the list
num_of_states = len(states_of_america)    #50 inputs

#Index Error- List index out of range
#Index sorting starts with 0. 
#That's why it gives an error when searching for the 50th input.
print(states_of_america[num_of_states])  

#Find the 50th input(last of the list) result
print(states_of_america[num_of_states - 1]) 

# Nested Lists
#List of foods high in pesticides
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

#List of fruits containing high pesticides
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

#List of vegetables containing high pesticides
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]


#New list for dirty_dozen with nested list
#1. Option
dirty_dozen = [fruits, vegetables]

#2. Option
dirty_dozen = [["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"], ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]]
