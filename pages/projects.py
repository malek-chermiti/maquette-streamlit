"""
TOWERMIND - Projects Dashboard (M2 API)
Streamlit frontend + CRUD + HTML table + actions
"""

import streamlit as st
import requests

from config import API_URL
from services.auth_service import get_auth_headers



# =========================================================
# FETCH PROJECTS (M2 API)
# =========================================================
def fetch_projects(recherche="", client="", statut=""):

    params = []

    if recherche:
        params.append(f"recherche={recherche}")
    if client:
        params.append(f"client={client}")
    if statut:
        params.append(f"statut={statut}")

    query = "&".join(params)
    url = f"{API_URL}/projets"

    if query:
        url += "?" + query

    try:
        response = requests.get(
            url,
            headers=get_auth_headers()
        )

        return response.json() if response.status_code == 200 else []

    except:
        return []



# =========================================================
# UPDATE PROJECT
# =========================================================
def update_project(project_id, data):

    try:
        requests.put(
            f"{API_URL}/projets/{project_id}",
            json=data,
            headers=get_auth_headers()
        )
    except:
        pass



# =========================================================
# DELETE PROJECT
# =========================================================
def delete_project(project_id):

    try:
        requests.delete(
            f"{API_URL}/projets/{project_id}",
            headers=get_auth_headers()
        )
    except:
        pass



# =========================================================
# MAIN PAGE
# =========================================================
def show():


    st.markdown(
        "<h1 style='text-align:center;'>TOWERMIND - Projects</h1>",
        unsafe_allow_html=True
    )


    # =========================
    # SEARCH BAR
    # =========================

    col1, col2, col3 = st.columns(3)

    with col1:
        search = st.text_input("Search project")

    with col2:
        client = st.text_input("Client")

    with col3:
        statut = st.selectbox(
            "Status",
            ["", "actif", "en_cours", "termine"]
        )



    projects = fetch_projects(
        recherche=search,
        client=client,
        statut=statut
    )



    # =========================
    # KPI SECTION
    # =========================

    total = len(projects)

    active = len([p for p in projects if p.get("statut") == "actif"])
    ongoing = len([p for p in projects if p.get("statut") == "en_cours"])
    done = len([p for p in projects if p.get("statut") == "termine"])



    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("TOTAL PROJECTS", total)

    with c2:
        st.metric("ACTIVE", active)

    with c3:
        st.metric("DONE", done)



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
        grid-template-columns:60px 120px 1fr 150px 120px 200px;
        ">

        <div>ID</div>
        <div>CODE</div>
        <div>NAME</div>
        <div>CLIENT</div>
        <div>STATUS</div>
        <div>ACTIONS</div>

        </div>
        """,
        unsafe_allow_html=True
    )



    # =========================================================
    # TABLE ROWS WITH ACTIONS
    # =========================================================

    for p in projects:

        col1, col2, col3, col4, col5, col6 = st.columns([1,1,3,2,2,3])

        with col1:
            st.write(p.get("id"))

        with col2:
            st.write(p.get("code_projet"))

        with col3:
            st.write(p.get("nom"))

        with col4:
            st.write(p.get("client"))

        with col5:
            st.write(p.get("statut"))



        with col6:

            b1, b2 = st.columns(2)


            # =========================
            # UPDATE BUTTON
            # =========================
            with b1:

                if st.button("✏️", key=f"upd_{p['id']}"):

                    new_status = "en_cours"

                    if p.get("statut") == "en_cours":
                        new_status = "termine"
                    elif p.get("statut") == "actif":
                        new_status = "en_cours"


                    update_project(
                        p["id"],
                        {"statut": new_status}
                    )

                    st.success("Updated")
                    st.rerun()



            # =========================
            # DELETE BUTTON
            # =========================
            with b2:

                if st.button("🗑", key=f"del_{p['id']}"):

                    delete_project(p["id"])

                    st.warning("Deleted")
                    st.rerun()



    # =========================================================
    # FOOTER ACTION INFO
    # =========================================================

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    st.info("Click ✏️ to change status | Click 🗑 to delete project")