##LAS FUNCIONES PEQUEÑAS 
##VAN AQUÍ 
import pandas as pd
#Mostrar los encabezados con su índice. Es una función de guía para el desarrollo de este proyecto.
def encabezados_con_indice(df):
    return [(index, col) for index, col in enumerate(df.columns)]
    
#Mostrar los encabezados sin su índice. Es una función de guía para el desarrollo de este proyecto.
def encabezados_sin_indice(df):
    return [col for col in df.columns]

#Obtiene una lista con los nombres de los colaboradores. Se utiliza de forma dinámica para generar los diferentes reportes.
def generar_lista_de_colaboradores(df):
    return df.columns.get_level_values(1)[16:35+1].to_list()

def generar_lista_de_servicios(df):
    return df.iloc[:, 14].value_counts().index.to_list()

def main():
    from data_processing import limpiar_dataframe, mappear_df
    df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])
    df = limpiar_dataframe(df)
    df_mappeada = mappear_df(df)
    colaboradores = generar_lista_de_colaboradores(df)
    servicios = generar_lista_de_servicios(df)

    print(servicios)

if __name__ == '__main__':
    main()


