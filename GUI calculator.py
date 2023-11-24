import tkinter as tk
import math

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operation == "sqrt":
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            result = "Error: Imaginary result"
    # Add more complex operations here as needed
    else:
        result = "Invalid operation"
    
    label_result.config(text="Result: " + str(result))

# Create the main window
root = tk.Tk()
root.title("Complex Calculator")

# Create input fields for numbers and operation
entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation

# Create a dropdown menu for operation selection
operation_choices = ["+", "-", "*", "/", "sqrt"]
operation_menu = tk.OptionMenu(root, operation_var, *operation_choices)

# Create a button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Create a label to display the result
label_result = tk.Label(root, text="Result: ")

# Arrange widgets using grid layout
entry_num1.grid(row=0, column=0, padx=10, pady=10)
operation_menu.grid(row=0, column=1, padx=10, pady=10)
entry_num2.grid(row=0, column=2, padx=10, pady=10)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
label_result.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
