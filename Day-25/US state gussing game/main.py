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

        for sts in all_states:
            if sts not in states:
                missing_states.append(sts)
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


