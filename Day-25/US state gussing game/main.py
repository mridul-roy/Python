import turtle
import pandas

img = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("Welcome to US States Guessing game")
screen.addshape(img)
turtle.shape(img)

states = []
missing_states = []
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
while len(states) < 50:
    user_answer = screen.textinput(title=f"{len(states)}/50 States",
                                   prompt="What is the name of the States?").title()
    if user_answer == "Exit":
        missing_states = [sts for sts in all_states if not sts in states]
        learn_data = (pandas.DataFrame(missing_states))
        print(learn_data)
        break

    if user_answer in all_states:
        states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(user_answer)


"""
hello,this is totally fun to guess how many states you know about USA.

enter the name of state by saw the map and test your guessing score

to play this game go to this link:

link:https://replit.com/@mridulroy010/US-states-guessing-game?v=1

control:
you can enter as much as you can guess
to end of your guessing type "exit"
then you will saw your score & how many states you missed out.

enjoy. Fell free to feedback.Thank you  




"""