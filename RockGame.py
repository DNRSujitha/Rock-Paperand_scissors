import tkinter as tk
import random

# Tkinter window setup
root = tk.Tk()
root.title("AI Rock, Paper, Scissors")
root.geometry("450x400")
root.config(bg="#1e1e1e")

# Choices
choices = ["Rock", "Paper", "Scissors"]
user_history = {"Rock": 0, "Paper": 0, "Scissors": 0}
score = {"User": 0, "Computer": 0}

def predict_user_choice():
    # Predict the user's next move based on their most frequent choice
    if sum(user_history.values()) == 0:
        return random.choice(choices)
    predicted = max(user_history, key=user_history.get)
    # Return what beats the predicted move
    if predicted == "Rock":
        return "Paper"
    elif predicted == "Paper":
        return "Scissors"
    else:
        return "Rock"

def get_result(user_choice):
    user_history[user_choice] += 1
    computer_choice = predict_user_choice()

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        score["User"] += 1
    else:
        result = "Computer Wins!"
        score["Computer"] += 1

    result_label.config(text=f"Your Choice: {user_choice}\nComputer's Choice: {computer_choice}\n\n{result}", fg="white")
    score_label.config(text=f"Score - You: {score['User']} | Computer: {score['Computer']}", fg="white")

# UI Elements
title_label = tk.Label(root, text="AI-Enhanced Rock, Paper, Scissors", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="cyan")
title_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), bg="#444", fg="white",
                     command=lambda: get_result("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), bg="#444", fg="white",
                      command=lambda: get_result("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12), bg="#444", fg="white",
                         command=lambda: get_result("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#1e1e1e")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12, "bold"), bg="#1e1e1e")
score_label.pack()

# Run app
root.mainloop()
