
from agno.agent import Agent
from test_connection import model


def calculate_price_per_m2(price: float, surface: float) -> float:
    """Calcule le prix au m² d'un bien immobilier."""
    if surface <= 0:
        raise ValueError("La surface doit être positive.")

    print(">>> Outil Python exécuté")
    return round(price / surface, 2)


agent = Agent(
    name="Real Estate Pricing Agent",
    model=model,
    tools=[calculate_price_per_m2],
    instructions=[
        "Tu es spécialisé dans l'analyse immobilière.",
        "Utilise l'outil pour calculer le prix au m².",
        "N'invente jamais de résultats.",
        "Réponds en français.",
    ],
)

agent.print_response(
    "Calcule le prix au m² d'un appartement "
    "qui coûte 2 400 000 MAD pour 120 m². "
    "Utilise ton outil de calcul.",
    stream=False,
)
