def turn_right():
    turn_left()
    turn_left()
    turn_left()


def complete_step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(0,6):
    complete_step()
