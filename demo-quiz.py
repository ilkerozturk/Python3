class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def is_correct(self, choice):
        return choice == self.answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        for question in self.questions:
            print(" ************* Question Number: " + str(self.questions.index(question) + 1) + " of " + str(len(self.questions)) + " *************"+ "\n")
            print(question.text + "\n")
            for i, choice in enumerate(question.choices):
                print(f"{i + 1}. {choice}")
                
            answer = input("Your answer (enter the number): ")
            if question.is_correct(question.choices[int(answer) - 1]):
                self.score += 1
        print(f"You scored {self.score} out of {len(self.questions)}")






q1 = Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris")
q2 = Question("What is 2 + 2?", ["3", "4", "5", "6"], "4")
q3 = Question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Saturn"], "Jupiter")

QuizApp = Quiz()
QuizApp.add_question(q1)
QuizApp.add_question(q2)
QuizApp.add_question(q3)
QuizApp.take_quiz()# A simple quiz application