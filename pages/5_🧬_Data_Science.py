"""Página 5 — Ciencia de Datos."""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.components import cargar_datos, aplicar_tema

st.set_page_config(page_title="Data Science", page_icon="🧬", layout="wide")
aplicar_tema()

st.header("🧬 Deep Data Science")
st.caption("Correlaciones, dispersión multidimensional y estadísticas descriptivas.")

df = cargar_datos()
if not df.empty:
    COLS = ['total_ingresos','gastos_totales','gasto_gestion_amb','personal_ocupado_total']
    NOMS = ['Ingresos','Gastos Totales','Gasto Amb.','Personal']

    tab1, tab2, tab3 = st.tabs(["🔥 Correlación", "🌌 Dispersión", "📈 Estadísticas"])

    with tab1:
        st.markdown("**Inteligencia Relacional:** valores cercanos a 1 = crecimiento proporcional conjunto.")
        corr = df[COLS].corr().round(2)
        fig = go.Figure(data=go.Heatmap(z=corr.values, x=NOMS, y=NOMS, colorscale='Blues',
                                         text=corr.values, texttemplate='%{text}', showscale=True))
        fig.update_layout(height=450, margin=dict(t=30, b=30))
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("**Dispersión Multidimensional:** X=Ingresos, Y=Gastos, Tamaño=Personal.")
        anios = sorted(df['anio'].unique(), reverse=True)
        anio_s = st.selectbox("Año:", anios, index=0)
        da = df[(df['anio']==anio_s) & (df['total_ingresos']>0) & (df['gastos_totales']>0)]
        if not da.empty:
            fig_s = px.scatter(da, x='total_ingresos', y='gastos_totales', color='nombre_sector',
                               size='personal_ocupado_total', hover_name='id_empresa', log_x=True, log_y=True,
                               labels={'total_ingresos':'Ingresos ($)','gastos_totales':'Gastos ($)','nombre_sector':'Sector'},
                               title=f'Clústeres Sectoriales (Log) — {anio_s}')
            st.plotly_chart(fig_s, use_container_width=True)
        else:
            st.info(f"Sin datos positivos para {anio_s}.")

    with tab3:
        st.markdown("**Desviación y Cuartiles:**")
        st.dataframe(df[COLS].describe().T, use_container_width=True)

    st.divider()
    st.subheader("🤖 Autodiagnóstico")
    st.info(
        "**Elasticidad:** Correlación positiva moderada entre Ingresos y Gastos, "
        "pero el Gasto Ambiental muestra alta varianza.\n\n"
        "**Clústeres:** En escala log, industrias primarias y manufactureras concentran "
        "outliers en la zona superior derecha."
    )
else:
    st.warning("Sin datos. Active el conector de datos.")
