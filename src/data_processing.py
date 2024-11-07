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

    
    df = dataframe.dropna(subset=dataframe.columns[37:40+1])
    df = dataframe.dropna(subset=dataframe.columns[42:43+1])
    #dataframe.iloc[:, 3] = pd.to_datetime(dataframe.iloc[:, 3], errors='coerce')
    df['Fecha'] = pd.to_datetime(dataframe.iloc[:, 3], format = 'mixed', dayfirst = False).dt.date

    return df
    

df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])

unir_string_headers()
df = grit_150(df)

print(df.iloc[:, 3])
print(df['Fecha'])
