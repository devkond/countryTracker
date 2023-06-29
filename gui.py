from tkinter import *
from tkinter import messagebox
from tracker import search

def search_country():
    country_name = input_country.get()
    if country_name:
        country_data = search(country_name)
        if country_data:
            country = country_data[0]
            country_name_label.config(text=f"Country Name: {country['name']['common']}")
            capital_label.config(text=f"Capital: {country['capital'][0]}")
            population_label.config(text=f"Population: {country['population']}")
            region_label.config(text=f"Region: {country['region']}")
            area_label.config(text=f"Area: {country['area']} km²")
            country_code_label.config(text=f"Country Code: {country['cca2']}")
        else:
            messagebox.showerror("Error", "Country not found.")
    else:
        messagebox.showerror("Error", "Please enter a country name.")

        # Clear the information if the country is not found or no country is provided
        clear_labels()

def clear_labels():
    labels = [country_name_label, capital_label, population_label, region_label, area_label, country_code_label]
    for label in labels:
        label.config(text="")

window = Tk()
window.title("Country Tracker")

input_country = Entry(window)
input_country.pack()

search_button = Button(window, text="Search", command=search_country)
search_button.pack()

instruction_label = Label(window, text="Enter a country name to view its information")
instruction_label.pack()

labels_frame = Frame(window)
labels_frame.pack()

country_name_label = Label(labels_frame, text="Country Name:")
country_name_label.pack()

capital_label = Label(labels_frame, text="Capital:")
capital_label.pack()

population_label = Label(labels_frame, text="Population:")
population_label.pack()

region_label = Label(labels_frame, text="Region:")
region_label.pack()

area_label = Label(labels_frame, text="Area:")
area_label.pack()

country_code_label = Label(labels_frame, text="Country Code:")
country_code_label.pack()

window.mainloop()
