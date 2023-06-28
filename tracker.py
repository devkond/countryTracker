# import requests to use an api
import requests
import os

# asking to try the code
try:
    print("=" * 21)
    name = input("Choose an country by their name: ") 
    os.system("cls")

# Verify if theres an input
    if name:
        # define url
        url = f"https://restcountries.com/v3/name/{name}"
        # get url informations
        response = requests.get(url)
        data = response.json()

        if data:
            # Pick just the first information
            country = data[0]

            print("=" * 21)
            print("Country information:")
            print(f"Name: {country['name']['common']}")
            print(f"Capital: {country['capital'][0]}")
            print(f"Population: {country['population']}")
            print(f"Region: {country['region']}")
            print(f"Area: {country['area']} km²")
            print(f"Country Code: {country['cca2']}")
            print("=" * 21)
        else:
            # If dont exist no country with input name, then show this
            print("No country was found with this name.")
    else:
        print("Provide an country name.")

except Exception as ex:
    # To prevent mistakes
    print(f"ERROR: {ex}")
