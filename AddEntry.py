import tkinter as tk
from PIL import Image, ImageTk

class AddEntry(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Add Entry")
        self.geometry("700x500")

        # Load the background image
        bg_image = Image.open(r"C:\Users\Ruben\OneDrive\Pictures\Covid-19\covid.jpg")
        bg_image = bg_image.resize((900, 500))
        self.background = ImageTk.PhotoImage(bg_image)

        # Create a Label widget to display the background image
        bg_label = tk.Label(self, image=self.background)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        HDCF = tk.Label(self, text="Pursuant to Republic Act 11332, you are required to provide truthful information", font=("Helvetica", 12, "bold"))
        HDCF.place(x=50, y=20)

        HCDF = tk.Label(self, text="about your health condition and possible exposure.", font=("Helvetica", 12, "bold"))
        HCDF.place(x=140, y=40)

        #Create a Label
        name_label = tk.Label(self, text="Name:")
        name_label.place(x=5, y=80)

        age_label = tk.Label(self, text="Age:")
        age_label.place(x=5, y=110)

        sex_label = tk.Label(self, text="Sex:")
        sex_label.place(x=5, y=140)

        contact_number_label = tk.Label(self, text="Contact #:")
        contact_number_label.place(x=5, y=170)

        address_label = tk.Label(self, text="Address:")
        address_label.place(x=5, y=200)

        #Create an entry box
        name_entry = tk.Entry(self, width=50)  
        name_entry.place(x=120, y=80)

        age_entry = tk.Entry(self, width=50)  
        age_entry.place(x=120, y=110)

        sex_entry = tk.Entry(self, width=50)  
        sex_entry.place(x=120, y=140)

        contact_number_entry = tk.Entry(self, width=50)  
        contact_number_entry.place(x=120, y=170)

        address_entry = tk.Entry(self, width=50) 
        address_entry.place(x=120, y=200)

if __name__ == "__main__":
    entry = AddEntry()
    entry.mainloop()