import requests
from tqdm import tqdm

API_URL = "https://restcountries.com/v3.1/all"

def fetch_data():
    print("🌍 Récupération des pays...")
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    countries = response.json()

    result = []
    for country in tqdm(countries, desc="🔄 Chargement des pays", unit="pays"):
        result.append({
            "name": country["name"]["common"],
            "population": country.get("population", 0),
            "area": country.get("area", 0),
            "region": country.get("region", "N/A"),
        })

    print(f"✅ {len(result)} pays récupérés.")
    return result
