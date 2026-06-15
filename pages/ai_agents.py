"""AI Agents page - Orchestration LangGraph des agents"""

import streamlit as st
from config import PROJECTS, AI_AGENTS
from utils import render_page_header, render_card_with_title, render_agent_item


def show():
    """Render the AI agents workflow page."""
    render_page_header("🤖 Workflow Multi-Agents", "Orchestration LangGraph des 5 agents de vérification")

    st.selectbox("Sélectionner un projet", PROJECTS)
    st.button("▶ Lancer la vérification", use_container_width=False)

    st.markdown("<br>", unsafe_allow_html=True)
    render_card_with_title(
        "🔄 Pipeline de vérification",
        "Pipeline agents — visualisation à venir"
    )

    # Agent Pipeline Items
    for agent_label in AI_AGENTS:
        render_agent_item(agent_label)
