import csv
from pathlib import Path

from pydantic import ValidationError
from models.property import Property

DATA_FILE = Path("data/properties.csv")

# Test 1 : vérifier les annonces du CSV
with DATA_FILE.open(encoding="utf-8-sig", newline="") as file:
    properties = csv.DictReader(file)

    for row in properties:
        try:
            property_data = Property.model_validate(row)
            print(f"VALID : {property_data.id}")
        except ValidationError as error:
            print(f"INVALID : {row.get('id')}")
            print(error)

# Test 2 : vérifier une annonce invalide
invalid_property = {
    "id": "P999",
    "city": "Casablanca",
    "district": "Oasis",
    "transaction": "vente",
    "property_type": "appartement",
    "bedrooms": 3,
    "surface_m2": -50,
    "price_mad": 2000000,
}

try:
    Property.model_validate(invalid_property)
except ValidationError:
    print("TEST REUSSI : superficie négative rejetée")