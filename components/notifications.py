"""Alertes et notifications contextuelles."""

import streamlit as st


_VARIANTS = {
    "info": "notice-info",
    "warning": "notice-warning",
    "success": "notice-success",
    "error": "notice-error",
}

_ICONS = {
    "info": "i",
    "warning": "!",
    "success": "OK",
    "error": "X",
}


def render_alert(message: str, variant: str = "info", title: str = "") -> None:
    """Bloc d'alerte stylise coherent avec le design existant."""
    cls = _VARIANTS.get(variant, "notice-info")
    title_html = f"<div class='alert-title'>{title}</div>" if title else ""
    st.markdown(
        f"""
        <div class='notice {cls} alert-block'>
            {title_html}
            <div class='alert-message'>{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_toast(message: str, variant: str = "info") -> None:
    """Notification discrete en haut de contenu (HTML statique)."""
    icon = _ICONS.get(variant, "i")
    st.markdown(
        f"""
        <div class='toast toast-{variant}' role='status'>
            <span class='toast-icon'>{icon}</span>
            <span class='toast-message'>{message}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
