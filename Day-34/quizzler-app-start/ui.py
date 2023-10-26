from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UiInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20)
        self.window.config(width=300, height=250, bg=THEME_COLOR)

        self.score_lbl = Label(text=f"Score:{self.quiz.score}", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_lbl.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_lbl = self.canvas.create_text(
            150,
            130,
            width=280,
            text="Hello,I am come from UI",
            font=("Arial", 15, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        right_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=right_img, highlightthickness=0, command=self.ans_true)
        self.true_btn.grid(column=0, row=2)

        wrong_img = PhotoImage(file="./images/false.png")
        self.wrong_btn = Button(image=wrong_img, highlightthickness=0, command=self.ans_false)
        self.wrong_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_lbl, text=q_text)
            self.score_lbl.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text_lbl,
                                   text=f"You have reached the final round\n &"
                                        f""f"Your final Score is {self.quiz.score}/ {self.quiz.question_number} ")

            self.true_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def ans_true(self):
        is_right = self.quiz.check_answer("True")
        self.ans_feedback(is_right)

    def ans_false(self):
        is_right = self.quiz.check_answer("False")
        self.ans_feedback(is_right)

    def ans_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.canvas.after(1000, self.get_next_question)
