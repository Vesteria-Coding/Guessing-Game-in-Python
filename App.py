import random
import tkinter as tk

# Set up numbers
mode = 10
secret_number = random.randint(1, mode)
print(f'Secret Number is {secret_number}')
loop_times = 0
max_attempts = 3

# GUI set up
root = tk.Tk()
root.title("Number Guessing Game")

# Allow the window to be resizable
root.geometry("300x250")
root.resizable(True, True)

def restart():
    """Restart the game by resetting variables and clearing the UI."""
    global mode, secret_number, loop_times
    secret_number = random.randint(1, mode)
    loop_times = 0
    entry.delete(0, tk.END)
    feedback_label.config(text="")
    label.config(text=f"Guess a number between 1 and {mode}")
    guess_button.config(state=tk.NORMAL)
    print("Game restarted!")

def easy_mode():
    """Switch to Easy mode and restart the game."""
    global mode
    mode = 5
    restart()

def normal_mode():
    """Switch to Normal mode and restart the game."""
    global mode
    mode = 10
    restart()

def hard_mode():
    """Switch to Hard mode and restart the game."""
    global mode
    mode = 25
    restart()

def get_input():
    """Get the input from the text field and process it."""
    global loop_times
    try:
        user_input = int(entry.get())
        if loop_times < max_attempts:
            if user_input > secret_number:
                feedback_label.config(text=f"{user_input} is too high!")
            elif user_input < secret_number:
                feedback_label.config(text=f"{user_input} is too low!")
            else:
                feedback_label.config(text="Correct! You guessed the number!")
                guess_button.config(state=tk.DISABLED)  # Disable guessing when correct
                entry.delete(0, tk.END)  # Clear the text box
                return
            loop_times += 1
        if loop_times >= max_attempts:
            feedback_label.config(
                text=f"You lost! The number was {secret_number}."
            )
            guess_button.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
    except ValueError:
        feedback_label.config(text="Please enter a valid number.")
        entry.delete(0, tk.END)

mode_frame = tk.Frame(root)
mode_frame.pack(fill=tk.X, pady=5)

easy_mode_button = tk.Button(mode_frame, text="Easy", width=12, pady=2, command=easy_mode)
easy_mode_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

normal_mode_button = tk.Button(mode_frame, text="Normal", width=12, pady=2, command=normal_mode)
normal_mode_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

hard_mode_button = tk.Button(mode_frame, text="Hard", width=12, pady=2, command=hard_mode)
hard_mode_button.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

# Main frame for game elements
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label = tk.Label(frame, text=f"Guess a number between 1 and {mode}")
label.grid(row=0, column=0, columnspan=2, pady=5)

entry = tk.Entry(frame, width=20)
entry.grid(row=1, column=0, pady=5, padx=5)

guess_button = tk.Button(frame, text="Guess!", command=get_input)
guess_button.grid(row=1, column=1, pady=5)

feedback_label = tk.Label(frame, text="", fg="blue")
feedback_label.grid(row=2, column=0, columnspan=2, pady=5)

restart_button = tk.Button(root, text="Restart", command=restart)
restart_button.pack(pady=10, fill=tk.X, expand=True)

root.mainloop()