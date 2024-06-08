import tkinter as tk
from tkinter import messagebox
import json

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return f"{'[x]' if self.completed else '[ ]'} {self.description}"

class ToDoList:
    def __init__(self, file_name='tasks.json'):
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
            self.save_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            self.save_tasks()

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                tasks = json.load(file)
                self.tasks = [Task(**task) for task in tasks]
        except FileNotFoundError:
            pass

class ToDoApp:
    def __init__(self, root):
        self.todo_list = ToDoList()
        self.root = root
        self.root.title("To-Do List Application")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = tk.Button(root, text="Mark Complete", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.refresh_tasks()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.todo_list.add_task(description)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty")

    def update_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            index = selected_task[0]
            description = self.task_entry.get()
            if description:
                self.todo_list.update_task(index, description)
                self.task_entry.delete(0, tk.END)
                self.refresh_tasks()
            else:
                messagebox.showwarning("Input Error", "Task description cannot be empty")
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def delete_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            index = selected_task[0]
            self.todo_list.delete_task(index)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def complete_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            index = selected_task[0]
            self.todo_list.mark_task_complete(index)
            self.refresh_tasks()
        else:
            messagebox.showwarning("Selection Error", "No task selected")

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
