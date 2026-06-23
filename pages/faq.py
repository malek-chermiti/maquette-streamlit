"""Page FAQ - questions frequentes."""

import streamlit as st
from pages.static_layout import render_static_layout
from components.cards import render_accordion
from components.forms import render_search_bar


FAQ_ITEMS = [
    (
        "Qu'est-ce que TOWERMIND ?",
        "TOWERMIND est une plateforme de monitoring structurel pour pylones telecoms. "
        "Elle centralise la detection d'anomalies, la verification documentaire par agents IA "
        "et la visualisation 3D via jumeau numerique.",
    ),
    (
        "Comment fonctionnent les agents IA ?",
        "Cinq agents specialises (M1-M5) orchestrent un pipeline LangGraph : chaque agent "
        "traite une etape de conversion ou de validation (plans 2D, notes de calcul, "
        "SolidWorks, IFC). Les resultats sont consultables dans la page Agents IA.",
    ),
    (
        "D'ou proviennent les donnees d'anomalies ?",
        "Les anomalies sont detectees automatiquement par les agents IA a partir des modeles "
        "3D et documents techniques. Elles sont classees par criticite (Critique, Majeure, Mineure) "
        "et peuvent etre filtrees par region, etat et periode.",
    ),
    (
        "Comment generer un rapport ?",
        "Rendez-vous dans la page Rapports, selectionnez un projet, le format d'export (PDF ou Word), "
        "les sections souhaitees et la periode. Cliquez sur Generer le rapport puis telechargez le fichier.",
    ),
    (
        "Le viewer 3D est-il operationnel ?",
        "Le viewer Three.js est prevu pour l'integration J15-J21. La page Jumeau 3D affiche "
        "actuellement un placeholder en attendant le branchement aux fichiers IFC/SolidWorks.",
    ),
    (
        "Comment me connecter ?",
        "Creez d'abord un compte depuis l'ecran d'inscription. Apres validation, "
        "vous serez redirige vers la connexion et pourrez utiliser votre email et votre mot de passe.",
    ),
]


def show():
    render_static_layout(
        "Foire aux questions",
        "Reponses aux questions les plus frequentes sur la plateforme",
    )

    query = render_search_bar("Rechercher une question...", key="faq_search")

    items = FAQ_ITEMS
    if query:
        q = query.lower()
        items = [(q_text, a) for q_text, a in FAQ_ITEMS if q in q_text.lower() or q in a.lower()]

    if not items:
        st.info("Aucune question ne correspond a votre recherche.")
    else:
        render_accordion(items)
