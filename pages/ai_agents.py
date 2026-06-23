"""AI Agents page - Orchestration LangGraph des agents"""

import streamlit as st
from config import PROJECTS, AI_AGENTS
from components.cards import render_card_with_title, render_card_header, render_card_footer, render_progress_bar


def show():
    """Render the AI agents workflow page."""
    st.markdown("<div class='page-title'>🤖 Workflow Multi-Agents</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Orchestration LangGraph des 5 agents de vérification</div>", unsafe_allow_html=True)

    st.selectbox("Sélectionner un projet", PROJECTS)
    st.button("▶ Lancer la vérification", use_container_width=False)

    st.markdown("<br>", unsafe_allow_html=True)

    render_card_with_title(
        "🔄 Pipeline de vérification",
        "Pipeline agents — visualisation à venir",
    )

    st.markdown("<br>", unsafe_allow_html=True)

    render_card_header("📊 Résultats des agents")
    for agent_label in AI_AGENTS:
        render_progress_bar(agent_label, percent=0, status="Statut — données à venir")
    render_card_footer()
