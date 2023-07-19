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

        search_button = tk.Button(self, text="Search", command=self.search_info)
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

        if found_entries:
            found = tk.Label(self, text="Here's what we have found", font=("Helvetica", 11, "bold"))
            found.place(x=250, y=80)
            name_label = tk.Label(self, text=f"Name: {found_entries[0][0]}", font=("Helvetica", 11))
            name_label.place(x=30, y=130)
            age_label = tk.Label(self, text=f"Age: {found_entries[0][1]}", font=("Helvetica", 11))
            age_label.place(x=250, y=130)
            sex_label = tk.Label(self, text=f"Sex: {found_entries[0][2]}", font=("Helvetica", 11))
            sex_label.place(x=340, y=130)
            contact_label = tk.Label(self, text=f"Contact Number: {found_entries[0][3]}", font=("Helvetica", 11))
            contact_label.place(x=440, y=130)
            address_label = tk.Label(self, text=f"Address: {found_entries[0][4]}", font=("Helvetica", 11))
            address_label.place(x=30, y=160)
            symptom_label = tk.Label(self, text=f"Fever or chills? {found_entries[0][5]}", font=("Helvetica", 11))
            symptom_label.place(x=30, y=220)
            symptom1_label = tk.Label(self, text=f"Loss of smell, loss of taste? {found_entries[0][6]}", font=("Helvetica", 11))
            symptom1_label.place(x=30, y=250)
            symptom2_label = tk.Label(self, text=f"Cough, colds, sore throat? {found_entries[0][7]}", font=("Helvetica", 11))
            symptom2_label.place(x=30, y=280)
            symptom3_label = tk.Label(self, text=f"Diarrhea? {found_entries[0][8]}", font=("Helvetica", 11))
            symptom3_label.place(x=290, y=220)
            symptom4_label = tk.Label(self, text=f"Muscle pain? {found_entries[0][9]}", font=("Helvetica", 11))
            symptom4_label.place(x=290, y=250)
            symptom5_label = tk.Label(self, text=f"Shortness of breath? {found_entries[0][10]}", font=("Helvetica", 11))
            symptom5_label.place(x=290, y=280)
            symptom6_label = tk.Label(self, text=f"Excessive Fatigue? {found_entries[0][11]}", font=("Helvetica", 11))
            symptom6_label.place(x=490, y=220)
            consult_label = tk.Label(self, text=f"Did you consult a medical doctor for the above mentioned signs and symptoms? {found_entries[0][12]}", font=("Helvetica", 11))
            consult_label.place(x=30, y=340)
            be_safe = tk.Label(self, text="Be Informed, Prepared, Smart, and Safe! Be Ready to fight COVID-19", font=("Helvetica", 11, "bold"))
            be_safe.place(x=110, y=390)
        else:
            self.result_label = tk.Label(self, text="No entries found", font=("Helvetica", 11, "bold"))
            self.result_label.place(x=290, y=80)

    def back_to_main(self):
        self.destroy()
        from Covid_Contact_Tracing_App import AddSearch
        entry = AddSearch()
        entry.mainloop()

if __name__ == "__main__":
    search = SearchEntry()
    search.mainloop()