"""Page Contact - coordonnees et formulaire de contact."""

import streamlit as st
from pages.static_layout import render_static_layout
from components.notifications import render_alert, render_toast


def show():
    render_static_layout(
        "Contact",
        "Une question ? L'equipe BIMLO Technologies est a votre ecoute",
    )

    c1, c2 = st.columns([1, 1])

    with c1:
        st.subheader("Coordonnees")
        st.markdown(
            """
            **Societe**  
            BIMLO Technologies

            **Email**  
            contact@bimlo.tech

            **Telephone**  
            +216 XX XXX XXX

            **Adresse**  
            Tunis, Tunisie
            """
        )

        render_alert(
            "Les demandes sont traitees sous 48 h ouvrees. "
            "Pour les anomalies critiques, utilisez le canal d'urgence dedie.",
            variant="info",
        )

    with c2:
        st.subheader("Envoyer un message")
        with st.form("contact_form"):
            name = st.text_input("Nom complet", placeholder="Votre nom")
            email = st.text_input("Email", placeholder="votre@email.com")
            subject = st.selectbox(
                "Sujet",
                ["Question generale", "Support technique", "Demande de demo", "Partenariat"],
            )
            message = st.text_area("Message", placeholder="Decrivez votre demande...", height=120)
            submitted = st.form_submit_button("Envoyer le message", use_container_width=True)

        if submitted:
            st.session_state.contact_sent = bool(name and email and message)

        if st.session_state.get("contact_sent"):
            render_toast("Votre message a bien ete enregistre (maquette - envoi simule).", "success")
