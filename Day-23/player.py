from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.turtle_r()

    def turtle_r(self):
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def strat_again(self):
        self.goto(STARTING_POSITION)
