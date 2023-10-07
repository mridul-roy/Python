import turtle
from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("Welcome to classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset_game()
        snake.reset()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            score_board.reset_game()
            snake.reset()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increasing_score()

screen.exitonclick()

"""
hello, this is basic 'classic Snake game'
to play this game click in this link

Link: https://replit.com/@mridulroy010/Classic-Snake-game?v=1

Constrains:

If hit the wall game over
If hit on snake body game over

Score:
Hit the food and get 1 point

game Control :
use Up (arrow) key to move up
use Down (arrow) key to move down
use Left(arrow) key to move Left
use Right(arrow) key to move Right

"""