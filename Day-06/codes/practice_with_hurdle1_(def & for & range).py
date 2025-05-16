# TASK:
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.

#Lines of code written without using the def function:
#This task completede with 77 line code
move()
turn_left()
move()
turn_left()
turn_left()
turn_left() 
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()

move()
turn_left()
move()
turn_left()
turn_left()
turn_left() 
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()

move()
turn_left()
move()
turn_left()
turn_left()
turn_left() 
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()

move()
turn_left()
move()
turn_left()
turn_left()
turn_left() 
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()

move()
turn_left()
move()
turn_left()
turn_left()
turn_left() 
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()

move()
turn_left()
move()
turn_left()
turn_left()
turn_left() 
move()
turn_left()
turn_left()
turn_left()
move()
turn_left()


#Lines of code written using the def function:
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
jump()
jump()
jump()
jump()
jump()
jump()


#Lines of code written using the def function, for  and range:
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
