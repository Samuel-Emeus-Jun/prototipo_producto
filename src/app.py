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
    # Por ahora, solo simulamos que se subió un archivo correctamente
    # En el futuro, aquí procesaremos el archivo
    return redirect(url_for('reporte_general'))

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
