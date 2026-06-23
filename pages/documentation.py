"""Page Documentation utilisateur."""

import streamlit as st
from pages.static_layout import render_static_layout
from components.cards import render_card_with_title


DOC_SECTIONS = {
    "Demarrage": [
        ("Inscription", "Au premier lancement, creez votre compte avec votre nom, votre email et un mot de passe."),
        ("Connexion", "Apres l'inscription, connectez-vous avec l'email et le mot de passe que vous venez de creer. Le tableau de bord s'affiche apres authentification."),
        ("Navigation", "Utilisez la sidebar pour acceder aux modules : Tableau de bord, Projets, Anomalies, Detail Pylone, Agents IA, Jumeau 3D, Chatbot RAG et Rapports."),
    ],
    "Modules principaux": [
        ("Tableau de bord", "Vue globale avec KPIs, tendance d'integrite structurale et verifications recentes."),
        ("Projets", "Liste et recherche de projets pylones avec filtres par statut et periode."),
        ("Anomalies", "Dashboard des defauts structurels classes par severite avec tableau filtrable."),
        ("Agents IA", "Lancement du pipeline multi-agents LangGraph et suivi des resultats."),
    ],
    "Fonctionnalites avancees": [
        ("Jumeau 3D", "Visualisation IFC/SolidWorks avec controles rotation, zoom et couches."),
        ("Chatbot RAG", "Posez des questions en langage naturel sur les notes de calcul et anomalies."),
        ("Rapports", "Generation automatique de rapports PDF/Word avec sections configurables."),
    ],
}


def show():
    render_static_layout(
        "Documentation utilisateur",
        "Guide d'utilisation de la plateforme TOWERMIND",
    )

    section_names = list(DOC_SECTIONS.keys())
    selected = st.radio(
        "Sections",
        section_names,
        horizontal=True,
        label_visibility="collapsed",
        key="doc_section_nav",
    )

    st.write("")

    for title, paragraphs in DOC_SECTIONS[selected]:
        with st.expander(title, expanded=True):
            st.write(paragraphs)

    st.write("")
    render_card_with_title(
        "Ressources complementaires",
        "API backend - Swagger docs - Guide d'integration IFC - a venir",
        height="120px",
    )
