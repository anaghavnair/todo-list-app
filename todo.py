import tkinter as tk
from tkinter import messagebox
from plyer import notification
import os

# --------- Functions ---------
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
        notification.notify(
            title="Task Added ✅",
            message=f"'{task}' was added to your To-Do list!",
            timeout=3
        )
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        save_tasks()
        notification.notify(
            title="Task Deleted ❌",
            message=f"'{task}' was removed from your list.",
            timeout=3
        )
    else:
        messagebox.showinfo("No Selection", "Please select a task to delete.")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        if not task.startswith("✅"):
            task = "✅ " + task
            task_listbox.delete(selected)
            task_listbox.insert(selected, task)
            save_tasks()
            notification.notify(
                title="Task Completed 🎉",
                message=f"Great job! '{task}' is marked as done.",
                timeout=3
            )

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())

# --------- GUI Setup ---------
root = tk.Tk()
root.title("📝 To-Do List App")
root.geometry("400x500")
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(root, font=("Arial", 14), width=28, bd=2)
task_entry.pack(pady=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f4f4f4")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", width=10, bg="#6fbf73", fg="white", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="Mark Done", width=10, bg="#4fa3d1", fg="white", command=mark_done)
done_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", width=10, bg="#e74c3c", fg="white", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Task Listbox
task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=15, bd=2, selectbackground="#a1d8f0")
task_listbox.pack(pady=10)

# Load tasks if tasks.txt exists
load_tasks()

# Start the main app
root.mainloop()


