import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

game_is_on = True

while game_is_on:
    car.create_car()
    car.car_move()
    time.sleep(0.1)
    screen.update()

    for c in car.all_cars:

        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_end()

        elif player.ycor() == -290:
            player.strat_again()

        elif player.ycor() == 280:
            player.strat_again()
            car.spreed_up()
            scoreboard.level_up()
            scoreboard.update_level()

screen.exitonclick()
"""
hello, this is Turtle racing game
to play the game goto this link

https://replit.com/@mridulroy010/turtle-racinggame?v=1

game control:
Up(arrow) key to move up
Down (arrow) key to move down

constains:
If turtle hit the car then game over
"""
