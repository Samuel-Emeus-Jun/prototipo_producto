##ESTE ES NUESTRO MAIN 

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import plotly as plt
import plotly.express as px
from data_processing import limpiar_dataframe, mappear_df
from plot_generator import evaluacion_desempeño, generar_donas
from utils import generar_lista_de_colaboradores, cleanup_static

app = Flask(__name__, template_folder="../templates")

barras = {}
donas = {}
evaluaciones = {"general": {}, "anual": {}, "trimestral": {}}
texto = []

colaboradores = None
df_global = None

# Ruta principal para cargar el formulario
@app.route('/')
def upload_form():
    return render_template('upload.html')

# Ruta para procesar el archivo CSV (simulación por ahora)
@app.route('/upload', methods=['POST'])
def upload_file():
    global df_global, colaboradores, barras, donas, evaluaciones, texto
    # Verificar si hay un archivo en el formulario
    if 'file' not in request.files:
        return 'No se adjuntó ningún archivo'
    
    file = request.files['file']

    # Verificar que se seleccionó un archivo
    if file.filename == '':
        return 'No se seleccionó ningún archivo'

    # Verificar que el archivo sea un .csv
    if file and file.filename.endswith('.csv'):

        ##AQUI SE DEBE AGREGAR LA PANTALLA DE CARGA
        render_template('cargando.html')

        # Leer el archivo CSV directamente en un DataFrame
        df = pd.read_csv(file, header = [0,1])
        df_limpia = limpiar_dataframe(df)
        colaboradores = generar_lista_de_colaboradores(df_limpia)
        df_global = mappear_df(df_limpia)

        ##FUNCIÓN DE LIMPIEZA DE ARCHIVOS EN STATIC
        #cleanup_static()

        # GENERAR REPORTE GENERAL

        tipo_de_reporte = "general"
        servicios_minimos = 5

        ##FUNCIÓN DE BARRAS

        ##FUNCIÓN DONAS
        generar_donas(df_global, tipo_de_reporte)

        ##FUNCIÓN DE EVALUACIÓN DE DESEMPEÑO
        for colaborador in colaboradores:
            temp_df = df_global[df_global[colaborador] == colaborador]
            if len(temp_df) >= servicios_minimos:
                evaluacion_desempeño(temp_df, colaborador, tipo_de_reporte)

        ##FUNCIÓN DE TEXTO

        
        # Verificar si carga correctamente el archivo en un df
        #print(df)
            
        # REDIRIGE A REPORTE GENERAL
        return redirect(url_for('reporte_general'))
    
    return 'El archivo debe ser un archivo CSV (.csv)'


# Ruta para el Reporte General
@app.route('/general')
def reporte_general():
    global barras, donas, evaluaciones, texto, colaboradores
    print(donas, evaluaciones)
    
    return render_template('reporte_general.html',
                           tipo_de_reporte="general",
                           barras=barras,
                           donas=donas,
                           evaluaciones=evaluaciones,
                           texto=texto,
                           colaboradores=colaboradores)

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
