"""
TOWERMIND - Pylônes Dashboard (M2 API)
Streamlit + HTML SaaS table + actions
"""

import streamlit as st
import requests

from config import API_URL
from services.auth_service import get_auth_headers


# =========================================================
# FETCH PYLONES
# =========================================================
def fetch_pylones():
    try:
        response = requests.get(
            f"{API_URL}/pylones",
            headers=get_auth_headers()
        )
        return response.json() if response.status_code == 200 else []
    except:
        return []


# =========================================================
# DELETE PYLONE
# =========================================================
def delete_pylone(pylone_id):
    try:
        requests.delete(
            f"{API_URL}/pylones/{pylone_id}",
            headers=get_auth_headers()
        )
    except:
        pass


# =========================================================
# UPDATE PYLONE (simple example)
# =========================================================
def update_pylone(pylone_id, data):
    try:
        requests.put(
            f"{API_URL}/pylones/{pylone_id}",
            json=data,
            headers=get_auth_headers()
        )
    except:
        pass


# =========================================================
# MAIN PAGE
# =========================================================
def show():
    st.markdown(
        "<h1 style='text-align:center;'>🗼 TOWERMIND - Pylônes</h1>",
        unsafe_allow_html=True
    )

    pylones = fetch_pylones()

    # =========================================================
    # KPI SECTION
    # =========================================================
    total = len(pylones)
    actif = len([p for p in pylones if p.get("etat") == "actif"])
    maintenance = len([p for p in pylones if p.get("etat") == "maintenance"])

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("TOTAL PYLONES", total)
    with c2:
        st.metric("ACTIFS", actif)
    with c3:
        st.metric("MAINTENANCE", maintenance)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================================================
    # TABLE HEADER (HTML)
    # =========================================================
    st.markdown(
        """
        <div style="
        background:#0f172a;
        color:white;
        padding:12px;
        border-radius:8px;
        font-weight:bold;
        display:grid;
        grid-template-columns:60px 120px 120px 120px 120px 200px;
        ">

        <div>ID</div>
        <div>NAME</div>
        <div>TYPE</div>
        <div>HEIGHT</div>
        <div>STATE</div>
        <div>ACTIONS</div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================================================
    # TABLE ROWS (HTML + ACTIONS)
    # =========================================================
    for p in pylones:
        st.markdown(
        f"""
        <div style="
        display:grid;
        grid-template-columns:60px 120px 120px 120px 120px 200px;
        padding:10px;
        border-bottom:1px solid #e5e7eb;
        align-items:center;
        ">

            <div>{p.get('id')}</div>
            <div>{p.get('nom')}</div>
            <div>{p.get('type_pylone')}</div>
            <div>{p.get('hauteur_m')} m</div>
            <div>{p.get('etat')}</div>

            <div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
        )

        # =====================================================
        # ACTION BUTTONS (Streamlit inside row)
        # =====================================================
        col1, col2 = st.columns(2)

        with col1:
            if st.button("✏️", key=f"upd_{p['id']}"):
                new_state = "maintenance"
                if p.get("etat") == "maintenance":
                    new_state = "actif"

                update_pylone(
                    p["id"],
                    {"etat": new_state}
                )
                st.success("Updated")
                st.rerun()

        with col2:
            if st.button("🗑", key=f"del_{p['id']}"):
                delete_pylone(p["id"])
                st.warning("Deleted")
                st.rerun()

    # =========================================================
    # DETAILS SECTION (OPTIONAL SELECT VIEW)
    # =========================================================
    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    ids = [p["id"] for p in pylones]
    selected = st.selectbox("Select pylône", ids)
    pylone = next((p for p in pylones if p["id"] == selected), None)

    if pylone:
        st.markdown(
        f"""
        <div class='card'>
            <h3>📐 Pylône Details</h3>

            <p><b>Name:</b> {pylone.get('nom')}</p>
            <p><b>Type:</b> {pylone.get('type_pylone')}</p>
            <p><b>Height:</b> {pylone.get('hauteur_m')} m</p>
            <p><b>State:</b> {pylone.get('etat')}</p>
        </div>
        """,
        unsafe_allow_html=True
        )