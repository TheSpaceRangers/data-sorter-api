import requests

API_URL = "https://restcountries.com/v3.1/all"

def fetch_data():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    countries = response.json()

    return [
        {
            "name": country["name"]["common"],
            "population": country.get("population", 0),
            "area": country.get("area", 0),
            "region": country.get("region", "N/A"),
        }
        for country in countries
    ]
