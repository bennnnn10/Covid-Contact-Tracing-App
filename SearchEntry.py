import tkinter as tk

class SearchEntry(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Search Entry")
        self.geometry("700x500")

        search = tk.Label(self, text="Search")
        search.grid(row=2, column=0, sticky=tk.E)
        
        SearchEntry = tk.Entry(self)
        SearchEntry.grid(row=2, column=1)

if __name__ == "__main__":
    search = SearchEntry()
    search.mainloop()