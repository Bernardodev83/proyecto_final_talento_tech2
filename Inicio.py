"""Página principal — Landing con KPIs globales."""
import streamlit as st
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from components import cargar_datos, aplicar_tema

st.set_page_config(page_title="EcoAnalytics Pro", page_icon="⚡", layout="wide",
                   initial_sidebar_state="expanded")
aplicar_tema()

st.header("⚡ EcoAnalytics Dashboard")
st.caption("Ecoeficiencia Empresarial · Inteligencia de Datos · 2019-2023")
st.divider()

df = cargar_datos()
if not df.empty:
    c1, c2, c3 = st.columns(3)
    c1.metric("💰 Inversión Acumulada", f"${df['gastos_totales'].sum() / 1e6:,.1f} M")
    c2.metric("🏢 Compañías Analizadas", f"{df['id_empresa'].nunique():,}")
    c3.metric("📈 Ingreso Promedio", f"${df['total_ingresos'].mean() / 1e6:,.1f} M")

    st.divider()
    st.subheader("Módulos Analíticos")
    st.markdown(
        "- 🌳 **Diagnóstico** — Métricas macro por año y treemap sectorial\n"
        "- 🦠 **COVID-19** — Curva histórica de inversión ambiental\n"
        "- 🔍 **Consultor** — Riesgos y recomendaciones por periodo\n"
        "- 🏢 **Empresarial** — Perfil individual por ID de empresa\n"
        "- 🏭 **Sectorial** — Boxplots y benchmarking por sector\n"
        "- 🧬 **Data Science** — Correlaciones, dispersión y estadísticas\n\n"
        "👈 *Utiliza el menú lateral para navegar.*"
    )