import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def create_task():
    task = task_entry.get()
    time = time_entry.get()
    
    if task and time:
        task_time = datetime.strptime(time, "%Y-%m-%d %H:%M")
        current_time = datetime.now()
        
        if task_time < current_time:
            messagebox.showerror("Invalid Time", "Please enter a future time for the task.")
        else:
            tasks.append((task, task_time))
            update_task_list()
    else:
        messagebox.showerror("Missing Information", "Please fill in both task and time fields.")

def update_task_list():
    task_list.delete(0, tk.END)
    for task, time in tasks:
        task_list.insert(tk.END, f"{task} - {time.strftime('%Y-%m-%d %H:%M')}")

def check_alerts():
    current_time = datetime.now()
    for task, time in tasks:
        if current_time + timedelta(minutes=1) >= time >= current_time:
            messagebox.showinfo("Task Alert", f"It's time for: {task}")

def start_alerts():
    check_alerts()
    root.after(60000, start_alerts)  # Check every minute

tasks = []

root = tk.Tk()
root.title("ToDo App")

task_label = tk.Label(root, text="Task:")
task_label.pack()

task_entry = tk.Entry(root)
task_entry.pack()

time_label = tk.Label(root, text="Time (YYYY-MM-DD HH:MM):")
time_label.pack()

time_entry = tk.Entry(root)
time_entry.pack()

add_button = tk.Button(root, text="Add Task", command=create_task)
add_button.pack()

task_list = tk.Listbox(root)
task_list.pack()

start_alerts()  # Start checking for alerts

root.mainloop()
