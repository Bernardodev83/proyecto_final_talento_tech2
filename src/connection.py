import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Cargamos las variables del archivo secreto .env
load_dotenv()

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            auth_plugin='mysql_native_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"❌ ERROR TÉCNICO DE CONEXIÓN: {e}") 
        return None