"""3D Twin page - Visualisation 3D du pylône"""

import streamlit as st
from config import PROJECTS
from utils import render_page_header, render_card_with_title, render_3d_viewer_placeholder


def show():
    """Render the 3D twin visualization page."""
    render_page_header("🧊 Jumeau 3D", "Visualisation 3D du pylône — IFC / SolidWorks")

    st.selectbox("Sélectionner un projet", PROJECTS)

    c1, c2 = st.columns([3, 1])

    with c1:
        render_3d_viewer_placeholder()

        # Viewer Controls
        b1, b2, b3, b4 = st.columns(4)
        with b1:
            st.button("🔄 Rotation", use_container_width=True)
        with b2:
            st.button("🔍 Zoom +", use_container_width=True)
        with b3:
            st.button("🔎 Zoom −", use_container_width=True)
        with b4:
            st.button("⟲ Reset", use_container_width=True)

    with c2:
        render_card_with_title(
            "📐 Propriétés",
            "Propriétés IFC — données à venir",
            height="120px"
        )
        render_card_with_title(
            "🎨 Couches",
            "Couches 3D — données à venir",
            height="120px"
        )
