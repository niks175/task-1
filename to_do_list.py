import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_input = tk.Entry(root, width=40)
        self.task_input.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Selected", width=15, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", width=15, command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    def remove_task(self):
        selected = self.tasks_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]
                self.update_listbox()
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
