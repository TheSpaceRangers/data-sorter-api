from sources import SOURCES
from storage import store_in_redis, retrieve_from_redis
from utils import paginate_launches
from sorting import bubble_sort, selection_sort, insertion_sort, quick_sort
from search import binary_search
from datetime import datetime

def compare_algorithms(data, key, reverse=False):
    results = {}
    sorted_versions = {}

    for name, func in {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Quick Sort": quick_sort
    }.items():
        sorted_data, exec_time = func(data, key, reverse)
        results[name] = exec_time
        sorted_versions[name] = sorted_data

    print("\n=== Temps d'exécution des tris (en ms) ===")
    for name, t in results.items():
        print(f"{name:<15}: {t:.3f} ms")

    best = min(results.items(), key=lambda x: x[1])
    print(f"\n🚀 Meilleur algorithme : {best[0]} ({best[1]:.3f} ms)")
    return sorted_versions[best[0]]

def fetch_and_cache_data(module, label, redis_key):
    data = module.fetch_data()

    for item in data:
        if "date_utc" in item and isinstance(item["date_utc"], str):
            try:
                item["date_utc"] = datetime.fromisoformat(item["date_utc"].replace("Z", "+00:00"))
            except ValueError:
                pass

    store_in_redis(data, key=redis_key)
    return data

def select_source():
    print("=== Choisissez une source de données ===")
    for key, conf in SOURCES.items():
        print(f"{key}. {conf['label']}")

    choice = input("Votre choix : ").strip()
    if choice not in SOURCES:
        print("⛔ Source invalide.")
        return None
    return SOURCES[choice]


def get_data(conf):
    label = conf["label"]
    module = conf["module"]
    redis_key = f"{label.lower()}:data"
    cached_data = retrieve_from_redis(key=redis_key)

    if cached_data:
        print(f"\n🔁 Données en cache Redis trouvées pour {label}.")
        print("1. Utiliser les données en cache")
        print("2. Récupérer à nouveau depuis l'API")
        source_choice = input("Votre choix : ").strip()

        if source_choice == "1":
            return cached_data
        elif source_choice == "2":
            return fetch_and_cache_data(module, label, redis_key)
        else:
            print("⛔ Choix invalide.")
            return None
    else:
        print(f"📡 Pas de cache disponible pour {label}. Récupération depuis l'API...")
        return fetch_and_cache_data(module, label, redis_key)


def search_element(sorted_data, conf):
    search_key = conf.get("search_key", None)
    display_keys = conf["display_keys"]

    if not search_key:
        print("🔒 La recherche n'est pas disponible pour cette source.")
        return

    print(search_key)

    search_sorted, *_ = quick_sort(sorted_data, key=search_key, reverse=False)
    search_value = input(f"\n🔎 Entrez une valeur à rechercher par '{search_key}' : ").strip()
    result = binary_search(search_sorted, key=search_key, target=search_value)

    if result:
        print("\n✅ Élément trouvé :")
        paginate_launches([result], display_keys=display_keys)
    else:
        print("❌ Aucun résultat trouvé.")


def paginate_elements(data, display_keys):
    if len(data) > 1:
        paginate_launches(data, display_keys=display_keys)
    elif data:
        paginate_launches([data[0]], display_keys=display_keys)
    else:
        print("📭 Aucune donnée à afficher.")


def handle_user_action(sorted_data, conf):
    display_keys = conf["display_keys"]

    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. 🔍 Rechercher un élément")
        print("2. 📑 Parcourir tous les éléments")
        print("q. ❌ Quitter")
        action_choice = input("Votre choix : ").strip()

        if action_choice == "1":
            search_element(sorted_data, conf)
        elif action_choice == "2":
            paginate_elements(sorted_data, display_keys)
        elif action_choice == "q":
            print("👋 À bientôt !")
            break
        else:
            print("⛔ Choix invalide.")


def menu():
    conf = select_source()
    if not conf:
        return

    data = get_data(conf)
    if not data:
        return

    sorted_data = compare_algorithms(data, key=conf["sort_key"], reverse=conf.get("reverse", False))
    handle_user_action(sorted_data, conf)



if __name__ == "__main__":
    menu()
