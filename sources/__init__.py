from . import spacex, crypto, countries, products, pokemon

SOURCES = {
    "1": {
        "label": "SpaceX",
        "module": spacex,
        "sort_key": "date_utc",
        "display_keys": ["name", "date_utc", "success", "rocket", "launchpad", "flight_number"],
        "reverse": True  # tri décroissant
    },
    "2": {
        "label": "Crypto",
        "module": crypto,
        "sort_key": "price",
        "display_keys": ["name", "symbol", "price", "market_cap", "volume", "last_updated"],
        "reverse": True
    },
    "3": {
        "label": "Pays",
        "module": countries,
        "sort_key": "population",
        "display_keys": ["name", "region", "population", "area"],
        "reverse": True
    },
    "4": {
        "label": "Produits",
        "module": products,
        "sort_key": "price",
        "display_keys": ["name", "brand", "price", "rating", "category", "stock"],
        "reverse": True
    },
    "5": {
        "label": "Pokémon",
        "module": pokemon,
        "sort_key": "base_experience",
        "display_keys": ["name", "height", "weight", "base_experience"],
        "reverse": True
    },
}
