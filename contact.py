import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.configure(bg='#f0f0f0')
        
        self.custom_font = ("Helvetica", 12)
        self.title_font = ("Helvetica", 16, "bold")
        
        self.contacts = {}  # Dictionary to store contacts
        
        # Title
        self.title_label = tk.Label(
            self.root, 
            text="Contact Manager", 
            fg='#333333', 
            bg='#f0f0f0', 
            font=self.title_font
        )
        self.title_label.pack(pady=10)
        
        # Form frame
        self.form_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.form_frame.pack(pady=10)

        self.name_label = tk.Label(self.form_frame, text="Name", bg='#f0f0f0', font=self.custom_font)
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.name_entry = tk.Entry(self.form_frame, font=self.custom_font, bg='#ffffff', highlightthickness=1, highlightbackground='#cccccc')
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.phone_label = tk.Label(self.form_frame, text="Phone", bg='#f0f0f0', font=self.custom_font)
        self.phone_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.phone_entry = tk.Entry(self.form_frame, font=self.custom_font, bg='#ffffff', highlightthickness=1, highlightbackground='#cccccc')
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.email_label = tk.Label(self.form_frame, text="Email", bg='#f0f0f0', font=self.custom_font)
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
        self.email_entry = tk.Entry(self.form_frame, font=self.custom_font, bg='#ffffff', highlightthickness=1, highlightbackground='#cccccc')
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.country_label = tk.Label(self.form_frame, text="Country", bg='#f0f0f0', font=self.custom_font)
        self.country_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.E)
        self.country_entry = tk.Entry(self.form_frame, font=self.custom_font, bg='#ffffff', highlightthickness=1, highlightbackground='#cccccc')
        self.country_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.button_frame.pack(pady=10)
        
        self.add_contact_btn = tk.Button(
            self.button_frame, 
            text="Add Contact", 
            command=self.add_contact, 
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
        self.add_contact_btn.pack(side=tk.LEFT, padx=10)
        
        self.view_contacts_btn = tk.Button(
            self.button_frame, 
            text="View Contacts", 
            command=self.view_contacts, 
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
        self.view_contacts_btn.pack(side=tk.LEFT, padx=10)
        
        self.search_contact_btn = tk.Button(
            self.button_frame, 
            text="Search Contact", 
            command=self.search_contact, 
            fg='#ffffff', 
            bg='#ffc107', 
            font=self.custom_font,
            activebackground='#e0a800',
            activeforeground='#ffffff',
            bd=0,
            padx=10,
            pady=5,
            relief=tk.FLAT
        )
        self.search_contact_btn.pack(side=tk.LEFT, padx=10)
        
        self.update_contact_btn = tk.Button(
            self.button_frame, 
            text="Update Contact", 
            command=self.update_contact, 
            fg='#ffffff', 
            bg='#17a2b8', 
            font=self.custom_font,
            activebackground='#117a8b',
            activeforeground='#ffffff',
            bd=0,
            padx=10,
            pady=5,
            relief=tk.FLAT
        )
        self.update_contact_btn.pack(side=tk.LEFT, padx=10)
        
        self.delete_contact_btn = tk.Button(
            self.button_frame, 
            text="Delete Contact", 
            command=self.delete_contact, 
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
        self.delete_contact_btn.pack(side=tk.LEFT, padx=10)
        
        # Display frame
        self.display_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.display_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.display_text = tk.Text(
            self.display_frame, 
            font=self.custom_font, 
            fg='#333333', 
            bg='#ffffff', 
            wrap=tk.WORD,
            bd=1,
            padx=10,
            pady=10,
            highlightthickness=1,
            highlightbackground='#cccccc'
        )
        self.display_text.pack(fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.display_frame, command=self.display_text.yview, bg='#f0f0f0')
        self.display_text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        country = self.country_entry.get()
        
        if name and phone and email and country:
            self.contacts[name] = {"phone": phone, "email": email, "country": country}
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "All fields must be filled.")

    def view_contacts(self):
        self.display_text.delete(1.0, tk.END)
        if self.contacts:
            for name, details in self.contacts.items():
                self.display_text.insert(tk.END, f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nCountry: {details['country']}\n\n")
        else:
            self.display_text.insert(tk.END, "No contacts found.")

    def search_contact(self):
        query = simpledialog.askstring("Input", "Enter name or phone number to search:", parent=self.root)
        if query:
            self.display_text.delete(1.0, tk.END)
            found = False
            for name, details in self.contacts.items():
                if query.lower() in name.lower() or query in details["phone"]:
                    self.display_text.insert(tk.END, f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nCountry: {details['country']}\n\n")
                    found = True
            if not found:
                self.display_text.insert(tk.END, "No contact found.")
        else:
            messagebox.showwarning("Warning", "Search query cannot be empty.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:", parent=self.root)
        if name and name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            country = self.country_entry.get()
            
            if phone or email or country:
                if phone:
                    self.contacts[name]["phone"] = phone
                if email:
                    self.contacts[name]["email"] = email
                if country:
                    self.contacts[name]["country"] = country
                messagebox.showinfo("Success", "Contact updated successfully.")
                self.clear_entries()
            else:
                messagebox.showwarning("Warning", "At least one field must be filled.")
        else:
            messagebox.showwarning("Warning", "Contact not found or name cannot be empty.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:", parent=self.root)
        if name and name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Contact not found or name cannot be empty.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.country_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
