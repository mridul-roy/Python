from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fd():
    tim.forward(10)


def move_back():
    tim.backward(10)


def move_clk():
    tim.left(10)


def move_anti_clk():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_clk)
screen.onkey(key="d", fun=move_anti_clk)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
