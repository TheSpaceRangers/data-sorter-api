import requests
import time
from tqdm import tqdm

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PER_PAGE = 100
MAX_PAGES = 20
DELAY = 2

def fetch_data():
    all_coins = []
    print("💰 Récupération des cryptos CoinGecko...")

    for page in tqdm(range(1, MAX_PAGES + 1), desc="🔄 Chargement des pages", unit="page"):
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": PER_PAGE,
            "page": page
        }
        response = requests.get(API_URL, params=params, timeout=10)

        if response.status_code == 429:
            print("⚠️ Limite atteinte (429). Pause plus longue...")
            time.sleep(10)
            continue

        response.raise_for_status()
        coins = response.json()

        if not coins:
            break

        all_coins.extend(coins)
        time.sleep(DELAY)

    print(f"\n✅ {len(all_coins)} cryptos récupérées.")

    return [
        {
            "name": coin["name"],
            "symbol": coin["symbol"],
            "price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "volume": coin["total_volume"],
            "last_updated": coin["last_updated"]
        }
        for coin in all_coins
    ]
