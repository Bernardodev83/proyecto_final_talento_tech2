import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# 1. CARGAR VARIABLES SEGUROTAS
# Buscamos el .env un nivel arriba de la carpeta /pages
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# 2. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="EcoAnalytics | Diagnóstico", layout="wide", page_icon="🌳")

# 3. FUNCIÓN DE CONEXIÓN INTEGRADA (Para evitar el error de importación)
def get_connection_internal():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "proyecto"),
            auth_plugin='mysql_native_password'
        )
        return connection
    except Error as e:
        st.error(f"❌ Error de conexión a la DB: {e}")
        return None

# 4. CARGA DE DATOS
def obtener_datos():
    conn = get_connection_internal()
    if not conn: return pd.DataFrame(), None
    try:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        if not tablas: return pd.DataFrame(), None
        
        tabla_nombre = tablas[0][0]
        df = pd.read_sql(f"SELECT * FROM {tabla_nombre}", conn)
        
        # Limpieza de columnas
        df.columns = [c.strip().replace('"', '').lower() for c in df.columns]
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.replace('"', '').str.strip()
            
        conn.close()
        return df, tabla_nombre
    except Exception as e:
        st.error(f"Error al leer la tabla: {e}")
        return pd.DataFrame(), None

# 5. INTERFAZ PRINCIPAL
def main():
    st.title("🌳 Diagnóstico de Impacto Ambiental")
    st.write("Visualización optimizada: Top 10 Sectores.")

    df, tabla_activa = obtener_datos()

    if not df.empty:
        # Detectar columnas
        col_anio = 'periodo' if 'periodo' in df.columns else df.columns[0]
        col_sec = 'seccion' if 'seccion' in df.columns else df.columns[1]
        col_val = 'gastos_tot' if 'gastos_tot' in df.columns else df.columns[2]

        # Filtros
        anios = sorted(df[col_anio].unique(), reverse=True)
        anio_sel = st.sidebar.selectbox("Seleccione el Año", anios)
        
        # Top 10
        df_f = df[df[col_anio] == anio_sel]
        df_top = df_f.sort_values(col_val, ascending=False).head(10)

        # MÉTRICAS
        c1, c2, c3 = st.columns(3)
        total_anio = df_f[col_val].sum()
        total_top = df_top[col_val].sum()
        
        c1.metric("Inversión Total", f"${total_anio:,.0f} M")
        c2.metric("Inversión Top 10", f"${total_top:,.0f} M")
        c3.metric("% del Total", f"{(total_top/total_anio)*100:.1f}%")

        st.markdown("---")

        # GRÁFICO TREEMAP
        st.subheader(f"Distribución de la Inversión ({anio_sel})")
        fig = px.treemap(
            df_top, path=[col_sec], values=col_val,
            color=col_val, color_continuous_scale='YlGnBu'
        )
        fig.update_layout(margin=dict(t=10, l=10, r=10, b=10), height=500)
        fig.update_traces(textinfo="label+value+percent root")
        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("⚠️ No se cargaron datos. Revisa tu MariaDB y el archivo .env")

if __name__ == "__main__":
    main()