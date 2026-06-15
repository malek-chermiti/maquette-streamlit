"""Configuration and constants for TOWERMIND application."""

# Page Configuration
PAGE_CONFIG = {
    "page_title": "TOWERMIND — BIMLO",
    "page_icon": "🏗️",
    "layout": "wide"
}

# Navigation Pages
PAGES = [
    "🏠  Tableau de bord",
    "📁  Projets",
    "⚠️  Anomalies",
    "🗼  Détail Pylône",
    "🤖  Agents IA",
    "🧊  Jumeau 3D",
    "💬  Chatbot RAG",
    "📄  Rapports",
]

# Sidebar Configuration
SIDEBAR_BRAND = {
    "name": "TOWERMIND",
    "icon": "🏗️",
    "tagline": "BIMLO Technologies · VERTWIN"
}

SIDEBAR_USER = {
    "name": "Malek Chermiti",
    "role": "Développeur Front · M4"
}

# Dashboard KPIs
DASHBOARD_KPIS = [
    "🗼 Pylônes surveillés",
    "⚠️ Anomalies actives",
    "✅ Précision vérification",
    "⚡ Temps moyen de traitement",
]

# Filter Options
FILTER_OPTIONS = {
    "modules": ["Tous", "M1", "M2", "M3", "M4", "M5"],
    "criticality": ["Toutes", "Critique", "Majeure", "Mineure"],
    "agents": ["Tous", "①", "②", "③", "④", "⑤"],
    "status": ["Tous", "Vérifié", "En cours", "Anomalie"],
    "period": ["Ce mois", "3 mois", "6 mois", "Tout"],
    "export_format": ["PDF", "Word (.docx)"],
}

# Project Selection
PROJECTS = ["PRJ-2024-001", "PRJ-2024-002", "PRJ-2024-003"]

# AI Agents Pipeline
AI_AGENTS = [
    "Agent ① — Plans 2D → Note de Calcul",
    "Agent ② — NC → Plans Fabrication",
    "Agent ③ — NC → SolidWorks",
    "Agent ④ — SolidWorks → IFC",
    "Agent ⑤ — Plans Fabrication ↔ IFC",
]

# Report Sections
REPORT_SECTIONS = [
    "Anomalies",
    "Résultats agents",
    "KPIs",
    "Graphiques",
    "Recommandations"
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
