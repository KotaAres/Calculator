import tkinter as tk

def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main View
root = tk.Tk()
root.title("Basic Calculator")

entry = tk.Entry(root, width=25, borderwidth=3, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Making Buttons
for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    else:
        action = lambda x=text: click(x)
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=action).grid(row=row, column=col)

tk.Button(root, text="Clear", width=22, height=2, font=('Arial', 14), command=clear).grid(row=5, column=0, columnspan=4)

# Start GUI
root.mainloop()
