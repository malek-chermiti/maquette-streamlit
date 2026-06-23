"""TOWERMIND - BIMLO Main Application."""

import streamlit as st
from config import PAGE_CONFIG
from utils import load_styles
from components.sidebar import render_sidebar
from components.footer import render_footer
from pages import (
    dashboard,
    projects,
    anomalies,
    tower_detail,
    ai_agents,
    twin_3d,
    chatbot,
    reports,
    about,
    faq,
    contact,
    documentation,
    legal,
    privacy,
)


def safe_rerun():
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()


def _handle_logout():
    from services.auth_service import logout

    logout()
    safe_rerun()


PAGE_MODULES = {
    "Tableau de bord": dashboard,
    "Projets": projects,
    "Anomalies": anomalies,
    "Detail Pylone": tower_detail,
    "Agents IA": ai_agents,
    "Jumeau 3D": twin_3d,
    "Chatbot RAG": chatbot,
    "Rapports": reports,
    "A propos": about,
    "FAQ": faq,
    "Contact": contact,
    "Documentation utilisateur": documentation,
    "Mentions legales": legal,
    "Politique de confidentialite": privacy,
}


st.set_page_config(**PAGE_CONFIG)
load_styles()

import auth_page

if not st.session_state.get("authenticated", False):
    auth_page.show_auth()
else:
    page = render_sidebar(on_logout=_handle_logout)

    if page in PAGE_MODULES:
        PAGE_MODULES[page].show()

    render_footer()
