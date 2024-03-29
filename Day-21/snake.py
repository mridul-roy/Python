from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_STEPS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.shapesize(0.8, 0.8)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg_num - 1].xcor()
            y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_position, y_position)

        self.head.forward(MOVING_STEPS)

    def reset(self):
        for seg in self.segments:
            seg.goto(900,900)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
