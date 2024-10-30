import tkinter as tk
from tkinter import messagebox

# Initialize the flashcard storage
flashcards = {}

# Function to add a flashcard


def add_flashcard():
    question = question_entry.get()
    answer = answer_entry.get()
    if question and answer:
        flashcards[question] = answer
        question_entry.delete(0, tk.END)
        answer_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Flashcard added successfully!")
    else:
        messagebox.showwarning(
            "Input Error", "Both question and answer are required.")

# Function to view a random flashcard


def view_flashcard():
    if flashcards:
        question, answer = flashcards.popitem()
        question_label.config(text=f"Question: {question}")
        answer_label.config(text=f"Answer: {answer}")
    else:
        messagebox.showinfo(
            "No Flashcards", "No flashcards available. Please add some.")

# Function to delete a specific flashcard


def delete_flashcard():
    question = question_entry.get()
    if question in flashcards:
        del flashcards[question]
        messagebox.showinfo("Success", f"Flashcard '{question}' deleted.")
    else:
        messagebox.showwarning("Not Found", "Flashcard not found.")


# Set up the GUI
root = tk.Tk()
root.title("Flashcard Application")

# Question Entry
tk.Label(root, text="Question:").grid(row=0, column=0)
question_entry = tk.Entry(root, width=50)
question_entry.grid(row=0, column=1)

# Answer Entry
tk.Label(root, text="Answer:").grid(row=1, column=0)
answer_entry = tk.Entry(root, width=50)
answer_entry.grid(row=1, column=1)

# Add Button
add_button = tk.Button(root, text="Add Flashcard", command=add_flashcard)
add_button.grid(row=2, column=0, columnspan=2, pady=5)

# View Button
view_button = tk.Button(root, text="View Flashcard", command=view_flashcard)
view_button.grid(row=3, column=0, columnspan=2, pady=5)

# Delete Button
delete_button = tk.Button(
    root, text="Delete Flashcard", command=delete_flashcard)
delete_button.grid(row=4, column=0, columnspan=2, pady=5)

# Labels for displaying question and answer
question_label = tk.Label(root, text="Question: -", font=("Arial", 12))
question_label.grid(row=5, column=0, columnspan=2, pady=5)
answer_label = tk.Label(root, text="Answer: -", font=("Arial", 12))
answer_label.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
