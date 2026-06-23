"""UI Helper functions for TOWERMIND application.

Les fonctions historiques délèguent aux composants modulaires
pour garantir la rétrocompatibilité avec les pages existantes.
"""

import streamlit as st
from pathlib import Path

from components.cards import (
    render_kpi_card,
    render_kpi_row,
    render_card_with_title,
    render_card_header,
    render_card_footer,
)
from components.sidebar import _render_sidebar_header, _render_sidebar_footer


def load_styles() -> None:
    """Load CSS styles from style.css and assets/css/components.css."""
    root = Path(__file__).parent
    for css_path in [root / "style.css", root / "assets" / "css" / "components.css"]:
        if css_path.exists():
            with open(css_path, "r", encoding="utf-8") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_sidebar_header(brand: dict, user: dict) -> None:
    """Render the sidebar header with branding (rétrocompatibilité)."""
    _render_sidebar_header(brand)


def render_sidebar_footer(user: dict) -> None:
    """Render the sidebar footer with user information (rétrocompatibilité)."""
    _render_sidebar_footer(user)


def render_page_header(title: str, subtitle: str) -> None:
    """Render page title and subtitle."""
    st.markdown(f"<div class='page-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='page-sub'>{subtitle}</div>", unsafe_allow_html=True)


def render_agent_item(label: str) -> None:
    """Render a single agent item in the pipeline."""
    st.markdown(
        f"""
        <div class='card card-compact card-hover'>
            <div class='agent-card-title'>{label}</div>
            <div class='agent-card-status'>Statut — données à venir</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_3d_viewer_placeholder() -> None:
    """Render the 3D viewer placeholder."""
    st.markdown(
        """
        <div class='card card-hover'>
            <div class='section-title'>🧊 Viewer 3D</div>
            <div class='viewer-3d-placeholder'>
                <div class='viewer-3d-icon'>🏗️</div>
                <div class='viewer-3d-text'>
                    Viewer Three.js — intégration J15-J21
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Ré-export des fonctions cartes pour rétrocompatibilité
__all__ = [
    "load_styles",
    "render_sidebar_header",
    "render_sidebar_footer",
    "render_page_header",
    "render_kpi_card",
    "render_kpi_row",
    "render_card_with_title",
    "render_card_header",
    "render_card_footer",
    "render_agent_item",
    "render_3d_viewer_placeholder",
]
