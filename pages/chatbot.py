"""Chatbot RAG page - Questions sur les notes de calcul et anomalies"""

import streamlit as st
from utils import render_page_header, render_card_with_title


def show():
    """Render the RAG chatbot page."""
    render_page_header("💬 Chatbot RAG", "Posez vos questions sur les notes de calcul et anomalies")

    render_card_with_title(
        "💬 Conversation",
        "Zone de conversation — chatbot à venir",
        height="350px"
    )

    c1, c2 = st.columns([5, 1])
    with c1:
        st.text_input("Question", placeholder="Posez votre question...", label_visibility="collapsed")
    with c2:
        st.button("Envoyer ➤", use_container_width=True)
