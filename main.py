import tkinter
import random

# Main Window
screen = tkinter.Tk()
screen.title("Number Guessing Game")
screen.minsize(500, 500)
screen.config(padx=50, pady=50)

# Random Number (Global Variable)
target_number = random.randint(1, 100)
attempts = 0

# Input
guess_entry = tkinter.Entry(width=15)
guess_entry.grid(row=0, column=1, padx=10, pady=10)

tkinter.Label(text="Guess (1-100):", font=("Arial", 18)).grid(row=0, column=0)

# Output
result_label = tkinter.Label(text="Try guessing!", font=("Arial", 15))
result_label.grid(row=2, column=1, padx=10, pady=5)

attempts_label = tkinter.Label(text="Attempts: 0", font=("Arial", 15))
attempts_label.grid(row=3, column=1, padx=10, pady=5)

# Check Function
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        if guess < 1 or guess > 100:
            result_label.config(text="Out of range! (1-100)")
            return

        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if guess < target_number:
            result_label.config(text="Too Low!")
        elif guess > target_number:
            result_label.config(text="Too High!")
        else:
            result_label.config(text=f"🎉 Correct! It took {attempts} tries!")
    except ValueError:
        result_label.config(text="Invalid Input! Enter a number.")

# Reset Function
def reset_game():
    global target_number, attempts
    target_number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, 'end')
    result_label.config(text="Try guessing!")
    attempts_label.config(text="Attempts: 0")

# Buttons
tkinter.Button(text="Check", command=check_guess, font=("Arial", 16)).grid(row=1, column=1)
tkinter.Button(text="Reset", command=reset_game, font=("Arial", 16)).grid(row=4, column=1, pady=20)

screen.mainloop()
