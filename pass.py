import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.configure(bg='#0d0d0d')
        
        self.custom_font = ("Helvetica", 12, "bold")

        self.length_label = tk.Label(
            self.root, 
            text="Password Length:", 
            fg='#39ff14', 
            bg='#0d0d0d', 
            font=self.custom_font
        )
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(
            self.root, 
            font=self.custom_font, 
            fg='#39ff14', 
            bg='#0d0d0d', 
            insertbackground='#39ff14', 
            highlightthickness=2, 
            highlightcolor='#33ccff', 
            bd=0
        )
        self.length_entry.pack(pady=10)

        self.options_frame = tk.Frame(self.root, bg='#0d0d0d')
        self.options_frame.pack(pady=10)

        self.include_letters = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_specials = tk.BooleanVar()

        self.letters_check = tk.Checkbutton(
            self.options_frame, 
            text="Include Letters", 
            variable=self.include_letters, 
            onvalue=True, 
            offvalue=False, 
            fg='#39ff14', 
            bg='#0d0d0d', 
            font=self.custom_font, 
            selectcolor='#0d0d0d',
            activebackground='#0d0d0d'
        )
        self.letters_check.pack(anchor='w')

        self.digits_check = tk.Checkbutton(
            self.options_frame, 
            text="Include Digits", 
            variable=self.include_digits, 
            onvalue=True, 
            offvalue=False, 
            fg='#39ff14', 
            bg='#0d0d0d', 
            font=self.custom_font, 
            selectcolor='#0d0d0d',
            activebackground='#0d0d0d'
        )
        self.digits_check.pack(anchor='w')

        self.specials_check = tk.Checkbutton(
            self.options_frame, 
            text="Include Special Characters", 
            variable=self.include_specials, 
            onvalue=True, 
            offvalue=False, 
            fg='#39ff14', 
            bg='#0d0d0d', 
            font=self.custom_font, 
            selectcolor='#0d0d0d',
            activebackground='#0d0d0d'
        )
        self.specials_check.pack(anchor='w')

        self.generate_btn = tk.Button(
            self.root, 
            text="Generate Password", 
            command=self.generate_password, 
            fg='#0d0d0d', 
            bg='#33ccff', 
            font=self.custom_font,
            activebackground='#39ff14',
            activeforeground='#0d0d0d',
            bd=0,
            padx=10,
            pady=5,
            relief=tk.FLAT,
            highlightbackground='#33ccff',
            highlightthickness=2
        )
        self.generate_btn.pack(pady=10)

        self.password_label = tk.Label(
            self.root, 
            text="", 
            fg='#39ff14', 
            bg='#0d0d0d', 
            font=self.custom_font
        )
        self.password_label.pack(pady=10)

    def generate_password(self):
        length = self.length_entry.get()
        if not length.isdigit() or int(length) <= 0:
            messagebox.showwarning("Warning", "Please enter a valid length.")
            return
        
        length = int(length)
        characters = ""
        if self.include_letters.get():
            characters += string.ascii_letters
        if self.include_digits.get():
            characters += string.digits
        if self.include_specials.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one option.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
