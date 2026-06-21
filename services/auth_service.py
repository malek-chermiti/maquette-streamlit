import requests
import streamlit as st
from config import API_URL


# =========================
# 1. LOGIN (GET JWT)
# =========================
def login(email: str, password: str):
    """
    Appel API login
    Retourne response backend (JWT inclus si succès)
    """

    url = f"{API_URL}/login"

    try:
        response = requests.post(
            url,
            json={
                "email": email,
                "password": password
            }
        )

        return response

    except Exception as e:
        return None


# =========================
# 2. STOCKER TOKEN
# =========================
def save_token(token: str):
    """
    Stocker JWT dans session Streamlit
    """

    st.session_state.token = token
    st.session_state.authenticated = True


# =========================
# 3. RECUPERER TOKEN
# =========================
def get_token():

    return st.session_state.get("token", None)


# =========================
# 4. HEADERS AUTH (IMPORTANT)
# =========================
def get_auth_headers():

    token = get_token()

    if not token:
        return {}

    return {
        "Authorization": f"Bearer {token}"
    }


# =========================
# 5. APPEL API PROTEGEE
# =========================
def api_request(method: str, endpoint: str, data=None):
    """
    Envoie requête avec JWT au backend
    """

    url = f"{API_URL}{endpoint}"
    headers = get_auth_headers()

    try:

        if method.lower() == "get":

            response = requests.get(url, headers=headers)
        elif method.lower() == "post":

            response = requests.post(
                url,
                json=data,
                headers=headers
            )

        else:
            raise ValueError("Method not supported")

        return response

    except Exception as e:
        return None


# =========================
# 6. LOGOUT
# =========================
def logout():

    st.session_state.clear()
    st.session_state.authenticated = False
    