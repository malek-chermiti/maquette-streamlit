"""Configuration and constants for TOWERMIND application."""

# Page Configuration
PAGE_CONFIG = {
    "page_title": "TOWERMIND - BIMLO",
    "page_icon": "T",
    "layout": "wide",
}

# Backend API
API_URL = "http://localhost:8000"

# Local authentication store used when the backend is not available.
AUTH_STORE_PATH = "users_auth.json"

# Authentication fallback for the mock when the backend is offline.
ALLOW_DEMO_LOGIN = True

# Navigation - liste unique (pages principales + pages statiques)
ALL_PAGES = [
    "Tableau de bord",
    "Projets",
    "Anomalies",
    "Detail Pylone",
    "Agents IA",
    "Jumeau 3D",
    "Chatbot RAG",
    "Rapports",
    "A propos",
    "FAQ",
    "Contact",
    "Documentation utilisateur",
    "Mentions legales",
    "Politique de confidentialite",
]

# Retrocompatibilite
PAGES = ALL_PAGES[:8]

# Sidebar Configuration
SIDEBAR_BRAND = {
    "name": "TOWERMIND",
    "icon": "T",
    "tagline": "BIMLO Technologies - VERTWIN",
}

SIDEBAR_USER = {
    "name": "Malek Chermiti",
    "role": "Developpeur Front - M4",
}

# Dashboard KPIs
DASHBOARD_KPIS = [
    "Pylones surveilles",
    "Anomalies actives",
    "Precision verification",
    "Temps moyen de traitement",
]

# Filter Options
FILTER_OPTIONS = {
    "modules": ["Tous", "M1", "M2", "M3", "M4", "M5"],
    "criticality": ["Toutes", "Critique", "Majeure", "Mineure"],
    "agents": ["Tous", "M1", "M2", "M3", "M4", "M5"],
    "status": ["Tous", "Verifie", "En cours", "Anomalie"],
    "period": ["Ce mois", "3 mois", "6 mois", "Tout"],
    "export_format": ["PDF", "Word (.docx)"],
}

# Project Selection
PROJECTS = ["PRJ-2024-001", "PRJ-2024-002", "PRJ-2024-003"]

# AI Agents Pipeline
AI_AGENTS = [
    "Agent M1 - Plans 2D vers Note de Calcul",
    "Agent M2 - NC vers Plans Fabrication",
    "Agent M3 - NC vers SolidWorks",
    "Agent M4 - SolidWorks vers IFC",
    "Agent M5 - Plans Fabrication / IFC",
]

# Report Sections
REPORT_SECTIONS = [
    "Anomalies",
    "Resultats agents",
    "KPIs",
    "Graphiques",
    "Recommandations",
]

# Color Scheme
COLORS = {
    "dark_bg": "#0F172A",
    "light_bg": "#F8FAFC",
    "white": "white",
    "border": "#1e293b",
    "border_light": "#e2e8f0",
    "text_primary": "#0F172A",
    "text_secondary": "#64748b",
    "text_muted": "#94a3b8",
    "bg_placeholder": "#f1f5f9",
}
