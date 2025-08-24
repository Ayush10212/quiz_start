# question_model.py
class Question:
    def __init__(self, q_text: str, q_answer: str):
        self.text = q_text
        self.answer = q_answer

    def __repr__(self) -> str:
        # Helpful when printing a list of Question objects
        return f"Question(text={self.text!r}, answer={self.answer!r})"
