
from tools.data_loader import load_properties


def compare_property_prices(property_ids: list[str]) -> dict:
    """Compare les prix au m² des biens immobiliers validés."""

    requested_ids = {
        property_id.strip().upper()
        for property_id in property_ids
    }

    # Charger uniquement les annonces validées par Pydantic
    properties = load_properties()

    results = []

    for property_data in properties:
        if property_data["id"].strip().upper() not in requested_ids:
            continue

        if property_data["transaction"] != "vente":
            continue

        surface = property_data["surface_m2"]
        price = property_data["price_mad"]

        results.append({
            "id": property_data["id"],
            "district": property_data["district"],
            "surface_m2": surface,
            "price_mad": price,
            "price_per_m2": round(price / surface, 2),
        })

    if not results:
        return {"error": "Aucun bien valide trouvé."}

    # Classement du prix au m² le plus bas au plus élevé
    results.sort(key=lambda item: item["price_per_m2"])

    comparison = {
        "properties": results,
        "cheapest_per_m2": results[0]["id"],
        "note": (
            "Comparaison entre annonces fictives, "
            "pas une estimation du marché."
        ),
    }

    if len(results) >= 2:
        lowest = results[0]["price_per_m2"]
        highest = results[-1]["price_per_m2"]

        # Différence absolue en MAD/m²
        comparison["price_gap_per_m2"] = round(
            highest - lowest, 2
        )

        # Pourcentage : le plus cher par rapport au moins cher
        comparison["higher_price_percent"] = round(
            (highest - lowest) / lowest * 100, 2
        )

        # Pourcentage : le moins cher par rapport au plus cher
        comparison["lower_price_percent"] = round(
            (highest - lowest) / highest * 100, 2
        )

    print(">>> Pricing Analysis Tool exécuté")

    return comparison
