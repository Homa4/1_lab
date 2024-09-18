import tkinter as tk
from tkinter import messagebox

class SecondW:
    def __init__(self):
        self.listbox = None
    
    def showSelection(self):
        selection = self.listbox.curselection()
        index = selection[0]
        value = self.listbox.get(index)
        messagebox.showinfo("Chosen element", f"You chose: {value}")

    def displayListW(self):
        root = tk.Tk()
        root.title("choose group from list")
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack(padx=40, pady=60)

        items = ["IM-31", "IM-32", "IM-33", "IM-34"]
        for item in items:
            self.listbox.insert(tk.END, item)

        btn = tk.Button(root, text='Yes', command=self.showSelection)
        btnBack = tk.Button(root, text='Back', command=root.destroy)
        btn.pack()
        btnBack.pack()

        root.mainloop()
