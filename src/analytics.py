import plotly.graph_objects as go
import plotly.express as px

def generar_gauge_inversion(valor_actual, meta):
    """Crea el velocímetro para la inversión ambiental."""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = valor_actual,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Inversión Ambiental Actual", 'font': {'size': 20, 'color': '#2E7D32'}},
        gauge = {
            'axis': {'range': [0, meta if meta > valor_actual else valor_actual * 1.1]},
            'bar': {'color': "#2E7D32"},
            'steps': [
                {'range': [0, meta * 0.5], 'color': "#f1f8e9"},
                {'range': [meta * 0.5, meta], 'color': "#c8e6c9"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': meta
            }
        }
    ))
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def generar_grafico_liderazgo(df):
    """Crea el gráfico de cuadrantes (Scatter Plot) con escala logarítmica."""
    if df.empty:
        return None
    
    avg_inv = df['inversion_total'].mean()
    avg_gasto = df['gasto_operativo'].mean()

    fig = px.scatter(
        df, 
        x="gasto_operativo", 
        y="inversion_total",
        size="indice_compromiso", 
        color="sector",
        hover_name="id_empresa",
        log_x=True, 
        log_y=True,
        title="Matriz de Desempeño: Inversión vs Gasto Operativo",
        labels={
            "gasto_operativo": "Gasto Operativo (Escala Log)",
            "inversion_total": "Inversión Ambiental (Escala Log)"
        },
        template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Safe
    )

    # Líneas de referencia (Promedios) para crear los cuadrantes
    fig.add_hline(y=avg_inv, line_dash="dot", annotation_text="Promedio Inv.", line_color="red")
    fig.add_vline(x=avg_gasto, line_dash="dot", annotation_text="Promedio Gasto", line_color="red")
    
    fig.update_layout(height=550, margin=dict(l=0, r=0, t=40, b=0))
    return fig

def generar_grafico_correlacion(df):
    """Gráfico de dispersión simple para la pestaña de hallazgos."""
    if df.empty: return None
    return px.scatter(df, x="inversion_total", y="gasto_operativo", color="sector", template="plotly_white")