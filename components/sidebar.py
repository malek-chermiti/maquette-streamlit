"""Sidebar - navigation simple en une seule liste."""

import streamlit as st
from config import ALL_PAGES, SIDEBAR_BRAND, SIDEBAR_USER


def _render_sidebar_header(brand: dict) -> None:
    st.markdown(
        f"""
        <div class='sidebar-header'>
            <div class='sidebar-title'>{brand['icon']} {brand['name']}</div>
            <div class='sidebar-subtitle'>{brand['tagline']}</div>
        </div>
        <hr class='sidebar-divider'>
        """,
        unsafe_allow_html=True,
    )


def _render_sidebar_footer(user: dict) -> None:
    st.markdown(
        f"""
        <hr class='sidebar-divider'>
        <div class='user-info'>
            <div class='user-info-label'>Connecte en tant que</div>
            <div class='user-info-name'>{user['name']}</div>
            <div class='user-info-role'>{user['role']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(on_logout) -> str:
    """Rend la sidebar et retourne la page selectionnee."""
    with st.sidebar:
        _render_sidebar_header(SIDEBAR_BRAND)
        page = st.radio(
            "Navigation",
            ALL_PAGES,
            label_visibility="collapsed",
        )
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        if st.button("Se deconnecter", use_container_width=True):
            on_logout()
        _render_sidebar_footer(SIDEBAR_USER)
    return page
