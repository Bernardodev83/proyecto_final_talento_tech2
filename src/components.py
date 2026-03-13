import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

ECO_COLORS = {
    'danger': '#e63946',
    'warning': '#ffb703',
    'success': '#2d6a4f',
    'info': '#0077b6',
    'light_green': '#b7e4c7'
}

def crear_gauge_inversion(valor_actual, meta=5000):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=valor_actual,
        delta={'reference': meta, 'increasing': {'color': ECO_COLORS['success']}},
        title={'text': "Inversión Total ($M)", 'font': {'size': 18}},
        gauge={
            'axis': {'range': [None, max(meta * 1.2, valor_actual * 1.1)]},
            'bar': {'color': ECO_COLORS['info']},
            'steps': [
                {'range': [0, meta*0.5], 'color': '#f8d7da'},
                {'range': [meta, meta*1.5], 'color': '#d4edda'}
            ],
        }
    ))
    fig.update_layout(height=250, margin=dict(l=20, r=20, t=40, b=20))
    return fig

def crear_barras_comparativas(df, promedio):
    fig = px.bar(
        df, x='sector', y='valor',
        title="Inversión vs Promedio",
        color_discrete_sequence=[ECO_COLORS['info']]
    )
    fig.add_hline(y=promedio, line_dash="dash", line_color=ECO_COLORS['danger'])
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', height=400)
    return fig

def crear_mapa_colombia(df_mapa):
    repo_url = 'https://raw.githubusercontent.com/marianofrizzera/colombia-geojson/master/colombia.geo.json'
    
    # Limpieza rápida: asegurar mayúsculas para que coincida con GeoJSON
    df_mapa['departamento'] = df_mapa['departamento'].str.upper().str.strip()
    
    fig = px.choropleth(
        df_mapa,
        geojson=repo_url,
        locations='departamento',
        featureidkey='properties.DPTO_CNMBRE',
        color='valor',
        color_continuous_scale="GnBu", # Escala Verde-Azul muy "Eco"
        scope="south america",
        title="Inversión por Departamento"
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0}, height=400)
    return fig