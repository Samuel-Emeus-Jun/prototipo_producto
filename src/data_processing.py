##AQUÍ VAMOS A INSERTAR LAS FUNCIONES 
##DE PROCESAMIENTO DE DATOS
import pandas as pd
from tabulate import tabulate
from datetime import datetime
from dateutil.relativedelta import relativedelta

def unir_string_headers():
    df.columns = [
        f"{str(col1).strip()}_{str(col2).strip()}" if pd.notna(col1) and pd.notna(col2)
        else str(col1) if pd.notna(col1)
        else str(col2)
        for col1, col2 in df.columns
    ]

##GRIT 150: Funciones para limpieza tosca del df
def grit_150(dataframe):
    #Droppea las filas con valores nulos en las columnas 37 a 43, sin contar la 41
    df = dataframe.dropna(subset=dataframe.columns[37:40+1])
    df = dataframe.dropna(subset=dataframe.columns[42:43+1])
    #Crea la columna de fechas y cambia de tipo <object> a <datetime> para hacer operaciones con fechas
    df['Fecha'] = pd.to_datetime(dataframe.iloc[:, 3].str[:10])
    #print(df['Fecha'])
    ##Intento de Melt para ordenar los valores de la columna 'Otro (especifique)'
    otros_idx = df.columns.get_loc(('Unnamed: 36_level_0', 'Otro (especifique)'))
    subheaders = df.columns.levels[1]
    for idx, row in df.iterrows():
        valor = row[otros_idx]
        if pd.notna(valor) and valor in subheaders:
            df.loc[idx, (slice(None), valor)] = valor
    ##Convertir columnas cualitativas a cuantitativas
    map_dict = {"Pésimo" : 0, "Muy Malo" : 1, "Malo" : 3, "Regular - Malo" : 5,
                "Regular - Bueno" : 6, "Bueno" : 8, "Muy Bueno" : 9, "Excelente" : 10}
    df['Atencion'] = df.iloc[:, 37].map(map_dict)
    df['Profesionalismo'] = df.iloc[:, 38].map(map_dict)
    df['Tiempo de Entrega'] = df.iloc[:, 39].map(map_dict)
    df['Calidad del Producto'] = df.iloc[:, 40].map(map_dict)
    
    return df


##FIltrar grit_150 a 12 meses    
def grit_1200(df_general): 
    #Establecer la fecha límite para filtrar los datos
    fecha_limite = datetime.now() - relativedelta(months=12)
    #Filtrar los datos de la columna 'Fecha' mayores a la fecha límite
    df_last_12_moths=df_general[df_general['Fecha'] > fecha_limite]
    print(df_last_12_moths.iloc[:, -5:])
    return df_last_12_moths

##Filtrar grit_150 a 3 meses
def grit_3000(df_general):
    #Establecer la fecha límite para filtrar los datos
    fecha_limite = datetime.now() - relativedelta(months=3)
    #Filtrar los datos de la columna 'Fecha' mayores a la fecha límite
    df_last_3_months=df_general[df_general['Fecha'] > fecha_limite]
    print(df_last_3_months.iloc[:, -5:])
    return df_last_3_months

df = pd.read_csv('data/Satisfacción de servicio para UPG 2024.csv', header = [0,1])

#unir_string_headers()
colaboradores = df.columns.get_level_values(1)[16:35+1].to_list()
grit_1200(grit_150(df))
grit_3000(grit_150(df))
##VISORES

#print(df.iloc[:, 3])
#print(df.iloc[:, 16].to_list())
#print(df['Tiempo de Entrega'])
#print(df.xs('Ana Aguirre', axis=1, level=1))
#print(df['Unnamed: 36_level_0']['Otro (especifique)'])
#print(colaboradores)
#print(tabulate(df, tablefmt='psql'))