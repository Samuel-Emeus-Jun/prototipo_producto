##AQUÍ VAMOS A INSERTAR LAS FUNCIONES 
##DE PROCESAMIENTO DE DATOS
import pandas as pd

##TIMEDATE Completo 


##Limpieza general del DataFrame: Elimina filas con valores nulos en columnas 37 a 43, sin contar la 41, convierte la columna de fechas a formato que todos podamos leer, 
##ordena los valores de la columna 'Otro (especifique)' en los colaboradores correspondientes y genera columnas cuantitativas a partir de columnas cualitativas

def limpiar_dataframe(dataframe):
    
    df = dataframe
    ##Droppea las filas con valores nulos en las columnas 37 a 43, sin contar la 41
    df = df.dropna(subset=df.columns[37:40+1])
    df = df.dropna(subset=df.columns[42:43+1])
    #Convierte la columna de fechas a formato que todos podamos leer
    df['Fecha'] = pd.to_datetime(df.iloc[:, 3], format = 'mixed').dt.strftime('%d-%m-%Y')
    ##Ordenar los valores de la columna 'Otro (especifique)' en los colaboradores correspondientes
    otros_idx = 36 ##df.columns.get_loc(('Unnamed: 36_level_0', 'Otro (especifique)'))
    subheaders = df.columns.levels[1]
    for idx, row in df.iterrows():
        valor = row[otros_idx]
        if pd.notna(valor) and valor in subheaders:
            df.loc[idx, (slice(None), valor)] = valor
    ##Generar columnas cuantitativas a partir de columnas cualitativas
    map_dict = {"Pésimo" : 0, "Muy Malo" : 1, "Malo" : 3, "Regular - Malo" : 5,
                "Regular - Bueno" : 6, "Bueno" : 8, "Muy Bueno" : 9, "Excelente" : 10}
    df['Atención brindada'] = df.iloc[:, 37].map(map_dict)
    df['Profesionalismo'] = df.iloc[:, 38].map(map_dict)
    df['Tiempo de entrega'] = df.iloc[:, 39].map(map_dict)
    df['Calidad del producto'] = df.iloc[:, 40].map(map_dict)
    
    return df

def mappear_df(dataframe):

    mapped_df = pd.DataFrame()
    mapped_df = pd.concat([mapped_df, dataframe['Fecha']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe.iloc[:, 10].rename("Nombre de la Compañía")], axis =1)
    for col in dataframe.iloc[:, 16 : 35+1]:
        mapped_df = pd.concat([mapped_df, dataframe[col].rename(dataframe[col].name[1])], axis =1)
    # for col in dataframe.iloc[:, 37:40+1]:
    #     mapped_df = pd.concat([mapped_df, dataframe[col].rename(dataframe[col].name[1])], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe['Atención brindada']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe['Profesionalismo']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe['Tiempo de entrega']], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe['Calidad del producto']], axis =1)
    for col in dataframe.iloc[:, 42:43+1]:
        mapped_df = pd.concat([mapped_df, dataframe[col].rename(dataframe[col].name[1])], axis =1)
    mapped_df = pd.concat([mapped_df, dataframe.iloc[: , 44].rename("Comentarios")], axis =1)

    return mapped_df



##FIltrar df obtenido de limpiar_df a 12 meses    
def filtro_12_meses(): 
    return 0


##Filtrar df obtenido de limpiar_df a 3 meses
def filtro_3_meses():
    return 0



df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])



df = limpiar_dataframe(df)
df_mappeada = mappear_df(df)


##VISORES

#print(df.iloc[:, 3])
#print(df.iloc[:, 16].to_list())
#print(df['Fecha'])
#print(df.xs('Ana Aguirre', axis=1, level=1))
#print(df['Unnamed: 36_level_0']['Otro (especifique)'])
#print(colaboradores)