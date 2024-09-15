import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.", parent=window)

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def clear_all_tasks():
    listbox.delete(0, tk.END)


window = tk.Tk()
window.title("To-Do List Application")
window.configure(bg="#2d4155")
window.state("zoomed")

frame = tk.Frame(window, bd=5, relief="groove", bg="#1c2b36")
frame.pack(pady=60)

frame1 = tk.Frame(frame, bg="#1c2b36")
frame1.pack(pady=10)

listbox = tk.Listbox(
    frame1,
    width=50,
    height=10,
    bd=0,
    font=("Arial", 12),
    selectbackground="#4a7ebB",
    selectforeground="white",
    bg="#2d4155",
    fg="white",
    highlightthickness=0
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=(15,0))

scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(
    frame,
    font=("Arial", 12),
    width=45,
    bd=3,
    relief="groove",
    bg="#2d4155",
    fg="white",
    insertbackground='white'
)
entry.pack(pady=10)

button_frame = tk.Frame(frame, bg="#1c2b36", bd=3, relief="groove")
button_frame.pack(pady=20)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    width=15,
    bg="#d9534f",
    fg="white",
    font=("Arial", 12),
    command=add_task
)
add_button.grid(row=0, column=0, padx=10)

remove_button = tk.Button(
    button_frame,
    text="Remove Task",
    width=15,
    bg="#d9534f",
    fg="white",
    font=("Arial", 12),
    command=remove_task
)
remove_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    bg="#d9534f",
    fg="white",
    width=15,
    font=("Arial", 12),
    command=clear_all_tasks
)
clear_button.grid(row=0, column=2, padx=10)
window.mainloop()
