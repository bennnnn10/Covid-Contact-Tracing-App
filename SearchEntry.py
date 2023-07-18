import tkinter as tk

class SearchEntry(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Search Entry")
        self.geometry("700x500")

if __name__ == "__main__":
    search = SearchEntry()
    search.mainloop()