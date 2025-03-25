from sources import SOURCES
from storage import store_in_redis, retrieve_from_redis
from utils import paginate_launches
from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort
from datetime import datetime

def compare_algorithms(data, key, reverse=False):
    results = {}
    sorted_versions = {}

    from time import perf_counter
    from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort
    for name, func in {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort
    }.items():
        sorted_data, exec_time = func(data, key, reverse)
        results[name] = exec_time
        sorted_versions[name] = sorted_data

    # Affichage des temps
    print("\n=== Temps d'exécution des tris (en ms) ===")
    for name, t in results.items():
        print(f"{name:<15}: {t:.3f} ms")

    best = min(results.items(), key=lambda x: x[1])
    print(f"\n🚀 Meilleur algorithme : {best[0]} ({best[1]:.3f} ms)")
    return sorted_versions[best[0]]

def convert_dates(data):
    for item in data:
        try:
            item["date_utc"] = datetime.fromisoformat(item["date_utc"].replace("Z", "+00:00"))
        except Exception as e:
            print(f"Erreur de conversion de date pour {item['name']}: {e}")
    return data

def menu():
    print("=== Choisissez une source de données ===")
    for key, conf in SOURCES.items():
        print(f"{key}. {conf['label']}")

    choice = input("Votre choix : ").strip()
    if choice not in SOURCES:
        print("⛔ Source invalide.")
        return

    conf = SOURCES[choice]
    label = conf["label"]
    module = conf["module"]
    sort_key = conf["sort_key"]
    display_keys = conf["display_keys"]
    reverse = conf.get("reverse", False)

    data = module.fetch_data()
    print(f"✅ Données récupérées depuis {label} ({len(data)} éléments)")

    # conversion éventuelle de date
    for item in data:
        if "date_utc" in item:
            try:
                item["date_utc"] = datetime.fromisoformat(item["date_utc"].replace("Z", "+00:00"))
            except:
                pass

    redis_key = f"{label.lower()}:data"
    store_in_redis(data, key=redis_key)
    data = retrieve_from_redis(key=redis_key)

    sorted_data = compare_algorithms(data, key=sort_key, reverse=reverse)
    paginate_launches(sorted_data, display_keys=display_keys)

if __name__ == "__main__":
    menu()
