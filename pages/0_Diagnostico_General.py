import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="EcoAnalytics | Diagnóstico", layout="wide", page_icon="🌳")

def cargar_datos():
    # Intentamos varias rutas posibles para encontrar el archivo en la nube
    nombre_archivo = 'dane.csv'
    ruta_csv = os.path.join(os.path.dirname(__file__), '..', nombre_archivo)
    
    # Si no existe en la ruta relativa, probamos en la raíz
    if not os.path.exists(ruta_csv):
        ruta_csv = nombre_archivo

    if os.path.exists(ruta_csv):
        # Probamos codificaciones específicas (CORREGIDO: 'in' en lugar de 'en')
        for enc in ['latin-1', 'iso-8859-1', 'cp1252', 'utf-8']:
            try:
                df = pd.read_csv(ruta_csv, encoding=enc)
                
                # Limpieza de nombres de columnas
                df.columns = [str(c).strip().replace('"', '').lower() for c in df.columns]
                
                # Conversión de datos
                if 'periodo' in df.columns:
                    df['periodo'] = pd.to_numeric(df['periodo'], errors='coerce')
                    df = df.dropna(subset=['periodo'])
                    df['periodo'] = df['periodo'].astype(int)
                
                if 'gastos_tot' in df.columns:
                    df['gastos_tot'] = pd.to_numeric(df['gastos_tot'], errors='coerce').fillna(0)
                
                return df
            except (UnicodeDecodeError, Exception):
                continue  # Si falla esta codificación, salta a la siguiente
    
    return pd.DataFrame()

def main():
    st.title("🌳 Diagnóstico Ambiental (Datos DANE)")
    
    df = cargar_datos()

    if not df.empty:
        # Filtro de Año
        anios = sorted(df['periodo'].unique(), reverse=True)
        anios = [a for a in anios if a >= 2020] # Filtramos años recientes
        
        if anios:
            anio_sel = st.sidebar.selectbox("Seleccione el Año de Análisis", anios)

            # Filtrado por año seleccionado
            df_f = df[df['periodo'] == anio_sel].copy()
            
            # Identificar columna de sección
            col_sec = 'seccion' if 'seccion' in df.columns else df.columns[4]
            
            # Agrupación para el gráfico
            df_grafico = df_f.groupby(col_sec)['gastos_tot'].sum().reset_index()
            df_top = df_grafico.sort_values('gastos_tot', ascending=False).head(10)

            # Métricas principales
            inv_total = df_f['gastos_tot'].sum()
            registros = len(df_f)
            
            c1, c2 = st.columns(2)
            c1.metric(f"Inversión Total {anio_sel}", f"${inv_total:,.0f}")
            c2.metric("Empresas/Registros", f"{registros:,}")

            st.markdown("---")

            if inv_total > 0:
                st.subheader(f"Distribución de Inversión por Sector - {anio_sel}")
                fig = px.treemap(
                    df_top, 
                    path=[col_sec], 
                    values='gastos_tot',
                    color='gastos_tot',
                    color_continuous_scale='YlGnBu'
                )
                fig.update_layout(height=500, margin=dict(t=30, l=10, r=10, b=10))
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning(f"No se encontraron montos de inversión mayores a $0 para el año {anio_sel}")
        else:
            st.warning("No se encontraron años válidos en el archivo.")
    else:
        st.error("❌ No se pudo cargar el archivo 'dane.csv'. Verifica que esté en la raíz de tu proyecto en GitHub.")

if __name__ == "__main__":
    main()