from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.color("black")
        self.goto(-290, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level:{self.current_level}", align="left", font=FONT)

    def level_up(self):
        self.current_level += 1

    def game_end(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
