from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreborad import Scoreborad
import time

screen = Screen()
screen.title("The Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
scoreborad = Scoreborad()

screen.listen()

screen.onkey(l_paddle.move_up, "Up")
screen.onkey(l_paddle.move_down, "Down")
screen.onkey(r_paddle.move_up, "w")
screen.onkey(r_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 40 and ball.xcor() > -390 or ball.distance(l_paddle) < 40 and ball.xcor() > 340:
        ball.x_bounce()

    # left side tong missed
    if ball.xcor() > 390:
        ball.reset_position()
        scoreborad.l_point()

    # right side tong missed
    if ball.xcor() < -390:
        ball.reset_position()
        scoreborad.r_point()

screen.exitonclick()

"""
hello, if you want to play this pong game go to this link:
https://replit.com/@mridulroy010/the-pong-game?v=1

to control paddle use 
for Right paddle:
-----------------
Up (arrow) key to move UP
Down (arrow) key to move DOWN


for Left paddle:
----------------
w (small_letter) key to move UP
s (small_letter) key to move DOWN


feel free to give a feedback on comments.Thank you.
"""
