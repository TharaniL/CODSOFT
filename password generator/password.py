import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError
        password = generate_password(length)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid length (positive integer).")

root = tk.Tk()
root.title("Password Generator")
root.state("zoomed")
root.resizable(False, False)
root.configure(bg='#e0f7fa')

style = ttk.Style()
style.configure('TButton', padding=10, relief='flat', background='#00796b', foreground='white', font=('Helvetica', 12, 'bold'))
style.configure('TEntry', padding=10, relief='flat', font=('Helvetica', 12))
style.configure('TFrame', background='#ffffff')

frame = ttk.Frame(root, padding="20", relief='flat', borderwidth=2, style='TFrame')
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame, text="Password Length:", font=('Helvetica', 16, 'bold'), background='#ffffff', foreground='#00796b').grid(row=0, column=0, padx=10, pady=10, sticky='w')

length_entry = tk.Entry(frame, font=('Helvetica', 12), bg='#e0f2f1', fg='#00796b', bd=2, relief='groove')
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(frame, text="Generate Password", command=generate, font=('Helvetica', 12, 'bold'), bg='#00796b', fg='white', relief='flat')
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(frame, text="Generated Password:", font=('Helvetica', 16, 'bold'), background='#ffffff', foreground='#00796b').grid(row=2, column=0, padx=10, pady=10, sticky='w')

password_entry = tk.Entry(frame, font=('Helvetica', 12), bg='#e0f2f1', fg='#00796b', bd=2, relief='groove', width=50)
password_entry.grid(row=2, column=1, padx=10, pady=10)

frame.configure(borderwidth=4, relief='groove')

root.mainloop()
