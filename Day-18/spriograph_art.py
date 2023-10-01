import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('classic')
tim.speed(50)
turtle.colormode(255)


def set_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color


for _ in range(100):
    tim.color(set_color())
    tim.circle(100, 360)
    tim.left(5)

# set_color()
screen = Screen()
screen.exitonclick()
