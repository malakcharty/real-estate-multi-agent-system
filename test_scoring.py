
from tools.recommendation_tools import rank_properties

result = rank_properties(
    city="Casablanca",
    transaction="vente",
    max_price_mad=2500000,
    min_bedrooms=3,
    min_surface_m2=100,
    preferred_districts=[],
)

print("\nCLASSEMENT DES BIENS\n")

for property_data in result["properties"]:
    print(
        f"Rang {property_data['rank']} : "
        f"{property_data['id']} "
        f"({property_data['district']}) - "
        f"Score : {property_data['score']}/100"
    )

assert result["best_property"] == "P001"
assert len(result["properties"]) == 2

print("\nTest réussi !")

