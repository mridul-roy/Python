from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.create_car()
        self.moving_spreed = STARTING_MOVE_DISTANCE
        self.car_move()

    def create_car(self):
        ran_choose = random.randint(1, 8)
        if ran_choose == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setposition(x=280, y=0)
            y_position = random.randint(-260, 260)
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.setheading(-180)
            car.forward(self.moving_spreed)

    def spreed_up(self):
        self.moving_spreed += MOVE_INCREMENT
