import tkinter as tk
from tkinter import ttk

# Function for button click
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the expression
def button_equal():
    try:
        global expression
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Function to change the theme
def change_theme(theme):
    if theme == "dark":
        root.configure(bg="#333")
        style.configure('TButton', background="#555", foreground="white", font=('Arial', 12))
        display.configure(bg="#333", fg="white")
    elif theme == "light":
        root.configure(bg="#f0f0f0")
        style.configure('TButton', background="#e0e0e0", foreground="black", font=('Arial', 12))
        display.configure(bg="white", fg="black")
    elif theme == "blue":
        root.configure(bg="#4a90e2")
        style.configure('TButton', background="#6db1ff", foreground="white", font=('Arial', 12))
        display.configure(bg="#3a70c2", fg="white")

# Initialize the window
root = tk.Tk()
root.title("Themed Calculator")
root.geometry("400x500")

expression = ""
input_text = tk.StringVar()

# Style configuration
style = ttk.Style()
style.theme_use('clam')

# Entry field for the calculator
display = tk.Entry(root, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Adding buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=10, height=3, command=button_equal).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        tk.Button(root, text=text, width=10, height=3, command=button_clear).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=10, height=3, command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Theme selection buttons
tk.Button(root, text="Dark Theme", width=12, height=2, command=lambda: change_theme("dark")).grid(row=5, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text="Light Theme", width=12, height=2, command=lambda: change_theme("light")).grid(row=5, column=2, columnspan=2, padx=5, pady=5)
tk.Button(root, text="Blue Theme", width=12, height=2, command=lambda: change_theme("blue")).grid(row=6, column=0, columnspan=4, padx=5, pady=5)

# Set default theme
change_theme("light")

# Run the main loop
root.mainloop()
