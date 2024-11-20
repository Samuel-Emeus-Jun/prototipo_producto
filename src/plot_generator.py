##AQUÍ VAMOS A HACER LAS FUNCIONES 
##PARA GENERAR GRÁFICOS

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px


##PRUEBA DE SUNBURST


# data = {
#     "servicio": ["servicio 1", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1"],
#     "aceptacion": ["si", "si", "si", "no", "si", "no", "si", "si", "si", "no", "si", "no"],
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

# df = pd.DataFrame(data)

# # Contamos las ocurrencias para cada combinación de 'aceptacion' y 'servicio'
# counts = df.groupby(["aceptacion", "servicio"]).size().reset_index(name="counts")

# # Definimos listas dinámicamente
# labels = ["Aceptación"]
# parents = [""]
# values = [len(df)]  # Total de respuestas

# # Añadimos el total de "Sí" como un solo nodo
# labels.append("Sí")
# parents.append("Aceptación")
# values.append(counts[counts["aceptacion"] == "si"]["counts"].sum())  # Total de "Sí"

# # Añadimos el nodo de "No" y sus detalles por servicio
# labels.append("No")
# parents.append("Aceptación")
# values.append(counts[counts["aceptacion"] == "no"]["counts"].sum())  # Total de "No"

# for servicio in counts[counts["aceptacion"] == "no"]["servicio"]:
#     labels.append(f"{servicio} (No)")
#     parents.append("No")
#     count_value = counts[(counts["aceptacion"] == "no") & (counts["servicio"] == servicio)]["counts"].values[0]
#     values.append(count_value)

# # Creamos el gráfico Sunburst
# fig = go.Figure(go.Sunburst(
#     labels=labels,
#     parents=parents,
#     values=values,
#     branchvalues="total"
# ))

# # Personalización del gráfico
# fig.update_layout(
#     title="Distribución de aceptación con desglose en 'No'",
#     margin=dict(t=40, l=0, r=0, b=0)
# )

# # Mostramos el gráfico
# fig.show()


##AQUÍ VA LA FUNCIÓN DE LA BARRA DE SERVICIOS


def generar_barra(dataframe, tipo_de_reporte, lista):
    """Esta función genera una gráfica de barras para conocer la distribución de servicios brindados por la empresa.
    Se utiliza plotly para generar la gráfica. se debe insertar el tipo de reporte que desea sea insertado en la gráfica y
    la lista donde se almacenarán los url de las gráficas realizadas"""	

    df = dataframe
    df_relevant = df[['servicio', 'Atención brindada', 'Profesionalismo', 'Tiempo de entrega', 'Calidad del producto']]

    # Calcular el conteo y los porcentajes de cada servicio
    service_counts_normalized = df_relevant['servicio'].value_counts(normalize=True) * 100
    service_counts = df_relevant['servicio'].value_counts()
    # Calcular promedios por servicio para las métricas
    service_means = df_relevant.groupby('servicio').mean()

    # Configuración de colores
    marker_colors_servicios = {
        'Encuesta de Mercado Laboral, Salarios, Estadísticos y Análisis de Mercado': "#31c4be",  # Cyan suave con un toque verde
        'Asesoría Legal': "#2b91a8",  # Azul intermedio con una pizca de verde
        'PAD Ponte al Día': "#0098a0",  # Cyan-azulado intenso
        'Desarrollo Organizacional': "#005c73",  # Azul oscuro con un tinte verde
        'Otro (especifique)': "#1d3a4a"  # Azul verdoso marino
    }

    # Crear trazas para cada servicio en la barra apilada
    fig = go.Figure()

    for servicio, porcentaje in service_counts_normalized.items():
        # Definir color del servicio
        color = marker_colors_servicios.get(servicio, "#D0E2F2")  # Color de respaldo
        
        # Agregar traza con hover personalizado para cada servicio
        fig.add_trace(
            go.Bar(
                y=["Servicios"],
                x=[porcentaje],
                name=servicio,
                orientation='h',
                marker=dict(color=color),
                hovertemplate=(
                    f"<b>{servicio}</b><br>" +
                    f"Porcentaje: {porcentaje:.2f}%<br>" +
                    f"Atención: {service_means.loc[servicio, 'Atención brindada']:.1f}<br>" +
                    f"Velocidad: {service_means.loc[servicio, 'Tiempo de entrega']:.1f}<br>" +
                    f"Profesionalismo: {service_means.loc[servicio, 'Profesionalismo']:.1f}<br>" +
                    f"Calidad: {service_means.loc[servicio, 'Calidad del producto']:.1f}<extra></extra>"
                ),
                width = 0.35,
                text = str(service_counts[servicio]),
                textposition = 'inside',
            )
        )

        # Personalizar la visualización para que solo sea la barra, sin ejes ni fondo
        fig.update_layout(
            title_text = f"Total de servicios brindados: {len(df)}",
            title_x = 0,
            title_y = 0.9,
            title_font = dict(size=24),
            barmode='stack',
            showlegend=True,
            legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            title_text="Servicios"
            ),           
            plot_bgcolor="white",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            margin=dict(l=0, r=0, t=20, b=20)
        )

    fig.show()
    #fig.write_html(f"static/{tipo_de_reporte}/barras/barra_{tipo_de_reporte}.html")
    #lista[tipo_de_reporte] = [f"{tipo_de_reporte}/barras/barra_{tipo_de_reporte}.html"]##REVISAR SUBCARPETAS


##AQUÍ VA LA FUNCIÓN DE EVALUACIÓN DE DESEMPEÑO


def evaluacion_desempeño(dataframe, colaborador, tipo_de_reporte, lista):
    """Esta función genera un reporte de desempeño para un colaborador en específico iterando a través de una lista 
    generada en utils.py. Se generan dos gráficas: una de barras stackeadas para las calificaciones y una de dona para
    los servicios brindados. Se utiliza plotly para generar las gráficas.
    Se debe inyectar una data base en formato de dataframe de pandas, el nombre del colaborador y el tipo de reporte, así como 
    la lista donde se almacenarán los url de las gráficas realizadas"""	 
    
    df = dataframe
    map_dict = {0: "Pésimo", 1: "Muy Malo", 3: "Malo", 5: "Regular - Malo",
                        6: "Regular - Bueno", 8: "Bueno", 9: "Muy Bueno", 10: "Excelente"}
    ##Diccionario de colores para las diferentes gráficas
    marker_colors_servicios = {
        'Encuesta de Mercado Laboral, Salarios, Estadísticos y Análisis de Mercado': "#31c4be",  # Cyan suave con un toque verde
        'Asesoría Legal': "#2b91a8",  # Azul intermedio con una pizca de verde
        'PAD Ponte al Día': "#0098a0",  # Cyan-azulado intenso
        'Desarrollo Organizacional': "#005c73",  # Azul oscuro con un tinte verde
        'Otro (especifique)': "#1d3a4a"  # Azul verdoso marino
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
        0: "#0a0c1a",  # Very dark navy blue (lowest score)
        1: "#1a2450",  # Darker navy blue
        3: "#2a3b70",  # Deep blue with more saturation
        5: "#3f5aa0",  # Medium navy with a hint of brightness
        6: "#31659b",  # Mid blue
        8: "#4b85d1",  # Bright blue for higher scores
        9: "#63a1e8",  # Light blue with high contrast
        10: "#82c6ff"  # Brightest blue (highest score)
    }


    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]], subplot_titles=("Evaluación de desempeño", "Distribución de servicios brindados"))

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
        cal_counts = df[col_name].value_counts().sort_index(ascending=False)
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

    
    ##Data extra para el menú hover
    df_relevant = df[['servicio', 'Atención brindada', 'Profesionalismo', 'Tiempo de entrega', 'Calidad del producto']]
    service_means = df_relevant.groupby('servicio').mean()

    # Generate `text` with metric info for each service
    labels_order = df['servicio'].value_counts().index  # Get services in the correct pie chart order
    hover_text = [
        f"Atención: {service_means.loc[servicio, 'Atención brindada']:.1f}<br>"
        f"Profesionalismo: {service_means.loc[servicio, 'Profesionalismo']:.1f}<br>"
        f"Velocidad: {service_means.loc[servicio, 'Tiempo de entrega']:.1f}<br>"
        f"Calidad: {service_means.loc[servicio, 'Calidad del producto']:.1f}"
        for servicio in labels_order
    ]

    # Define the pie chart using `text` for hover info
    fig.add_trace(go.Pie(
        labels=labels_order,
        values=df['servicio'].value_counts().values,
        name="Servicio Brindado",
        hole=0.7,
        text=hover_text,  # Set hover text directly
        textinfo="label+percent",  # Display label and percentage on the chart
        textposition="inside",
        showlegend=False,
        marker=dict(
            colors=[marker_colors_servicios[servicio] for servicio in labels_order],
            line=dict(color='white', width=1)
        ),
        textfont_size=12,
        domain=dict(x=[0.55, 0.95], y=[0.1, 0.9]),
        hovertemplate=(
            "<b>%{label}</b><br>" +
            "Total servicios: %{value}<br>" +
            "Porcentaje: %{percent}%<br>" +           
            "%{text}<extra></extra>"
        )  # Use text with pre-calculated metrics
    ), row=1, col=2)


    ##Se agrega la gráfica de dona para los servicios
    # fig.add_trace(go.Pie(
    #     labels=df['servicio'].value_counts().index,
    #     values=df['servicio'].value_counts().values,
    #     name="Servicio Brindado",
    #     hole=0.7,
    #     textinfo="label+percent",
    #     textposition="inside",
    #     showlegend=False,
    #     marker=dict(colors=[marker_colors_servicios[servicio] for servicio in df['servicio'].value_counts().index],
    #                 line=dict(color='white', width=1)),
    #     textfont_size=12,
    #     domain=dict(x=[0.55, 0.95], y=[0.1, 0.9])  # Control the size and position of the pie chart
    # ), row=1, col=2)

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
        hovermode = 'closest',
        autosize=True,
        uniformtext_minsize=8,
        uniformtext_mode='hide',)
        # annotations = [dict(text=f"Servicios totales: {len(df)}", x=sum(fig.get_subplot(1, 2).x) / 2, y=0.5,
        #     font_size=16, showarrow=False, xanchor="center")])

    fig.add_annotation(
        text=f"Total de<br>Servicios brindados:<br>{len(df)}",  # Text to display
        x=0.83, y=0.5,  # Coordinates for the pie chart
        xref='paper', yref='paper',
        font=dict(size=14, color="black"),
        showarrow=False
    )


    fig.show()
    #fig.write_html(f"static/{tipo_de_reporte}/evaluaciones/evaluacion_{tipo_de_reporte}_{colaborador}.html")
    #lista[tipo_de_reporte][colaborador] = [f"{tipo_de_reporte}/evaluaciones/evaluacion_{tipo_de_reporte}_{colaborador}.html"]##REVISAR SUBCARPETAS


##AQUÍ VA LA FUNCIÓN DE DONAS


def generar_donas(dataframe, tipo_de_reporte, lista):
    """Esta función genera una gráfica de pastel para conocer la aceptación de los clientes respecto a los servicios brindados.
    Se utiliza plotly para generar la gráfica que contienen dos subplots, cada uno haciendo referencia a las preguntas 
    '¿Contratarías nuevamente nuestros servicios?'y '¿Recomendarías nuestros servicios?'.
    Se debe inyectar una data base en formato de dataframe de pandas, el tipo de reporte que se desea realizar y la lista donde se almacenarán 
    los url de las gráficas realizadas"""	

    df = dataframe
    pastel_colors = {
         'Sí': "#326aa8",  # Azul corporativo
         'No': "#c93458"   # Color burgundy
    }

    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]], subplot_titles=("Contrataría Nuevamente", "Recomendaría Nuestros Servicios"))

    fig.add_trace(go.Pie(
        labels=df['¿Contratarías nuevamente nuestros servicios?'].value_counts().index,
        values=df['¿Contratarías nuevamente nuestros servicios?'].value_counts().values,
        name="Contrataría Nuevamente",
        hole=0.7,
        textinfo="percent+label",
        textposition="inside",
        showlegend=False,
        marker=dict(colors=[pastel_colors[respuesta] for respuesta in df['¿Contratarías nuevamente nuestros servicios?'].value_counts().index],
                    line=dict(color='white', width=1)),
        textfont_size=12,
        domain=dict(x=[0.0, 0.45], y=[0.1, 0.9])  # Control the size and position of the first pie chart
    ), row=1, col=1)

    
    fig.add_trace(go.Pie(
        labels=df['¿Recomendarías nuestros servicios?'].value_counts().index,
        values=df['¿Recomendarías nuestros servicios?'].value_counts().values,
        name="Recomendaría Nuestros Servicios",
        hole=0.7,
        textinfo="percent+label",
        textposition="inside",
        showlegend=True,
        marker=dict(colors=[pastel_colors[respuesta] for respuesta in df['¿Recomendarías nuestros servicios?'].value_counts().index],
                    line=dict(color='white', width=1)),
        textfont_size=12,
        domain=dict(x=[0.55, 1.0], y=[0.1, 0.9])  # Control the size and position of the second pie chart
    ), row=1, col=2)
        
    fig.update_layout(
        title_text = f"Percepción {tipo_de_reporte} de nuestros clientes",
        title_x = 0,
        title_font = dict(size=24),
        legend=dict(
            title="Respuestas",
            orientation="h",
            yanchor="top",
            y=0.01,
            xanchor="center",
            x=0.5,
            bgcolor="rgba(255, 255, 255, 0.5)"
        ),
        autosize=True,
        uniformtext_minsize=8,
        uniformtext_mode='hide',
    )
    #fig.show()
    fig.write_html(f"static/{tipo_de_reporte}/donas/donas_{tipo_de_reporte}.html")
    lista[tipo_de_reporte] = f"{tipo_de_reporte}/donas/donas_{tipo_de_reporte}.html"#REVISAR SUBCARPETAS

#barras = {}
# donas = {}
evaluaciones = {"general": {}, "anual": {}, "trimestral": {}}
# texto = []

def main():
    from data_processing import limpiar_dataframe, mappear_df
    from utils import generar_lista_de_colaboradores
    df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])
    df = limpiar_dataframe(df)
    colaboradores = generar_lista_de_colaboradores(df)
    df_mappeada = mappear_df(df)

    servicios_minimos = 5
    tipo_de_reporte = "general"

    # for colaborador in colaboradores:
    #         temp_df = df_mappeada[df_mappeada[colaborador] == colaborador]
    #         if len(temp_df) >= servicios_minimos:
    #             evaluacion_desempeño(temp_df, colaborador, tipo_de_reporte)

    # print(evaluaciones)    
    # print(len(evaluaciones["general"]))
    # generar_donas(df_mappeada, "general")
    # print(donas)

    colaborador = "Ana Aguirre"
    temp_df = df_mappeada[df_mappeada[colaborador] == colaborador]
    evaluacion_desempeño(temp_df, colaborador, tipo_de_reporte, evaluaciones)

    ##generar_barra(df_mappeada, "general", barras)

if __name__ == '__main__':
    main()