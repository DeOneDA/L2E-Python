import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Bill Splitter App")
root.geometry("500x340")

def calculate_tip(bill, tip_percent):
    if tip_percent == 0: return bill
    return bill / tip_percent

def total_with_tip(bill, tip_percent):
    if tip_percent == 0: return bill
    return (bill/tip_percent) + bill

def split_bill(total, people):
    if people < 1: return "None"
    return round(total / people, 2)


def starter1():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    
    result_label.config(text="Result: " + str(calculate_tip(a, b)))

def starter2():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    
    result_label.config(text="Result: " + str(total_with_tip(a, b)))

def starter3():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numbers only.")
        return
    
    result_label.config(text="Result: " + str(split_bill(a, b)))

def on_clear():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_label.config(text="Result: ")

tk.Label(root, text="Bill:").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Tip Percentage / No of People:").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Button(root, text="Calculate Tip", command=starter1).pack(pady=5)
tk.Button(root, text="Total With Tip", command=starter2).pack(pady=5)
tk.Button(root, text="Split Bill", command=starter3).pack(pady=5)
tk.Button(root, text="Clear", command=on_clear).pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

tk.Label(root, text="Built by ~De One~", font =("Arial", 14)).pack(pady = 20)

root.mainloop()