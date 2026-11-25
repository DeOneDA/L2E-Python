import tkinter as tk

root = tk.Tk()
root.title("To Do List")
root.geometry("600x500")

tasks = []

def proper(text):
    return text[0].upper() + "".join(text[x].upper() if text[x-1] == " " else text[x] for x in range(1, len(text)))

def add_task(tasks, title):
    if not title: return
    tasks.append({"title": proper(title), "done": False})
    return

def mark_done(tasks, index):
    tasks[index]["done"] = True
    return

def remove_tasks(tasks, index):
    tasks.pop(index)
    return

def count_remaining(tasks):
    return sum(1 if task["done"] == False else 0 for task in tasks)


def op1():
    task = proper(add_item_entry.get())
    add_task(tasks, task)
    todo_listbox.delete(0, tk.END)
    for index, item in enumerate(tasks):
        todo_listbox.insert(tk.END, f"[ ] {index + 1}. {proper(item['title'])}" if item['done'] == False else f"[x] {index + 1}. {proper(item['title'])}")
    add_item_entry.delete(0, tk.END)
    return

def op2():
    if todo_listbox.curselection():
        mark_done(tasks, todo_listbox.curselection()[0])
        todo_listbox.delete(0, tk.END)
        for index, item in enumerate(tasks):
            todo_listbox.insert(tk.END, f"[ ] {index + 1}. {proper(item['title'])}" if item['done'] == False else f"[x] {index + 1}. {proper(item['title'])}")
        return

def op3():
    if todo_listbox.curselection():
        remove_tasks(tasks, todo_listbox.curselection()[0])
        todo_listbox.delete(0, tk.END)
        for index, item in enumerate(tasks):
            todo_listbox.insert(tk.END, f"[ ] {index + 1}. {proper(item['title'])}" if item['done'] == False else f"[x] {index + 1}. {proper(item['title'])}")
        return

def op4():
    global tasks
    tasks = []
    add_item_entry.delete(0, tk.END)
    todo_listbox.delete(0, tk.END)
    remaining_label.config(text="0")
    return

def op5():
    remaining_label.config(text=f"{sum(1 for item in tasks if item["done"] == False)}")
    return

todo_label = tk.Label(root, text="My List:")
todo_label.pack()

frame = tk.Frame(root)
frame.pack()

todo_listbox =tk.Listbox(frame, height=10, width=30)
todo_listbox.grid(row=0, column=0, rowspan=3)

button1 = tk.Button(frame, text="Remove Task", command=op3)
button1.grid(row=0, column=1, padx=10)

button2 = tk.Button(frame, text="Mark Done", command=op2)
button2.grid(row=1, column=1, padx=10)

button3 = tk.Button(frame, text="Clear", command=op4)
button3.grid(row=2, column=1, padx=10)

add_task_label = tk.Label(root, text="What would you like to add?")
add_task_label.pack(pady=10)
add_item_entry = tk.Entry(root, width=25)
add_item_entry.pack()

button4 = tk.Button(root, text="Add Task", command=op1)
button4.pack(pady=10)

button5 = tk.Button(root, text="Count Remaining", command=op5)
button5.pack(pady=10)

remaining_label = tk.Label(root, text="0")
remaining_label.pack()

tk.Label(root, text="Built by ~De One~", font =("Arial", 14)).pack(pady = 20)

root.mainloop()