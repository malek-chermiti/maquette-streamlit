"""UI Helper functions for TOWERMIND application."""

import streamlit as st
from pathlib import Path


def load_styles() -> None:
    """Load CSS styles from style.css file."""
    css_file = Path(__file__).parent / "style.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)


def render_sidebar_header(brand: dict, user: dict) -> None:
    """Render the sidebar header with branding and user info."""
    st.markdown(f"""
        <div class='sidebar-header'>
            <div class='sidebar-title'>{brand['icon']} {brand['name']}</div>
            <div class='sidebar-subtitle'>{brand['tagline']}</div>
        </div>
        <hr class='sidebar-divider'>
    """, unsafe_allow_html=True)


def render_sidebar_footer(user: dict) -> None:
    """Render the sidebar footer with user information."""
    st.markdown(f"""
        <hr class='sidebar-divider'>
        <div class='user-info'>
            <div class='user-info-label'>Connecté en tant que</div>
            <div class='user-info-name'>{user['name']}</div>
            <div class='user-info-role'>{user['role']}</div>
        </div>
    """, unsafe_allow_html=True)


def render_page_header(title: str, subtitle: str) -> None:
    """Render page title and subtitle."""
    st.markdown(f"<div class='page-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='page-sub'>{subtitle}</div>", unsafe_allow_html=True)


def render_kpi_card(label: str) -> None:
    """Render a single KPI card placeholder."""
    st.markdown(f"""
        <div class='card card-center'>
            <div class='kpi-value'>—</div>
            <div class='kpi-label'>{label}</div>
            <div class='kpi-note'>—</div>
        </div>
    """, unsafe_allow_html=True)


def render_kpi_row(labels: list) -> None:
    """Render a row of KPI cards."""
    cols = st.columns(len(labels))
    for col, label in zip(cols, labels):
        with col:
            render_kpi_card(label)


def render_card_with_title(title: str, content: str = "", height: str = "180px") -> None:
    """Render a card with title and content placeholder."""
    placeholder_class = {
        "120px": "placeholder-short",
        "180px": "",
        "350px": "placeholder-chat",
        "380px": "placeholder-tall",
    }.get(height, "")

    st.markdown(f"""
        <div class='card'>
            <div class='section-title'>{title}</div>
            <div class='placeholder {placeholder_class}'>{content}</div>
        </div>
    """, unsafe_allow_html=True)


def render_card_header(title: str) -> None:
    """Render a card header with title."""
    st.markdown(f"""
        <div class='card'>
            <div class='section-title'>{title}</div>
    """, unsafe_allow_html=True)


def render_card_footer(content: str = "") -> None:
    """Render a card footer (closing div)."""
    if content:
        st.markdown(f"<div class='placeholder'>{content}</div></div>", unsafe_allow_html=True)
    else:
        st.markdown("</div>", unsafe_allow_html=True)


def render_agent_item(label: str) -> None:
    """Render a single agent item in the pipeline."""
    st.markdown(f"""
        <div class='card card-compact'>
            <div class='agent-card-title'>{label}</div>
            <div class='agent-card-status'>Statut — données à venir</div>
        </div>
    """, unsafe_allow_html=True)


def render_3d_viewer_placeholder() -> None:
    """Render the 3D viewer placeholder."""
    st.markdown("""
        <div class='card'>
            <div class='section-title'>🧊 Viewer 3D</div>
            <div class='viewer-3d-placeholder'>
                <div class='viewer-3d-icon'>🏗️</div>
                <div class='viewer-3d-text'>
                    Viewer Three.js — intégration J15-J21
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
