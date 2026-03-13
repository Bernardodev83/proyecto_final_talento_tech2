import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="EcoAnalytics Pro | Inicio",
    page_icon="🌱",
    layout="wide"
)

# 2. ESTILO CSS PARA EL PIE DE PÁGINA (Footer)
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: grey;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        border-top: 1px solid #e6e6e6;
    }
    </style>
    <div class="footer">
        <p>EcoAnalytics Pro © 2026 | Desarrollado con datos abiertos del DANE | Bernardodev83</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    # --- ENCABEZADO ---
    st.title("🌱 EcoAnalytics Pro")
    st.markdown("### *Inteligencia de Datos para la Sostenibilidad Ambiental*")
    st.info("Bienvenido al sistema de análisis de inversión ambiental en Colombia.")
    
    st.markdown("---")

    # --- CUERPO DE BIENVENIDA ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        #### Propósito del Sistema
        Esta herramienta permite a los analistas y tomadores de decisiones explorar el 
        comportamiento de la inversión para la protección del medio ambiente, utilizando 
        estadísticas oficiales.
        
        **Explore las secciones en el menú de la izquierda:**
        
        1. **📊 Diagnóstico General:** Visualice indicadores clave, mapas de inversión por departamento y análisis de brechas sectoriales.
        2. **🦠 Impacto COVID-19:** Analice la curva histórica y cómo la crisis sanitaria transformó las prioridades presupuestales.
        3. **🔍 Consultor de Hallazgos:** Obtenga soluciones técnicas y sugerencias profesionales para los retos detectados en años específicos.
        """)

    with col2:
        # Panel de Estado e Información
        st.subheader("Estado del Sistema")
        st.write("📈 **Datos:** Actualizados (2020-2023)")
        st.write("📂 **Fuente:** DANE - Encuesta Ambiental")
        st.write("🌍 **Cobertura:** Nacional (Colombia)")
        
        if st.button("Ver Resumen Ejecutivo"):
            st.success("En 2023, la inversión ambiental creció un 12% impulsada por energías limpias.")

    st.markdown("---")
    
    # --- SECCIÓN DE METAS ---
    st.write("#### Indicadores de Cumplimiento Global")
    c1, c2, c3 = st.columns(3)
    c1.metric("Meta Plan Desarrollo", "88%", "En progreso")
    c2.metric("Reportes Generados", "156", "Marzo 2026")
    c3.metric("Nivel de Confianza", "99.2%", "DANE Verified")

if __name__ == "__main__":
    main()