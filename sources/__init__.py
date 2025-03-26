from . import spacex, crypto, countries, products, pokemon

SOURCES = {
    "1": {
        "label": "SpaceX",
        "module": spacex,
        "sort_key": "date_utc",
        "search_key": "flight_number",
        "display_keys": ["name", "date_utc", "success", "rocket", "launchpad", "flight_number"],
        "reverse": True
    },
    "2": {
        "label": "Crypto",
        "module": crypto,
        "sort_key": "price",
        "search_key": "symbol",
        "display_keys": ["name", "symbol", "price", "market_cap", "volume", "last_updated"],
        "reverse": True
    },
    "3": {
        "label": "Pays",
        "module": countries,
        "sort_key": "population",
        "search_key": "name",
        "display_keys": ["name", "region", "population", "area"],
        "reverse": True
    },
    "4": {
        "label": "Produits",
        "module": products,
        "sort_key": "price",
        "search_key": "name",
        "display_keys": ["name", "price", "rating", "category", "stock"],
        "reverse": True
    },
    "5": {
        "label": "Pokémon",
        "module": pokemon,
        "sort_key": "base_experience",
        "search_key": "name",
        "display_keys": ["name", "height", "weight", "base_experience"],
        "reverse": True
    },
}
