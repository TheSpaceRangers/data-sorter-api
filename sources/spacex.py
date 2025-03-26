import requests
from tqdm import tqdm

API_URL = "https://api.spacexdata.com/v5/launches"

def fetch_data():
    try:
        print("🚀 Récupération des lancements SpaceX...")
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        launches = response.json()

        filtered = [
            launch for launch in launches
            if launch.get("date_utc") is not None
        ]

        print(f"✅ {len(filtered)} lancements récupérés.")

        result = []
        for launch in tqdm(filtered, desc="🔄 Traitement des données", unit="launch"):
            result.append({
                "name": launch["name"],
                "date_utc": launch["date_utc"],
                "success": launch["success"],
                "rocket": launch["rocket"],
                "launchpad": launch["launchpad"],
                "flight_number": launch["flight_number"]
            })

        return result

    except requests.RequestException as e:
        print(f"❌ Erreur API : {e}")
        return []
