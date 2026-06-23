"""Barre de navigation supérieure et fil d'Ariane."""

import streamlit as st


def render_breadcrumbs(items: list[tuple[str, str | None]]) -> None:
    """Affiche un fil d'Ariane. Chaque item est (label, page_key ou None si actif)."""
    crumbs = []
    for i, (label, page_key) in enumerate(items):
        is_last = i == len(items) - 1
        if is_last or page_key is None:
            crumbs.append(f"<span class='breadcrumb-current'>{label}</span>")
        else:
            crumbs.append(
                f"<span class='breadcrumb-link' data-page='{page_key}'>{label}</span>"
            )

    st.markdown(
        f"<nav class='breadcrumbs' aria-label='Fil d\\'Ariane'>"
        f"{'<span class=\"breadcrumb-sep\">›</span>'.join(crumbs)}"
        f"</nav>",
        unsafe_allow_html=True,
    )


def render_topbar(title: str = "", badge: str = "") -> None:
    """Barre supérieure discrète avec titre contextuel optionnel."""
    badge_html = f"<span class='topbar-badge'>{badge}</span>" if badge else ""
    title_html = f"<span class='topbar-title'>{title}</span>" if title else ""
    st.markdown(
        f"<div class='topbar'>{title_html}{badge_html}</div>",
        unsafe_allow_html=True,
    )
