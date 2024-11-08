##AQUÍ VAMOS A INSERTAR LAS FUNCIONES 
##DE PROCESAMIENTO DE DATOS
import pandas as pd

def unir_string_headers():
    df.columns = [
        f"{str(col1).strip()}_{str(col2).strip()}" if pd.notna(col1) and pd.notna(col2)
        else str(col1) if pd.notna(col1)
        else str(col2)
        for col1, col2 in df.columns
    ]


##Mostrar el DataFrame con los encabezados más legibles
#print(df.head())

##Mostrar los encabezados con su índice
# headers_with_index = [(index, col) for index, col in enumerate(df.columns)]
# headers = [col for col in df.columns]
# print(headers_with_index)
# print(headers)


###GRIT 150: Funciones para limpieza tosca del df

#Funcion para droppear filas con valores nulos
def grit_150(dataframe):

    ##Droppea las filas con valores nulos en las columnas 37 a 43, sin contar la 41
    df = dataframe.dropna(subset=dataframe.columns[37:40+1])
    df = dataframe.dropna(subset=dataframe.columns[42:43+1])
    #Convierte la columna de fechas a formato que todos podamos leer
    df['Fecha'] = pd.to_datetime(dataframe.iloc[:, 3], format = 'mixed').dt.strftime('%d-%m-%Y')
    ##Intento de Melt para ordenar los valores de la columna 'Otro (especifique)'
    otros_idx = df.columns.get_loc(('Unnamed: 36_level_0', 'Otro (especifique)'))
    subheaders = df.columns.levels[1]
    for idx, row in df.iterrows():
        valor = row[otros_idx]
        if pd.notna(valor) and valor in subheaders:
            df.loc[idx, (slice(None), valor)] = valor
    ##Convertir columnas cualitativas a cuantitativas
    

    return df
    

df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])

#unir_string_headers()
colaboradores = df.columns.get_level_values(1)[16:35+1].to_list()
df = grit_150(df)


##VISORES

#print(df.iloc[:, 3])
#print(df.iloc[:, 16].to_list())
#print(df['Fecha'])
#print(df.xs('Ana Aguirre', axis=1, level=1))
#print(df['Unnamed: 36_level_0']['Otro (especifique)'])
print(colaboradores)