import tkinter as tk
from PIL import Image, ImageTk

class GatheredInformation(tk.Tk):
    
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

        # Create a Label widget to display the background image
        bg_label = tk.Label(self, image=self.background, highlightthickness=0)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        go_back_to_main = tk.Button(self, text="Back", command=self.back_to_main)
        go_back_to_main.place(x=300, y=450)

        close = tk.Button(self, text="Close", command=self.close_window)
        close.place(x=360, y=450)

    def close_window(self):
        self.destroy()

    def back_to_main(self):
        self.destroy()
        from Covid_Contact_Tracing_App import AddSearch
        entry = AddSearch()
        entry.mainloop()

if __name__ == "__main__":
    info = GatheredInformation()
    info.mainloop()