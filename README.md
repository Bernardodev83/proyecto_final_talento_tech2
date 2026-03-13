# 🌳 EcoAnalytics Pro: Gestión de Inteligencia Ambiental

**EcoAnalytics Pro** es una plataforma de análisis de datos desarrollada en Python y Streamlit, diseñada para visualizar y diagnosticar la inversión ambiental en Colombia basándose en estadísticas oficiales del **DANE**.

El sistema permite transformar datos complejos de bases de datos MariaDB en tableros de control estratégicos (Dashboards) para facilitar la toma de decisiones en sostenibilidad.

---

## 🚀 Características Principales

* **Conexión Dinámica:** Integración robusta con MariaDB/MySQL.
* **Visualización Estratégica:** Uso de *Treemaps* y gráficos interactivos para evitar la saturación de información.
* **Top 10 de Impacto:** Filtrado automático de los sectores con mayor relevancia en el gasto ambiental.
* **Seguridad:** Arquitectura protegida mediante variables de entorno (`.env`).
* **Interfaz Profesional:** Diseño limpio y métricas en tiempo real.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Framework Web:** Streamlit
* **Base de Datos:** MariaDB / MySQL
* **Visualización:** Plotly Express & Pandas
* **Seguridad:** Python-Dotenv

## 📦 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto localmente:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Bernardodev83/proyecto_final_talento_tech2.git](https://github.com/Bernardodev83/proyecto_final_talento_tech2.git)
cd proyecto_dane_pro

2. Instalar dependencias

pip install -r requirements.txt

3. Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto con el siguiente formato:

Plaintext
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=tu_contraseña
DB_NAME=proyecto


4. Ejecutar la aplicación

streamlit run Inicio.py
📊 Estructura del Proyecto
Plaintext
proyecto_dane_pro/
├── Inicio.py                # Página principal de bienvenida
├── .env                     # Variables sensibles (No incluido en GitHub)
├── .gitignore               # Archivos excluidos de Git
├── requirements.txt         # Librerías necesarias
└── pages/
    └── 0_Diagnostico_General.py  # Reporte de inversión ambiental
Desarrollado con  por Bernardodev83.