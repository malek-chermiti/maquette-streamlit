"""Reports page - Génération automatique des rapports"""

import streamlit as st
from config import PROJECTS, FILTER_OPTIONS, REPORT_SECTIONS
from utils import render_page_header, render_card_with_title, render_card_header, render_card_footer


def show():
    """Render the reports generation page."""
    render_page_header("📄 Rapports", "Génération automatique des rapports PDF et Word")

    c1, c2 = st.columns([1, 2])

    with c1:
        render_card_header("⚙️ Configuration")
        st.selectbox("Projet", PROJECTS)
        st.selectbox("Format export", FILTER_OPTIONS["export_format"])
        st.multiselect("Sections à inclure", REPORT_SECTIONS)
        st.date_input("Période du rapport")
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("📄 Générer le rapport", use_container_width=True)
        st.button("⬇️ Télécharger", use_container_width=True)
        render_card_footer()

    with c2:
        render_card_with_title(
            "👁️ Aperçu",
            "Aperçu du rapport — génération à venir",
            height="380px"
        )
