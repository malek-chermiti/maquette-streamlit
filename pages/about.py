"""Page À propos — présentation de TOWERMIND / BIMLO."""

import streamlit as st
from pages.static_layout import render_static_layout
from components.cards import render_info_section
from components.notifications import render_alert


def show():
    render_static_layout(
        "À propos de TOWERMIND",
        "Plateforme de surveillance structurelle et vérification IA pour pylônes télécoms",
    )

    c1, c2 = st.columns([2, 1])

    with c1:
        st.markdown(
            """
            <div class='card static-content'>
                <h3>Notre mission</h3>
                <p>
                    TOWERMIND est une solution développée par <strong>BIMLO Technologies</strong>
                    en partenariat avec <strong>VERTWIN</strong>, dédiée à la surveillance
                    intelligente des pylônes de télécommunication. La plateforme combine
                    jumeau numérique 3D, agents IA et analyse documentaire pour garantir
                    l'intégrité structurelle des infrastructures critiques.
                </p>
                <h3>Modules fonctionnels</h3>
                <p>
                    Le pipeline couvre cinq agents de vérification (M1 à M5) : conversion
                    Plans 2D → Note de Calcul, génération de plans de fabrication, intégration
                    SolidWorks, export IFC et validation croisée des documents techniques.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        render_info_section("Informations clés", [
            ("Version", "Maquette v1.0"),
            ("Éditeur", "BIMLO Technologies"),
            ("Partenaire", "VERTWIN"),
            ("Stack", "Streamlit · FastAPI · LangGraph"),
            ("Développeur", "Malek Chermiti · M4"),
        ])

    render_alert(
        "Cette application est une maquette fonctionnelle. Les données affichées sont des placeholders en attente d'intégration backend.",
        variant="info",
        title="Maquette de démonstration",
    )
