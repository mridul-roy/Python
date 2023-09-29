class QuizBrain:

    def __init__(self, question_list):
        self.quiz_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_a_question(self):
        if self.quiz_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.quiz_number]
        self.quiz_number += 1
        user_answer = input(f"Q.{self.quiz_number}:{current_question.text} ('True/False'): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"You get the right answer.")
        else:
            print(f"You are wrong.")
            print(f"Correct answer is {correct_answer}")

        print(f"Your score is {self.score} / {self.quiz_number}")
        print("\n")
