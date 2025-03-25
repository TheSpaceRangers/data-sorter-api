import requests

API_URL = "https://api.spacexdata.com/v5/launches"

def get_launches_from_api():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        launches = response.json()
        print(f"✅ {len(launches)} lancements récupérés depuis l'API.")
        return [
            {
                "name": launch["name"],
                "date_utc": launch["date_utc"],
                "success": launch["success"],
                "rocket": launch["rocket"],
                "launchpad": launch["launchpad"],
                "flight_number": launch["flight_number"]
            }
            for launch in launches
            if launch.get("date_utc") is not None
        ]
    except requests.RequestException as e:
        print(f"❌ Erreur API : {e}")
        return []
