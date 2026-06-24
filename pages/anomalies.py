"""
TOWERMIND - Anomalies Dashboard (M2 API)
Streamlit + HTML table + inline actions (Edit/Delete)
"""

import streamlit as st
import requests

from config import API_URL
from services.auth_service import get_auth_headers


# =========================================================
# FETCH ANOMALIES
# =========================================================
def fetch_anomalies():

    try:
        response = requests.get(
            f"{API_URL}/anomalies",
            headers=get_auth_headers()
        )

        return response.json() if response.status_code == 200 else []

    except:
        return []


# =========================================================
# UPDATE ANOMALY
# =========================================================
def update_anomaly(anomaly_id, data):

    try:
        requests.put(
            f"{API_URL}/anomalies/{anomaly_id}",
            json=data,
            headers=get_auth_headers()
        )

    except:
        pass


# =========================================================
# DELETE ANOMALY
# =========================================================
def delete_anomaly(anomaly_id):

    try:
        requests.delete(
            f"{API_URL}/anomalies/{anomaly_id}",
            headers=get_auth_headers()
        )

    except:
        pass



# =========================================================
# MAIN PAGE
# =========================================================
def show():

    st.markdown(
        "<h1 style='text-align:center;'>TOWERMIND - Anomalies</h1>",
        unsafe_allow_html=True
    )


    anomalies = fetch_anomalies()


    # =========================================================
    # KPI
    # =========================================================

    critical = len([
        a for a in anomalies 
        if a.get("severite") == "critique"
    ])

    open_ = len([
        a for a in anomalies 
        if a.get("statut") == "ouverte"
    ])

    resolved = len([
        a for a in anomalies 
        if a.get("statut") == "resolue"
    ])


    c1, c2, c3 = st.columns(3)


    with c1:
        st.metric("CRITICAL", critical)

    with c2:
        st.metric("OPEN", open_)

    with c3:
        st.metric("RESOLVED", resolved)



    st.markdown("<br>", unsafe_allow_html=True)



    # =========================================================
    # TABLE HEADER
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
        grid-template-columns:
        60px 
        180px
        150px
        150px
        120px
        120px
        200px;
        ">

        <div>ID</div>
        <div>PROJECT</div>
        <div>ELEMENT</div>
        <div>TYPE</div>
        <div>SEVERITY</div>
        <div>STATUS</div>
        <div>ACTIONS</div>


        </div>
        """,
        unsafe_allow_html=True
    )



    # =========================================================
    # TABLE ROWS
    # =========================================================

    for a in anomalies:


        col1, col2, col3, col4, col5, col6, col7 = st.columns(
            [1,3,2,2,2,2,3]
        )


        # ID
        with col1:
            st.write(a.get("id"))


        # PROJECT
        with col2:
            st.write(
                a.get(
                    "projet_nom",
                    "Unknown project"
                )
            )


        # ELEMENT
        with col3:
            st.write(
                a.get(
                    "element_id",
                    "-"
                )
            )


        # TYPE
        with col4:
            st.write(
                a.get("type_anomalie")
            )


        # SEVERITY
        with col5:
            st.write(
                a.get("severite")
            )


        # STATUS
        with col6:
            st.write(
                a.get("statut")
            )



        # ACTIONS
        with col7:


            b1, b2 = st.columns(2)



            # =========================
            # EDIT
            # =========================

            with b1:


                if st.button(
                    "✏️",
                    key=f"edit_{a['id']}"
                ):


                    new_status = "ouverte"


                    if a.get("statut") == "ouverte":

                        new_status = "en_revision"


                    elif a.get("statut") == "en_revision":

                        new_status = "resolue"



                    update_anomaly(
                        a["id"],
                        {
                            "statut": new_status
                        }
                    )


                    st.success("Updated")

                    st.rerun()



            # =========================
            # DELETE
            # =========================

            with b2:


                if st.button(
                    "🗑",
                    key=f"del_{a['id']}"
                ):


                    delete_anomaly(
                        a["id"]
                    )


                    st.warning("Deleted")

                    st.rerun()



    # =========================================================
    # FOOTER
    # =========================================================

    st.markdown(
        "<br><hr><br>",
        unsafe_allow_html=True
    )


    st.info(
        "✏️ Click to change status"
    )