from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=40, bg=YELLOW)


# Reset Timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")
    timer_label.config(text="Timer")
    tick_mark_label.config(text="")
    global reps
    reps = 0


# Timer MECHANISM
def count_start():
    global reps
    reps += 1

    short_break_sec = SHORT_BREAK_MIN * 60

    long_break_sec = LONG_BREAK_MIN * 60

    working_sec = WORK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)

    else:
        count_down(working_sec)
        timer_label.config(text="Work", fg=GREEN)


# Count_down Mechanism

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        count_start()
        marks = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += "✔"
        tick_mark_label.config(text=marks)


# UI design with tkinter

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

btn_stat = Button(text="Start", command=count_start, highlightthickness=0)
btn_stat.grid(column=0, row=2)

tick_mark_label = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
tick_mark_label.grid(column=1, row=3)

btn_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
btn_reset.grid(column=2, row=2)
window.mainloop()
