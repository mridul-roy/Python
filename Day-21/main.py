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
        is_game_on = False
        score_board.game_over()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increasing_score()

screen.exitonclick()
