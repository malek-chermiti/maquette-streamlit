"""Projects page - Gestion de tous les projets pylônes"""

import streamlit as st
from config import FILTER_OPTIONS, PROJECTS
from utils import render_page_header, render_card_with_title


def show():
    """Render the projects page."""
    render_page_header("📁 Projets", "Gestion de tous les projets pylônes")

    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        st.text_input("Rechercher", placeholder="Nom, référence, pylône...")
    with c2:
        st.selectbox("Statut", FILTER_OPTIONS["status"])
    with c3:
        st.selectbox("Période", FILTER_OPTIONS["period"])

    st.markdown("<br>", unsafe_allow_html=True)
    render_card_with_title(
        "📋 Liste des projets",
        "Liste des projets — données à venir"
    )
