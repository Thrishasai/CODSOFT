import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.score = 0
        self.current_question = 0
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["London", "Berlin", "Paris", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "What is 2 + 2?",
                "choices": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "how many wonders are there in the world??",
                "choices": ["6", "7", "10", "8"],
                "answer": "7"
            },
        ]
        
        self.label_question = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400, justify="center")
        self.label_question.pack(pady=20)
        
        self.var_choice = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var_choice, value="", font=("Helvetica", 12))
            self.radio_buttons.append(rb)
            rb.pack(anchor="w")
        
        self.button_submit = tk.Button(root, text="Submit", command=self.submit_answer)
        self.button_submit.pack(pady=10)
        
        self.label_feedback = tk.Label(root, text="", font=("Helvetica", 12))
        self.label_feedback.pack(pady=10)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.label_question.config(text=question["question"])
            choices = random.sample(question["choices"], len(question["choices"]))
            for i in range(4):
                self.radio_buttons[i].config(text=choices[i], value=choices[i])
            self.var_choice.set("")
            self.label_feedback.config(text="")
        else:
            self.show_final_results()
    
    def submit_answer(self):
        if self.var_choice.get():
            question = self.questions[self.current_question]
            user_answer = self.var_choice.get()
            correct_answer = question["answer"]
            
            if user_answer == correct_answer:
                self.score += 1
                feedback = "Correct!"
            else:
                feedback = f"Incorrect. The correct answer is: {correct_answer}"
            
            self.label_feedback.config(text=feedback)
            
            self.current_question += 1
            self.load_question()
    
    def show_final_results(self):
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
