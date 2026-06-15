"""Anomalies page - Détection et classification par les agents IA"""

import streamlit as st
from config import FILTER_OPTIONS
from utils import render_page_header, render_card_with_title


def show():
    """Render the anomalies page."""
    render_page_header("⚠️ Dashboard Anomalies", "Détection et classification par les agents IA")

    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.selectbox("Module", FILTER_OPTIONS["modules"])
    with f2:
        st.selectbox("Criticité", FILTER_OPTIONS["criticality"])
    with f3:
        st.selectbox("Agent", FILTER_OPTIONS["agents"])
    with f4:
        st.button("🔄 Actualiser", use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    render_card_with_title(
        "📋 Liste des anomalies",
        "Tableau des anomalies — données à venir"
    )
