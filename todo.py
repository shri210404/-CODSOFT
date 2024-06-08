import tkinter as tk
from tkinter import messagebox, font

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg='#e9ecef')
        
        self.custom_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")

        self.tasks = []

        self.title_label = tk.Label(
            self.root, 
            text="📝 To-Do List", 
            font=self.title_font, 
            fg='#212529', 
            bg='#e9ecef'
        )
        self.title_label.pack(pady=20)

        self.frame = tk.Frame(self.root, bg='#e9ecef')
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame, 
            width=50, 
            height=10, 
            bd=0, 
            font=self.custom_font, 
            fg='#212529', 
            bg='#ffffff', 
            highlightthickness=1, 
            highlightcolor='#adb5bd', 
            selectbackground="#d1e7dd", 
            selectforeground='#212529'
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame, highlightthickness=0)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry_frame = tk.Frame(self.root, bg='#e9ecef')
        self.entry_frame.pack(pady=10)

        self.entry_label = tk.Label(
            self.entry_frame, 
            text="New Task:", 
            font=self.custom_font, 
            fg='#495057', 
            bg='#e9ecef'
        )
        self.entry_label.pack(side=tk.LEFT, padx=5)

        self.entry = tk.Entry(
            self.entry_frame, 
            font=self.custom_font, 
            fg='#adb5bd', 
            bg='#ffffff', 
            insertbackground='#495057', 
            highlightthickness=1, 
            highlightcolor='#adb5bd', 
            bd=0,
            width=30
        )
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.entry.insert(0, "Type your task here...")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<FocusOut>", self.add_placeholder)

        self.button_frame = tk.Frame(self.root, bg='#e9ecef')
        self.button_frame.pack(pady=20)

        self.add_task_btn = tk.Button(
            self.button_frame, 
            text="➕ Add Task", 
            command=self.add_task, 
            fg='#ffffff', 
            bg='#28a745', 
            font=self.custom_font,
            activebackground='#218838',
            activeforeground='#ffffff',
            bd=0,
            padx=10,
            pady=5,
            relief=tk.FLAT
        )
        self.add_task_btn.pack(side=tk.LEFT, padx=10)

        self.del_task_btn = tk.Button(
            self.button_frame, 
            text="❌ Delete Task", 
            command=self.delete_task, 
            fg='#ffffff', 
            bg='#dc3545', 
            font=self.custom_font,
            activebackground='#c82333',
            activeforeground='#ffffff',
            bd=0,
            padx=10,
            pady=5,
            relief=tk.FLAT
        )
        self.del_task_btn.pack(side=tk.LEFT, padx=10)

        self.mark_done_btn = tk.Button(
            self.button_frame, 
            text="✔️ Mark as Done", 
            command=self.mark_as_done, 
            fg='#ffffff', 
            bg='#007bff', 
            font=self.custom_font,
            activebackground='#0056b3',
            activeforeground='#ffffff',
            bd=0,
            padx=10,
            pady=5,
            relief=tk.FLAT
        )
        self.mark_done_btn.pack(side=tk.LEFT, padx=10)

    def clear_placeholder(self, event):
        if self.entry.get() == "Type your task here...":
            self.entry.delete(0, tk.END)
            self.entry.config(fg='#212529')

    def add_placeholder(self, event):
        if self.entry.get() == "":
            self.entry.insert(0, "Type your task here...")
            self.entry.config(fg='#adb5bd')

    def add_task(self):
        task = self.entry.get()
        if task != "" and task != "Type your task here...":
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
            self.add_placeholder(None)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_as_done(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.tasks[selected_task_index] = self.tasks[selected_task_index] + " ✔️"
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.listbox.insert(tk.END, f"{index}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
