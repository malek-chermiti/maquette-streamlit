"""Layout commun pour les pages statiques."""

import streamlit as st


def render_static_layout(title: str, subtitle: str):
    """En-tête standardisé pour les pages statiques."""
    st.markdown(
        f"""
        <div class='static-page-hero'>
            <h2>{title}</h2>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
