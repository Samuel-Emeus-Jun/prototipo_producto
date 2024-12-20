##AQUÍ VAMOS A INSERTAR LAS FUNCIONES DE PROCESAMIENTO DE DATOS
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


##Función para limpiar el DataFrame

def limpiar_dataframe(dataframe):

    ##Limpieza general del DataFrame: Elimina filas con valores nulos en columnas 37 a 43, sin contar la 41, convierte la columna de fechas a formato que todos podamos leer, 
    ##ordena los valores de la columna 'Otro (especifique)' en los colaboradores correspondientes y genera columnas cuantitativas a partir de columnas cualitativas

    df = dataframe

    ##Droppea las filas con valores nulos en las columnas 37 a 43, sin contar la 41
    df = df.dropna(subset=df.columns[37:40+1])
    df = df.dropna(subset=df.columns[42:43+1])

    #Convierte la columna de fechas a formato que todos podamos leer
    df['Fecha'] = pd.to_datetime(df.iloc[:, 3], format = 'mixed')##.dt.strftime('%d-%m-%Y')

    ##Ordenar los valores de la columna 'Otro (especifique)' en los colaboradores correspondientes
    otros_idx = 36 ##df.columns.get_loc(('Unnamed: 36_level_0', 'Otro (especifique)'))
    subheaders = df.columns.levels[1]
    for idx, row in df.iterrows():
        valor = row[otros_idx]
        if pd.notna(valor) and valor in subheaders:
            df.loc[idx, (slice(None), valor)] = valor
    
    ##Generar columnas cuantitativas a partir de columnas cualitativas
    map_dict = {"Pésimo" : 0, "Muy Malo" : 1, "Malo" : 3, "Regular - Malo" : 5,
                "Regular - Bueno" : 6, "Bueno" : 8, "Muy Bueno" : 9, "Excelente" : 10} ##Mapeo de calificaciones cualitativas a cuantitativas
    df['Atención brindada'] = df.iloc[:, 37].map(map_dict)
    df['Profesionalismo'] = df.iloc[:, 38].map(map_dict)
    df['Tiempo de entrega'] = df.iloc[:, 39].map(map_dict)
    df['Calidad del producto'] = df.iloc[:, 40].map(map_dict)
    
    return df


##Función para mapear el DataFrame

def mappear_df(dataframe):

    ##Función creada para obtener un df mas limpio, de mas fácil acceso a las columnas y  
    ##disminuir la cantidad de data que será procesada en plot_generator.py

    mapped_df = pd.DataFrame()
    mapped_df = pd.concat([mapped_df, dataframe['Fecha']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe.iloc[:, 10].rename("Nombre de la Compañía")], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe.iloc[:, 14].rename("servicio")], axis =1)

    ##Esto es para agregar a los colaboradores
    for col in dataframe.iloc[:, 16 : 35+1]:
        mapped_df = pd.concat([mapped_df, dataframe[col].rename(dataframe[col].name[1])], axis =1)

    ##Aquí también se puede agregar las calificaciones cualitativas   
    # for col in dataframe.iloc[:, 37:40+1]:
    #     mapped_df = pd.concat([mapped_df, dataframe[col].rename(dataframe[col].name[1])], axis =1)

    ##Se agregan las calificaciones cuantitativas
    mapped_df = pd.concat([mapped_df, dataframe['Atención brindada']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe['Profesionalismo']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe['Tiempo de entrega']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe['Calidad del producto']], axis =1)

    ##Se agregan las columnas de opiniones
    for col in dataframe.iloc[:, 42:43+1]:
        mapped_df = pd.concat([mapped_df, dataframe[col].rename(dataframe[col].name[0])], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe.iloc[: , 44].rename("Comentarios")], axis =1)

    return mapped_df


##Función para cortar el DataFrame a un lapso de tiempo determinado

def cortar_dataframe(dataframe, lapso):
    ##Función para cortar el dataframe a un lapso de tiempo determinado

    #Establecer la fecha límite para filtrar los datos
    fecha_limite = datetime.now() - relativedelta(months=lapso)

    #Filtrar los datos de la columna 'Fecha' mayores a la fecha límite
    return dataframe[dataframe['Fecha'] > fecha_limite]


##FIltrar df obtenido de limpiar_df a 12 meses    
def filtro_12_meses(df_general): 
    #Establecer la fecha límite para filtrar los datos
    fecha_limite = datetime.now() - relativedelta(months=12)
    #Filtrar los datos de la columna 'Fecha' mayores a la fecha límite
    df_last_3_months=df_general[df_general['Fecha'] > fecha_limite]


##Filtrar df obtenido de limpiar_df a 3 meses
def filtro_3_meses(df_general):
    #Establecer la fecha límite para filtrar los datos.
    fecha_limite = datetime.now() - relativedelta(months=3)
    #Filtrar los datos de la columna 'Fecha' mayores a la fecha límite
    df_last_3_months=df_general[df_general['Fecha'] > fecha_limite]



# df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])



# df = limpiar_dataframe(df)
# df_mappeada = mappear_df(df)


def main():
    df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])
    df = limpiar_dataframe(df)
    df_mappeada = mappear_df(df)

    lapso = 12

    df_recortado = cortar_dataframe(df_mappeada, lapso)
    print(df_recortado)

if __name__ == '__main__':
    main()
    
##VISORES

#print(df.iloc[:, 3])
#print(df.iloc[:, 16].to_list())
#print(df['Fecha'])
#print(df.xs('Ana Aguirre', axis=1, level=1))
#print(df['Unnamed: 36_level_0']['Otro (especifique)'])
#print(colaboradores)
##print(df_mappeada.columns)
##SORRY, TODAVÍA NO SABÍA USAR MAIN##