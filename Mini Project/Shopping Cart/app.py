import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Shopping Cart")
root.geometry("800x600")

cart = []
def add_items(cart, name, price, qty):
    for items in cart:
        if items["name"] == name:
            items["qty"] += qty
            return

    cart.append({"name": name, "price": price, "qty": qty})
    return

def remove_items(cart, name):
    for index, items in enumerate(cart):
            if items["name"] == name:
                cart.pop(index)
                return

def cart_total(cart):
    total = 0
    for items in cart:
        total += items["price"] * items["qty"]
    return total

def apply_discount(total, percent):
    return total - ((total * percent)/100)


def operator1():
    try:
        price = float(price_entry.get())
        qty = int(quantity_entry.get())
    except:
        messagebox.showerror("Wrong Input", "Please only input numbers for the price and quantity.")
    name = name_entry.get().title()
    add_items(cart, name, price, qty)
    cart_label.config(text = f"Your Cart: \n{"\n".join(f"{item["name"].title()} ({item["qty"]}) - {item["qty"] * item["price"]}" for item in cart)}", pady=5)
    total_label.config(text="Total:\n" + str(sum(items["price"] * items["qty"] for items in cart)), pady=10)

def operator2():
    name = name_entry.get().title()
    remove_items(cart, name)
    cart_label.config(text = f"Your Cart: \n{"\n".join(f"{item["name"].title()} ({item["qty"]}) - {item["qty"] * item["price"]}" for item in cart)}", pady=5)
    total_label.config(text="Total:\n" + str(sum(items["price"] * items["qty"] for items in cart)), pady=10)

def operator3():
    try:
        percentage = int(discount_entry.get())
    except:
        messagebox.showerror("Wrong Input", "Please only input numbers for the discount percentage.")
    total = sum(items["price"] * items["qty"] for items in cart)
    discounted_total_label.config(text="Discounted Total:\n" + str(apply_discount(total, percentage)))

def operator4():
    global cart
    cart = []
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    discount_entry.delete(0, tk.END)
    cart_label.config(text="Your Cart:")
    total_label.config(text="Total: 0")
    discounted_total_label.config(text="Discounted Total: 0")
    

cart_label = tk.Label(root, text="Your Cart:")
cart_label.pack(pady=5)

total_label = tk.Label(root, text="Total: " + str(sum(items["price"] * items["qty"] for items in cart)))
total_label.pack(pady=10)

form = tk.Frame(root)
form.pack()

name_label = tk.Label(form, text="Item Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(form)
name_entry.grid(row=0, column=1)

price_label = tk.Label(form, text="Item Price:")
price_label.grid(row=1, column=0)
price_entry = tk.Entry(form)
price_entry.grid(row=1, column=1)

quantity_label = tk.Label(form, text="Select the quantity:")
quantity_label.grid(row= 2, column=0)
quantity_entry = tk.Spinbox(form, from_=1, to=20, width=5)
quantity_entry.grid(row= 2, column=1)

button1 = tk.Button(form, text = "Add Item", command = operator1)
button1.grid(row=0, column=2, padx=15)

button2 = tk.Button(form, text = "Remove Item", command = operator2)
button2.grid(row=1, column=2, padx=15, pady=10)

discount_label = tk.Label(root, text= "Discount Percentage:")
discount_label.pack(pady=5)
discount_entry = tk.Entry(root, width = 5)
discount_entry.pack(pady=5)

button3 = tk.Button(root, text = "Calculate Discount", command = operator3)
button3.pack(pady=10)

discounted_total_label = tk.Label(root, text="Discounted Total: 0")
discounted_total_label.pack(pady=10)

button4 = tk.Button(root, text="Clear Cart", command=operator4)
button4.pack(pady=10)

tk.Label(root, text="Built by ~De One~", font =("Arial", 14)).pack(pady = 20)

root.mainloop()