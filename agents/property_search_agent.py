import os

from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai.like import OpenAILike

from tools.property_tools import search_properties

load_dotenv()

model = OpenAILike(
    id=os.environ["IFM_MODEL"],
    api_key=os.environ["IFM_API_KEY"],
    base_url=os.environ["IFM_BASE_URL"],
)

property_search_agent = Agent(
    name="Property Search Agent",
    id="property-search-agent",
    role="Real Estate Property Research Specialist",
    model=model,
    tools=[search_properties],
    instructions=[
        "Tu es un agent spécialisé dans la recherche immobilière.",
        "Utilise systématiquement search_properties pour rechercher des biens.",
        "Présente uniquement les biens retournés par l'outil.",
        "Les données sont fictives et destinées à la démonstration.",
        "Si aucun bien ne correspond, indique-le clairement.",
        "Ne fabrique jamais de biens immobiliers.",
        "Réponds en français avec les identifiants des biens.",
    ],
    markdown=True,
)


if __name__ == "__main__":
    property_search_agent.print_response(
        "Recherche des appartements à vendre à Casablanca "
        "avec au moins 3 chambres et un budget maximum "
        "de 2 500 000 MAD.",
        stream=False,
    )
