from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forword():
    tim.forward(15)


def move_up():
    tim.left(90)
    tim.forward(5)


screen.listen()
screen.onkey(key="space", fun=move_forword)
screen.onkey(key="b", fun=move_up)

screen.exitonclick()
