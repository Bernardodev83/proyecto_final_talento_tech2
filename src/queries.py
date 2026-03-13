import pandas as pd
from src.connection import get_connection

def leer_datos_generales():
    conn = get_connection()
    if conn:
        try:
            # Esta consulta coincide EXACTAMENTE con la tabla que creamos arriba
            query = """
                SELECT anio, id_empresa, sector, inversion_total, 
                       gasto_operativo, gestion_directa, consumo_simulado,
                       personal_ambiental, inversion_energia_limpia
                FROM datos
            """
            df = pd.read_sql(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error en leer_datos: {e}")
            return pd.DataFrame()
    return pd.DataFrame()