"""
TOWERMIND - Anomalies Dashboard (M2 API)
Streamlit + React Component
"""

import streamlit as st
import requests
import streamlit.components.v1 as components

from config import API_URL
from services.auth_service import get_auth_headers


# =========================
# FETCH ANOMALIES
# =========================
def fetch_anomalies():
    try:
        response = requests.get(
            f"{API_URL}/anomalies",
            headers=get_auth_headers()
        )
        if response.status_code == 200:
            return response.json()
        return []
    except Exception:
        return []


# =========================
# UPDATE
# =========================
def update_anomaly(anomaly_id, data):
    try:
        requests.put(
            f"{API_URL}/anomalies/{anomaly_id}",
            json=data,
            headers=get_auth_headers()
        )
    except:
        pass


# =========================
# DELETE
# =========================
def delete_anomaly(anomaly_id):
    try:
        requests.delete(
            f"{API_URL}/anomalies/{anomaly_id}",
            headers=get_auth_headers()
        )
    except:
        pass


# =========================
# PAGE
# =========================
def show():
    st.markdown(
        """
        <h1 style="text-align:center">
        TOWERMIND
        </h1>
        """,
        unsafe_allow_html=True
    )

    anomalies = fetch_anomalies()

    # Envoyer les données au composant React
    components.html(
        f"""
        <script>
        window.anomalies = {anomalies}
        </script>

        <iframe
        src="http://localhost:5173"
        style="
        width:100%;
        height:900px;
        border:none;
        "
        >
        </iframe>
        """,
        height=900
    )