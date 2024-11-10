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

for col_name in df.columns[5:8+1]:

    promedio = df[col_name].mean()
    cal_counts = df[col_name].value_counts()
    cal_lista = cal_counts.index.to_list()
    porcentajes = (cal_counts/len(df))*100

    for cal, percent in zip(cal_lista, porcentajes):
        etiqueta_cualitativa = map_dict.get(cal, " ")
        fig.add_trace(go.Bar(
            x = [percent],
            y = [col_name],
            name = etiqueta_cualitativa,
            hoverinfo = 'text',
            marker_color = marker_colors_calificaciones.get(cal, "gray"),
            orientation = 'h',
            text = f'{etiqueta_cualitativa}: {percent:.2f}%',
            #textposition = 'inside',

        ), row=1, col=1)

    fig.add_trace(go.Bar(
        x = [promedio],
        y = [col_name],
        name = col_name,
        marker_color = 'blue',
        orientation = 'h',
        base = 0,
    ), row=1, col=1)
    


    # fig.add_trace(go.Bar(
    #     x = [promedio],
    #     y = [col_name],
    #     name = col_name,
    #     marker_color = 'blue',
    #     orientation = 'h',
    # ), row=1, col=1)

    # for cal, percent in zip(cal_lista, porcentajes):
    #     etiqueta_cualitativa = map_dict.get(cal, " ")
    #     fig.add_trace(go.Bar(
    #         x = [percent],
    #         y = [col_name],
    #         name = etiqueta_cualitativa,
    #         hoverinfo = 'text',
    #         marker_color = marker_colors_calificaciones.get(cal, "gray"),
    #         orientation = 'h',
    #         text = f'{etiqueta_cualitativa}: {percent:.2f}%',
    #         #textposition = 'inside',

    #     ), row=1, col=1)


fig.add_trace(go.Pie(
    labels = df['servicio'].value_counts().index,
    values = df['servicio'].value_counts().values,
    name = "Servicio Brindado",
    hole = 0.3,
    textinfo = "percent+label",
    textposition = "inside",
    marker_colors = [marker_colors_servicios[servicio] for servicio in df['servicio'].value_counts().index]),
    row=1, col=2
    )

fig.update_layout(
    title_text="Promedio de Calificaciones por Servicio y Servicios brindados",
    yaxis = dict(title= 'Promedios de Calificaciones \ Servicios Brindados'),
    barmode='stack',
    showlegend=False,
)

fig.show()

