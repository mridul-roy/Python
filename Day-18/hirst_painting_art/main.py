import random
import random
import turtle
# import colorgram
# from colorgram import *
from turtle import Turtle, Screen

# rgb_color = []
#
# img_color = colorgram.extract("image.jpg", 30)
#
#
# for color in img_color:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

rgb_color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82),
                  (4, 211, 101), (3, 138, 64), (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251),
                  (211, 106, 5), (35, 35, 252), (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56),
                  (216, 114, 171), (16, 127, 144), (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215),
                  (99, 8, 50), (231, 163, 205), (204, 119, 35), (112, 6, 4)]

tim = turtle.Turtle()
tim.shape("classic")
turtle.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(230)
tim.forward(300)
tim.setheading(0)
tim.speed("fastest")

for dot_count in range(1, 100 + 1):
    tim.dot(20, random.choice(rgb_color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

    # tim.fillcolor(color)

screen = Screen()
screen.exitonclick()
""""
to run the code you need to install turtle library
to find the colour code , can use colorgram library

"""