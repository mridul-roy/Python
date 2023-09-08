def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front():
        turn_right() 
    elif right_is_clear():
        #turn_left()
        move()
        turn_left()
        
        
    else:
        move()
        
        
        