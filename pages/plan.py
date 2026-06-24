import streamlit as st
import requests

from config import API_URL
from services.auth_service import get_auth_headers


# =========================================================
# FETCH PLANS WITH API FILTERS
# =========================================================
def fetch_plans(projet_id=None, type_plan=None):

    params = {}

    if projet_id:
        params["projet_id"] = projet_id

    if type_plan:
        params["type_plan"] = type_plan

    try:
        res = requests.get(
            f"{API_URL}/plans",
            headers=get_auth_headers(),
            params=params
        )

        return res.json() if res.status_code == 200 else []

    except:
        return []


# =========================================================
# DELETE
# =========================================================
def delete_plan(plan_id):

    requests.delete(
        f"{API_URL}/plans/{plan_id}",
        headers=get_auth_headers()
    )


# =========================================================
# UI
# =========================================================
def show():

    st.title("📄 PLANS DASHBOARD")

    # =========================
    # FILTERS (API BASED)
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        projet_id = st.number_input(
            "Projet ID",
            min_value=0,
            value=0
        )

    with col2:
        type_plan = st.selectbox(
            "Type plan",
            ["", "structure", "fabrication", "foundation"]
        )

    # convert empty values
    if projet_id == 0:
        projet_id = None

    if type_plan == "":
        type_plan = None


    # =========================
    # LOAD DATA FROM API
    # =========================
    plans = fetch_plans(projet_id, type_plan)


    st.write(f"Total: {len(plans)} plans")


    # =========================
    # TABLE HEADER
    # =========================
    st.markdown("""
    <div style="
        display:grid;
        grid-template-columns:60px 200px 150px 100px 120px 120px;
        background:#0f172a;
        color:white;
        padding:10px;
        border-radius:8px;
        font-weight:bold;
    ">
        <div>ID</div>
        <div>FILE</div>
        <div>TYPE</div>
        <div>PYLÔNE</div>
        <div>PROJECT</div>
        <div>ACTIONS</div>
    </div>
    """, unsafe_allow_html=True)


    # =========================
    # ROWS
    # =========================
    for p in plans:

        st.markdown(f"""
        <div style="
            display:grid;
            grid-template-columns:60px 200px 150px 100px 120px 120px;
            padding:10px;
            border-bottom:1px solid #eee;
        ">
            <div>{p['id']}</div>
            <div>{p['nom_fichier']}</div>
            <div>{p['type_plan']}</div>
            <div>{p['pylone_id']}</div>
            <div>{p['projet_id']}</div>
            <div></div>
        </div>
        """, unsafe_allow_html=True)


        c1, c2 = st.columns(2)

        with c1:
            if st.button("👁", key=f"v_{p['id']}"):
                st.session_state["plan"] = p

        with c2:
            if st.button("🗑", key=f"d_{p['id']}"):
                delete_plan(p["id"])
                st.rerun()


    # =========================
    # DETAILS
    # =========================
    if "plan" in st.session_state:

        p = st.session_state["plan"]

        st.markdown("## 📄 Details")

        st.json(p.get("contenu_extrait", {}))