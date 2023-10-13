from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRONT_TITLE = ("Arial", 30, "italic")
FRONT_WORD = ("Arial", 45, "bold")
pick_word = {}

window = Tk()
window.title("The Flash Game")
window.config(padx=50, pady=40, bg=BACKGROUND_COLOR)

data = pandas.read_csv("./data/french_words.csv")
word_dict = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(learn_img, image=back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=pick_word["English"], fill="white")


# Retrive Data
def word_selection():
    global pick_word, flip_timer
    window.after_cancel(flip_timer)
    pick_word = random.choice(list(word_dict))
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=pick_word["French"], fill="black")
    canvas.itemconfig(learn_img, image=front_img)
    window.after(3000, func=flip_card)


flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
learn_img = canvas.create_image(400, 263, image=front_img)
back_img = PhotoImage(file="./images/card_back.png")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="", font=FRONT_TITLE)
word_text = canvas.create_text(400, 263, text="", font=FRONT_WORD)
canvas.grid(row=0, column=0, columnspan=2)

#button
wrong_img = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=wrong_img, highlightthickness=0, command=word_selection)
btn_wrong.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
btn_right = Button(image=right_img, highlightthickness=0, command=word_selection)
btn_right.grid(row=1, column=1)

word_selection()

window.mainloop()
