"""Cartes, statistiques et blocs d'affichage réutilisables."""

import streamlit as st


def render_kpi_card(label: str, value: str = "—", note: str = "—") -> None:
    st.markdown(
        f"""
        <div class='card card-center card-hover'>
            <div class='kpi-value'>{value}</div>
            <div class='kpi-label'>{label}</div>
            <div class='kpi-note'>{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_kpi_row(labels: list, values: list | None = None, notes: list | None = None) -> None:
    cols = st.columns(len(labels))
    for i, (col, label) in enumerate(zip(cols, labels)):
        with col:
            val = values[i] if values and i < len(values) else "—"
            note = notes[i] if notes and i < len(notes) else "—"
            render_kpi_card(label, val, note)


def render_card_with_title(title: str, content: str = "", height: str = "180px") -> None:
    placeholder_class = {
        "120px": "placeholder-short",
        "180px": "",
        "350px": "placeholder-chat",
        "380px": "placeholder-tall",
    }.get(height, "")

    st.markdown(
        f"""
        <div class='card card-hover'>
            <div class='section-title'>{title}</div>
            <div class='placeholder {placeholder_class}'>{content}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_card_header(title: str) -> None:
    st.markdown(
        f"""
        <div class='card card-hover'>
            <div class='section-title'>{title}</div>
        """,
        unsafe_allow_html=True,
    )


def render_card_footer(content: str = "") -> None:
    if content:
        st.markdown(f"<div class='placeholder'>{content}</div></div>", unsafe_allow_html=True)
    else:
        st.markdown("</div>", unsafe_allow_html=True)


_SEVERITY_STYLES = {
    "critical": ("severity-card-critical", "text-critical", "text-critical-note"),
    "high": ("severity-card-high", "text-high", "text-high-note"),
    "medium": ("severity-card-medium", "text-medium", "text-medium-note"),
    "resolved": ("severity-card-resolved", "text-resolved", "text-resolved-note"),
}


def render_severity_card(
    level: str,
    label: str,
    value: str = "—",
    note: str = "",
) -> None:
    """Carte de sévérité (factorise le pattern de la page Anomalies)."""
    style = _SEVERITY_STYLES.get(level, _SEVERITY_STYLES["medium"])
    card_cls, text_cls, note_cls = style
    value_cls = "text-high-value" if level == "high" else text_cls

    st.markdown(
        f"""
        <div class='card {card_cls} card-hover'>
            <div class='severity-label {text_cls}'>{label}</div>
            <div class='severity-value {value_cls}'>{value}</div>
            <div class='severity-note {note_cls}'>{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_info_section(title: str, items: list[tuple[str, str]]) -> None:
    """Grille d'informations clé-valeur."""
    rows = "".join(
        f"""
        <div>
            <div class='info-label'>{label}</div>
            <div class='info-value'>{value}</div>
        </div>
        """
        for label, value in items
    )
    st.markdown(
        f"""
        <div class='card card-hover'>
            <div class='section-title'>{title}</div>
            <div class='info-grid'>
                <div class='info-grid-content'>{rows}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_badge(text: str, variant: str = "default") -> str:
    """Retourne le HTML d'un badge (à insérer dans du markdown)."""
    return f"<span class='badge badge-{variant}'>{text}</span>"


def render_progress_bar(label: str, percent: float = 0, status: str = "") -> None:
    width = max(0, min(100, percent))
    st.markdown(
        f"""
        <div class='agent-result'>
            <div class='agent-result-title'>{label}</div>
            <div class='agent-result-row'>
                <div class='progress-track'>
                    <div class='progress-bar-fill' style='width:{width}%;'></div>
                </div>
                <div class='agent-status'>{status or '—'}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_accordion(items: list[tuple[str, str]]) -> None:
    """Accordéon utilisant les widgets Streamlit natifs."""
    for question, answer in items:
        with st.expander(question, expanded=False):
            st.markdown(answer)


def render_loading_state(message: str = "Chargement en cours…") -> None:
    st.markdown(
        f"""
        <div class='loading-state'>
            <div class='loading-spinner'></div>
            <div class='loading-text'>{message}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
