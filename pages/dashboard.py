"""Dashboard page - Vue globale de la plateforme"""

import streamlit as st
from config import DASHBOARD_KPIS
from utils import render_page_header, render_kpi_row, render_card_with_title


def show():
    """Render the dashboard page."""
    render_page_header("🏠 Tableau de bord", "Vue globale de la plateforme")

    # KPI Cards
    render_kpi_row(DASHBOARD_KPIS)

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts Section
    g1, g2 = st.columns([2, 1])

    with g1:
        render_card_with_title(
            "📈 Tendance d'intégrité structurale",
            "Score de santé agrégé sur l'ensemble des pylônes surveillés"
        )
        # Period Filter Buttons
        b1, b2, b3, b4, _ = st.columns([1, 1, 1, 1, 5])
        with b1:
            st.button("7J")
        with b2:
            st.button("30J")
        with b3:
            st.button("90J")
        with b4:
            st.button("1A")

    with g2:
        pass

    # Recent Verifications
    render_card_with_title(
        "🕐 Vérifications récentes",
        "Dernières évaluations structurales par les agents IA",
        height="120px"
    )
