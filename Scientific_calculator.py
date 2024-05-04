import math
import sympy as sp
import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of a negative number."
    else:
        return math.sqrt(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def integrate(expression):
    x = sp.Symbol('x')
    integrated_expr = sp.integrate(expression, x)
    return integrated_expr

def differentiate(expression):
    x = sp.Symbol('x')
    diff_expr = sp.diff(expression, x)
    return diff_expr

def calculate():
    operation = operation_var.get()

    if operation in ('Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation'):
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        if operation == 'Addition':
            result = add(num1, num2)
        elif operation == 'Subtraction':
            result = subtract(num1, num2)
        elif operation == 'Multiplication':
            result = multiply(num1, num2)
        elif operation == 'Division':
            result = divide(num1, num2)
        elif operation == 'Exponentiation':
            result = power(num1, num2)

    elif operation in ('Square Root', 'Sine', 'Cosine', 'Tangent'):
        num = float(num1_entry.get())

        if operation == 'Square Root':
            result = square_root(num)
        elif operation == 'Sine':
            result = sin(num)
        elif operation == 'Cosine':
            result = cos(num)
        elif operation == 'Tangent':
            result = tan(num)

    elif operation == 'Integration':
        expr = expr_entry.get()
        result = integrate(expr)

    elif operation == 'Differentiation':
        expr = expr_entry.get()
        result = differentiate(expr)

    result_label.config(text="Result: " + str(result))

# Create GUI
root = tk.Tk()
root.title("Scientific Calculator")

# Operation selection
operation_var = tk.StringVar()
operation_var.set("Addition")
operation_label = tk.Label(root, text="Select Operation:")
operation_label.grid(row=0, column=0, padx=5, pady=5)
operation_menu = tk.OptionMenu(root, operation_var, "Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Square Root", "Sine", "Cosine", "Tangent", "Integration", "Differentiation")
operation_menu.grid(row=0, column=1, padx=5, pady=5)

# Inputs
num1_label = tk.Label(root, text="Number 1:")
num1_label.grid(row=1, column=0, padx=5, pady=5)
num1_entry = tk.Entry(root)
num1_entry.grid(row=1, column=1, padx=5, pady=5)

num2_label = tk.Label(root, text="Number 2:")
num2_label.grid(row=2, column=0, padx=5, pady=5)
num2_entry = tk.Entry(root)
num2_entry.grid(row=2, column=1, padx=5, pady=5)

expr_label = tk.Label(root, text="Expression:")
expr_label.grid(row=1, column=2, padx=5, pady=5)
expr_entry = tk.Entry(root)
expr_entry.grid(row=1, column=3, padx=5, pady=5)

# Calculate button
calculate_btn = tk.Button(root, text="Calculate", command=calculate)
calculate_btn.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
