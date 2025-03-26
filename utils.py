def paginate_launches(launches, display_keys=None, page_size=5):
    total = len(launches)
    if total == 0:
        print("❌ Aucun élément à afficher.")
        return

    total_pages = (total + page_size - 1) // page_size
    current_page = 0

    while True:
        start = current_page * page_size
        end = start + page_size
        page_items = launches[start:end]

        if total_pages > 1:
            print(f"\n📄 Page {current_page + 1}/{total_pages} — Affichage {start + 1} à {min(end, total)} sur {total}\n")

        for launch in page_items:
            for key in display_keys or launch.keys():
                value = launch.get(key, "N/A")
                if isinstance(value, str) and "date" in key.lower():
                    print(f"📅 {key.capitalize():<12}: {value}")
                else:
                    print(f"{key.capitalize():<12}: {value}")
            print("-" * 40)

        if total_pages == 1:
            break

        print("\n[N] Suivant | [P] Précédent | [Q] Quitter")
        choice = input("Votre choix : ").strip().lower()

        if choice == "n" and current_page < total_pages - 1:
            current_page += 1
        elif choice == "p" and current_page > 0:
            current_page -= 1
        elif choice == "q":
            print("🔚 Fin de la pagination.")
            break
        else:
            print("⛔ Choix invalide ou limite atteinte.")
