##LAS FUNCIONES PEQUEÑAS VAN AQUÍ 

import pandas as pd
from pathlib import Path

#Mostrar los encabezados con su índice. Es una función de guía para el desarrollo de este proyecto.
def encabezados_con_indice(df):
    return [(index, col) for index, col in enumerate(df.columns)]
    

#Mostrar los encabezados sin su índice. Es una función de guía para el desarrollo de este proyecto.
def encabezados_sin_indice(df):
    return [col for col in df.columns]


#Obtiene una lista con los nombres de los colaboradores. Se utiliza de forma dinámica para generar los diferentes reportes.
def generar_lista_de_colaboradores(df):
    return df.columns.get_level_values(1)[16:35+1].to_list()


##Obtiene una lista de los servicios brindados por la empresa. Esta lista se debe agrega manualmente a las funciones plot.
def generar_lista_de_servicios(df):
    return df.iloc[:, 14].value_counts().index.to_list()


##Función para limpiar la carpeta  'static' de archivos .html
def cleanup_static():
    """Limpia todos los archivos .html en el directorio static, incluyendo subcarpetas.
    Como el formato de este proyecto sobre escribe en static los archivos generados, no es implementado en la versión final."""
    for file_path in Path('static').rglob('*.html'):
        file_path.unlink()  # Elimina el archivo .html
    print("Archivos eliminados")  # Mensaje opcional para confirmar


lista_encabezados = [('respondent_id', 'Unnamed: 0_level_1'),
                     ('collector_id', 'Unnamed: 1_level_1'),
                     ('date_created', 'Unnamed: 2_level_1'), 
                     ('date_modified', 'Unnamed: 3_level_1'), 
                     ('ip_address', 'Unnamed: 4_level_1'), 
                     ('email_address', 'Unnamed: 5_level_1'), 
                     ('first_name', 'Unnamed: 6_level_1'), 
                     ('last_name', 'Unnamed: 7_level_1'), 
                     ('custom_1', 'Unnamed: 8_level_1'), 
                     ('Nombre', 'Open-Ended Response'), 
                     ('Compañía', 'Open-Ended Response'), 
                     ('Puesto', 'Open-Ended Response'), 
                     ('Correo Electrónico', 'Open-Ended Response'), 
                     ('Teléfono', 'Open-Ended Response'), 
                     ('¿Qué tipo de servicio te brindamos?', 'Response'), 
                     ('Unnamed: 15_level_0', 'Otro (especifique)'), 
                     ('Por favor, seleccione el o los ejecutivos que les asesoran', 'Ana Aguirre'), 
                     ('Unnamed: 17_level_0', 'Luis Castanedo'), ('Unnamed: 18_level_0', 'Paloma Ramos'), 
                     ('Unnamed: 19_level_0', 'Rodrigo Arciniegas'), 
                     ('Unnamed: 20_level_0', 'Juan Carlos Felix'), 
                     ('Unnamed: 21_level_0', 'Luis Cadena'), 
                     ('Unnamed: 22_level_0', 'Rosalba Falcon'), 
                     ('Unnamed: 23_level_0', 'Manuel Mares'), 
                     ('Unnamed: 24_level_0', 'Miguel Flores'), 
                     ('Unnamed: 25_level_0', 'Sergio Palafox'), 
                     ('Unnamed: 26_level_0', 'Laura Naima Juárez'), 
                     ('Unnamed: 27_level_0', 'Tania Belmonte'), 
                     ('Unnamed: 28_level_0', 'Ximena Robledo'), 
                     ('Unnamed: 29_level_0', 'Victor Manuel Salgado'), 
                     ('Unnamed: 30_level_0', 'Isaac Vallejo'), 
                     ('Unnamed: 31_level_0', 'Alonso Gallardo'), 
                     ('Unnamed: 32_level_0', 'Valeria Roqueñí'), 
                     ('Unnamed: 33_level_0', 'Abril Jasso'), 
                     ('Unnamed: 34_level_0', 'Cristian Chavez'), 
                     ('Unnamed: 35_level_0', 'Angel Hernandez'), 
                     ('Unnamed: 36_level_0', 'Otro (especifique)'), 
                     ('Nivel de Atención Recibida', '¿Cómo te atendimos?'), 
                     ('Unnamed: 38_level_0', '¿Qué tan profesionales fuimos?'), 
                     ('Unnamed: 39_level_0', '¿Nuestro tiempo de entrega fue?'), 
                     ('Unnamed: 40_level_0', '¿La calidad de nuestro servicio fue?'), 
                     ('Unnamed: 41_level_0', '¿La utilidad de nuestro servicio fue?'), 
                     ('¿Contratarías nuevamente nuestros servicios?', 'Response'), 
                     ('¿Recomendarías nuestros servicios?', 'Response'), 
                     ('¿Existe algo que podría ayudarnos a mejorar nuestro servicio?', 'Open-Ended Response'), 
                     ('Por favor, comparte un breve mensaje que podamos publicar en nuestras redes sociales', 'Open-Ended Response'), 
                     ('¿Qué tipo de servicio te brindamos? ', 'Response'), ('Unnamed: 47_level_0', 'Otro (especifique)'), 
                     ('Por favor, seleccione el o los ejecutivos que les asesoran', 'Ana Aguirre.1'), 
                     ('Unnamed: 49_level_0', 'Rosalba Falcón'), ('Unnamed: 50_level_0', 'Rodrigo Arciniegas'), 
                     ('Unnamed: 51_level_0', 'Fernanda Roqueñí'), ('Unnamed: 52_level_0', 'Otro (especifique)'), 
                     ('Nivel de Atención Recibida', '¿Cómo fue la atención de tu ejecutivo de cuenta?'), 
                     ('Unnamed: 54_level_0', '¿Qué tan profesional fue tu ejecutivo de cuenta?'), 
                     ('Unnamed: 55_level_0', '¿Cómo fue la calidad del servicio de tu ejecutivo?'), 
                     ('Unnamed: 56_level_0', '¿Cómo fue la calidad del servicio de tu ejecutivo?'), 
                     ('Unnamed: 57_level_0', '¿Cómo fueron los tiempos de implementación y entrega del servicio?'), 
                     ('Unnamed: 58_level_0', '¿Cómo evaluarías la efectividad de los entregables del servicio?'), 
                     ('¿Contratarías nuevamente nuestros servicios?', 'Response.1'), 
                     ('¿Recomendarías nuestros servicios?', 'Response.1'), 
                     ('¿Existe algo que podría ayudarnos a mejorar nuestro servicio?', 'Open-Ended Response.1'), 
                     ('Comparte como fue tu experiencia con tu ejecutivo de cuenta en la implementación del servicio.', 'Open-Ended Response'), 
                     ('Para finalizar, nos encantaría poder presentarlos como uno más de nuestros clientes; ¿nos autorizan poder usar el nombre comercial como parte de nuestra cartera de clientes?Esto solo es por fines de referencia de nuestros servicios. Nos comprometemos a siempre guardar la confidencialidad de la información de nuestros clientes y asociados comerciales.Si tienes alguna duda, por favor pueden consultar nuestro aviso de confidencialidad.www.catch.com.mx/aviso_de_privacidad_consulting', 'Response')]



##Solo para pruebas

def main():
    from data_processing import limpiar_dataframe, mappear_df
    df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])
    # df = limpiar_dataframe(df)
    #df_mappeada = mappear_df(df)
    # colaboradores = generar_lista_de_colaboradores(df)
    # servicios = generar_lista_de_servicios(df)

    print(encabezados_sin_indice(df))
    # print(servicios)

if __name__ == '__main__':
    main()