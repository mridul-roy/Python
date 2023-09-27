from turtle import Turtle,Screen


tommy = Turtle()
print(tommy)
tommy.shape("turtle")
tommy.color("green")
tommy.forward(100)
screen = Screen()
print(screen.canvheight)
screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = (["Pokemon_Names", "Types"])
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmandar","Fire"])
table.align = "l"


print(table)

