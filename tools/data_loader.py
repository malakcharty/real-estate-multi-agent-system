import csv
from pathlib import Path

from pydantic import ValidationError
from models.property import Property


DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "properties.csv"
)


def load_properties() -> list[dict]:
    """Charge et valide les annonces immobilières."""

    valid_properties = []

    with DATA_FILE.open(
        encoding="utf-8-sig",
        newline=""
    ) as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                property_data = Property.model_validate(row)

                valid_properties.append(
                    property_data.model_dump()
                )

            except ValidationError as error:
                print(
                    f">>> Annonce invalide : {row.get('id')}"
                )
                print(error)

    print(
        f">>> {len(valid_properties)} annonces valides chargées"
    )

    return valid_properties