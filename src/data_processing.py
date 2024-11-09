##AQUÍ VAMOS A INSERTAR LAS FUNCIONES 
##DE PROCESAMIENTO DE DATOS
import pandas as pd
from tabulate import tabulate
from datetime import datetime
from dateutil.relativedelta import relativedelta

##TIMEDATE Completo 


##Limpieza general del DataFrame: Elimina filas con valores nulos en columnas 37 a 43, sin contar la 41, convierte la columna de fechas a formato que todos podamos leer, 
##ordena los valores de la columna 'Otro (especifique)' en los colaboradores correspondientes y genera columnas cuantitativas a partir de columnas cualitativas

def limpiar_dataframe(dataframe):
    #Droppea las filas con valores nulos en las columnas 37 a 43, sin contar la 41
    df=dataframe
    df = df.dropna(subset=df.columns[37:40+1])
    df = df.dropna(subset=df.columns[42:43+1])
    #Crea la columna de fechas y cambia de tipo <object> a <datetime> para hacer operaciones con fechas
    df['Fecha'] = pd.to_datetime(dataframe.iloc[:, 3], format='mixed')
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
    df['Atencion'] = df.iloc[:, 37].map(map_dict)
    df['Profesionalismo'] = df.iloc[:, 38].map(map_dict)
    df['Tiempo de Entrega'] = df.iloc[:, 39].map(map_dict)
    df['Calidad del Producto'] = df.iloc[:, 40].map(map_dict)
    return df


##FIltrar df obtenido de limpiar_df a 12 meses   
def filtro_12_meses(df_general): 
    #Establecer la fecha límite para filtrar los datos
    fecha_limite = datetime.now() - relativedelta(months=12)
    #Filtrar los datos de la columna 'Fecha' mayores a la fecha límite
    df_last_12_moths=df_general[df_general['Fecha'] > fecha_limite]
    #Imprimir las últimas 5 columnas del DataFrame *Pura vista, no va a estar en el código final*
    print(df_last_12_moths.iloc[:, -5:])
    return df_last_12_moths

##Filtrar df obtenido de limpiar_df a 3 meses
def filtro_3_meses(df_general):
    #Establecer la fecha límite para filtrar los datos
    fecha_limite = datetime.now() - relativedelta(months=3)
    #Filtrar los datos de la columna 'Fecha' mayores a la fecha límite
    df_last_3_months=df_general[df_general['Fecha'] > fecha_limite]
    #Imprimir las últimas 5 columnas del DataFrame *Pura vista, no va a estar en el código final*
    print(df_last_3_months.iloc[:, -5:])
    return df_last_3_months

df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])
df=limpiar_dataframe(df)

print(df.iloc[:, -5:])
filtro_12_meses(limpiar_dataframe(df))
filtro_3_meses(limpiar_dataframe(df))

#Imprimir las últimas 5 columnas del dataframe para corroborar la correcta inserción de los datos generados


##VISORES

#print(df.iloc[:, 3])
#print(df.iloc[:, 16].to_list())
#print(df['Fecha'])

#print(df.xs('Ana Aguirre', axis=1, level=1))
#print(df['Unnamed: 36_level_0']['Otro (especifique)'])
#print(colaboradores)
#print(tabulate(df, tablefmt='psql'))