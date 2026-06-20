"""TOWERMIND — BIMLO Main Application.

A comprehensive Streamlit application for structural tower monitoring,
AI-powered verification, and 3D visualization.
"""

import streamlit as st
from config import PAGE_CONFIG, PAGES, SIDEBAR_BRAND, SIDEBAR_USER
from utils import load_styles, render_sidebar_header, render_sidebar_footer
from pages import dashboard, projects, anomalies, tower_detail, ai_agents, twin_3d, chatbot, reports


def safe_rerun():
    """Rerun the Streamlit app safely across different versions."""
    try:
        st.rerun()
    except AttributeError:
        st.experimental_rerun()


# ═══════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════

st.set_page_config(**PAGE_CONFIG)
load_styles()

# ═══════════════════════════════════════════════════════════════════
# AUTHENTICATION SHIELD
# ═══════════════════════════════════════════════════════════════════

import login

if not st.session_state.get("authenticated", False):
    login.show_login()
else:
    # ═══════════════════════════════════════════════════════════════════
    # SIDEBAR NAVIGATION
    # ═══════════════════════════════════════════════════════════════════

    with st.sidebar:
        render_sidebar_header(SIDEBAR_BRAND, SIDEBAR_USER)
        page = st.radio("Navigation", PAGES, label_visibility="collapsed")
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        if st.button("🚪 Se déconnecter", use_container_width=True):
            from services.auth_service import logout
            logout()
            safe_rerun()
            
        render_sidebar_footer(SIDEBAR_USER)

    # ═══════════════════════════════════════════════════════════════════
    # PAGE ROUTING
    # ═══════════════════════════════════════════════════════════════════

    page_modules = {
        PAGES[0]: dashboard,      # 🏠 Tableau de bord
        PAGES[1]: projects,       # 📁 Projets
        PAGES[2]: anomalies,      # ⚠️ Anomalies
        PAGES[3]: tower_detail,   # 🗼 Détail Pylône
        PAGES[4]: ai_agents,      # 🤖 Agents IA
        PAGES[5]: twin_3d,        # 🧊 Jumeau 3D
        PAGES[6]: chatbot,        # 💬 Chatbot RAG
        PAGES[7]: reports,        # 📄 Rapports
    }

    # Render the selected page
    page_modules[page].show()

