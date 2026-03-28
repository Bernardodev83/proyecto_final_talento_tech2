"""
Módulo centralizado de componentes para EcoAnalytics Pro.
Solo funciones puras de datos + CSS mínimo para sidebar.
NO usa unsafe_allow_html con contenido dinámico.
"""
import streamlit as st
import pandas as pd
import plotly.io as pio
import os


# ---------------------------------------------------------------------------
# 1. CARGA DE DATOS (cacheada)
# ---------------------------------------------------------------------------

@st.cache_data
def cargar_datos() -> pd.DataFrame:
    """Carga datos_unificados.csv con limpieza de tipos."""
    rutas = [
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'datos_unificados.csv'),
        'datos_unificados.csv',
        os.path.join('..', 'datos_unificados.csv'),
    ]
    ruta = next((r for r in rutas if os.path.exists(r)), None)
    if ruta is None:
        st.error("No se encontró **datos_unificados.csv**. Ejecute `python src/unificar_datos.py`.")
        return pd.DataFrame()

    df = pd.read_csv(ruta, low_memory=False)
    if 'anio' in df.columns:
        df = df.dropna(subset=['anio'])
        df['anio'] = df['anio'].astype(int)
    for col in ('gastos_totales', 'gasto_gestion_amb', 'total_ingresos', 'personal_ocupado_total'):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    return df


# ---------------------------------------------------------------------------
# 2. TEMA VISUAL — solo CSS estático mínimo para sidebar
# ---------------------------------------------------------------------------

_SIDEBAR_CSS = """
<style>
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent !important; }
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%) !important;
}
section[data-testid="stSidebar"] * { color: #cbd5e1 !important; }
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stMultiSelect label {
    color: #94a3b8 !important; font-size: 0.8rem;
    text-transform: uppercase; letter-spacing: 0.05em;
}
section[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.08) !important; }
section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] {
    padding: 0.55rem 1rem !important; margin: 2px 8px;
    border-radius: 8px !important; font-weight: 500 !important;
    font-size: 0.9rem !important; color: #94a3b8 !important;
    transition: background 0.15s ease, color 0.15s ease !important;
}
section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"]:hover {
    background: rgba(59,130,246,0.15) !important; color: #e2e8f0 !important;
}
section[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"][aria-current="page"] {
    background: rgba(59,130,246,0.2) !important; color: #60a5fa !important;
    font-weight: 700 !important; border-left: 3px solid #3b82f6 !important;
}
</style>
"""


def aplicar_tema() -> None:
    """Inyecta CSS estático mínimo para sidebar y configura Plotly."""
    st.markdown(_SIDEBAR_CSS, unsafe_allow_html=True)
    pio.templates.default = "plotly"


# ---------------------------------------------------------------------------
# 3. HELPERS (funciones puras, sin HTML)
# ---------------------------------------------------------------------------

def delta_pct(actual, anterior):
    """Calcula variación porcentual. Soporta escalares y pandas Series."""
    if isinstance(anterior, pd.Series):
        return ((actual - anterior) / anterior.replace(0, float('nan')) * 100).fillna(0)
    return ((actual - anterior) / anterior * 100) if anterior > 0 else 0.0