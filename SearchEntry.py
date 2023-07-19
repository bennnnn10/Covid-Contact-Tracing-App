import tkinter as tk
import csv
from PIL import Image, ImageTk

class SearchEntry(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Search Entry")
        self.geometry("700x500")

         # Load the background image
        bg_image = Image.open(r"C:\Users\Ruben\OneDrive\Pictures\Covid-19\covid.jpg")
        bg_image = bg_image.resize((900, 500))
        self.background = ImageTk.PhotoImage(bg_image)

        # Create a Label widget to display the background image
        bg_label = tk.Label(self, image=self.background, highlightthickness=0)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        search = tk.Label(self, text="Enter the Name:")
        search.place(x=30, y=30)

        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.place(x=130, y=30)

        search_button = tk.Button(self, text="Search")
        search_button.place(x=325, y=27)

        go_back_to_main = tk.Button(self, text="Back", command=self.back_to_main)
        go_back_to_main.place(x=300, y=450)

        close = tk.Button(self, text="Close", command=self.destroy)
        close.place(x=360, y=450)

    def search_info(self):
        name_to_search = self.search_entry.get()

        with open("gathered_information.csv", mode="r") as file:
            reader = csv.reader(file)
            found_entries = []
            for row in reader:
                if row[0] == name_to_search:
                    found_entries.append(row)

    def back_to_main(self):
        self.destroy()
        from Covid_Contact_Tracing_App import AddSearch
        entry = AddSearch()
        entry.mainloop()

if __name__ == "__main__":
    search = SearchEntry()
    search.mainloop()