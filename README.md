# 🧠 True/False Quiz Game (Python)

A simple **True/False quiz game** built in Python using **OOP principles**.  
Questions are stored in a separate `data.py` file and turned into `Question` objects, which are then used by the `QuizBrain` class to run the game.

---

## 🚀 Features
- Text-based True/False quiz in the terminal.
- Score tracking after every question.
- Case-insensitive input (`True/False` or `T/F`).
- Easy to extend — just add more questions in `data.py`.
- Clean structure following **Object-Oriented Programming**.

---

## 📂 Project Structure
quiz/
├── data.py # Stores question text and answers
├── question_model.py # Defines the Question class
├── quiz_brain.py # Quiz logic (iteration, scoring, validation)
├── main.py # Entry point to run the quiz
└── README.md # Project documentation

---

## 📦 Requirements
- Python **3.x**
- No external libraries required (uses only standard Python).

---

## ⚡ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Ayushb10212/quiz_start.git
   cd quiz_start
