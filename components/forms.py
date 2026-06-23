"""Formulaires, recherche et filtres réutilisables."""

import streamlit as st


def render_search_bar(
    placeholder: str = "Rechercher…",
    label: str = "Rechercher",
    key: str = "search_input",
) -> str:
    """Barre de recherche standardisée."""
    st.markdown("<div class='search-wrapper'>", unsafe_allow_html=True)
    value = st.text_input(label, placeholder=placeholder, key=key, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)
    return value


def render_filter_row(filters: list[dict]) -> dict:
    """
    Rend une ligne de filtres dynamiques.
    Chaque filtre : {"label", "options", "key", "default" (optionnel)}.
    Retourne un dict {key: valeur sélectionnée}.
    """
    if not filters:
        return {}

    cols = st.columns(len(filters))
    results = {}
    for col, f in zip(cols, filters):
        with col:
            results[f["key"]] = st.selectbox(
                f["label"],
                f["options"],
                index=f.get("default", 0),
                key=f"filter_{f['key']}",
            )
    return results
