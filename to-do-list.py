import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk. END, task)
        entry.delete(0, tk. END)
    else: messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk. END)

# Createthe main window

root = tk.Tk()

root.title("To-Do List")
root.config(bg='gold')
# Create widgets

entry= tk.Entry(root, width=40)
add_button= tk.Button(root, text="Add Task",bg = "light green", command = add_task)
remove_button = tk.Button(root, text="Remove Task",bg = "light blue", command = remove_task)
clear_button= tk.Button(root, text="Clear All",bg = "pink", command = clear_tasks)
listbox = tk.Listbox (root, width=40)

# Place widgets on the grid
entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=1, column=0, padx=10, pady=10)
remove_button.grid(row=2, column=0, padx=10, pady=10)
clear_button.grid(row=3, column=0, padx=10, pady=10)
listbox.grid(row=4, columnspan=4, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
