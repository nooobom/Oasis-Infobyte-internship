import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4")
            return
        characters = ""
        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if digit_var.get():
            characters += string.digits

        if special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type")
            return
        password = []
        if upper_var.get():
            password.append(random.choice(string.ascii_uppercase))

        if lower_var.get():
            password.append(random.choice(string.ascii_lowercase))

        if digit_var.get():
            password.append(random.choice(string.digits))

        if special_var.get():
            password.append(random.choice(string.punctuation))

        while len(password) < length:
            password.append(random.choice(characters))
        random.shuffle(password)
        final_password = ''.join(password)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, final_password)
    except ValueError:
        messagebox.showerror("Error", "Enter a valid length")
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first")
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("500x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)
title_label = tk.Label(
    root,
    text="🔐 Advanced Password Generator",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title_label.pack(pady=15)
length_frame = tk.Frame(root, bg="#1e1e1e")
length_frame.pack(pady=10)

length_label = tk.Label(
    length_frame,
    text="Password Length:",
    font=("Segoe UI", 11),
    fg="white",
    bg="#1e1e1e"
)
length_label.pack(side="left", padx=5)

length_entry = tk.Entry(
    length_frame,
    width=10,
    font=("Segoe UI", 11),
    justify="center"
)
length_entry.pack(side="left")
length_entry.insert(0, "12")
options_frame = tk.LabelFrame(
    root,
    text="Password Options",
    font=("Segoe UI", 10, "bold"),
    fg="white",
    bg="#2d2d2d",
    padx=15,
    pady=10
)
options_frame.pack(padx=20, pady=10, fill="x")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

checkbox_style = {
    "bg": "#2d2d2d",
    "fg": "white",
    "selectcolor": "#3d3d3d",
    "activebackground": "#2d2d2d",
    "activeforeground": "white",
    "font": ("Segoe UI", 10)
}

tk.Checkbutton(
    options_frame,
    text="Include Uppercase Letters",
    variable=upper_var,
    **checkbox_style
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Include Lowercase Letters",
    variable=lower_var,
    **checkbox_style
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Include Numbers",
    variable=digit_var,
    **checkbox_style
).pack(anchor="w")

tk.Checkbutton(
    options_frame,
    text="Include Special Characters",
    variable=special_var,
    **checkbox_style
).pack(anchor="w")
generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Segoe UI", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
    cursor="hand2"
)
generate_btn.pack(pady=20)
password_entry = tk.Entry(
    root,
    width=35,
    font=("Consolas", 14),
    justify="center",
    bd=2
)
password_entry.pack(pady=10)
copy_btn = tk.Button(
    root,
    text="📋 Copy Password",
    command=copy_password,
    font=("Segoe UI", 11, "bold"),
    bg="#2196F3",
    fg="white",
    padx=10,
    pady=5,
    relief="flat",
    cursor="hand2"
)
copy_btn.pack(pady=10)
footer = tk.Label(
    root,
    text="Generate secure passwords instantly",
    font=("Segoe UI", 9),
    fg="gray",
    bg="#1e1e1e"
)
footer.pack(side="bottom", pady=10)
root.mainloop()
