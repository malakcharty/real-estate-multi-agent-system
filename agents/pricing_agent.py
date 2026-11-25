from agno.agent import Agent

from agents.property_search_agent import model
from tools.pricing_tools import compare_property_prices


pricing_agent = Agent(
    name="Pricing Analysis Agent",
    id="pricing-analysis-agent",
    role="Real Estate Pricing Analyst",
    model=model,
    tools=[compare_property_prices],
    instructions=[
        "Tu es spécialisé dans l'analyse des prix immobiliers.",
        "Utilise toujours l'outil pour effectuer les calculs.",
        "Compare les prix au m² des biens sélectionnés.",
        "Explique clairement les différences observées.",
        "Ne présente pas ces données fictives comme des prix réels du marché.",
        "Un prix au m² plus élevé ne signifie pas forcément qu'un bien est surévalué.",
        "Réponds en français.",
        "Utilise exclusivement les calculs retournés par l'outil.",
        "Distingue le pourcentage plus cher du pourcentage moins cher.",
        "Ne justifie pas les différences de prix par des données de marché non fournies.",
    ],
    markdown=True,
)


if __name__ == "__main__":
    pricing_agent.print_response(
        "Compare les appartements P001 et P002. "
        "Calcule leurs prix au m² et l'écart en pourcentage. "
        "Indique lequel est le moins cher au m².",
        stream=False,
    )
