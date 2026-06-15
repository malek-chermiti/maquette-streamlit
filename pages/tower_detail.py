"""Tower Detail page - Fiche complète et résultats de vérification"""

import streamlit as st
from config import PROJECTS
from utils import render_page_header, render_card_with_title


def show():
    """Render the tower detail page."""
    render_page_header("🗼 Détail Pylône", "Fiche complète et résultats de vérification")

    st.selectbox("Sélectionner un projet", PROJECTS)

    c1, c2 = st.columns([1, 2])
    with c1:
        render_card_with_title(
            "📐 Informations générales",
            "Infos pylône — données à venir"
        )
    with c2:
        render_card_with_title(
            "🤖 Résultats des 5 agents",
            "Résultats agents — données à venir"
        )
