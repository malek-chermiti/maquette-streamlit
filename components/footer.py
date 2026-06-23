"""Pied de page simple."""

import streamlit as st
from config import SIDEBAR_BRAND


def render_footer() -> None:
    """Affiche le footer avec branding."""
    brand = SIDEBAR_BRAND
    st.markdown(
        f"""
        <div class='footer-spacer'></div>
        <div class='app-footer'>
            <div class='footer-brand'>
                <span class='footer-logo'>{brand['icon']} {brand['name']}</span>
                <span class='footer-tagline'>{brand['tagline']}</span>
            </div>
            <div class='footer-copy'>
                Copyright 2024 BIMLO Technologies - Tous droits reserves
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
