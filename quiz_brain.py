# quiz_brain.py
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False): ").strip()
        self.check_answer(user_answer, current_q.answer)

    def check_answer(self, user_answer: str, correct_answer: str):
        normalized_user = user_answer.lower()
        normalized_correct = correct_answer.lower()

        is_correct = (
            normalized_user == normalized_correct
            or (normalized_user in {"t", "true"} and normalized_correct == "true")
            or (normalized_user in {"f", "false"} and normalized_correct == "false")
        )

        if is_correct:
            self.score += 1
            print("Correct!")
        else:
            print(f"Wrong! Correct answer: {correct_answer}")
        print(f"Score: {self.score}/{self.question_number}\n")
