import streamlit as st

st.set_page_config(page_title="Consultor de Hallazgos", page_icon="🔍", layout="wide")

st.title("🔍 Consultor de Dificultades y Sugerencias")
st.markdown("---")

st.write("Seleccione el año de su reporte para identificar las dificultades detectadas por el sistema y las sugerencias profesionales.")

# Diccionario de base de conocimiento
conocimiento_dane = {
    2020: {
        "dificultad": "Restricciones de movilidad impidieron la recolección presencial de datos de vertimientos.",
        "sugerencia": "Fortalecer la red de sensores IoT para monitoreo remoto en tiempo real."
    },
    2021: {
        "dificultad": "Interrupción en las cadenas de suministro de tecnologías para transición energética.",
        "sugerencia": "Fomentar la economía circular local para reducir la dependencia de insumos importados."
    },
    2022: {
        "dificultad": "Aumento en los costos operativos de gestión de residuos por inflación post-pandemia.",
        "sugerencia": "Optimizar rutas de recolección mediante algoritmos de inteligencia de datos."
    },
    2023: {
        "dificultad": "Brecha de conocimiento técnico en el personal para el manejo de nuevas métricas de carbono.",
        "sugerencia": "Establecer convenios de capacitación técnica con el SENA y universidades regionales."
    }
}

# Selector
anio = st.selectbox("¿Qué año desea analizar?", [2020, 2021, 2022, 2023])

# Presentación profesional
st.subheader(f"Reporte de Hallazgos - Gestión {anio}")

col_error, col_plan = st.columns(2)

with col_error:
    st.error("**Dificultad Encontrada**")
    st.write(conocimiento_dane[anio]["dificultad"])

with col_plan:
    st.success("**Sugerencia Profesional**")
    st.write(conocimiento_dane[anio]["sugerencia"])

st.markdown("---")
st.caption("EcoAnalytics Pro - Generado automáticamente basado en indicadores de gestión ambiental.")