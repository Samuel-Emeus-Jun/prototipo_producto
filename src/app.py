##ESTE ES NUESTRO MAIN 

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import plotly as plt
import plotly.express as px
from data_processing import limpiar_dataframe, mappear_df
from plot_generator import evaluacion_desempeño
from utils import generar_lista_de_colaboradores

app = Flask(__name__)

barras = {"general": [], "anual": [], "trimestral": []}
donas = {"general": [], "anual": [], "trimestral": []}
evaluaciones = {"general": [], "anual": [], "trimestral": []}

colaboradores = None
df_global = None

# Ruta principal para cargar el formulario
@app.route('/')
def upload_form():
    return render_template('upload.html')

# Ruta para procesar el archivo CSV (simulación por ahora)
@app.route('/upload', methods=['POST'])
def upload_file():
    global df_global
    global colaboradores
    # Verificar si hay un archivo en el formulario
    if 'file' not in request.files:
        return 'No se adjuntó ningún archivo'
    
    file = request.files['file']

    # Verificar que se seleccionó un archivo
    if file.filename == '':
        return 'No se seleccionó ningún archivo'

    # Verificar que el archivo sea un .csv
    if file and file.filename.endswith('.csv'):
        # Leer el archivo CSV directamente en un DataFrame
        df = pd.read_csv(file)
        df_limpia = limpiar_dataframe(df)
        colaboradores = generar_lista_de_colaboradores(df_limpia)
        df_global = mappear_df(df_limpia)

        # Generar reporte general
        tipo_de_reporte = "general"
        servicios_minimos = 5
        ##FUNCIÓN DE BARRAS

        ##FUNCIÓN DE EVALUACIÓN DE DESEMPEÑO
        for colaborador in colaboradores:
            temp_df = df_global[df_global[colaborador] == colaborador]
            if len(temp_df) >= servicios_minimos:
                evaluacion_desempeño(temp_df, colaborador, tipo_de_reporte)
                

    


        
        # Verificar si carga correctamente el archivo en un df
        #print(df)
            
        # Continuar con el flujo de datos (por ahora solo redirigimos al reporte anual)
        return redirect(url_for('reporte_general'))
    
    return 'El archivo debe ser un archivo CSV (.csv)'


# Ruta para el Reporte General
@app.route('/general')
def reporte_general():
    ##print(evaluaciones)
    return render_template('reporte_general.html')

# Ruta para el Reporte Anual
@app.route('/anual')
def reporte_anual():
    return render_template('reporte_anual.html')

# Ruta para el Reporte Trimestral
@app.route('/trimestral')
def reporte_trimestral():
    return render_template('reporte_trimestral.html')

if __name__ == '__main__':
    app.run(debug=True)
