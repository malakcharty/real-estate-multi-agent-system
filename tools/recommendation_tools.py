import unicodedata

from tools.property_tools import search_properties


def normalize_text(value: str) -> str:
    """Normalise les accents et les majuscules."""
    text = unicodedata.normalize("NFKD", value)
    return "".join(
        char for char in text
        if not unicodedata.combining(char)
    ).strip().casefold()


def rank_properties(
    city: str,
    transaction: str,
    max_price_mad: int,
    min_bedrooms: int,
    min_surface_m2: float = 0,
    preferred_districts: list[str] | None = None,
) -> dict:
    """Classe les appartements selon un score multicritère."""

    if max_price_mad <= 0 or min_bedrooms < 0 or min_surface_m2 < 0:
        raise ValueError("Critères de recherche invalides.")

    # Étape 1 : rechercher les biens éligibles
    properties = search_properties(
        city=city,
        transaction=transaction,
        max_price_mad=max_price_mad,
        min_bedrooms=min_bedrooms,
    )

    eligible = []

    for item in properties:
        surface = float(item["surface_m2"])
        price = float(item["price_mad"])

        if item["property_type"].casefold() != "appartement":
            continue

        if surface <= 0 or price <= 0:
            continue

        if surface < min_surface_m2:
            continue

        eligible.append({
            "id": item["id"],
            "district": item["district"],
            "surface_m2": surface,
            "price_mad": price,
            "price_per_m2": price / surface,
        })

    if not eligible:
        return {
            "properties": [],
            "message": "Aucun appartement ne correspond aux critères.",
        }

    # Étape 2 : références pour le scoring relatif
    min_price_m2 = min(p["price_per_m2"] for p in eligible)
    min_price = min(p["price_mad"] for p in eligible)
    max_surface = max(p["surface_m2"] for p in eligible)

    preferences = {
        normalize_text(district)
        for district in (preferred_districts or [])
    }

    # Étape 3 : calculer les scores
    for item in eligible:
        price_m2_score = (
            min_price_m2 / item["price_per_m2"]
        ) * 40

        surface_score = (
            item["surface_m2"] / max_surface
        ) * 25

        total_price_score = (
            min_price / item["price_mad"]
        ) * 20

        district_match = (
            not preferences
            or normalize_text(item["district"]) in preferences
        )

        district_score = 15 if district_match else 0

        item["score_details"] = {
            "price_per_m2": round(price_m2_score, 2),
            "surface": round(surface_score, 2),
            "total_price": round(total_price_score, 2),
            "district": district_score,
        }

        item["score"] = round(
            price_m2_score
            + surface_score
            + total_price_score
            + district_score,
            2,
        )

        item["price_per_m2"] = round(
            item["price_per_m2"], 2
        )

    # Étape 4 : trier du meilleur score au moins bon
    eligible.sort(
        key=lambda p: (-p["score"], p["price_mad"], p["id"])
    )

    for rank, item in enumerate(eligible, start=1):
        item["rank"] = rank

    print(">>> Recommendation Scoring Tool exécuté")

    return {
        "properties": eligible,
        "total": len(eligible),
        "best_property": eligible[0]["id"],
        "note": (
            "Scores relatifs à ce groupe de biens fictifs. "
            "Il ne s'agit pas d'une estimation du marché."
        ),
    }
