"""AI Agents page - Orchestration LangGraph des agents"""

import streamlit as st
from config import PROJECTS, AI_AGENTS
from utils import render_page_header, render_card_with_title, render_agent_item


def show():
    """Render the AI agents workflow page."""
    st.markdown("<div class='page-title'>🤖 Workflow Multi-Agents</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Orchestration LangGraph des 5 agents de vérification</div>", unsafe_allow_html=True)

    st.selectbox("Sélectionner un projet", PROJECTS)
    st.button("▶ Lancer la vérification", use_container_width=False)

    st.markdown("<br>", unsafe_allow_html=True)

    # Pipeline Visualization
    st.markdown("""
    <div class='card'>
        <div class='section-title'>🔄 Pipeline de vérification</div>
        <div style='font-size:0.85rem; color:#94a3b8; padding:2rem; background:#f8fafc; border-radius:8px; border:2px dashed #e2e8f0; text-align:center;'>
            Pipeline agents — visualisation à venir
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Agent Results
    st.markdown("""
    <div class='card'>
        <div class='section-title'>📊 Résultats des agents</div>
    """, unsafe_allow_html=True)

    # Agent Pipeline Items
    for agent_label in AI_AGENTS:
        st.markdown(f"""
        <div style='padding:1.5rem; border-bottom:1px solid #e2e8f0;'>
            <div style='font-weight:600; color:#0F172A; font-size:0.95rem; margin-bottom:0.5rem;'>{agent_label}</div>
            <div style='display:flex; align-items:center; gap:0.75rem;'>
                <div style='flex-grow:1; height:8px; background:#e2e8f0; border-radius:4px;'>
                    <div style='height:100%; width:0%; background:#3b82f6; border-radius:4px;'></div>
                </div>
                <div style='color:#94a3b8; font-size:0.8rem;'>Statut — données à venir</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
