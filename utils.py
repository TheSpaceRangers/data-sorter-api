def paginate_launches(launches, page_size=5):
    total = len(launches)
    current_page = 0
    total_pages = (total + page_size - 1) // page_size  # arrondi supérieur

    while True:
        start = current_page * page_size
        end = start + page_size
        page_items = launches[start:end]

        print(f"\n📄 Page {current_page + 1}/{total_pages} — Affichage de {len(page_items)} lancements :\n")
        for launch in page_items:
            print(f"{launch['name']} - {launch['date_utc'].strftime('%Y-%m-%d %H:%M:%S')}")

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
