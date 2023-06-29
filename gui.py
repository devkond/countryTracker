from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import tracker

def CountryTrackerGUI():

    def search_country():
        country_name = input_country.get()
        if country_name:
            country_data = tracker.search(country_name)
            if country_data:
                country = country_data[0]
                country_name_label.configure(text=f"Country Name: {country['name']['common']}")
                capital_label.configure(text=f"Capital: {country['capital'][0]}")
                population_label.configure(text=f"Population: {country['population']}")
                region_label.configure(text=f"Region: {country['region']}")
                area_label.configure(text=f"Area: {country['area']} km²")
                country_code_label.configure(text=f"Country Code: {country['cca2']}")
            else:
                messagebox.showerror("Error", "Country not found.")

        # Clear the input field
        input_country.delete(0, END)

    def clear_labels():
        country_name_label.configure(text="Country Name:")
        capital_label.configure(text="Capital:")
        population_label.configure(text="Population:")
        region_label.configure(text="Region:")
        area_label.configure(text="Area:")
        country_code_label.configure(text="Country Code:")

    window = ctk.CTk()
    window.title("tracker")
    window.geometry("400x300")

    input_country = ctk.CTkEntry(window)
    input_country.pack(padx=10, pady=10)

    search_button = ctk.CTkButton(window, text="Search", command=search_country)
    search_button.pack(padx=10, pady=5)

    labels_frame = ctk.CTkFrame(window)
    labels_frame.pack(padx=10, pady=10)

    country_name_label = ctk.CTkLabel(labels_frame, text="Country Name:")
    country_name_label.pack(anchor="w")

    capital_label = ctk.CTkLabel(labels_frame, text="Capital:")
    capital_label.pack(anchor="w")

    population_label = ctk.CTkLabel(labels_frame, text="Population:")
    population_label.pack(anchor="w")

    region_label = ctk.CTkLabel(labels_frame, text="Region:")
    region_label.pack(anchor="w")

    area_label = ctk.CTkLabel(labels_frame, text="Area:")
    area_label.pack(anchor="w")

    country_code_label = ctk.CTkLabel(labels_frame, text="Country Code:")
    country_code_label.pack(anchor="w")

    window.mainloop()