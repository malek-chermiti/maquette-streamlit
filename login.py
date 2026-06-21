import streamlit as st

from services.auth_service import login, save_token


def show_login():

    st.markdown(
        """
        <div class="login-container">
        """,
        unsafe_allow_html=True
    )
    st.title("TOWERMIND")
    email = st.text_input(
        "Email"
    )
    password = st.text_input(
        "mot de passe",
        type="password"
    )

    if st.button("Connexion"):

        response = login(
            email,
            password
        )


        if response and response.status_code == 200:

            data = response.json()

            save_token(
                data["access_token"]
            )

            st.success(
                "Connexion réussie"
            )

            st.rerun()


        else:

            st.error(
                "Erreur de connexion"
            )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )