import tkinter as tk
from tkinter import messagebox
import os

FILENAME = "todo_tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())

# Save tasks to file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Add a new task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty.")

# Delete selected task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showinfo("Info", "No task selected.")

# Mark selected task as done
def mark_done():
    selected = task_listbox.curselection()
    if selected:
        current = task_listbox.get(selected[0])
        if not current.endswith(" ✅"):
            task_listbox.delete(selected[0])
            task_listbox.insert(selected[0], current + " ✅")
    else:
        messagebox.showinfo("Info", "Select a task to mark done.")

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.resizable(False, False)

# Input
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()
tk.Button(root, text="Mark as Done", command=mark_done).pack()

# Task list display
task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

# Save on close
def on_close():
    save_tasks()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# Load existing tasks
load_tasks()

# Run the app
root.mainloop()
