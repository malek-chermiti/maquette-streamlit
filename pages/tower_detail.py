"""Tower Detail page - Fiche complète et résultats de vérification"""

import streamlit as st
from config import PROJECTS
from utils import render_page_header, render_card_with_title


def show():
    """Render the tower detail page."""
    st.markdown("<div class='page-title'>🗼 Détail Pylône</div>", unsafe_allow_html=True)
    st.markdown("<div class='page-sub'>Fiche complète et résultats de vérification</div>", unsafe_allow_html=True)

    st.selectbox("Sélectionner un projet", PROJECTS)

    # General Information
    st.markdown("""
    <div class='card'>
        <div class='section-title'>📐 Informations générales</div>
        <div style='font-size:0.85rem; color:#64748b; line-height:1.8;'>
            <div style='display:grid; grid-template-columns: 1fr 1fr; gap:1.5rem; margin-bottom:1rem;'>
                <div>
                    <div style='font-weight:600; color:#0F172A;'>Référence</div>
                    <div style='color:#94a3b8; margin-top:4px;'>—</div>
                </div>
                <div>
                    <div style='font-weight:600; color:#0F172A;'>Région</div>
                    <div style='color:#94a3b8; margin-top:4px;'>—</div>
                </div>
                <div>
                    <div style='font-weight:600; color:#0F172A;'>Hauteur</div>
                    <div style='color:#94a3b8; margin-top:4px;'>—</div>
                </div>
                <div>
                    <div style='font-weight:600; color:#0F172A;'>Type</div>
                    <div style='color:#94a3b8; margin-top:4px;'>—</div>
                </div>
                <div>
                    <div style='font-weight:600; color:#0F172A;'>Année installation</div>
                    <div style='color:#94a3b8; margin-top:4px;'>—</div>
                </div>
                <div>
                    <div style='font-weight:600; color:#0F172A;'>Statut</div>
                    <div style='color:#94a3b8; margin-top:4px;'>—</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Detected Anomalies
    st.markdown("""
    <div class='card'>
        <div class='section-title'>⚠️ Anomalies détectées</div>
        <div style='font-size:0.85rem; color:#94a3b8; padding:1rem; background:#f1f5f9; border-radius:8px; border-left:3px solid #f97316;'>
            Aucune anomalie détectée — données à venir
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Existing Diagnostics
    st.markdown("""
    <div class='card'>
        <div class='section-title'>📋 Diagnostics existants</div>
        <div style='font-size:0.85rem; color:#94a3b8; padding:1rem; background:#f1f5f9; border-radius:8px; border-left:3px solid #3b82f6;'>
            Aucun diagnostic disponible — données à venir
        </div>
    </div>
    """, unsafe_allow_html=True)

