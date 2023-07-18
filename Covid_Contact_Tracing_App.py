#Vargas, Ruben A
#BSCPE 1-4
#Object-Oriented Programming

import tkinter as tk
from AddEntry import AddEntry
from SearchEntry import SearchEntry

class AddSearch(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Contact Tracing App")
        self.geometry("700x500")
        self.pack_propagate(0)  # Prevent the window from resizing

        # Create a frame to hold the labels and buttons
        frame = tk.Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        self.header_label = tk.Label(frame, text="Covid-19: Contact Tracing App", font=("Helvetica", 14, "bold"))
        self.header_label.pack()

        AddEntryButton = tk.Button(frame, text="Add Entry", command=self.open_add_entry)
        AddEntryButton.pack()

        SearchEntryButton = tk.Button(frame, text="Search Entry", command=self.destroy)
        SearchEntryButton.pack()

    def open_add_entry(self):
        self.destroy()
        entry = AddEntry()
        entry.mainloop()

if __name__ == "__main__":
    app = AddSearch()
    app.mainloop()