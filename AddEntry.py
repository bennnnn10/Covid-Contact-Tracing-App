import tkinter as tk

class AddEntry(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Add Entry")
        self.geometry("700x500")

        HDCF = tk.Label(self, text="Pursuant to Republic Act 11332, you are required to provide truthful information", font=("Helvetica", 12, "bold"))
        HDCF.place(x=50, y=20)

        HCDF = tk.Label(self, text="about your health condition and possible exposure.", font=("Helvetica", 12, "bold"))
        HCDF.place(x=140, y=40)

        #Create a Label
        name_label = tk.Label(self, text="Name:")
        name_label.place(x=5, y=80)

        #Create an entry box
        name_entry = tk.Entry(self, width=50)  
        name_entry.place(x=120, y=80)

if __name__ == "__main__":
    entry = AddEntry()
    entry.mainloop()