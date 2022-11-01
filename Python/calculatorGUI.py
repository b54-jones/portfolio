import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title = "Calculator"
root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid()

def add():
    try:
        first = float(firstnumber_value.get())
        second = float(secondnumber_value.get())
        total = first + second
        result.set(f"{first} plus {second} is {total:.2f}")
        firstnumber_value.set("")
        secondnumber_value.set("")
    except ValueError:
        result.set("Invalid inputs!")
        firstnumber_value.set("")
        secondnumber_value.set("")

def subtract():
    try:
        first = float(firstnumber_value.get())
        second = float(secondnumber_value.get())
        total = first - second
        result.set(f"{first} minus {second} is {total:.2f}")
        firstnumber_value.set("")
        secondnumber_value.set("")
    except ValueError:
        result.set("Invalid inputs!")
        firstnumber_value.set("")
        secondnumber_value.set("")

def divide():
    try:
        first = float(firstnumber_value.get())
        second = float(secondnumber_value.get())
        total = first / second
        result.set(f"{first} divided {second} is {total:.2f}")
        firstnumber_value.set("")
        secondnumber_value.set("")
    except ValueError:
        result.set("Invalid inputs!")
        firstnumber_value.set("")
        secondnumber_value.set("")

def multiply():
    try:
        first = float(firstnumber_value.get())
        second = float(secondnumber_value.get())
        total = first * second
        result.set(f"{first} times {second} is {total:.2f}")
        firstnumber_value.set("")
        secondnumber_value.set("")
    except ValueError:
        result.set("Invalid inputs!")
        firstnumber_value.set("")
        secondnumber_value.set("")

firstnumber_value = tk.StringVar()
secondnumber_value = tk.StringVar()#
result = tk.StringVar(value="Result will be here")

first_number_input = ttk.Entry(root, width=10, textvariable = firstnumber_value)
second_number_input = ttk.Entry(root, width=10, textvariable = secondnumber_value)
add_button = ttk.Button(root, text="+", command=add)
subtract_button = ttk.Button(root, text="-", command=subtract)
divide_button = ttk.Button(root, text="/", command=divide)
multiply_button = ttk.Button(root, text="*", command=multiply)
results_label = ttk.Label(root, textvariable=result)

first_number_input.grid(column=0, row=0)
second_number_input.grid(column=1, row=0)
add_button.grid(column=0, row=1)
subtract_button.grid(column=1, row=1)
divide_button.grid(column=0, row=2)
multiply_button.grid(column=1, row=2)
results_label.grid(columnspan=2, column=0, row=3)

first_number_input.focus()


root.mainloop()
