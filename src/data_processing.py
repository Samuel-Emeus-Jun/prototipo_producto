##AQUÍ VAMOS A INSERTAR LAS FUNCIONES 
##DE PROCESAMIENTO DE DATOS
import pandas as pd

df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])


df.columns = [
    f"{str(col1).strip()}_{str(col2).strip()}" if pd.notna(col1) and pd.notna(col2)
    else str(col1) if pd.notna(col1)
    else str(col2)
    for col1, col2 in df.columns
]

##Mostrar el DataFrame con los encabezados más legibles
##print(df.head())

##Mostrar los encabezados con su índice

headers_with_index = [(index, col) for index, col in enumerate(df.columns)]
headers = [col for col in df.columns]
print(headers_with_index)
print(headers)