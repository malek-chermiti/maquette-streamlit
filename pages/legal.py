"""Page Mentions legales."""

import streamlit as st
from pages.static_layout import render_static_layout


def show():
    render_static_layout(
        "Mentions legales",
        "Informations legales relatives a l'utilisation de TOWERMIND",
    )

    st.subheader("Editeur du site")
    st.markdown(
        """
        **BIMLO Technologies**  
        Societe de developpement logiciel specialisee en BIM et intelligence artificielle.  
        Siege social : Tunis, Tunisie  
        Email : legal@bimlo.tech
        """
    )

    st.subheader("Hebergement")
    st.write(
        "L'application est hebergee sur l'infrastructure definie par le client ou "
        "l'environnement de demonstration BIMLO. Les conditions d'hebergement "
        "definitives seront precisees lors du deploiement en production."
    )

    st.subheader("Propriete intellectuelle")
    st.write(
        "L'ensemble des elements composant la plateforme TOWERMIND (interface, "
        "code source, logos, documentation) est protege par le droit de la propriete "
        "intellectuelle. Toute reproduction non autorisee est interdite."
    )

    st.subheader("Limitation de responsabilite")
    st.write(
        "Les informations presentees dans cette maquette sont fournies a titre "
        "indicatif. BIMLO Technologies ne saurait etre tenue responsable des "
        "decisions prises sur la base de donnees de demonstration."
    )

    st.subheader("Droit applicable")
    st.write(
        "Les presentes mentions legales sont regies par le droit tunisien. "
        "Tout litige releve de la competence des tribunaux de Tunis."
    )
