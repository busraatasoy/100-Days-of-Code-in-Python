#TASK:**

# Reeborg has entered a hurdles race. Make him run the course, following the path shown.

#Let's try the robot route sample codes that we practiced before with while.
#Using For Loop:

#This task completed with 17 line code
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

for step in range(6):
    jump()

# Using While Loop:
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

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print("number_of_hurdles")
