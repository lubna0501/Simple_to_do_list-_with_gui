import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")

        self.todo_list = []

        self.todo_entry = tk.Entry(master, width=40)
        self.todo_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add", command=self.add_item)
        self.add_button.grid(row=0, column=1, padx=5)

        self.remove_button = tk.Button(master, text="Remove", command=self.remove_item)
        self.remove_button.grid(row=0, column=2, padx=5)

        self.view_button = tk.Button(master, text="View List", command=self.view_list)
        self.view_button.grid(row=0, column=3, padx=5)

        self.listbox = tk.Listbox(master, width=50)
        self.listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    def add_item(self):
        item = self.todo_entry.get().strip()
        if item:
            self.todo_list.append(item)
            self.listbox.insert(tk.END, item)
            self.todo_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Input", "Please enter an item.")

    def remove_item(self):
        selection = self.listbox.curselection()
        if selection:
            idx = selection[0]
            item = self.listbox.get(idx)
            self.listbox.delete(idx)
            self.todo_list.remove(item)
        else:
            messagebox.showwarning("No Selection", "Please select an item to remove.")

    def view_list(self):
        if self.todo_list:
            messagebox.showinfo("To-Do List", "\n".join(self.todo_list))
        else:
            messagebox.showinfo("To-Do List", "To-Do List is empty.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
