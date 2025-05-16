# Excaping the Maze Project

#TASK:
'''
Reeborg was exploring a dark maze and the battery in its flashlight ran out.
Write a program using an **`if/elif/else`** statement so Reeborg can find the exit.
The robot's position and direction are random. '''

#Solution Code  for Beginner Level in Python:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# Error Display:
# It works with this code. However; there may be no walls around the robot's starting position like this image. In this case, the code enters an infinite loop.

#Debugging to get out of infinite loop 
''' Solution Code  for Intermediate Level in Python:

- It is tested according to 3 cases including different world scenarios.
- Check out the relevant test source code
- To test the code, load the source from in the test files.'''


def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Debugging to get out of infinite loop   

while front_is_clear():  #This loop makes sure that the robot has a wall in front of it.
    move()
turn_left()              #If it's found a wall in front, we tell it to turn left to turn that wall on the right side of the robot.
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
