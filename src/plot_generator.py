##AQUÍ VAMOS A HACER LAS FUNCIONES 
##PARA GENERAR GRÁFICOS

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

##DF PARA PRUEBAS

# data = {
#     "servicio": ["servicio 1", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1"],
#     "colaborador_1": ["n/a", "n/a", "colaborador_1", "n/a", "colaborador_1", "n/a", "n/a", "n/a", "n/a", "colaborador_1", "n/a", "n/a",],
#     "colaborador_2": ["n/a", "colaborador_2", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a",],
#     "colaborador_3": ["colaborador_3", "n/a", "colaborador_3", "n/a", "colaborador_3", "n/a", "n/a", "n/a", "colaborador_3", "n/a", "n/a", "n/a"],
#     "colaborador_4": ["n/a", "colaborador_4", "n/a", "n/a", "colaborador_4", "colaborador_4", "n/a", "n/a", "n/a", "colaborador_4", "n/a", "n/a",],
#     "atencion_servicio": [1, 5, 4, 4, 3, 4, 2, 4, 4, 3, 4, 2,],
#     "velocidad_servicio": [4, 5, 4, 3, 3, 2, 2, 4, 5, 4, 3, 2,],
#     "profesionalismo_servicio": [4, 2, 5, 3, 0, 2, 2, 5,3, 0, 2, 4,],
#     "calidad_servicio": [3, 2, 5, 4, 3, 2, 3, 5, 3, 2, 5, 4,],
# }



# map_dict = {0: "Pésimo" , 1: "Malo", 2: "Regular", 3: "Bueno", 4: "Muy Bueno", 5: "Excelente"}
            
# df['Atencion'] = df['atencion_servicio'].map(map_dict)
# df['Profesionalismo'] = df['profesionalismo_servicio'].map(map_dict)
# df['Tiempo de Entrega'] = df["velocidad_servicio"].map(map_dict)
# df['Calidad del Producto'] = df["calidad_servicio"].map(map_dict)

##AQUÍ VA A EMPEZAR LA FUNCIÓN 
def evaluacion_desempeño(dataframe, colaborador, tipo_de_reporte):
    """Esta función genera un reporte de desempeño para un colaborador en específico iterando a través de una lista 
    generada en utils.py. Se generan dos gráficas: una de barras stackeadas para las calificaciones y una de dona para
    los servicios brindados. Se utiliza plotly para generar las gráficas.
    Se debe inyectar una data base en formato de dataframe de pandas, el nombre del colaborador y el tipo de reporte."""	 
        
    df = dataframe
    map_dict = {0: "Pésimo" , 1: "Malo", 2: "Regular", 3: "Bueno", 4: "Muy Bueno", 5: "Excelente"}
    ##Diccionario de colores para las diferentes gráficas
    marker_colors_servicios = {
        'servicio 1': "#1E3A5F",  # Azul oscuro
        'servicio 2': "#4B78A3",  # Azul medio
        'servicio 3': "#7FA5D0",  # Azul claro
        'servicio 4': "#9B4D98",  # Morado suave
        'servicio 5': "#A3B8D8",  # Azul claro grisáceo
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
        0: "#D0E2F2",  # Azul muy claro
        1: "#7FA5D0",  # Azul claro
        3: "#A3B8D8",  # Azul grisáceo
        5: "#4B78A3",  # Azul medio
        6: "#9B4D98",  # Morado suave
        8: "#1E3A5F",  # Azul oscuro
        9: "#5A2A8C",  # Azul oscuro con matiz morado
        10: "#274466"   # Azul marino
    }


    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]])

    promedios = df.mean(numeric_only=True)

    ##Se agrega la barra de promedios. Esta sirve como base para las barras stackeadas
    ##Se genera una lista de las columnas a iterar de forma manual 
    columnas_iteradas = ["Atención brindada", "Profesionalismo", "Tiempo de entrega", "Calidad del producto"]
    for col_name in columnas_iteradas:

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
            width = 0.1, ##Truco para que funcione el hover de las barras apiladas
            opacity = 0.85,
        ), row=1, col=1)

    ##Se generan las categorias existentes para la leyenda    
    categorias_mostradas = set()

    ##Se calculan las barras stackeadas; se settea la base como 0 para que se vayan sumando las barras
    for col_name in columnas_iteradas:
        cal_counts = df[col_name].value_counts().sort_index()
        cal_lista = cal_counts.index.to_list()
        base = 0 

    ##Se genera una etiqueta cualitativa para las calificaciones y se calcula la altura de la barras. Se agregan las categorias al set de la leyenda
        for cal, count in cal_counts.items():
            percent =(count/len(df))*100
            altura_barra = (percent/100)*promedios[col_name]
            etiqueta_cualitativa = map_dict.get(cal, " ")
            showlegend = False if cal in categorias_mostradas else True
            categorias_mostradas.add(cal)  

    ##Se agregan las barras stackeadas
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

            base += altura_barra ##Aquí se van sumando las alturas de las barras

    ##Se mofifican las anotaciones de los ejes
    fig.update_yaxes(title_text="Metricas Aplicadas", row=1, col=1)
    fig.update_xaxes(title_text="Promedio de las Calificaciones", row=1, col=1)

    ##Se agregan subtítulos a los gráficos. Esto es un mess.
    fig.add_annotation(
        x = 0.1, y = -0.1, xref =  'paper', yref = 'paper', text = "Evaluación de los servicios brindados",
        showarrow=False, font=dict(size=16, color="black"))

    ##Se agrega la gráfica de dona para los servicios
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

    ##Se agregan subtítulos a los gráficos. Esto es un mess.
    fig.add_annotation(
        x = 0.85, y = -0.1 , xref = 'paper', yref = 'paper', text = "Distribución de los servicios brindados",
        showarrow=False, font=dict(size=16, color="black"))

    ##Ajuste de tamaño de la gráfica de dona
    fig.update_traces(textfont_size=12, marker=dict(line=dict(color='white', width=1)),
        domain=dict(x=[0.55, 0.95], y=[0.1, 0.9]), row=1, col=2)

    ##Se agregan las leyendas y se stackean las barras
    fig.update_layout(
        title_text=f"Evaluación de desempeño {tipo_de_reporte}: {colaborador}",
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