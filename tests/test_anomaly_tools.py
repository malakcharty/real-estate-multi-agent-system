
from tools.anomaly_tools import detect_property_anomalies


def test_anomaly_detection():
    base_property = {
        "id": "P100",
        "city": "Casablanca",
        "district": "Oasis",
        "transaction": "vente",
        "property_type": "appartement",
        "bedrooms": 3,
        "surface_m2": 120,
        "price_mad": 600000,
    }

    rows = [
        base_property,
        {**base_property},  # Identifiant en double
        {
            **base_property,
            "id": "P999",
            "surface_m2": -50,  # Surface invalide
        },
    ]

    result = detect_property_anomalies(
        rows,
        min_price_per_m2=10000,
        max_price_per_m2=35000,
    )

    anomaly_types = {
        anomaly["type"]
        for anomaly in result["anomalies"]
    }

    assert "duplicate_id" in anomaly_types
    assert "invalid_data" in anomaly_types
    assert "price_per_m2_out_of_range" in anomaly_types