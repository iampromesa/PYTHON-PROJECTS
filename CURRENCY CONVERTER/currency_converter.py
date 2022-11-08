import requests
import json

# importing from tkinter
from tkinter import *

# importing tkk from tkinter 
from tkinter import ttk

API_KEY = "816bff4d73dcc1d96466bdf0"

#the standard request url 
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

# making the Standard request to the API and converting the request to json
response = requests.get(f"{url}").json()

#converting the currencies into dictionaries
currencies = dict(response["conversion_rates"])

# creating the main window 
window = Tk()

# this gives the window width(310) ,height(340) and the position center 
window.geometry("310x340+500+200")

# window title 
window.title("Promesa's Currency Converter")

# this will make the window non resizeable since height and width = FALSE
window.resizable(height=TRUE, width=TRUE)

# colours for the application
primary = "#081F4D"
secondary = "#0083FF"
white = "#FFFFFF"

# the top frame
top_frame = Frame(window, bg=primary, width=300, height=80)
top_frame.grid(row=0, column=0)

# label for the text Currency Converter
name_label = Label(top_frame, text="Currency Converter", bg=primary, fg=white, pady=30, padx=24, justify=CENTER, font=('Poppins 20 bold'))
name_label.grid(row=0, column=0)

# the bottom frame
bottom_frame = Frame(window, width=300, height=250)
bottom_frame.grid(row=1, column=0)

# widgets inside the bottom frame
from_currency_label = Label(bottom_frame, text="FROM:", font=("Poppins 10 bold"), justify=LEFT)
from_currency_label.place(x=5, y=10)
to_currency_label = Label(bottom_frame, text="TO:", font=("Poppins 10 bold"), justify=RIGHT)
to_currency_label.place(x=160, y=10)

# this is the combobox for holding from_currencies
from_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=14, font=('Poppins 10 bold'))
from_currency_combo.place(x=5, y=30)

# this is the combobox for holding to_currencies
to_currency_combo = ttk.Combobox(bottom_frame, width=14, font=("Poppins 10 bold"))
to_currency_combo.place(x=160, y=30)

# the label for AMOUNT
amount_label = Label(bottom_frame, text='AMOUNT:', font=("Poppins 10 bold"))
amount_label.place(x=5, y=55)

# entry for amount
amount_entry = Entry(bottom_frame, width=25, font=("Poppins 15 bold"))
amount_entry.place(x=5, y=80)

# an empty label for displaying the result
result_label = Label(bottom_frame, text=" ", font=("Poppins 10 bold"))
result_label.place(x=5, y=115)

# an empty label for displaying the time
time_label = Label(bottom_frame, text=" ", font=('Poppins 10 bold'))
time_label.place(x=5, y=135)

# the clickable button for converting the currency
convert_button = Button(bottom_frame, text="CONVERT", bg=secondary, fg=white, font=('Poppins 10 bold'))
convert_button.place(x=5, y=165)

# this run the windows until it is closed 
window.mainloop()
