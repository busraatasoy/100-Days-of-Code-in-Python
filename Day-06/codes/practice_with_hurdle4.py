#TASK:

#The position, the height and the number of hurdles changes each time this world is reloaded.
#The walls and height of walls in the image are variable.

def turn_right():
    turn_left()
    turn_left()
    turn_left()   

def jump():
    turn_left()
    while wall_on_right:
        move()    
    turn_right()
    move()
    
    turn_right()
    
    while front_is_clear():
        move()
    
    turn_left()
    

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
      
