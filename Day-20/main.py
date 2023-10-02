import turtle
from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Welcome to classic Snake Game")
screen.tracer(0)


snake = Snake()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()



screen.exitonclick()
