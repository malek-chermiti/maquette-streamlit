"""Tower Detail page - Fiche complète et résultats de vérification"""

import streamlit as st
from config import PROJECTS
from components.cards import render_info_section
from components.notifications import render_alert


def show():
    """Render the tower detail page."""
    st.markdown("<div class='page-title'>🗼 Détail Pylône</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Fiche complète et résultats de vérification</div>", unsafe_allow_html=True)

    st.selectbox("Sélectionner un projet", PROJECTS)

    render_info_section("📐 Informations générales", [
        ("Référence", "—"),
        ("Région", "—"),
        ("Hauteur", "—"),
        ("Type", "—"),
        ("Année installation", "—"),
        ("Statut", "—"),
    ])

    st.markdown("<div class='card card-hover'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>⚠️ Anomalies détectées</div>", unsafe_allow_html=True)
    render_alert("Aucune anomalie détectée — données à venir", variant="warning")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='card card-hover'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>📋 Diagnostics existants</div>", unsafe_allow_html=True)
    render_alert("Aucun diagnostic disponible — données à venir", variant="info")
    st.markdown("</div>", unsafe_allow_html=True)
