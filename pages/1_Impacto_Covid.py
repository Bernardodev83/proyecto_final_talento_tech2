import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Impacto COVID-19", page_icon="🦠", layout="wide")

st.title("🦠 Análisis de Impacto COVID-19")
st.markdown("---")

st.write("""
Esta sección analiza el comportamiento de la inversión ambiental en Colombia durante el periodo de crisis sanitaria (2020-2021) 
y la posterior reactivación económica.
""")

# Datos para el análisis histórico
df_hist = pd.DataFrame({
    'Año': [2019, 2020, 2021, 2022, 2023],
    'Inversión ($M)': [4200, 2900, 3300, 4600, 5100],
    'Etapa': ['Pre-Pandemia', 'Caída Crítica', 'Recuperación Temprana', 'Estabilización', 'Crecimiento']
})

# Gráfico de área para mostrar la "vaguada" del Covid
fig = px.area(df_hist, x='Año', y='Inversión ($M)', text='Etapa',
              title="Evolución de la Inversión Ambiental (2019-2023)",
              color_discrete_sequence=['#6d597a'])

fig.update_traces(textposition='top center')
st.plotly_chart(fig, use_container_width=True)

st.info("""
**Observación Técnica:** El descenso observado en 2020 responde a la reorientación de recursos públicos hacia el sector salud. 
Sin embargo, el repunte en 2022 indica un compromiso renovado con las metas de sostenibilidad del DANE.
""")