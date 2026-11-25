
from tools.data_loader import load_properties


def search_properties(
    city: str,
    transaction: str,
    max_price_mad: int,
    min_bedrooms: int,
    min_surface_m2: float = 0,
) -> list[dict]:
    """Recherche des biens immobiliers parmi les annonces validées."""

    # Vérification des critères
    if (
        max_price_mad <= 0
        or min_bedrooms < 0
        or min_surface_m2 < 0
    ):
        return []

    # Normalisation des types de transactions
    transaction_mapping = {
        "sell": "vente",
        "sale": "vente",
        "buy": "vente",
        "achat": "vente",
        "vente": "vente",
        "rent": "location",
        "rental": "location",
        "louer": "location",
        "location": "location",
    }

    transaction = transaction.strip().casefold()
    transaction = transaction_mapping.get(
        transaction, transaction
    )

    # Chargement des données validées par Pydantic
    properties = load_properties()

    results = []

    # Filtrage des annonces
    for property_data in properties:
        if (
            property_data["city"].strip().casefold()
            == city.strip().casefold()
            and property_data["transaction"] == transaction
            and property_data["price_mad"] <= max_price_mad
            and property_data["bedrooms"] >= min_bedrooms
            and property_data["surface_m2"] >= min_surface_m2
        ):
            results.append(property_data)

    print(
        f">>> Property Search Tool exécuté : "
        f"{len(results)} biens trouvés"
    )

    return results
