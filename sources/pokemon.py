import requests

API_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_data():
    pokemons = []
    for id in range(1, 201):
        response = requests.get(f"{API_URL}/{id}", timeout=10)
        if response.status_code == 200:
            p = response.json()
            pokemons.append({
                "name": p["name"],
                "height": p["height"],
                "weight": p["weight"],
                "base_experience": p["base_experience"]
            })
    return pokemons