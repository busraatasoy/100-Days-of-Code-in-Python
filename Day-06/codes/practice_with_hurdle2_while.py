#TASK:

# As stated in the image; the robot will participate in a running race. The targeted finish line, i.e. the flag location, is variable.

#This task completed with 20 line code
def turn_right():
    turn_left()
    turn_left()
    turn_left()   

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():           #or at_goal !=True
    jump()
