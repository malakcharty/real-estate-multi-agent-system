from typing import Literal

from pydantic import BaseModel, Field


class Property(BaseModel):
    """Modèle de validation d'un bien immobilier."""

    id: str = Field(min_length=1)
    city: str = Field(min_length=1)
    district: str = Field(min_length=1)

    transaction: Literal["vente", "location"]
    property_type: str = Field(min_length=1)

    bedrooms: int = Field(ge=0)
    surface_m2: float = Field(gt=0)
    price_mad: float = Field(gt=0)
