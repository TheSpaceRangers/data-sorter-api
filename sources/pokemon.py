import requests
from tqdm import tqdm

API_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_data(limit=1302):
    pokemons = []
    url = f"{API_URL}?limit={limit}&offset=0"

    print("🐾 Récupération de la liste des Pokémon...")
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    results = response.json().get("results", [])

    for entry in tqdm(results, desc="🔄 Chargement Pokémon", unit="poke"):
        details = requests.get(entry["url"], timeout=10)
        if details.status_code == 200:
            p = details.json()
            pokemons.append({
                "name": p["name"],
                "height": p["height"],
                "weight": p["weight"],
                "base_experience": p["base_experience"]
            })

    print(f"✅ {len(pokemons)} Pokémon récupérés.")
    return pokemons
