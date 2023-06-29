# import requests to use an API
import requests
import os

api = "https://restcountries.com/v3/name/{}"

def search(name):
    response = requests.get(api.format(name))
    if (response.status_code==200):
        return response.json()
    return False

def search_and_display(name):
    try:
        print("=" * 21)
        os.system("cls")

        if name:
            # Get URL information
            data = search(name)

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
                # If no country exists with the input name, then show this
                print("No country was found with this name.")
        else:
            print("Provide a country name.")

    except Exception as ex:
        # To handle errors
        print(f"ERROR: {ex}")