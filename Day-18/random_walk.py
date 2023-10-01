import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

turtle.colormode(255)

# color_list = ["dark green","dark olive green","green yellow","cyan","yellow","purple","medium blue","red","deep pink"]

direction = [0, 90, 180, 270]
tim.speed(30)


def color_mode():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rd_color = (r, g, b)
    return rd_color


for _ in range(200):
    tim.pensize(8)
    tim.forward(25)
    tim.setheading(random.choice(direction))
    # tim.color(random.choice(color_list))
    tim.color(color_mode())

color_mode()

screen = Screen()
screen.exitonclick()
