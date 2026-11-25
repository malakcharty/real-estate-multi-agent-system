
from agno.team import Team, TeamMode

from agents.property_search_agent import (
    property_search_agent,
    model,
)
from agents.pricing_agent import pricing_agent
from agents.recommendation_agent import recommendation_agent


real_estate_team = Team(
    name="Real Estate Analysis Team",
    model=model,
    mode=TeamMode.coordinate,

    members=[
        property_search_agent,
        pricing_agent,
        recommendation_agent,
    ],

    instructions=[
        "Tu es le coordinateur d'une équipe d'analyse immobilière.",
        "Réponds toujours en français.",

        # Recherche
        "Délègue la recherche immobilière au Property Search Agent.",
        "Attends les résultats de la recherche avant de poursuivre.",
        "Si aucun bien n'est trouvé, indique-le clairement.",

        # Analyse des prix
        "Si des biens sont trouvés, délègue leur analyse "
        "au Pricing Analysis Agent.",
        "Transmets les identifiants exacts des biens trouvés.",
        "Utilise les calculs retournés par le Pricing Agent.",

        # Recommandation
        "Délègue le classement multicritère "
        "au Recommendation Agent.",
        "Transmets les critères du client : ville, transaction, "
        "budget, chambres, surface et préférences.",
        "Le Recommendation Agent doit utiliser son outil "
        "de scoring pour classer les biens.",

        
        # Fiabilité
        "N'invente jamais de biens, d'identifiants ou de prix.",
        "Utilise uniquement les résultats retournés par les outils.",
        "Ne modifie jamais les scores calculés par les outils.",

        "Respecte exactement les pourcentages calculés "
        "par le Pricing Analysis Agent.",
        "Distingue toujours le pourcentage d'augmentation "
        "du pourcentage de diminution : ils n'utilisent pas "
        "la même valeur de référence.",
        "Ne recalcule pas les écarts si l'outil les fournit.",

        "Ne justifie pas les prix par des données de marché "
        "qui ne sont pas disponibles.",
        "Ne présente pas le score comme une mesure de "
        "la qualité réelle du bien.",
        "Les annonces sont fictives.",
        "Les scores sont relatifs aux biens comparés.",
        "Justifie la recommandation uniquement par les critères "
        "réellement évalués : prix, surface, budget et quartier.",

        # Rapport final
        "Présente les biens trouvés avec leurs caractéristiques.",
        "Présente la comparaison des prix au m².",
        "Présente le classement final avec les scores.",
        "Explique la recommandation à partir des données vérifiées.",
    ],

    show_members_responses=True,
    markdown=True,
)


if __name__ == "__main__":
    real_estate_team.print_response(
        input=(
            "Je cherche un appartement à vendre à Casablanca "
            "avec au moins 3 chambres, une surface minimum "
            "de 100 m² et un budget maximum de 2 500 000 MAD. "
            "Je n'ai pas de préférence de quartier. "
            "Recherche les biens, compare les prix au m² "
            "et établis un classement multicritère. "
            "Présente une recommandation finale justifiée."
        ),
        stream=False,
    )
