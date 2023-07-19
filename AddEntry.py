import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

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
        var2 = tk.IntVar()
        var3 = tk.IntVar()
        var4 = tk.IntVar()
        var5 = tk.IntVar()
        var6 = tk.IntVar()
        var7 = tk.IntVar()
        var8 = tk.IntVar()

        style = ttk.Style()
        style.configure("Custom.TRadiobutton", background="lightgray", foreground="black")

        questions = tk.Label(self, text="Do you and/or your child have the following or have had the following in the last 14 days?", font=("Helvetica", 11, "bold"))
        questions.place(x=33, y=180)
        
        yes_check_button_1_label = tk.Label(self, text="Fever or chills?", font=("Helvetica", 11, "bold"))
        yes_check_button_1_label.place(x=33, y=220)

        yes_check_button_1 = ttk.Radiobutton(self, variable=var1, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_check_button_1.place(x=33, y=250)

        no_check_button_1 = ttk.Radiobutton(self, variable=var1, value=0, text="No", style="Custom.TRadiobutton")
        no_check_button_1.place(x=100, y=250)

        check_button_2_label = tk.Label(self, text="Loss of smell, loss of taste?", font=("Helvetica", 11, "bold"))
        check_button_2_label.place(x=33, y=290)

        yes_check_button_2 = ttk.Radiobutton(self, variable=var2, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_check_button_2.place(x=33, y=320)

        no_check_button_2 = ttk.Radiobutton(self, variable=var2, value=0, text="No", style="Custom.TRadiobutton")
        no_check_button_2.place(x=100, y=320)

        yes_check_button_3_label = tk.Label(self, text="Cough, colds, sore throat?", font=("Helvetica", 11, "bold"))
        yes_check_button_3_label.place(x=180, y=220)

        yes_check_button_3 = ttk.Radiobutton(self, variable=var3, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_check_button_3.place(x=180, y=250)

        no_check_button_3 = ttk.Radiobutton(self, variable=var3, value=0, text="No", style="Custom.TRadiobutton")
        no_check_button_3.place(x=247, y=250)

        yes_check_button_4_label = tk.Label(self, text="Diarrhea?", font=("Helvetica", 11, "bold"))
        yes_check_button_4_label.place(x=405, y=220)

        yes_check_button_4 = ttk.Radiobutton(self, variable=var4, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_check_button_4.place(x=405, y=250)

        no_check_button_4 = ttk.Radiobutton(self, variable=var4, value=0, text="No", style="Custom.TRadiobutton")
        no_check_button_4.place(x=472, y=250)

        yes_check_button_5_label = tk.Label(self, text="Muscle pain?", font=("Helvetica", 11, "bold"))
        yes_check_button_5_label.place(x=550, y=220)

        yes_check_button_5 = ttk.Radiobutton(self, variable=var5, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_check_button_5.place(x=550, y=250)

        no_check_button_5 = ttk.Radiobutton(self, variable=var5, value=0, text="No", style="Custom.TRadiobutton")
        no_check_button_5.place(x=617, y=250)

        check_button_6_label = tk.Label(self, text="Shortness of breath?", font=("Helvetica", 11, "bold"))
        check_button_6_label.place(x=270, y=290)

        yes_check_button_6 = ttk.Radiobutton(self, variable=var6, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_check_button_6.place(x=270, y=320)

        no_check_button_6 = ttk.Radiobutton(self, variable=var6, value=0, text="No", style="Custom.TRadiobutton")
        no_check_button_6.place(x=337, y=320)

        check_button_7_label = ttk.Label(self, text="Excessive Fatigue?", font=("Helvetica", 11, "bold"))
        check_button_7_label.place(x=480, y=290)

        yes_check_button_7 = ttk.Radiobutton(self, variable=var7, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_check_button_7.place(x=480, y=320)

        no_check_button_7= ttk.Radiobutton(self, variable=var7, value=0, text="No", style="Custom.TRadiobutton")
        no_check_button_7.place(x=547, y=320)

        label_8 = tk.Label(self, text="Did you consult a medical doctor for the above mentioned signs and symptoms?", font=("Helvetica", 11, "bold"))
        label_8.place(x=70, y=370)

        yes_label_8_button = ttk.Radiobutton(self, variable=var8, value=1, text="Yes", style="Custom.TRadiobutton")
        yes_label_8_button.place(x=300, y=400)

        no_label_8_button = ttk.Radiobutton(self, variable=var8, value=0, text="No", style="Custom.TRadiobutton")
        no_label_8_button.place(x=360, y=400)
         
        #Submit Button
        submit_button = tk.Button(self, text="Submit", command=self.destroy)
        submit_button.place(x=305, y=450)

        go_back_to_main = tk.Button(self, text="Back", command=self.back_to_main)
        go_back_to_main.place(x=365, y=450)

    def back_to_main(self):
        self.destroy()
        from Covid_Contact_Tracing_App import AddSearch
        entry = AddSearch()
        entry.mainloop()

if __name__ == "__main__":
    entry = AddEntry()
    entry.mainloop()