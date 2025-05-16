#What is the Range Function?

# The range () function is used to generate a sequence of numbers and is commonly used with for loops.

#Basic Usage:
for i in range(5):  # Prints numbers from 0 to 4
    print(i)

#range() Parameters:
# 1. range(stop): Generates numbers from 0 to stop -1.
range(5)  # 0, 1, 2, 3, 4

# 2. range(start, stop): Generates numbers from start to stop -1.
range(2, 6)  # 2, 3, 4, 5

# 3. range(start, stop, step): Generates numbers from start to stop-1 with a step value.
range(1, 10, 2)  # 1, 3, 5, 7, 9

# 4. Counting backwards with a negative step:
range(10, 0, -2)  # 10, 8, 6, 4, 2

#In short, range() creates a sequence of numbers and is very useful in loops.

#Create loops with for and range:
for number in range(a, b):
      print(number)
