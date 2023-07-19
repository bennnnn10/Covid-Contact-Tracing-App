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
        name_label.place(x=33, y=80)

        age_label = tk.Label(self, text="Age:")
        age_label.place(x=370, y=80)

        sex_label = tk.Label(self, text="Sex:")
        sex_label.place(x=370, y=110)

        contact_number_label = tk.Label(self, text="Contact #:")
        contact_number_label.place(x=33, y=110)

        address_label = tk.Label(self, text="Address:")
        address_label.place(x=33, y=140)

        #Create an entry box
        name_entry = tk.Entry(self, width=40)  
        name_entry.place(x=100, y=80)

        age_entry = tk.Entry(self, width=40)  
        age_entry.place(x=420, y=80)

        sex_entry = tk.Entry(self, width=40)  
        sex_entry.place(x=420, y=110)

        contact_number_entry = tk.Entry(self, width=40)  
        contact_number_entry.place(x=100, y=110)

        address_entry = tk.Entry(self, width=93) 
        address_entry.place(x=101, y=140)

        #Check button
        var1 = tk.IntVar()

        questions = tk.Label(self, text="Do you and/or your child have the following or have had the following in the last 14 days?", font=("Helvetica", 11, "bold"))
        questions.place(x=33, y=180)
        
        yes_check_button_1_label = tk.Label(self, text="Fever or chills?", font=("Helvetica", 11, "bold"))
        yes_check_button_1_label.place(x=33, y=220)

        yes_check_button_1 = tk.Radiobutton(self, variable=var1, value=1, text="Yes")
        yes_check_button_1.place(x=33, y=250)

        no_check_button_1 = tk.Radiobutton(self, variable=var1, value=0, text="No")
        no_check_button_1.place(x=100, y=250)

if __name__ == "__main__":
    entry = AddEntry()
    entry.mainloop()