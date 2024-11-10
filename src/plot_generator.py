##AQUÍ VAMOS A HACER LAS FUNCIONES 
##PARA GENERAR GRÁFICOS

import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go



##DF PARA PRUEBAS

data = {
    "servicio": ["servicio 1", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1", "servicio 2", "servicio 1", "servicio 3", "servicio 1"],
    "colaborador_1": ["n/a", "n/a", "colaborador_1", "n/a", "colaborador_1", "n/a", "n/a", "n/a", "n/a", "colaborador_1", "n/a", "n/a",],
    "colaborador_2": ["n/a", "colaborador_2", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a", "n/a",],
    "colaborador_3": ["colaborador_3", "n/a", "colaborador_3", "n/a", "colaborador_3", "n/a", "n/a", "n/a", "colaborador_3", "n/a", "n/a", "n/a"],
    "colaborador_4": ["n/a", "colaborador_4", "n/a", "n/a", "colaborador_4", "colaborador_4", "n/a", "n/a", "n/a", "colaborador_4", "n/a", "n/a",],
    "calidad_servicio": [1, 5, 4, 4, 3, 4, 2, 4, 4, 3, 4, 2,],
    "velocidad_servicio": [4, 5, 4, 3, 3, 2, 2, 4, 5, 4, 3, 2,],
    "profesionalismo_servicio": [4, 2, 5, 3, 0, 2, 2, 5,3, 0, 2, 4,],
    "contacto_durante_servicio": [3, 2, 5, 4, 3, 2, 3, 5, 3, 2, 5, 4,],
}


df = pd.DataFrame(data)

marker_colors = {
    'servicio 1': "#0700de",
    'servicio 2': "#0085de",
    'servicio 3': "##00cbde",
}

fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]])



fig.add_trace(go.Pie(
    labels = df['servicio'].value_counts().index,
    values = df['servicio'].value_counts().values,
    name = "Servicio Brindado",
    hole = 0.3,
    textinfo = "percent+label",
    textposition = "inside",
    marker_colors = [marker_colors[servicio] for servicio in df['servicio'].value_counts().index]),
    row=1, col=2
    )

fig.update_layout(title_text="Servicios Brindados")

fig.show()