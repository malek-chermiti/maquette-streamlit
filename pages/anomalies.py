"""Anomalies page - Détection et classification par les agents IA"""

import streamlit as st
from components.cards import render_severity_card, render_card_header, render_card_footer
from components.forms import render_search_bar, render_filter_row


def show():
    """Render the anomalies page."""
    st.markdown("<div class='page-title'>⚠️ Anomalies Dashboard</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='page-sub'>AI-flagged structural defects awaiting verification or remediation</div>",
        unsafe_allow_html=True,
    )

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        render_severity_card("critical", "CRITICAL", note="Immediate action")
    with k2:
        render_severity_card("high", "HIGH", note="Within 48h")
    with k3:
        render_severity_card("medium", "MEDIUM", note="Within 7 days")
    with k4:
        render_severity_card("resolved", "RESOLVED (30D)", note="+12% vs prev.")

    st.markdown("<br>", unsafe_allow_html=True)

    render_search_bar("Search anomaly ID, tower, type...", key="anomaly_search")

    st.markdown("<br>", unsafe_allow_html=True)

    render_filter_row([
        {"label": "Severity", "key": "severity", "options": ["All severities", "Critical", "High", "Medium", "Low"]},
        {"label": "Region", "key": "region", "options": ["All regions", "Tunis", "Sfax", "Sousse", "Bizerte"]},
        {"label": "State", "key": "state", "options": ["All states", "Open", "Reviewing", "Resolved"]},
        {"label": "Period", "key": "period", "options": ["Last 30 days", "Last 7 days", "Last 24h", "All"]},
    ])

    st.markdown("<br>", unsafe_allow_html=True)

    render_card_header("📋 Anomalies List")
    st.markdown(
        """
        <div class='table-scroll'>
            <table class='data-table'>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>TOWER</th>
                        <th>ANOMALY</th>
                        <th>SEVERITY</th>
                        <th>CONFIDENCE</th>
                        <th>REGION</th>
                        <th>DETECTED</th>
                        <th>STATE</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td colspan='8' class='empty-table-cell'>
                            📋 Anomalies data — coming soon
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_card_footer()
