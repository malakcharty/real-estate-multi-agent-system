import csv

from pydantic import ValidationError

from models.property import Property
from tools.data_loader import DATA_FILE


def detect_property_anomalies(
    rows: list[dict],
    min_price_per_m2: float | None = None,
    max_price_per_m2: float | None = None,
) -> dict:
    """Détecte les anomalies dans les annonces immobilières."""

    if (
        min_price_per_m2 is not None
        and min_price_per_m2 < 0
    ):
        raise ValueError("Le prix minimum doit être positif.")

    if (
        max_price_per_m2 is not None
        and max_price_per_m2 <= 0
    ):
        raise ValueError("Le prix maximum doit être positif.")

    if (
        min_price_per_m2 is not None
        and max_price_per_m2 is not None
        and min_price_per_m2 > max_price_per_m2
    ):
        raise ValueError("Plage de prix incohérente.")

    anomalies = []
    seen_ids = set()
    valid_count = 0

    for row in rows:
        property_id = str(row.get("id") or "UNKNOWN")

        # 1. Validation des données avec Pydantic
        try:
            property_data = Property.model_validate(row)
        except ValidationError as error:
            anomalies.append({
                "id": property_id,
                "type": "invalid_data",
                "details": [
                    str(e["loc"][0])
                    for e in error.errors()
                ],
            })
            continue

        valid_count += 1
        normalized_id = property_data.id.strip().upper()

        # 2. Détection des identifiants en double
        if normalized_id in seen_ids:
            anomalies.append({
                "id": property_id,
                "type": "duplicate_id",
                "details": "Identifiant déjà présent",
            })
        else:
            seen_ids.add(normalized_id)

        # 3. Détection des prix au m² inhabituels
        if property_data.transaction == "vente":
            price_per_m2 = (
                property_data.price_mad
                / property_data.surface_m2
            )

            outside_min = (
                min_price_per_m2 is not None
                and price_per_m2 < min_price_per_m2
            )

            outside_max = (
                max_price_per_m2 is not None
                and price_per_m2 > max_price_per_m2
            )

            if outside_min or outside_max:
                anomalies.append({
                    "id": property_id,
                    "type": "price_per_m2_out_of_range",
                    "price_per_m2": round(price_per_m2, 2),
                    "details": "Prix hors de la plage configurée",
                })

    return {
        "total_rows": len(rows),
        "valid_rows": valid_count,
        "anomaly_count": len(anomalies),
        "anomalies": anomalies,
    }


def scan_property_data(
    min_price_per_m2: float | None = None,
    max_price_per_m2: float | None = None,
) -> dict:
    """Analyse le fichier CSV immobilier."""

    with DATA_FILE.open(
        encoding="utf-8-sig",
        newline=""
    ) as file:
        rows = list(csv.DictReader(file))

    return detect_property_anomalies(
        rows,
        min_price_per_m2=min_price_per_m2,
        max_price_per_m2=max_price_per_m2,
    )