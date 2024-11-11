##AQUÍ VAMOS A HACER LAS FUNCIONES 
##PARA GENERAR GRÁFICOS

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

##DF PARA PRUEBAS

data = {
    "servicio": ["servicio 1", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1"],
    "colaborador_1": ["n/a", "n/a", "colaborador_1", "n/a", "colaborador_1", "n/a", "n/a", "n/a", "n/a", "colaborador_1", "n/a", "n/a",],
    "colaborador_2": ["n/a", "colaborador_2", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a",],
    "colaborador_3": ["colaborador_3", "n/a", "colaborador_3", "n/a", "colaborador_3", "n/a", "n/a", "n/a", "colaborador_3", "n/a", "n/a", "n/a"],
    "colaborador_4": ["n/a", "colaborador_4", "n/a", "n/a", "colaborador_4", "colaborador_4", "n/a", "n/a", "n/a", "colaborador_4", "n/a", "n/a",],
    "atencion_servicio": [1, 5, 4, 4, 3, 4, 2, 4, 4, 3, 4, 2,],
    "velocidad_servicio": [4, 5, 4, 3, 3, 2, 2, 4, 5, 4, 3, 2,],
    "profesionalismo_servicio": [4, 2, 5, 3, 0, 2, 2, 5,3, 0, 2, 4,],
    "calidad_servicio": [3, 2, 5, 4, 3, 2, 3, 5, 3, 2, 5, 4,],
}

df = pd.DataFrame(data)

map_dict = {0: "Pésimo" , 1: "Malo", 2: "Regular", 3: "Bueno", 4: "Muy Bueno", 5: "Excelente"}
            
df['Atencion'] = df['atencion_servicio'].map(map_dict)
df['Profesionalismo'] = df['profesionalismo_servicio'].map(map_dict)
df['Tiempo de Entrega'] = df["velocidad_servicio"].map(map_dict)
df['Calidad del Producto'] = df["calidad_servicio"].map(map_dict)

marker_colors_servicios = {
    'servicio 1': "#0700de",
    'servicio 2': "#0085de",
    'servicio 3': "##00cbde",
}

# marker_colors_calificaciones = {
#     "Pésimo" : "#ff0000",
#     "Malo" : "#ff8000",
#     "Regular" : "#ffbf00",
#     "Bueno" : "#80ff00",
#     "Muy Bueno" : "#00ff00",
#     "Excelente" : "#00ff80",
# }


marker_colors_calificaciones = {
    0 : "#ff0000",
    1 : "#ff8000",
    2 : "#ffbf00",
    3 : "#80ff00",
    4 : "#00ff00",
    5 : "#00ff80",
}


fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]])

promedios = df.mean(numeric_only=True)

for col_name in df.columns[5:8+1]:

    promedio = df[col_name].mean()
    fig.add_trace(go.Bar(
        y = [col_name],
        x = [promedio],
        name = f'Promedio {col_name}',
        marker_color = 'light gray',
        orientation = 'h',
        base = 0,
        text = f'{promedio:.2f}',
        textposition = 'outside',
        hoverinfo = 'none',
        showlegend=False,
        width = 0.1,
        opacity = 0.85,
    ), row=1, col=1)
    
categorias_mostradas = set()

for col_name in df.columns[5:8+1]:
    cal_counts = df[col_name].value_counts().sort_index()
    cal_lista = cal_counts.index.to_list()
    base = 0 

    for cal, count in cal_counts.items():
        percent =(count/len(df))*100
        altura_barra = (percent/100)*promedios[col_name]
        etiqueta_cualitativa = map_dict.get(cal, " ")
        showlegend = False if cal in categorias_mostradas else True
        categorias_mostradas.add(cal)  

        fig.add_trace(go.Bar(
            x = [altura_barra],
            y = [col_name],
            name = etiqueta_cualitativa,
            hovertemplate = f"Calificación: {etiqueta_cualitativa}<br>Porcentaje: {percent:.2f}%",
            hoverinfo = 'text',
            marker_color = marker_colors_calificaciones.get(cal, "gray"),
            orientation = 'h',
            text = f'{etiqueta_cualitativa}: {percent:.2f}%',
            textposition = 'none',
            showlegend= showlegend,
            base = base,
            width = 0.35,
            ), row=1, col=1)

        base += altura_barra

fig.update_yaxes(title_text="Metricas Aplicadas", row=1, col=1)
fig.update_xaxes(title_text="Promedio de las Calificaciones", row=1, col=1)

fig.add_annotation(
    x = 0.1, y = -0.1, xref =  'paper', yref = 'paper', text = "Evaluación de los servicios brindados",
    showarrow=False, font=dict(size=16, color="black"))

fig.add_trace(go.Pie(
    labels = df['servicio'].value_counts().index,
    values = df['servicio'].value_counts().values,
    name = "Servicio Brindado",
    hole = 0.7,
    textinfo = "percent+label",
    textposition = "inside",
    showlegend= False,
    marker_colors = [marker_colors_servicios[servicio] for servicio in df['servicio'].value_counts().index]),
    row=1, col=2
    )

fig.add_annotation(
    x = 0.85, y = -0.1 , xref = 'paper', yref = 'paper', text = "Distribución de los servicios brindados",
    showarrow=False, font=dict(size=16, color="black"))

fig.update_traces(textfont_size=12, marker=dict(line=dict(color='white', width=1)),
    domain=dict(x=[0.55, 0.95], y=[0.1, 0.9]), row=1, col=2)

fig.update_layout(
    title_text="Evaluación de desempeño de los colaboradores",
    title_x = 0,
    title_font = dict(size=24),
    legend=dict(
        title="Calificaciones",
        orientation="v",
        yanchor="top",
        y=0.2,
        xanchor="left",
        x=0.47,
        bgcolor="rgba(255, 255, 255, 0.5)"
    ),
    bargap = 0.1,
    bargroupgap = 0.1,
    legend_traceorder = 'normal',
    barmode='stack',
    showlegend=True,
    hovermode = 'closest'
)

fig.show()