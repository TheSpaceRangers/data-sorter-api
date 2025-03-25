def paginate_launches(launches, page_size=1):
    total = len(launches)
    current_page = 0
    total_pages = (total + page_size - 1) // page_size

    while True:
        start = current_page * page_size
        end = start + page_size
        page_items = launches[start:end]

        print(f"\n📄 Page {current_page + 1}/{total_pages} — Lancements {start + 1} à {min(end, total)} sur {total}\n")

        for launch in page_items:
            name = launch.get("name", "N/A")
            date = launch.get("date_utc", "N/A")
            if isinstance(date, str):
                date_str = date
            else:
                date_str = date.strftime("%Y-%m-%d %H:%M:%S UTC")

            success = launch.get("success")
            success_str = "✅ Succès" if success else ("❌ Échec" if success is False else "❓ Inconnu")

            rocket = launch.get("rocket", "N/A")
            launchpad = launch.get("launchpad", "N/A")
            flight_number = launch.get("flight_number", "N/A")

            print(f"🚀 {name}")
            print(f"📅 Date      : {date_str}")
            print(f"{success_str:>12}")
            print(f"🛩️ Rocket    : {rocket}")
            print(f"📍 Launchpad : {launchpad}")
            print(f"🔢 Vol n°    : {flight_number}")
            print("-" * 40)

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
