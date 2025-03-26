import requests
from tqdm import tqdm

API_URL = "https://dummyjson.com/products"

def fetch_data():
    products = []
    limit = 100
    skip = 0

    print("📦 Récupération des produits...")

    while True:
        url = f"{API_URL}?limit={limit}&skip={skip}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        batch = data.get("products", [])
        total = data.get("total", 0)

        if not batch:
            break

        products.extend(batch)
        skip += limit

        tqdm.write(f"🔄 {len(products)} / {total} produits...")

        if skip >= total:
            break

    print(f"✅ {len(products)} produits récupérés.")
    return [
        {
            "name": p["title"],
            "price": p["price"],
            "rating": p["rating"],
            "category": p["category"],
            "stock": p["stock"]
        }
        for p in products
    ]
