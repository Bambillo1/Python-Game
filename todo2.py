import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

def create_task():
    task = task_entry.get()
    time = time_entry.get()
    
    if task and time:
        try:
            task_time = datetime.strptime(time, "%Y-%m-%d %H:%M")
            current_time = datetime.now()
            
            if task_time < current_time:
                messagebox.showerror("Invalid Time", "Please enter a future time for the task.")
            else:
                tasks.append((task, task_time))
                update_task_list()
        except ValueError:
            messagebox.showerror("Invalid Format", "Please enter time in the format YYYY-MM-DD HH:MM.")
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

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

task_label = tk.Label(frame, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)

task_entry = tk.Entry(frame)
task_entry.grid(row=0, column=1, padx=5, pady=5)

time_label = tk.Label(frame, text="Time (YYYY-MM-DD HH:MM):")
time_label.grid(row=1, column=0, padx=5, pady=5)

time_entry = tk.Entry(frame)
time_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Add Task", command=create_task)
add_button.grid(row=2, columnspan=2, padx=5, pady=5)

task_list = tk.Listbox(frame, width=40)
task_list.grid(row=3, columnspan=2, padx=5, pady=5)

start_alerts()  # Start checking for alerts

root.mainloop()
