from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            color = "#f39c12"
        elif bmi < 25:
            category = "Normal Weight"
            color = "#27ae60"
        elif bmi < 30:
            category = "Overweight"
            color = "#e67e22"
        else:
            category = "Obese"
            color = "#e74c3c"

        result_label.config(
            text=f"BMI: {bmi:.2f}\n{category}",
            fg=color
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = Tk()
root.title("BMI Calculator")
root.geometry("450x450")
root.resizable(False, False)
root.configure(bg="#f4f7fc")

title_label = Label(
    root,
    text="⚖ BMI Calculator",
    font=("Segoe UI", 22, "bold"),
    bg="#f4f7fc",
    fg="#2c3e50"
)
title_label.pack(pady=20)

weight_label = Label(
    root,
    text="Weight (kg)",
    font=("Segoe UI", 11),
    bg="#f4f7fc",
    fg="#34495e"
)
weight_label.pack()

weight_entry = Entry(
    root,
    font=("Segoe UI", 12),
    width=25,
    justify="center",
    bd=2
)
weight_entry.pack(ipady=6, pady=8)

height_label = Label(
    root,
    text="Height (m)",
    font=("Segoe UI", 11),
    bg="#f4f7fc",
    fg="#34495e"
)
height_label.pack()

height_entry = Entry(
    root,
    font=("Segoe UI", 12),
    width=25,
    justify="center",
    bd=2
)
height_entry.pack(ipady=6, pady=8)

calc_button = Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    font=("Segoe UI", 12, "bold"),
    bg="#3498db",
    fg="white",
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
)
calc_button.pack(pady=20)

result_frame = Frame(
    root,
    bg="white",
    bd=1,
    relief="solid"
)
result_frame.pack(padx=40, pady=10, fill="x")

result_label = Label(
    result_frame,
    text="Enter your details",
    font=("Segoe UI", 16, "bold"),
    bg="white",
    fg="#2c3e50",
    pady=20
)
result_label.pack()

root.mainloop()
