"""Projects page - Gestion de tous les projets pylônes"""

import streamlit as st
from config import FILTER_OPTIONS
from utils import render_page_header, render_card_with_title
from components.forms import render_search_bar, render_filter_row


def show():
    """Render the projects page."""
    render_page_header("📁 Projets", "Gestion de tous les projets pylônes")

    c1, c2 = st.columns([2, 2])
    with c1:
        render_search_bar("Rechercher", placeholder="Nom, référence, pylône...", key="project_search")
    with c2:
        render_filter_row([
            {"label": "Statut", "key": "status", "options": FILTER_OPTIONS["status"]},
            {"label": "Période", "key": "period", "options": FILTER_OPTIONS["period"]},
        ])

    st.markdown("<br>", unsafe_allow_html=True)
    render_card_with_title(
        "📋 Liste des projets",
        "Liste des projets — données à venir",
    )
