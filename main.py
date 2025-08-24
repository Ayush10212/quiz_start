# main.py
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def build_question_bank(data):
    bank = []
    for item in data:
        bank.append(Question(item["text"], item["answer"]))
    return bank

def main():
    question_bank = build_question_bank(question_data)
    quiz = QuizBrain(question_bank)

    print("Welcome to the True/False Quiz!\nType True/False or T/F.\n")
    while quiz.still_has_questions():
        quiz.next_question()

    print("Quiz Complete!")
    print(f"Your final score: {quiz.score}/{len(question_bank)}")

if __name__ == "__main__":
    main()
