from turtle import Turtle, Screen
import random

tommy = Turtle()

tommy.shape('turtle')
# tommy.color('red')
# draw a square
# for _ in range(4):
#     tommy.forward(100)
#     tommy.right(90)

# draw dashed line for 15 times

# for _ in range(15):
#     tommy.color("black")
#     tommy.forward(10)
#     tommy.color("white")
#     tommy.forward(10)

color_list = ["dark green", "dark olive green", "green yellow", "cyan", "yellow", "purple", "medium blue", "red",
              "deep pink"]


# generate different shapes with random color
def shape_generator(num_of_side):
    angle = 360 / num_of_side
    for _ in range(num_of_side):
        tommy.forward(100)
        tommy.right(angle)


tommy.speed(10)

for n in range(3, 11):
    tommy.color(random.choice(color_list))
    shape_generator(n)

screen = Screen()
screen.exitonclick()
