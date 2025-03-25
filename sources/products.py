import requests

API_URL = "https://dummyjson.com/products"

def fetch_data():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    products = response.json().get("products", [])

    print(products)

    return [
        {
            "name": product["title"],
            # "brand": product["brand"],
            "price": product["price"],
            "rating": product["rating"],
            "category": product["category"],
            "stock": product["stock"]
        }
        for product in products
    ]