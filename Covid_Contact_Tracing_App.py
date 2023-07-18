#Vargas, Ruben A
#BSCPE 1-4
#Object-Oriented Programming

import tkinter as tk

class AddSearch(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Contact Tracing App")
        self.geometry("700x500")

        self.header_label = tk.Label(self, text="Covid-19: Contact Tracing App", font=("Helvetica", 14, "bold"))
        self.header_label.pack