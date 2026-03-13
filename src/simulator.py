import streamlit as st

def mostrar_simulador():
    st.header("⚡ Simulador de Impacto Energético")
    st.info("Ajusta los valores para proyectar el beneficio de tu inversión ambiental.")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Configuración")
        inversion = st.slider("Monto a Invertir ($ USD):", 1000, 50000, 5000, step=500)
        tipo = st.selectbox("Tipo de Proyecto:", [
            "Paneles Solares", 
            "Optimización de Agua", 
            "Filtros de Aire Pro"
        ])
    
    # Lógica de simulación (Valores promedio de mercado)
    if tipo == "Paneles Solares":
        co2_ahorrado = (inversion / 1000) * 0.5  # Tons de CO2 al año
        ahorro_dinero = inversion * 0.15          # 15% de retorno anual
        impacto = "Alta reducción de huella de carbono."
    elif tipo == "Optimización de Agua":
        co2_ahorrado = (inversion / 1000) * 0.1
        ahorro_dinero = inversion * 0.25          # El agua ahorra más rápido
        impacto = "Optimización de recursos hídricos críticos."
    else:
        co2_ahorrado = (inversion / 1000) * 0.8  # El aire impacta mucho en CO2
        ahorro_dinero = inversion * 0.05
        impacto = "Cumplimiento estricto de normas de salud."

    with col2:
        st.subheader("Resultados Proyectados")
        st.metric("CO2 Evitado (Tons/Año)", f"{co2_ahorrado:.2f}")
        st.metric("Ahorro Operativo Anual", f"${ahorro_dinero:,.0f} USD")
        st.write(f"**Análisis:** {impacto}")

    st.success("💡 Esta simulación ayuda a las empresas a justificar el retorno de inversión (ROI) ambiental.")