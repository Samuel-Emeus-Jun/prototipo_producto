##ESTE ES NUESTRO MAIN 

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import plotly as plt
import plotly.express as px


app = Flask(__name__)



# Ruta principal para cargar el formulario
@app.route('/')
def upload_form():
    return render_template('upload.html')

# Ruta para procesar el archivo CSV (simulación por ahora)
@app.route('/upload', methods=['POST'])
def upload_file():
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
        
        # Verificar si carga correctamente el archivo en un df
        #print(df)
            
        # Continuar con el flujo de datos (por ahora solo redirigimos al reporte anual)
        return redirect(url_for('reporte_general'))
    
    return 'El archivo debe ser un archivo CSV (.csv)'


# Ruta para el Reporte General
@app.route('/general')
def reporte_general():
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
