
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai.like import OpenAILike

# Charger les variables du fichier .env
load_dotenv()

# Configurer le modèle K2 Horizon
model = OpenAILike(
    id=os.environ["IFM_MODEL"],
    api_key=os.environ["IFM_API_KEY"],
    base_url=os.environ["IFM_BASE_URL"],
)

# Créer notre premier agent
agent = Agent(
    name="Real Estate Assistant",
    model=model,
    instructions=[
        "Tu es un assistant spécialisé dans l'immobilier.",
        "Réponds de manière claire et professionnelle.",
        "Réponds toujours en français.",
    ],
    markdown=True,
)

# Tester l'agent
agent.print_response(
    "Bonjour ! Présente-toi et explique comment tu peux aider un client immobilier.",
    stream=False,
)
