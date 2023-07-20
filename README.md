# Covid-19: Contact Tracing App

This Covid Contact Tracing App was created in Python using the Tkinter framework. For contact tracing purposes, the software allows users to add information about themselves, including their name, age, sex, phone number, and suspected Covid symptoms. Additionally, a search function is offered, allowing users to find and view previously added entries. 

## Features

### Main Application - Covid Contact Tracing App (AddSearch):


- Offers the choice of adding a new entry or searching for an already-existing record.
- Displays two buttons—"Add Entry" and "Search Entry"—along with a background image.
- Users can submit their data and symptoms in a new window by clicking the "Add Entry" button.
- Users can search for a particular entry by name in a new window by clicking the "Search Entry" button.


### Second Window / Add Entry Window - AddEntry:


- Users are given the option to provide their name, age, sex, contact information, address, and any potential Covid symptoms.
- Uses checkboxes for recording symptoms and radio buttons to indicate whether or not a doctor should be consulted.
- Checks for required fields and warns the user if any are missing.
- After submission, the input fields are cleared and the data is saved to a CSV file.


### Third Window / Search Entry Window - SearchEntry:


- Enables users to search for a certain entry by name.
- If matching entries are located, they are returned and displayed.
- If no matching entries are discovered, displays a "No entries found" message.
- Gives users the option to close the window or go back to the main window by using the "Back" or "Close" buttons, respectively.



## To run the app

- Install the necessary libraries, including: (Note: Check that Tkinter, PIL (Python Imaging Library), and ttkthemes are installed. )

```bash
pip install tk
pip install pillow
pip install ttkthemes
```
- Go to the directory containing the code files and open a terminal or command window there.
- Enjoy!!



## 🔗 Video Presentation

- Here's the video presentation of my output.

```bash
https://drive.google.com/drive/folders/1n569wvMSCX6z0OOPfSU6ukRd_Yf2cddx?usp=sharing
```
