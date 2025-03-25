import requests

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1
}

def fetch_data():
    response = requests.get(API_URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    coins = response.json()

    return [
        {
            "name": coin["name"],
            "symbol": coin["symbol"],
            "price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "volume": coin["total_volume"],
            "last_updated": coin["last_updated"]
        }
        for coin in coins
    ]
