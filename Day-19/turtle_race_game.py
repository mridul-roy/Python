import random
import turtle
from turtle import Turtle, Screen

is_game_on = False

screen = turtle.Screen()
user_choose = turtle.textinput(title="Welcome to race", prompt="Which turtle you want to choose? Select by color: ")

screen.setup(height=500, width=700)

colors = ["red", "yellow", "green", "purple", "blue", "black", "red", "yellow", "green", "purple", "blue", "black"]

y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

screen.listen()

for turtle_index in range(1, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-340, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_choose:
    is_game_on = True

while is_game_on:

    for turtle in all_turtles:

        if turtle.xcor() > 320:
            winner_turtle = turtle.pencolor()
            is_game_on = False
            if user_choose == winner_turtle:
                print(f"You won the race with {user_choose} turtle")
            else:
                print(f"You lose in race.")
                print(f"The winner turtle is {winner_turtle}.")

        turtle_distance = random.randint(1, 10)
        turtle.forward(turtle_distance)

screen.exitonclick()
"""
You can play this game on replit
goto this link:
https://replit.com/@mridulroy010/turtleracegame?v=1

""""
