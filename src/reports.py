import streamlit as st
import pandas as pd
from components import crear_gauge_inversion, crear_barras_comparativas, crear_mapa_colombia, ECO_COLORS

def generar_reporte_problemas(df_anio):
    st.markdown("---")
    st.subheader("📋 Diagnóstico y Análisis Espacial")
    
    if df_anio.empty:
        st.warning("⚠️ Seleccione un año con registros para generar el diagnóstico.")
        return

    # --- PROCESAMIENTO ---
    df_analisis = df_anio.copy()
    df_analisis['valor'] = pd.to_numeric(df_analisis['valor'], errors='coerce').fillna(0)
    
    inv_total = df_analisis['valor'].sum()
    promedio_sector = df_analisis['valor'].mean()

    # --- FILA 1: MÉTRICAS Y VELOCÍMETRO ---
    col_metricas, col_gauge = st.columns([1, 2])
    
    with col_metricas:
        st.metric("Inversión Total", f"${inv_total:,.0f}M")
        st.metric("Promedio Sectorial", f"${promedio_sector:,.0f}M")
        st.metric("Sectores", len(df_analisis['sector'].unique()))
    
    with col_gauge:
        fig_gauge = crear_gauge_inversion(inv_total)
        st.plotly_chart(fig_gauge, use_container_width=True)

    # --- FILA 2: MAPA Y BARRAS ---
    col_mapa, col_barras = st.columns([1, 1])
    
    with col_mapa:
        # Nota: Asegúrate de tener una columna 'departamento' en tu DataFrame
        if 'departamento' in df_analisis.columns:
            # Agrupamos por departamento para el mapa
            df_geo = df_analisis.groupby('departamento')['valor'].sum().reset_index()
            fig_mapa = crear_mapa_colombia(df_geo)
            st.plotly_chart(fig_mapa, use_container_width=True)
        else:
            st.info("ℹ️ Agregue columna 'departamento' para visualizar el mapa.")

    with col_barras:
        fig_barras = crear_barras_comparativas(df_analisis, promedio_sector)
        st.plotly_chart(fig_barras, use_container_width=True)

    # --- FILA 3: DIAGNÓSTICOS ---
    st.markdown("### Identificación de Hallazgos")

    col_l, col_w = st.columns(2)
    
    with col_l:
        if inv_total < 3000:
            st.error(f"🚨 **ALERTA: Desinversión**")
            st.caption(f"Total: ${inv_total:,.0f}M")
            with st.expander("🛠️ Solución Sugerida"):
                st.markdown("* Deducción 120% renta.\n* Capacitación SENA.")

    with col_w:
        sectores_bajos = df_analisis[df_analisis['valor'] < promedio_sector]['sector'].unique()
        if len(sectores_bajos) > 0:
            st.warning(f"⚖️ **BRECHA: Desigualdad**")
            st.caption(f"{len(sectores_bajos)} sectores rezagados")
            with st.expander("💡 Propuesta"):
                st.markdown("* Apadrinamiento PYMES.\n* Sensores IoT.")

    st.markdown("---")
    st.success("🌱 **RECOMENDACIÓN ESTRATÉGICA FINAL**: Priorizar Medición de Huella de Carbono.")