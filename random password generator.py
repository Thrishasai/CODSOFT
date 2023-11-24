import tkinter as tk
import random
import string

def generate_password():
    length = int(entry_length.get())
    complexity = ""
    
    if check_lower.get():
        complexity += "l"
    if check_upper.get():
        complexity += "u"
    if check_digits.get():
        complexity += "d"
    if check_special.get():
        complexity += "s"
    
    if not complexity:
        result_label.config(text="Error: No character set selected")
        return
    
    characters = ''
    if 'l' in complexity:
        characters += string.ascii_lowercase
    if 'u' in complexity:
        characters += string.ascii_uppercase
    if 'd' in complexity:
        characters += string.digits
    if 's' in complexity:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input fields and checkboxes
label_length = tk.Label(root, text="Enter password length:")
entry_length = tk.Entry(root)
check_lower = tk.IntVar()
check_upper = tk.IntVar()
check_digits = tk.IntVar()
check_special = tk.IntVar()

checkbox_lower = tk.Checkbutton(root, text="Lowercase", variable=check_lower)
checkbox_upper = tk.Checkbutton(root, text="Uppercase", variable=check_upper)
checkbox_digits = tk.Checkbutton(root, text="Digits", variable=check_digits)
checkbox_special = tk.Checkbutton(root, text="Special characters", variable=check_special)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
result_label = tk.Label(root, text="")

# Arrange widgets using grid layout
label_length.grid(row=0, column=0, padx=10, pady=10)
entry_length.grid(row=0, column=1, padx=10, pady=10)
checkbox_lower.grid(row=1, column=0, padx=10, pady=10)
checkbox_upper.grid(row=1, column=1, padx=10, pady=10)
checkbox_digits.grid(row=2, column=0, padx=10, pady=10)
checkbox_special.grid(row=2, column=1, padx=10, pady=10)
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
