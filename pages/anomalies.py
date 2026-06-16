"""Anomalies page - Détection et classification par les agents IA"""

import streamlit as st
from config import FILTER_OPTIONS
from utils import render_page_header


def show():
    """Render the anomalies page."""
    st.markdown("<div class='page-title'>⚠️ Anomalies Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>AI-flagged structural defects awaiting verification or remediation</div>", unsafe_allow_html=True)

    # KPI Cards
    k1, k2, k3, k4 = st.columns(4)
    
    with k1:
        st.markdown("""
        <div class='card' style='background: #fce7f3; border-color: #fbcfe8;'>
            <div style='font-size:0.75rem; font-weight:700; color:#be185d; letter-spacing:0.05em;'>CRITICAL</div>
            <div style='font-size:2.5rem; font-weight:800; color:#be185d; margin:0.5rem 0;'>—</div>
            <div style='font-size:0.85rem; color:#ec4899;'>Immediate action</div>
        </div>
        """, unsafe_allow_html=True)
    
    with k2:
        st.markdown("""
        <div class='card' style='background: #fef3c7; border-color: #fde68a;'>
            <div style='font-size:0.75rem; font-weight:700; color:#92400e; letter-spacing:0.05em;'>HIGH</div>
            <div style='font-size:2.5rem; font-weight:800; color:#1f2937; margin:0.5rem 0;'>—</div>
            <div style='font-size:0.85rem; color:#78350f;'>Within 48h</div>
        </div>
        """, unsafe_allow_html=True)
    
    with k3:
        st.markdown("""
        <div class='card' style='background: #dbeafe; border-color: #bfdbfe;'>
            <div style='font-size:0.75rem; font-weight:700; color:#1e40af; letter-spacing:0.05em;'>MEDIUM</div>
            <div style='font-size:2.5rem; font-weight:800; color:#1e40af; margin:0.5rem 0;'>—</div>
            <div style='font-size:0.85rem; color:#1e3a8a;'>Within 7 days</div>
        </div>
        """, unsafe_allow_html=True)
    
    with k4:
        st.markdown("""
        <div class='card' style='background: #dcfce7; border-color: #bbf7d0;'>
            <div style='font-size:0.75rem; font-weight:700; color:#15803d; letter-spacing:0.05em;'>RESOLVED (30D)</div>
            <div style='font-size:2.5rem; font-weight:800; color:#15803d; margin:0.5rem 0;'>—</div>
            <div style='font-size:0.85rem; color:#22c55e;'>+12% vs prev.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Top Actions
    c1 = st.columns(1)[0]
    
    with c1:
        st.text_input("Search anomaly ID, tower, type...", placeholder="Search anomaly ID, tower, type...")

    st.markdown("<br>", unsafe_allow_html=True)

    # Filters
    f1, f2, f3, f4 = st.columns(4)
    with f1:
        st.selectbox("Severity", ["All severities", "Critical", "High", "Medium", "Low"])
    with f2:
        st.selectbox("Region", ["All regions", "Tunis", "Sfax", "Sousse", "Bizerte"])
    with f3:
        st.selectbox("State", ["All states", "Open", "Reviewing", "Resolved"])
    with f4:
        st.selectbox("Period", ["Last 30 days", "Last 7 days", "Last 24h", "All"])

    st.markdown("<br>", unsafe_allow_html=True)

    # Anomalies Table
    st.markdown("""
    <div class='card'>
        <div class='section-title'>📋 Anomalies List</div>
        <div style='overflow-x: auto;'>
            <table style='width:100%; border-collapse: collapse; font-size:0.85rem;'>
                <thead style='background:#f8fafc; border-bottom: 2px solid #e2e8f0;'>
                    <tr>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>ID</th>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>TOWER</th>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>ANOMALY</th>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>SEVERITY</th>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>CONFIDENCE</th>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>REGION</th>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>DETECTED</th>
                        <th style='padding:0.75rem; text-align:left; font-weight:600; color:#0F172A;'>STATE</th>
                    </tr>
                </thead>
                <tbody>
                    <tr style='border-bottom: 1px solid #e2e8f0;'>
                        <td colspan='8' style='padding:2rem; text-align:center; color:#94a3b8;'>
                            📋 Anomalies data — coming soon
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """, unsafe_allow_html=True)
