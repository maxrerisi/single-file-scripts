import tkinter as tk
from tkinter import messagebox

# Flashcards dictionary
FLASHCARDS = {
    "Python": "A high-level programming language.",
    "Tkinter": "A standard GUI library for Python.",
    "Dictionary": "A collection of key-value pairs in Python."
}

# Initialize variables
flashcards = list(FLASHCARDS.items())
current_index = 0
show_term = True
show_definition = True

# Functions


def update_flashcard():
    term, definition = flashcards[current_index]
    if show_term and show_definition:
        flashcard_text.set(f"Term: {term}\nDefinition: {definition}")
    elif show_term:
        flashcard_text.set(f"Term: {term}")
    elif show_definition:
        flashcard_text.set(f"Definition: {definition}")
    else:
        flashcard_text.set("")


def flip_flashcard():
    global show_term, show_definition
    show_term = not show_term
    show_definition = not show_definition
    update_flashcard()


def mark_known():
    global current_index
    flashcards.pop(current_index)
    if not flashcards:
        messagebox.showinfo(
            "Great Job!", "You've mastered all the flashcards! Keep up the awesome work!")
        root.quit()
    else:
        current_index %= len(flashcards)
        update_flashcard()


def mark_unknown():
    global current_index
    flashcards.append(flashcards.pop(current_index))
    current_index %= len(flashcards)
    update_flashcard()


def toggle_term():
    global show_term
    show_term = not show_term
    update_flashcard()


def toggle_definition():
    global show_definition
    show_definition = not show_definition
    update_flashcard()


# Set up the GUI
root = tk.Tk()
root.title("Flashcard Application")

flashcard_text = tk.StringVar()
flashcard_label = tk.Label(
    root, textvariable=flashcard_text, width=50, height=10)
flashcard_label.grid(row=0, column=0, columnspan=2)

flip_button = tk.Button(root, text="Flip", command=flip_flashcard)
flip_button.grid(row=1, column=0)

known_button = tk.Button(root, text="Known", command=mark_known)
known_button.grid(row=1, column=1)

unknown_button = tk.Button(root, text="Unknown", command=mark_unknown)
unknown_button.grid(row=2, column=0)

toggle_term_button = tk.Button(root, text="Toggle Term", command=toggle_term)
toggle_term_button.grid(row=2, column=1)

toggle_definition_button = tk.Button(
    root, text="Toggle Definition", command=toggle_definition)
toggle_definition_button.grid(row=3, column=0, columnspan=2)

update_flashcard()
root.mainloop()
