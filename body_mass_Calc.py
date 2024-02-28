import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get()) / 100
        weight = float(entry_weight.get())
        bmi = weight / (height * height)

        result_label.config(text=f"Your Body Mass Index is: {bmi:.2f}")

        if 0 < bmi <= 16:
            category_label.config(text="You are severely underweight")
        elif bmi <= 18.5:
            category_label.config(text="You are underweight")
        elif bmi <= 25:
            category_label.config(text="You are healthy")
        elif bmi <= 30:
            category_label.config(text="You are overweight")
        else:
            category_label.config(text="You are severely overweight")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for height and weight.")

def clear_all():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    result_label.config(text="")
    category_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and place widgets
label_height = tk.Label(window, text="Height (cm):")
label_weight = tk.Label(window, text="Weight (kg):")
entry_height = tk.Entry(window)
entry_weight = tk.Entry(window)
button_calculate = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
button_clear_all = tk.Button(window, text="Clear All", command=clear_all)
result_label = tk.Label(window, text="")
category_label = tk.Label(window, text="")

label_height.grid(row=0, column=0, padx=10, pady=10)
label_weight.grid(row=1, column=0, padx=10, pady=10)
entry_height.grid(row=0, column=1, padx=10, pady=10)
entry_weight.grid(row=1, column=1, padx=10, pady=10)
button_calculate.grid(row=2, column=0, padx=10, pady=10)
button_clear_all.grid(row=2, column=1, padx=10, pady=10)
result_label.grid(row=3, column=0, columnspan=2, pady=10)
category_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI
window.mainloop()
