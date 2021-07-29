from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzee")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text",
            fill=THEME_COLOR,
            font=("Aria", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        yes = PhotoImage(file="./images/true.png")
        self.yes_button = Button(image=yes, highlightthickness=0, command=self.yes_answer)
        self.yes_button.grid(row=2, column=0)

        no = PhotoImage(file="./images/false.png")
        self.no_button = Button(image=no, highlightthickness=0, command=self.no_answer)
        self.no_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz, final score: {self.quiz.score}/{self.quiz.question_number}")

    def yes_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def no_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



