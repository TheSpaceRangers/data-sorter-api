from api import get_launches_from_api
from storage import store_in_redis, retrieve_from_redis
from utils import paginate_launches
from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort
from datetime import datetime

def compare_algorithms(data, key):
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort
    }

    convert_dates(data)
    results = {}
    for name, func in algorithms.items():
        sorted_data, exec_time = func(data, key)
        results[name] = {
            "time": round(exec_time, 3),
            "data": sorted_data
        }

    print("\n=== Temps d'exécution des tris (en ms) ===")
    for name, result in results.items():
        print(f"{name:<15}: {result['time']} ms")

    # Trouver le plus rapide
    best_algo = min(results, key=lambda x: results[x]["time"])
    print(f"\n🚀 Meilleur algorithme : {best_algo} ({results[best_algo]['time']} ms)")
    return results[best_algo]["data"]

def convert_dates(data):
    for item in data:
        try:
            item["date_utc"] = datetime.fromisoformat(item["date_utc"].replace("Z", "+00:00"))
        except Exception as e:
            print(f"Erreur de conversion de date pour {item['name']}: {e}")
    return data

def menu():
    print("\n=== Menu Principal ===")
    print("1. Récupérer les données depuis l'API")
    print("2. Récupérer les données depuis Redis")
    choice = input("Votre choix (1 ou 2) : ")

    if choice == "1":
        data = get_launches_from_api()
        store_in_redis(data)
    elif choice == "2":
        data = retrieve_from_redis()
    else:
        print("Choix invalide.")
        return

    if not data:
        print("Aucune donnée à trier.")
        return

    sorted_data = compare_algorithms(data, key="date_utc")
    paginate_launches(sorted_data)

if __name__ == "__main__":
    menu()
