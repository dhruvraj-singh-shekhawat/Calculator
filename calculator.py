import tkinter as tk

def button_click(number):
    current = result_var.get()
    result_var.set(current + str(number))

def evaluate():
    try:
        expression = result_var.get()
        result = eval(expression)
        result_var.set(result)
    except Exception as e:
        result_var.set("Error")

def clear():
    result_var.set("")

window = tk.Tk()
window.title("Calculator")

result_var = tk.StringVar()

display = tk.Entry(window, textvariable=result_var, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)


button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


row = 1
col = 0
for label in button_labels:
    tk.Button(
        window, text=label, padx=20, pady=20, font=("Arial", 16),
        command=lambda label=label: button_click(label) if label != '=' else evaluate()
    ).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    window, text="C", padx=20, pady=20, font=("Arial", 16),
    command=clear
).grid(row=row, column=col)

window.mainloop()
