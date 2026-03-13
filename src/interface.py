import streamlit as st
import pandas as pd
from reports import generar_reporte_problemas

def main():
    st.set_page_config(page_title="EcoAnalytics Pro", layout="wide")
    st.title("🌱 EcoAnalytics Pro - DANE")

    # CARGA DE DATOS (Ajusta la ruta a tu archivo CSV)
    try:
        df = pd.read_csv('datos_ambientales.csv')
        
        # Limpieza Crítica para el Mapa y Cálculos
        if 'departamento' in df.columns:
            df['departamento'] = df['departamento'].str.upper().str.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        
        # Selector de Año
        anios = sorted(df['periodo'].unique(), reverse=True)
        anio_sel = st.sidebar.selectbox("Seleccione el Año de Análisis", anios)

        # Filtrado
        df_filtrado = df[df['periodo'] == anio_sel]

        # Llamada al Reporte Profesional
        generar_reporte_problemas(df_filtrado)

    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        st.info("Asegúrese de que el archivo CSV tenga las columnas: 'periodo', 'sector', 'valor' y 'departamento'.")

if __name__ == "__main__":
    main()