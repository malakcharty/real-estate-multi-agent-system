
from tools.property_tools import search_properties
from tools.pricing_tools import compare_property_prices
from tools.recommendation_tools import rank_properties


def test_search_properties():
    results = search_properties(
        city="Casablanca",
        transaction="vente",
        max_price_mad=2500000,
        min_bedrooms=3,
        min_surface_m2=115,
    )

    assert [p["id"] for p in results] == ["P001"]


def test_no_results():
    results = search_properties(
        city="Casablanca",
        transaction="vente",
        max_price_mad=100000,
        min_bedrooms=3,
    )

    assert results == []


def test_pricing():
    result = compare_property_prices(["P001", "P002"])

    assert result["cheapest_per_m2"] == "P001"
    assert result["higher_price_percent"] == 15.13
    assert result["lower_price_percent"] == 13.14


def test_recommendation():
    result = rank_properties(
        city="Casablanca",
        transaction="vente",
        max_price_mad=2500000,
        min_bedrooms=3,
        min_surface_m2=100,
    )

    assert result["best_property"] == "P001"
    assert result["total"] == 2
