#Vargas, Ruben A
#BSCPE 1-4
#Object-Oriented Programming

import tkinter as tk
from PIL import Image, ImageTk
from AddEntry import AddEntry
from SearchEntry import SearchEntry

class AddSearch(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Contact Tracing App")
        self.geometry("700x500")
        self.pack_propagate(0)  # Prevent the window from resizing

        # Load the background image
        bg_image = Image.open(r"C:\Users\Ruben\OneDrive\Pictures\Covid-19\first.png")
        bg_image = bg_image.resize((900, 500))
        self.background = ImageTk.PhotoImage(bg_image)

        # Create a Label widget to display the background image
        bg_label = tk.Label(self, image=self.background, highlightthickness=0)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame to hold the labels and buttons
        frame = tk.Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor='center')

        AddEntryButton = tk.Button(frame, text="Add Entry", command=self.open_add_entry)
        AddEntryButton.pack()

        SearchEntryButton = tk.Button(frame, text="Search Entry", command=self.open_search_entry)
        SearchEntryButton.pack()

    def open_add_entry(self):
        self.destroy()
        entry = AddEntry()
        entry.mainloop()

    def open_search_entry(self):
        self.destroy()
        search = SearchEntry()
        search.mainloop()

if __name__ == "__main__":
    app = AddSearch()
    app.mainloop()