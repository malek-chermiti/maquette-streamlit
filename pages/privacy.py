"""Page Politique de confidentialite."""

import streamlit as st
from pages.static_layout import render_static_layout
from components.cards import render_accordion


def show():
    render_static_layout(
        "Politique de confidentialite",
        "Comment TOWERMIND collecte, utilise et protege vos donnees",
    )

    st.write(
        "BIMLO Technologies s'engage a proteger la vie privee des utilisateurs de "
        "la plateforme TOWERMIND. Cette politique decrit les pratiques en vigueur "
        "dans le cadre de la maquette et du deploiement futur."
    )

    render_accordion(
        [
            (
                "Donnees collectees",
                "Lors de la connexion, nous collectons votre adresse email et un jeton JWT "
                "d'authentification stocke en session Streamlit. Les donnees de projets, "
                "anomalies et rapports proviennent du backend API et sont liees a votre compte.",
            ),
            (
                "Finalite du traitement",
                "Les donnees sont utilisees exclusivement pour fournir les services de surveillance "
                "structurelle, de verification IA et de generation de rapports. Aucune donnee "
                "n'est vendue a des tiers.",
            ),
            (
                "Duree de conservation",
                "Les jetons de session expirent a la deconnexion. Les donnees metier sont conservees "
                "selon la politique de retention definie par le client lors du deploiement production.",
            ),
            (
                "Securite",
                "Les communications avec l'API backend utilisent HTTPS. Les mots de passe ne sont "
                "jamais stockes cote frontend. L'acces est protege par authentification JWT.",
            ),
            (
                "Vos droits",
                "Conformement a la reglementation applicable, vous disposez d'un droit d'acces, "
                "de rectification et de suppression de vos donnees. Contact : privacy@bimlo.tech.",
            ),
        ]
    )
